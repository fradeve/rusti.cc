#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Perfectionanist'
TAGLINE = 'WebGIS dev, free software enthusiast, folk music fellow and proud monkey descendant.'
SITENAME = 'The perfectionanist'
SITEURL = 'http://fradeve.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'it'

THEME = 'andrewseidl-theme'

ARTICLE_URL = 'log/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'log/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = 'log/{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'log/{date:%Y}/{date:%m}/{slug}-{lang}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = None

# Files
PATH = 'content'
STATIC_PATHS = ["images"]

# Comments
DISQUS_SITENAME = 'fradeveorig'
DISQUS_PUBLICKEY = '4VY3RiHzHB4j6Z0jjyUpvKbVgM6homcEupgvIdIdrjNTaMtGh8Quz2w6Myy6VW4E'

# Links
SOCIAL = (
            ('icon-archive', SITEURL + '/archives.html'),
            ('icon-tags', SITEURL + '/tags.html'),
            ('icon-pushpin', SITEURL + '/featured.html'),
            ('icon-user', 'http://me.fradeve.org'),
            ('icon-github', 'http://github.com/fradeve/fradeve.org')
         )

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'featured')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
