#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'fradeve'
TAGLINE = 'WebGIS dev, free software enthusiast, folk music fellow and proud monkey descendant.'
SITENAME = 'A rustic guy'
SITEURL = 'http://rusti.cc'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME = 'tufte-theme'
CSS_FILE = 'tufte.css'
TYPOGRIFY = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None

# Files
PATH = 'content'
STATIC_PATHS = ['images', 'static']

PLUGINS = ['pelican_youtube', 'span', 'series']
PLUGIN_PATHS = ["/home/fradeve/git/rusti.cc/plugins"]

# Comments
DISQUS_SITENAME = 'fradeveorig'
DISQUS_PUBLICKEY = '4VY3RiHzHB4j6Z0jjyUpvKbVgM6homcEupgvIdIdrjNTaMtGh8Quz2w6Myy6VW4E'

# Links
SOCIAL = (
            ('posts', SITEURL + '/archives.html'),
            ('tags', SITEURL + '/tags.html'),
            ('feat', SITEURL + '/featured.html'),
            ('me', SITEURL + '/pages/social.html'),
            ('gh', 'https://github.com/fradeve/rusti.cc')
         )

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'featured')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
