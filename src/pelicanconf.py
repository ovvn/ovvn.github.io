#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Osman Mazinov'
SITENAME = u"Osman Mazinov's blog"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Fullstack Engineer'
SITELOGO='https://avatars1.githubusercontent.com/u/2973998?v=3&s=460'
PATH = 'content'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('About me', 'pages/about.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/osmanmazinov/'),
          ('github', 'https://github.com/ovvn'),
          ('google', 'https://google.com/+OsmanMazinov'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
FEED_ALL_RSS = 'rss/all.xml'
CATEGORY_FEED_RSS = 'rss/%s.xml'
