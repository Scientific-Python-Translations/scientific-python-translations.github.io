---
title: "Documentation for maintainers"
draft: false
---

This page details existing patterns for setting up and deploying translations
for project websites. As each project has their own set up, the patterns
described here may not fit exactly, but they will help you understand the
basic workflows.

At least some of the tasks described here rely on scripts from
https://github.com/Scientific-Python-Translations/automations/.

## Integration with Crowdin

Crowdin provides GitHub integration tools to sync all translated content from
the Crowdin web interface into project websites and vice-versa. However, a few
adaptations are needed.

Given a GitHub repository which has been synced to Crowdin, the
[`create_branch_for_language.sh` script](https://github.com/Scientific-Python-Translations/automations/blob/main/scripts/create_branch_for_language.sh)
is used to create a new branch including all (and only) commits from Crowdin's
branch for a particular language of interest. This script is useful because:

1. Crowdin will keep commits for all languages under translation under the same
   branch. However, we prefer to be able to create, review, and merge pull
   requests for one language at a time.

2. There are times when translations must be edited manually (outside of
   Crowdin) due to incorrect segmentation of the content into strings for
   translation. Crowdin's branch can only be edited through the Crowdin UI, and
   commits pushed to it outside of Crowdin will be lost when the branch is
   synced. By creating a new branch with only the commits we are interested in,
   we can bypass this limitation.

Ideally you will **not** have to run this script directly, but can include it as
part of your website deployment process (see, for example,
https://github.com/numpy/numpy.org/pull/772)

## Merging translations

As translators work on the Crowdin platform, a Pull Request is automatically
created in the project repository. This PR **should not** be merged, as it
contains all translations for all languages (see
https://github.com/numpy/numpy.org/pull/778 for an example). If your website is
set up through the Scientific Python Translations org, this PR will have the
`do-not-merge` label applied to it.

After translations for a language are completed and ready to be deployed, you
should:

1. Go to the repository corresponding to your project under
   https://github.com/Scientific-Python-Translations
2. Go to the Actions tab
3. Manually trigger the "Create translations PR" workflow, with the language
   code for your language of interest as input.

<center><img alt="Screenshot of the Actions tab from GitHub, with the Create translations PR workflow highlighted." src="../images/create_translations.png" width=800/></center>

<center><img alt="Screenshot of the Run workflow dialog from GitHub, with an input field labeled Crowding language code for the language of interest" src="../images/run_workflow.png" width=800/></center>

After these steps, a PR will be created to your website repo with the
translations for the language you selected (see
https://github.com/numpy/numpy.org/pull/774 for an example.) This PR should be
merged when you are ready to publish the translations.

## Setting up a language switcher

Ideally, the dropdown will be populated automatically.

(to be completed)

### Scientific Python Hugo Theme

### PyData Sphinx Theme

## Known limitations

### Missing translations

For items such as news items and release announcements, translations may not
always be up to date. In this case, your project can decide what to do with
these items (for example, keep them in english or hide them from the deployed
site.)
