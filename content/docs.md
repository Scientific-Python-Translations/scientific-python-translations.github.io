---
title: "Maintainers' documentation"
draft: false
---

This page details existing patterns for setting up and deploying translations
for project websites. As each project has their own set up, the patterns
described here may not fit exactly, but they will help you understand the
basic workflows.

At least some of the tasks described here rely on scripts from
https://github.com/Scientific-Python-Translations/automations/.

<!-- separate actual steps maintainers need to take from internal crowdin implementation details -->

## Integration with Crowdin

[Crowdin](https://scientific-python.crowdin.com/) provides GitHub integration
tools to sync all translated content from the Crowdin web interface into project
websites and vice-versa. However, a few adaptations are needed. The following
steps describe what maintainers need to do to set up the integration.

### Setting up Crowdin

Create a Crowdin project for your repository and turn on synchronization
between Crowdin and your source repo. If you are planning on using the
[Scientific Python Crowdin workspace](https://scientific-python.crowdin.com/),
please reach out to the
[Scientific Python translations team on discord](https://discord.com/invite/vur45CbwMz)
for help. For more information, see
[Crowdin's documentation](https://support.crowdin.com/enterprise/github-integration/).

To prevent extra activity in the original source repository, we recommend
creating a separate repository for the translations under
https://github.com/scientific-python-translations. To get you started with the project 
repository we provide a [translations-cookiecutter](https://github.com/Scientific-Python-Translations/translations-cookiecutter) template.

This template includes the necessary workflows that will run periodically to keep the infrastructure in sync. See [](#automation-details) for more information.

### Announce your project to potential translators

After your project is set up, you will have to add translators as members to
your Crowdin project so they can start translating. The general best practice is
to have two people per language (one translator, one reviewer) to ensure the
quality of the translations. However, your translations will not be published
until you approve them, so you can start with one translator and add a reviewer
later.

You can find potential translators by reaching out in the `#translation` channel
on the [Scientific Python Discord server](https://discord.com/invite/vur45CbwMz).

### Crowdin integration

As translators work on the Crowdin platform, a Pull Request is automatically
created in the project repository. This PR **should not** be merged, as it
contains all translations for all languages (see
[Scientific-Python-Translations/scipy.org-translations#187](https://github.com/Scientific-Python-Translations/scipy.org-translations/pull/187) for an
example). This PR will be opened againts the translations repository (e.g. Scientific-Python-Translations/scipy.org-translations). If your website is set up throughthe Scientific Python Translations
org, this PR will should have the `do-not-merge` label applied to it to ensure the PR
will not be merged accidentally.

{{< admonition important >}}

To prevent future conflicts with the GitHub/Crowdin integration, it is important
that you configure Crowdin to have duplicate strings share the same translation.
To do this, navigate to your project's Settings in Crowdin, select Import and under
"Source strings" -> "Duplicates" choose "Hide (regular detection)".

<center><img alt="Screenshot of the Crowdin Settings showing the 'Hide (regular detection)' option." src="../images/duplicate_strings.png" width=800/></center>

{{< /admonition >}}


## Automation details

The following diagram illustrates how the different components of automation work takeing the scipy.org webiste as an example.

```mermaid
flowchart TD
    B -.->|sync_translations.yml <br/> #40;PRs to add translations#41;| A
    A[Source repository <br/><br/> #40;scipy/scipy.org#41;] -->|sync_content.yml <br/> #40;PR to sync content - automerged#41;| B[Translation repository <br/><br/> #40;Scientific-Python-Translations/scipy.org-translations#41;]
    C[Crowdin <br/><br/> #40;scientific-python.crowdin.com#41;] -->|sync_translations.yml <br/> #40;PRs to add translations & contributors - automerged#41;| B
    A -->|Crowdin integration| C
```

### Cookiecutter template

Use the cookiecutter template to generate a translation-ready repo:

```bash
cookiecutter gh:Scientific-Python-Translations/translations-cookiecutter
```

When prompted, enter the details for your project (e.g. project name, organization, base branch). The structure will include necessary metadata, content folders, and pre-commit configuration. See the [Cookiecutter repository](https://github.com/Scientific-Python-Translations/translations-cookiecutter) for more information.

### Sync content from the source repo

The [`sync_content.yml` github workflow](https://github.com/Scientific-Python-Translations/translations-cookiecutter/blob/main/%7B%7Bcookiecutter.__translations_repo_name%7D%7D/.github/workflows/sync_content.yml) is in charge of keeping the **original source content** in sync with the translations repository within the Scientific Python Translations organization.

This workflow uses the `content-sync` [Github action](https://github.com/Scientific-Python-Translations/content-sync). 

### Example: Sync SciPy content

```yaml
name: Sync Content
on:
  schedule:
    - cron: '0 5 * * *'
  workflow_dispatch:
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Sync Scipy Content
        uses: Scientific-Python-Translations/content-sync@main
        with:
          source-repo: "scipy/scipy.org"
          source-path: "content/en/"
          source-ref: "main"
          translations-repo: "Scientific-Python-Translations/scipy.org-translations"
          translations-path: "content/"
          translations-source-path: "content/en/"
          translations-ref: "main"
          auto-merge: "true"
          # These are provided by the Scientific Python Project and allow
          # automation with bots
          gpg-private-key: ${{ secrets.GPG_PRIVATE_KEY }}
          passphrase: ${{ secrets.PASSPHRASE }}
          token: ${{ secrets.TOKEN }}
```

This ensures your translation repo always has the latest source material in English (the chosen source language). If the source content has changed since the latest workflow run, 
the translations bot will automatically create a Pull Request with signed commits and merge it automatically.

### Pull translations from Crowdin

The [`sync_translations.yml` github workflow](https://github.com/Scientific-Python-Translations/translations-cookiecutter/blob/main/%7B%7Bcookiecutter.__translations_repo_name%7D%7D/.github/workflows/sync_translations.yml) is in charge of keeping the **translated content** in sync with the translations repository within the Scientific Python Translations organization.

This workflow uses the `translations-sync` [Github action](https://github.com/Scientific-Python-Translations/translations-sync). 

#### Example: Sync SciPy.org translations

```yaml
name: Sync Translations
on:
  # schedule:
  #   - cron: '0 12 * * MON'  # Every Monday at noon
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Sync Scipy translations
        uses: Scientific-Python-Translations/translations-sync@main
        with:
          crowdin-project: "scipy.org"
          source-repo: "scipy/scipy.org"
          source-path: "content/en/"
          source-ref: "main"
          translations-repo: "Scientific-Python-Translations/scipy.org-translations"
          translations-path: "content/"
          translations-source-path: "content/en/"
          translations-ref: "main"
          translation-percentage: "90"
          approval-percentage: "0"
          use-precommit: "true"
          create-toml-file: "true"
          create-upstream-pr: "true"
          auto-merge: "true"
          # These are provided by the Scientific Python Project and allow
          # automation with bots
          gpg-private-key: ${{ secrets.GPG_PRIVATE_KEY }}
          passphrase: ${{ secrets.PASSPHRASE }}
          token: ${{ secrets.TOKEN }}
          crowdin-token: ${{ secrets.CROWDIN_TOKEN }}
```

In the Crowdin interface, source strings are _translated_ and then _approved_ (which means a second translator has reviewed and approved the translation of this source string). Everytime this workflow runs, the translations bot will check for the available languages and check if they meet the translation percentage (90% by default) and approval percentage (0% by default). For every language that passes the criteria, which can be defined by the project mainatiners, a new Pull Request with signed commits will be created in the translations repository and the source repository.

To gather information on translators, an additional Pull Request will be created on the translations repository with a `translators.yml` file that lists the details such as username, fullname and avatar from the crowdin site.

All Pull Requests created by the Automations Bot on the translation repositories will be automatically merged.

### Cleaning up

After merging the translations PR, the Crowdin service branch (by default, named `l10n_main`) may have merge conflicts with `main`. To fix this, we used the `clean-up` Github action to delete the Crowdin service branch. Crowdin will automatically recreate the service branch with merge conflicts resolved. This Action will also delete any stale
branches in the translations repository to keep things tidy.

### Example: Clean up SciPy translations repository

This workflow uses the `clean-up` [Github action](https://github.com/Scientific-Python-Translations/clean-up).

```yaml
name: Clean Up

on:
  schedule:
    - cron: '0 0 * * FRI'  # Every Fridat at midnight
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Clean Scipy translations repository
        uses: Scientific-Python-Translations/clean-up@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          translations-repo: "Scientific-Python-Translations/scipy.org-translations"
          translations-ref: "main"
          # These are provided by the Scientific Python Project and allow
          # automation with bots
          gpg-private-key: ${{ secrets.GPG_PRIVATE_KEY }}
          passphrase: ${{ secrets.PASSPHRASE }}
          token: "not-a-real-token"
          crowdin-token: ${{ secrets.CROWDIN_TOKEN }}
```

### The translations bot

All automations and pull requests are performed by:  
[**@scientificpythontranslations**](https://github.com/scientificpythontranslations)

Make sure to grant the bot appropriate repository permissions and exempt it from branch protection rules if needed.

## Preparing your project for internationalization and localization

### Folder structure

This will depend on the framework you are using as many of these will provide solutions
for localization. The principle is to have all files that have translatable content inside
a folder named `en`. You can take a look at different examples from the following projects

#### Hugo using the Scientific Python theme

All translatable content is stored in `content/en/`

- [scipy](https://github.com/scipy/scipy.org/)
- [numpy](https://github.com/numpy/numpy.org/)

#### NextJs with Babel and Lingui

On this project the content is stored in `src/locales/en/`

- [Xarray](https://github.com/xarray-contrib/xarray.dev/pull/772)

#### Jekyll 

- [Zarr](https://github.com/zarr-developers/zarr-developers.github.io/pull/144)

#### Static sites

On this project the content is stored in `build/en`

- [Networkx](https://github.com/networkx/website)

### Setting up a language switcher

Once again this will depend on the framework you are using as many of these may provide solutions
for this. You can look at examples from the project described in the previous section.

### Missing translations

Translations may not always be up to date for items such as news items and
release announcements. In this case, your project can decide what to do with
these items (for example, keep them in English or hide them from the deployed
site.)

### 📚 Additional resources

- [How to Translate Content](https://scientific-python-translations.github.io/translate/)
- [FAQ](https://scientific-python-translations.github.io/faq/)
- [Crowdin Setup](https://crowdin.com/)
- [Scientific Python Discord – `#translation`](https://scientific-python.org/community/)
- [Scientific Python Hugo Theme](https://github.com/scientific-python/scientific-python-hugo-theme/)
- [pydata/pydata-sphinx-theme#507](https://github.com/pydata/pydata-sphinx-theme/issues/)
