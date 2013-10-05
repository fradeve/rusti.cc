#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Perfectionanist'
TAGLINE = 'WebGIS dev, free software enthusiast, folk music fellow and proud monkey descendant.'
SITENAME = 'The perfectionanist'
SITEURL = 'http://fradeve.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'it'

THEME = 'theme-svbhack'

ARTICLE_URL = 'log/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'log/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = 'log/{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'log/{date:%Y}/{date:%m}/{slug}-{lang}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = None

# Comments
DISQUS_SITENAME = 'fradeveorig'

# Blogroll
LINKS =  (
            ('About', 'http://me.fradeve.org'),
            ('Code', 'http://github.com/fradeve'),
            ('Social', 'http://fradeve.org/social.html'),
         )

DEFAULT_PAGINATION = 5

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'featured')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
