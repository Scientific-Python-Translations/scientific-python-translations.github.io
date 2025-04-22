import json
import yaml
import os
import traceback
import tempfile
from datetime import datetime
from subprocess import Popen, PIPE
from pathlib import Path

from crowdin_api import CrowdinClient  # type: ignore
from github import Github, Auth



def parse_input() -> dict:
    gh_input = {
        # Automations Bot account
        "username": "scientificpythontranslations",
        "crowdin_token": os.environ["CROWDIN_TOKEN"],
        # Provided by gpg action based on organization secrets
        "name": os.environ["GPG_NAME"],
        "email": os.environ["GPG_EMAIL"],
    }
    return gh_input


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


def main() -> None:
    """Main function to run the script."""
    try:
        gh_input = parse_input()
        crowdin_project = gh_input["crowdin_project"]
        client = ScientificCrowdinClient(
            token=gh_input["crowdin_token"], organization="Scientific-python"
        )
        valid_languages = client.get_valid_languages(
            crowdin_project,
            int(gh_input["translation_percentage"]),
            int(gh_input["approval_percentage"]),
        )
        translators = client.get_project_translators(
            crowdin_project,
        )
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        return


if __name__ == "__main__":
    main()
