========
Projects
========

:date: 2014-05-05 23:24
:tags: projects
:slug: projects
:icon: fa-code

py-translate
===================
**py-translate is a CLI Tool for Google Translate written in Python!**

:Code: `Github Repo <http://github.com/jjangsangy/py-translate.git>`_
:Docs: `User Documentation <http://py-translate.readthedocs.org/>`_
:Packages: `Official Packages <https://pypi.python.org/pypi/py-translate>`_

At first, it was called GTranslate, but the name was taken on
`PyPI`_ (Python Packaging Index). Honestly though the name is starting to
grow on me and now I much more prefer it over GTranslate.

**py-translate was my first real programming project.**

|alice|

Although looking back, getting it to feature complete with version 0.0.1
wasn't too difficult, but for me this project became somewhat of
a `bootstrapping compiler`_ for learning the python language.
Getting it to the 0.0.1 release, it motivated me to learn about
each feature of the language and as well the standard library.
I then had to think whether those language components were beneficial
to use within my project. Some noteworthy things I learned about python
were

* **reStructuredText (reST)**

  * The language behind docutils Python's internal documentation module
    and the third party Sphinx documentation generation library.
  * The main reason for using Pelican for generating this blog over
    other more popular packages that use Markdown for it's main markup
    language.

* **Python Generators and Coroutines**

  * Generators and Coroutines are a powerful way to manipulate
    textual data. You can create modular programs by stitching
    generators like unix pipes, or coroutines that can feed from
    one source and send to multiple targets.

With developing and managing my own project, I also had to teach myself
the ins and outs of

* Python Package Management/Distribution (Not Trivial at all)
* Writing out a formal specification and external API for
  other developers to use and extend.
* Automated Documentation generation using Sphinx and Docutils
* Writing good unit tests for each module.
* Continuous Build Integration and testing with Travis-CI

.. _PyPI:
   https://pypi.python.org/pypi/py-translate

.. _bootstrapping compiler:
   http://en.wikipedia.org/wiki/Bootstrapping_(compilers)

.. |alice| image::
   https://raw.githubusercontent.com/jjangsangy/py-translate/master/img/alice.gif
