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
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = './themes/bootstrap'

# Blogroll
LINKS =  (('Photography', 'http://sanghanphotography.com'),
         ('Website', 'http://sanghan.me'),)

# Social widget
SOCIAL = (('github', 'http://github.com/jjangsangy'),
         ('facebook', 'http://facebook.com/jjangsangy'),
         ('linkedin', 'https://www.linkedin.com/pub/sang-han/40/9a8/323')
         ,)

DEFAULT_PAGINATION = 10

GITHUB_USER = 'jjangsangy'
GITHUB_SKIP_FORK = True
GITHUB_REPO_COUNT = 5
GITHUB_SHOW_USER_LINK = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
