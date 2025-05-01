import os
import traceback
from datetime import datetime
from pathlib import Path

from crowdin_api import CrowdinClient  # type: ignore
from dotenv import load_dotenv


load_dotenv()  # take environment variables


class ScientificCrowdinClient:

    def __init__(self, token: str, organization: str):
        self._token = token
        self._organization = organization
        self._client = CrowdinClient(token=token, organization=organization)

    def get_projects(self) -> dict:
        """Get projects from Crowdin."""
        result = {}
        projects = self._client.projects.with_fetch_all().list_projects()
        for project in projects["data"]:
            result[project["data"]["name"]] = project["data"]["id"]
        return result

    def get_project_id(self, project_name: str) -> int:
        """Get project ID from Crowdin."""
        projects = self._client.projects.with_fetch_all().list_projects()
        for project in projects["data"]:
            if project["data"]["name"] == project_name:
                return project["data"]["id"]
        else:
            raise ValueError(f"Project '{project_name}' not found.")

    def get_project_status(self, project_name: str) -> dict:
        """Get project status from Crowdin."""
        results = {}
        for p_name, project_id in self.get_projects().items():
            if project_name != p_name:
                continue

            languages = self._client.translation_status.get_project_progress(
                project_id
            )["data"]
            for language in languages:
                language_id = language["data"]["language"]["id"]
                results[language_id] = {
                    "language_name": language["data"]["language"]["name"],
                    "progress": language["data"]["translationProgress"],
                    "approval": language["data"]["approvalProgress"],
                }
        return results

    def get_project_languages(self, project_name: str) -> list:
        """Get project languages from Crowdin."""
        projects = self._client.projects.with_fetch_all().list_projects()
        for project in projects["data"]:
            if project["data"]["name"] == project_name:
                return project["data"]["targetLanguageIds"]
        else:
            raise ValueError(f"Project '{project_name}' not found.")

    def get_valid_languages(
        self, project_name: str, translation_percentage: int, approval_percentage: int
    ) -> dict:
        """Get valid languages based on translation and approval percentage.

        Parameters
        ----------
        project_name : str
            Name of the project.
        translation_percentage : int
            Minimum translation percentage.
        approval_percentage : int
            Minimum approval percentage.

        Returns
        -------
        valid_languages : dict
            Dictionary of valid languages.
        """
        valid_languages = {}
        project_languages = self.get_project_status(project_name)
        # print(json.dumps(project_languages, sort_keys=True, indent=4))
        for language_id, data in project_languages.items():
            approval = data["approval"]
            progress = data["progress"]
            language_name = data["language_name"]
            if progress >= translation_percentage and approval >= approval_percentage:
                # print(f"\n{language_id} {language_name}:  {progress}% / {approval}%")
                valid_languages[language_id] = {
                    "language_name": language_name,
                    "progress": progress,
                    "approval": approval,
                }
        return valid_languages

    def get_project_translators(self, project_name: str) -> dict:
        """Get project translators from Crowdin."""
        results: dict = {}
        project_id = self.get_project_id(project_name)
        languages = self.get_project_languages(project_name)
        for lang in sorted(languages):
            results[lang] = []
            offset = 0
            limit = 500
            while True:
                items = self._client.string_translations.list_language_translations(
                    lang, project_id, limit=limit, offset=offset
                )
                if data := items["data"]:
                    for item in data:
                        user_data = {
                            "username": item["data"]["user"]["username"],
                            "name": item["data"]["user"]["fullName"],
                            "img_link": item["data"]["user"]["avatarUrl"].replace(
                                "/medium/", "/large/"
                            ),
                        }
                        if user_data not in results[lang]:
                            results[lang].append(user_data)
                    offset += limit
                else:
                    break

        return results


def generate_card(
    name: str,
    img_link: str,
) -> str:
    """
    Generate a card in TOML format.
    """
    toml_card_template = """[[item]]
type = 'card'
classcard = 'text-center'
body = '''{{{{< image >}}}}
src = '{img_link}'
alt = 'Avatar of {name}'
{{{{< /image >}}}}
{name}'''"""
    return toml_card_template.format(
        img_link=img_link,
        name=name,
    )


def generate_contributors_md_file(data: dict) -> None:
    script_path = Path(__file__).resolve()
    parent_dir = script_path.parent.parent / "content"
    content = """---
title: Translation Contributors
draft: false
---

"""

    for crowdin_project in sorted(data, key=lambda x: x.lower()):
        content += f"\n## {crowdin_project}\n"
        content += '\n{{< grid columns="2 3 4 5" >}}\n\n'
        translators = data[crowdin_project]["translators"]
        all_translators = []
        for _, contributors in translators.items():
            if contributors:
                for contributor in contributors:
                    if contributor not in all_translators:
                        all_translators.append(contributor)

        for contributor in all_translators:
            content += "\n\n"
            content += generate_card(
                name=contributor["name"], img_link=contributor["img_link"]
            )
            content += "\n\n"

        content += "\n{{< /grid >}}"

    new_file_path = parent_dir / "contributors.md"
    content += f"\n\n---\n\nLast updated: {datetime.now().strftime('%Y-%m-%d')}\n"

    with open(new_file_path, "w") as f:
        f.write(content)


def generate_dashboard_md_file(data: dict) -> None:
    """Generate a markdown file for the dashboard."""
    script_path = Path(__file__).resolve()
    parent_dir = script_path.parent.parent / "content"
    content = """---
title: Translations Status
draft: false
---
"""
    new_file_path = parent_dir / "status.md"
    for crowdin_project in sorted(data, key=lambda x: x.lower()):
        project_id = data[crowdin_project]["project_id"]
        content += f"\n## {crowdin_project}\n"
        content += """\n<table class="dashboard">
<tr>
<th align="center">Language</th>
<th align="center" >Translators</th>
<th align="center" >Completion %</th>
<th align="center" >Approval %</th>
</tr>
"""
        status = data[crowdin_project]["status"]
        for language_id, _ in sorted(
            status.items(),
            key=lambda item: (item[1]["progress"], item[1]["approval"]),
            reverse=True,
        ):
            print(language_id)
            url = f"https://scientific-python.crowdin.com/u/projects/{project_id}/l/{language_id}"
            content += f"""<tr>
<td><a href='{url}'>{status[language_id]['language_name']} ({language_id})</a></td>
<td>{len(data[crowdin_project]['translators'][language_id])}</td>
<td>{status[language_id]['progress']}</td>
<td>{status[language_id]['approval']}</td>
</tr>"""

        content += "\n</table>\n\n"

    content += f"\n\n---\n\nLast updated: {datetime.now().strftime('%Y-%m-%d')}\n"

    with open(new_file_path, "w") as f:
        f.write(content)


def main() -> None:
    """Main function to run the script."""
    try:
        client = ScientificCrowdinClient(
            token=os.environ["CROWDIN_TOKEN"], organization="Scientific-python"
        )
        projects = client.get_projects()
        data = {}
        for crowdin_project, project_id in sorted(projects.items()):
            print(f"Project: {crowdin_project} ({project_id})")
            project_status = client.get_project_status(crowdin_project)
            translators = client.get_project_translators(
                crowdin_project,
            )
            data[crowdin_project] = {
                "status": project_status,
                "translators": translators,
                "project_id": project_id,
            }
        generate_dashboard_md_file(data)
        generate_contributors_md_file(data)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return


if __name__ == "__main__":
    main()
