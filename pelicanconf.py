#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sang Han'
SITENAME = 'Sang Han'
SITEURL = 'http://sanghan.me'
EMAIL_ADDR = 'jjangsangy@gmail.com'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
DATE_FORMATS = {'en': '%a, %d %b %Y'}
LOCALE = 'en_US'
DEFAULT_PAGINATION = 10
SEARCH_BOX = True

STATIC_PATHS = ['img', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
OUTPUT_PATH = 'output'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

THEME = './themes/bootstrap'
BOOTSTRAP_THEME = 'spacelab'
MARKUP = ('rst', 'md', 'ipynb')
PLUGIN_PATH = 'plugins'

GITHUB_USER = 'jjangsangy'
GITHUB_SKIP_FORK = True
GITHUB_REPO_COUNT = 5
GITHUB_SHOW_USER_LINK = False

# Blogroll
LINKS =  (('Photography', 'http://sanghanphotography.com'),
         ('Website', 'http://sanghan.me'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/jjangsangy'),
         ('Facebook', 'http://facebook.com/jjangsangy'),
         ('LinkedIn', 'https://www.linkedin.com/pub/sang-han/40/9a8/323')
         ,)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
