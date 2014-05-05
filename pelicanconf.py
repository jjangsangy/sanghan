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
         ('facebook', 'http://facebook.com/jjangsangy')
         ,)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
