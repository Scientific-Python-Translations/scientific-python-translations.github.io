---
title: "Frequently Asked Questions"
draft: false
---

##### What is the intended scope for the content to be translated?

At least to start, the plan is to limit the translations to the brochure
websites of the [Scientific Python Core
Projects](https://scientific-python.org/specs/core-projects/).  By a
brochure website, we mean the main landing page for the project plus
subpages containing basic information about the project. Technical
content such as API documentation and tutorials is considered to be out
of scope.

Eventually, we hope to expand to translations of the most important
beginner-focused tutorial(s).

##### Why should the scope for content to translate at least initially be limited to brochure websites?

Care must be taken to limit the burden on volunteer translators and to
limit the effort needed for coordinating the translation effort. For
this project, we believe that the amount of content selected for a
project should be restricted such that a competent volunteer can perform
the translations in a single language in at most one to two days of
work. Content which may receive frequent updates should also be avoided
in order to make it easier to keep translations up-to-date. Technical
documentation is often extensive, more difficult to translate, and more
liable to change or be expanded upon in the future. The brochure
websites ideally contain important information useful for those getting
started with a project which should remain relatively static over
time. The restriction to a subset of content which can be translated in
one to two days gives maintainers the freedom to make a complete
overhaul of their website and documentation without needing to worry
that a large effort would be needed to keep translations up to date.

##### Can you be more specific in describing what content should be translated?

Let's consider https://numpy.org/, the content that is currently
translated includes:

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

At a minimum, a brochure website should give an overview of a project
and what it is useful for and provide some direction for new users
looking to get started. It is valuable for potential users to be able to
see what a package does and whether it could be useful for them, so they
can judge whether it would be worth the effort to learn to use a tool
which is primarily developed and documented in a language they are
unfamiliar with. Those who decide a package is worth exploring will
benefit from any information which lowers the amount of thought and
effort needed to get started. We believe the qualities which would
make a brochure website useful in translation are the same as those
which characterize a useful brochure website in general.

##### Why are user supplied machine translations not sufficient?
First, machine translations can struggle with the technical language and
jargon of scientific computing. This was observed, for instance, in the
efforts to translate numpy.org. Machine translations are a great
starting point, and make work easier for translators, but for content of
this nature having a human in the loop helps ensure accuracy and
consistent quality. In addition, publishing official translations help
give a sense of inclusivity, making non-English speakers feel welcome
and making it more likely for rich user communities to develop among
clusters of non-English speakers.

##### What languages would be involved?
Languages with a large populations of speakers with no to low English
proficiency should be prioritized in order to maximize the impact per
amount of work. Any language with enthusiastic translators who are
committed to keeping translations up to date can be considered though.

Some resources that could be helpful for priortizing languages are:
* https://www.ef.edu/epi/ with information on levels of English
proficiency within different countries,
* https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers
tabulating the number of speakers per language
* https://languagerc.net/languages-by-countries/ listing common
languages for different countries.

##### What platform will be used for managing translations?
We are using [Crowdin](https://crowdin.com/) to manage
translations. They have generously offered a free supported enterprise
account to help us in this work. Crowdin offers convenient [GitHub
integration](https://support.crowdin.com/github-integration/) which
makes it easier to coordinate the process of keeping translations
up-to-date. Crowdin provides a convenient user interface for translators
and proofreaders which integrates machine translations in order to
streamline the translation process.

##### Where should the translations be published?
We hope the translations can be published directly on the core project
webpages, with some convenient means of switching between languages,
such as the drop-down selector used for https://numpy.org.  Publishing
official translations directly on the webpages helps to provide the
sense of inclusivity we seek, and helps establish trust in the
translations from potential users.

##### What work is expected from project maintainers?
We are commited to minimizing the work required from project
maintainers. This effort would not be viable if it required substantial
effort from the maintainers of individual projects. A small team of paid
[Quansight Labs](https://labs.quansight.org/) staff will work on setting
up translation infrastructure, recruiting and coordinating with
translators, and helping to integrate translations into core project
websites.

If maintainers of a core project agree to participate, we will create a
github repository in the [Scientific Python
Translations](https://github.com/Scientific-Python-Translations)
organization which mirrors the content of the project's brochure
website. It is this mirror repository which will be synced with Crowdin;
there is no need for maintainers to deal directly with Crowdin
integration. We are using a GitHub actions workflow to help keep the
content in these mirror repos up-to-date with the source
content. Through the efforts of the translators, these mirror repos will
host parallel versions of the brochure website content translated into a
variety languages, which we intend to keep up-to-date with the content
of the source web pages.

The sticking point where maintainer involvement may be necessary is in
publishing the translations on project's brochure website. A developer
from Quansight Labs can submit a pull request setting up the machinery
for publishing translations, but a maintainer will need to be involved
to review this pull request. Maintainers have the choice between having
translated content added directly to their repos in PRs, or having
machinery set up to download translated content from the corresponding
mirror repo at website build time. There are tradeoffs involved, with
the former requiring periodic review of pull requests for updating
content, and the latter requiring a greater up-front cost in reviewing a
more sophisticated PR and also requiring maintainers have sufficient
trust in the quality of translations to accept them without someone on
the team reviewing them in some way.

##### How is this work supported?
This work is supported by the CZI Scientific Python Community and
Communications Infrastructure
Grant. https://scientific-python.org/doc/scientific-python-community-and-communications-infrastructure-2022.pdf

At the moment, the most relevant deliverable from this grant is to
publish translations into 3 or more widely used languages (e.g. Spanish,
Chinese, Japanese) of the brochure websites of at least 8 Scientific
Python core projects. We are also committed to providing clear
documentation of the translation workflow, and eventually expanding 
to translations of the most important beginner-focused tutorial(s)
of at least 4 core projects.

##### What are the plans for keeping translations up to date?
Limiting the scope of content to translate for each project to a core
set of relatively static things which a competent volunteer can
translate for one language in one to two days will help in making it
manageable to keep translations up-to-date. Crowdin integrations
discussed earlier also help in the efforts to keep translations
up-to-date. Crowdin will become aware of any changes in the project
website content and notify translators that there are new strings
available to translate. The key factor however, will be in fostering
robust communities of volunteer translators willing to put in the work
to maintain translations, and if strong enough communities develop, it
may even become feasible to expand the scope of content to translate.

##### How will the quality of translations be verified?
You may have seen the
[incident](https://discourse.ubuntu.com/t/announcement-ubuntu-desktop-23-10-release-image-translation-incident-now-resolved/39365)
where hate speech was submitted in translations of the Ubuntu
desktop-installer. Outside of deliberate acts of vandalism, maintainers
may still feel weary about publishing translations on their webpages
which they are unable to read and evaluate for themselves. To help
ensure translations meet an acceptable standard, interested translators
and proofreaders will be individually vetted and an invitation to the
Scientific Python Crowdin organization will be required for them to
participate. Each translated string of content should validated by
at least one trusted proofreader distinct from the translator.

##### What if I'm a maintainer who's read all of this and is still skeptical about participating?
It's understandable that maintainers may be skeptical that it's actually
worth the effort to publish such translations. Let's take a moment to reframe things
The book [Working in Public: The Making and
Maintenance of Open Source Software](https://press.stripe.com/working-in-public) by Nadia Eghbal
makes the distinction between extractive and non-extractive contributions. An extractive
contribution is one "where the marginal cost of reviewing and merging that contribution is greater
than the marginal benefit to the project's producers." As an example, Eghbal eloquently describes
how translations can be an extractive contribution.

*Translations are one example of how a contribution can be either extractive or
non-extractive, depending on how it is managed. A common contribution for newcomers to a
popular project is offering to translate documentation into another language. At first
glance, it seems additive: Why not make the documentation available in more languages?
It’s also relatively self-directed (the maintainer doesn’t speak the language, so they
have to trust the contributor to handle it themselves), and relies on specialized skills
from the contributor (they’re presumably fluent in the language they’re translating into),
all of which make it seem like the ideal contribution.*

*But documentation is not static. As the primary language’s documentation changes over
time, translations will also need to stay synchronized. Will the contributor who’s
offering to translate documentation be willing to continue maintaining it indefinitely?
Probably not. Does the maintainer want to track down new contributors who can keep their
documentation up-to-date in Dutch, Slovenian, and Portuguese? Probably not.*

*It’s possible for a maintainer to sink hours into coordinating and synchronizing multiple
translations, with little benefit back to the project. So unless a maintainer wants to
manage that work, it’s more likely that they’ll either accept a one-time translation from
an eager contributor and clarify that it won’t be maintained or they just won’t accept
translations at all.*

Ou goal is to manage the translation process in such a way that it becomes non-extractive
for project maintainers. Maintainers will be able to outsource the effort needed for
"coordinating and synchronizing multiple translations" to a small team working across
projects. We hope that maintainers see this as an opportunity, rather than an attempt
by outsiders to impose work upon them. Maintainers have no obligation to participate,
but we hope they will at least agree up-front to let us set up mirror repos for their
website content and sync these repos with Crowdin. Doing so entails no commitment to
continue participating, but it will be helpful for us if we can carry out this work
together for all projects over a single block of time in order to reduce context switching
on our end.
