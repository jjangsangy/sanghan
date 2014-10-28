=============================================
Pelican: A Blogging Engine Written in Python
=============================================
:date:      06-09-14
:tags:      Python, Programming, Blog
:slug:      pelican_blog
:category:  Programming

There are many static site generators out there.

The most famous and well known being,
`Jekyll <http://jekyllrb.com>`_ and `Octopress <http://octopress.org>`_.

Jekyll is used by Github Pages as the default generator,
while Octopress is a framework for Jekyll geared specifically for blogging.
However, the reason why I decided to use Pelican over both,
is because Pelican is written in Python, and therefore support the
reStructuredText markup by default and
is a language I feel comfortable in case I need to get down and fix the
engine. One of my primary forcuses of blogging is so that I can also use it as
a platform for learning more about programming. I don't program in ruby
so, I wanted to go with an all Python solution.

Enter Pelican
-------------
So Pelican became my blogging engine of choice.
There are a couple other generators written with Python like
`Hyde <http://ringce.com/hyde>`_ and `Nicola <http://getnikola.com>`_,
but it seemed like Pelican was better supported and documented of the batch,
so thats what I went with.

|pelican|

So How does it Work?
---------------------

.. pull-quote::

    A generator is basically some arbitrary code that will output more arbitrary code.

In this case of pelican, it will take my articles written in the reStructuredText
markup and then generate HTML and CSS based on the `Jinja2`_ templating engine.

**Sounds simple enough right?**

Pelican utilized metadata that the user supplies in the form of a configuration file
located at the root of the project directory. This configuration file helps
Pelican figure out some user specific details that are necessary in order to
build the webpage, very similar to how Sphinx generates documentation.

Here is a snippet of how this blog's configuration file looks.


.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    sys.path.append(abspath(os.curdir))

    import sys
    import os
    from os.path import abspath

    AUTHOR = 'Sang Han'
    SINGLE_AUTHOR = True
    SITENAME = 'LightQuanta'

    SITEURL = 'http://sanghan.me'
    EMAIL_ADDR = 'jjangsangy@gmail.com'

    TIMEZONE = 'America/Los_Angeles'
    DEFAULT_LANG = 'en'
    DATE_FORMATS = {'en': '%a, %d %b %Y'}
    LOCALE = 'en_US'
    DEFAULT_PAGINATION = 7
    PATH = 'content'

    STATIC_PATHS = [
        'img',
        'extra/CNAME',
        'extra/robots.txt',
        'static'
    ]
    EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'},
    }
    OUTPUT_PATH = 'output'
    ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
    ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

..

Most of the configuration ends up setting enviornment variables that pelican will then use
to set up the site. But rather than being one big :code:`conf` file, it's
possible there is freedom to run executable code.

Templating
-----------
Above the generator, you have the templating language for laying out your HTML.
Pelican utilizes the `jinja2`_ templating engine, which also is the main
engine for `Flask`_, a great Pythonic alternative to the well known `Django`_
web framework. In fact, anyone with familiarity in any templating language should
feel right at home getting their own site up and running with these tools.

Tooling
--------
Pelican ultimately runs on a `Command Line Interface`_


.. |pelican| image::
    {filename}/img/bird-640.jpg

.. _Command Line Interface:
   https://github.com/getpelican/pelican.git

.. _jinja2:
    http://jinja.pocoo.org

.. _Flask:
    http://flask.pocoo.org

.. _Django:
   https://www.djangoproject.com
