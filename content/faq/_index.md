---
title: "Frequently Asked Questions"
draft: false
---

##### What is the intended scope for the content to be translated?

At least to start, the plan is to limit the translations to the brochure websites of the [Scientific Python Core Projects](https://scientific-python.org/specs/core-projects/).  By a brochure website, we mean the main landing page for the project plus subpages containing basic information about the project. Technical content such as API documentation and tutorials is considered to be out of scope.

Eventually, we hope to expand to translations of the most important beginner-focused tutorials.

##### Where should the translations be published?

We hope that official translations can be published directly on the core project web pages, with some convenient means of switching between languages, such as the drop-down selector used for https://numpy.org.  Publishing official translations directly on the web pages helps to provide the sense of inclusivity we seek, and helps establish trust in the translations from potential users.

##### Why should the scope for content to translate at least initially be limited to brochure websites?

Care must be taken to limit the burden on volunteer translators and to limit the effort needed for coordinating the translation effort. For this project, we believe that the amount of content selected for a project should be restricted such that a competent volunteer can perform the translations in a single language in at most one to two days of work. Content which may receive frequent updates should also be avoided in order to make it easier to keep translations up-to-date. Technical documentation is often extensive, more difficult to translate, and more liable to change or be expanded upon in the future. The brochure websites ideally contain important information useful for those getting started with a project which should remain relatively static over time. The restriction to a subset of content which can be translated in one to two days gives maintainers the freedom to make a complete overhaul of their website and documentation without needing to worry that a large effort would be needed to keep translations up to date.

##### Can you be more specific in describing what content should be translated?

It may be helpful to consider the content which is currently translated for https://numpy.org/. This currently includes:

* The landing page, which provides:
  * A concise overview of what NumPy does.
  * An interactive shell letting users try NumPy in the browser.
  * Lists of other projects in the NumPy ecosystem with brief
	descriptions.
  * Links to case studies showing how NumPy can be used in real world
	projects.
  * Links to informational subpages.
* Install: An overview for how to install NumPy
* Learn: Links to educational resources for learning about NumPy.
* Community: Information on places online and off to participate in the
  NumPy community.
* About us: Information on the people and institutions behind NumPy.
* News: Regular updates about NumPy releases and other important news
  related to NumPy.
* Contribute: How to get started contributing to NumPy in a variety of
  technical and nontechnical ways.
* Case Studies: Examples showing how NumPy is used in real world
  projects.
* Other: Miscellaneous small pages: how to cite NumPy, user surveys,
  where to ask for help, link to press kit.

##### Are translations restricted to the brochure websites actually even useful?

At a minimum, a brochure website should give an overview of a project and what it is useful for and provide some direction for new users looking to get started. It is valuable for potential users to be able to see what a package does and whether it could be useful for them, so they can judge whether it would be worth the effort to learn to use a tool which is primarily developed and documented in a language they are unfamiliar with. Those who decide a package is worth exploring will benefit from any information which lowers the amount of thought and effort needed to get started. We believe the qualities which would make a brochure website useful in translation are the same as those which characterize a useful brochure website in general.

##### Why are user supplied machine translations not sufficient?

Machine translations can still struggle with the technical language and jargon of scientific computing. Examples include machine translation having difficulty with terms which are commonly referred to by their English names in other languages, such as Git jargon like “branch” and “commit”; and machine translation producing incorrect literal translations of technical phrases. Translators who worked on the numpy.org project have attested to these challenges. While machine translations provide a good starting point for translators, for content of this nature, it is valuable to have a human in the loop to ensure accuracy and consistent quality. In addition, publishing official translations can help make new non-English speakers feel more welcome, increasing their likelihood of participating in user communities.

##### How is this work supported?

This work is supported by the CZI Scientific Python Community and Communications Infrastructure Grant. https://scientific-python.org/doc/scientific-python-community-and-communications-infrastructure-2022.pdf. This grant supports 25% full time engineer time per year to
work on translation infrastructure development and maintenance, and 15% full time engineer time per year to work on translation
coordination and actual translation work.

At the moment, the most relevant deliverable from this grant is to publish translations into 3 or more widely used languages (e.g. Spanish, Chinese, Japanese) of the brochure websites of at least 8 Scientific Python core projects. We are also committed to providing clear documentation of the translation workflow, and eventually expanding  to translations of the most important beginner-focused tutorial(s) of at least 4 core projects.

##### Why publish official translations instead of relying on independent community translations?

Community translations tend to be of varying quality and it is not uncommon for them to become unmaintained over time. However, in a sense this would be a community translation effort, but with paid staff working on translation infrastructure, finding and vetting translators, and coordinating the translations. The goal is to produce and maintain professional quality translations which project maintainers could confidently host on their project's web pages.

##### What languages would be involved?

Languages with a large population of speakers with no to low English proficiency should be prioritized in order to maximize the impact per amount of work. Any language with enthusiastic translators who are committed to keeping translations up to date can be considered though.

Some resources that could be helpful for prioritizing languages are:
* https://www.ef.edu/epi/ with information on levels of English
proficiency within different countries,
* https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers
tabulating the number of speakers per language
* https://languagerc.net/languages-by-countries/ listing common
languages for different countries.

##### What platform will be used for managing translations?

We are using [Crowdin](https://crowdin.com/) to manage translations. They have generously offered a free supported enterprise account to help us in this work. Crowdin offers convenient [GitHub integration](https://support.crowdin.com/github-integration/) which makes it easier to coordinate the process of keeping translations up-to-date. Crowdin provides a convenient user interface for translators and proofreaders which integrates machine translations in order to streamline the translation process.

##### What work is expected from project maintainers?

We are committed to minimizing the work required from project maintainers. This effort would not be viable if it required substantial effort from the maintainers of individual projects. A small team of paid [Quansight Labs](https://labs.quansight.org/) staff will work on setting up translation infrastructure, recruiting and coordinating with translators, and helping to integrate translations into core project websites.

If maintainers of a core project agree to participate, we will create a GitHub repository in the [Scientific Python Translations](https://github.com/Scientific-Python-Translations) organization which mirrors the content of the project's brochure website. It is this mirror repository which will be synced with Crowdin; there is no need for maintainers to deal directly with Crowdin integration. We are using a GitHub actions workflow to help keep the content in these mirror repos up-to-date with the source content. Through the efforts of the translators, these mirror repos will host parallel versions of the brochure website content translated into a variety of languages, which we intend to keep up-to-date with the content of the source web pages.

The point where maintainer involvement will be necessary is when publishing the translations on a project's brochure website. A developer from Quansight Labs can submit a pull request setting up the machinery for publishing translations, but a maintainer will need to be involved to review this pull request. Maintainers have the choice between having translated content added directly to their repos in PRs, or having machinery set up to download translated content from the corresponding mirror repo at website build time. There are trade offs involved, with the former requiring periodic review of pull requests for updating content, and the latter requiring a greater up-front cost in reviewing a more sophisticated PR and also requiring maintainers have sufficient trust in the quality of translations to accept them without having someone on the team review them in some way. We are also open to other suggestions for how translations can be published.

##### What are the plans for keeping translations up to date?

Limiting the scope of content to translate for each project to a core set of relatively static things which a competent volunteer can translate for one language in one to two days will help in making it manageable to keep translations up-to-date. Crowdin integrations discussed earlier also help in the efforts to keep translations up-to-date. Crowdin will become aware of any changes in the project website content and notify translators that there are new strings available to translate. The key factor however, will be in fostering robust communities of volunteer translators willing to put in the work to maintain translations, and if strong enough communities develop, it may even become feasible to expand the scope of content to translate.

##### How will the quality of translations be verified?

You may have seen the [incident](https://discourse.ubuntu.com/t/announcement-ubuntu-desktop-23-10-release-image-translation-incident-now-resolved/39365) where hate speech was submitted in translations of the Ubuntu desktop-installer. Outside of deliberate acts of vandalism, maintainers may still feel weary about publishing translations on their web pages which they are unable to read and evaluate for themselves. To help ensure translations meet an acceptable standard, interested translators and proofreaders will be individually vetted and an invitation to the Scientific Python Crowdin organization will be required for them to participate. Each translated string of content should be validated by at least one trusted proofreader distinct from the translator.

##### What if I'm a maintainer who's read all of this and is still skeptical about participating?

We hope any skeptical project maintainers will at least give initial approval for us to set up the translation infrastructure for their projects. Doing so will entail no commitment to eventually publish translations on the project's website. This will allow us to dedicate a block of time for setting up this infrastructure, without having to context switch back to this work if a project's maintainers later agree to move forward after seeing the results for other projects.
