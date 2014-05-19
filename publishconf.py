#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
import os
from os.path import abspath

sys.path.append(abspath(os.curdir))

from pelicanconf import *

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


SITEURL = 'http://sanghan.me'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
