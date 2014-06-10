=============================================
Pelican: A Blogging Engine Written in Python
=============================================
:date: 06-09-14
:tags: Python, Programming, Blog
:slug: pelican_blog
:category: Programming

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

So How does it Work?
---------------------

.. pull-quote::

    A generator is basically some arbitrary code that will output more arbitrary code.

In this case of pelican, it will take my articles written in the reStructuredText
markup and then generate HTML and CSS based on the Jinja2 templating engine.

**Sounds simple enough right?**

Pelican utilized metadata that the user supplies in the form of a configuration file
located at the root of the project directory. This configuration file helps
Pelican figure out some user specific details that are necessary in order to
build the webpage, very similar to how Sphinx generates documentation.

Here is a snippet of how this blog's configuration file looks.

.. code-block:: python
   :linenos: none

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

   import sys
   from os.path import abspath, curdir

   sys.path.append(abspath(curdir))

   AUTHOR = 'Sang Han'
   SINGLE_AUTHOR = True
   SITENAME = 'My Photoelectric Blog'
   SITEURL = 'http://sanghan.me'
   STATIC_PATHS = [
       'img',
       'extra/CNAME',
       'extra/robots.txt',
       'static',
   ]

As you can see, the syntax is just Python. The first block
is just a shebang line specifying the default python
interpreter. We then append the current directory into the
Python PATH and then start filling out some global variables which
Pelican will use later to generate the blog.
