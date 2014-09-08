#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
import os
from os.path import abspath

sys.path.append(abspath(os.curdir))

from pelicanconf import *

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

SITEURL = 'http://sanghan.me'
RELATIVE_URLS = False

DISQUS_SITENAME = 'sanghan'
DISQUS_SECRET_KEY = 'iQIq5Ra2Fx2kBnGbhUZ1sNjkhwpewkz5fSRsWUgZFTGj4BIZsqmixUAszepZXQ8I'
DISQUS_PUBLIC_KEY = 'JyNWL1mdpLOuqzbh5RZ3HfkzvKLYsElIMBLMTYv6k7HltM0RQKQnQfMBiLNbdV3K'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
GOOGLE_ANALYTICS = 'UA-51412306-1'

DELETE_OUTPUT_DIRECTORY = True
