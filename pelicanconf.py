#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sevas'
SITENAME = 'braindump_'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'


PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = [
    'sitemap',
    'extract_toc',
    'tipue_search',
    'html_rst_directive',
    'gist_directive']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = 'themes/elegant'


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

# Social
SOCIAL = (
        ('Twitter', 'http://twitter.com/sevas'),
        ('Github', 'http://github.com/sevas'),
        ('Email', 'mailto:f.degroef@gmail.com'),
          )

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.png': {'path': 'favicon.png'}
}


# LANDING_PAGE_ABOUT = {
#     'title': 'Hello',
#     'details': """
# <p>It appears I'm writing software for a living, mostly using python and C++.  This is a place to store written notes about things that I find interesting or
# useful, so they don't fill up my brain.
# </p>

# <p>Unpolished side-projects I work on can be found on
# <a href="http://github.com/sevas">github</a> and
# <a href="http://bitbucket.org/sevas">bitbucket</a>.
#  I share <a href="https://plus.google.com/u/0/117359550292524106955/about">things</a>  and
# occasionally <a href="https://twitter.com/sevas">whine</a> online.
# </p>

# <p>Nothing fancy, really.</p>

#     """
# }

# SMO
TWITTER_USERNAME = u'sevas'
#FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
