#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys

AUTHOR = u'Andrej Sýkora'
SITENAME = u'Data a Brewery'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = False

# PATHS


# URLS TO STATIC PAGES

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# DONT GENERATE ANYTHING ELSE
ARTICLE_SAVE_AS = False
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAGS_SAVE_AS = False
# INDEX_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# THEME

THEME = '../_global/theme'
EXTRA_TEMPLATES_PATHS=['templates']

# OUTPUT

OUTPUT_PATH = '../../prod/home/'

PLUGIN_PATH = '../plugins'
PLUGINS = ['textbox']
sys.path.insert(0, PLUGIN_PATH)

# Blogroll
LINKS =  False

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = False
FEED_DOMAIN = "http://databrewery.org"

# CUSTOM

ROOT_CUBES = "http://cubes.databrewery.org"
ROOT_BREWERY = "http://brewery.databrewery.org"
ROOT_BLOG = "http://blog.databrewery.org"