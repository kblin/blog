#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kai Blin'
SITENAME = "Kai's Development Blog"
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]


TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

THEME = u'pelican-bootstrap3'
BOOTSTRAP_THEME = u'simplex'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/kaiblin'),
          ('github', 'https://github.com/kblin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
