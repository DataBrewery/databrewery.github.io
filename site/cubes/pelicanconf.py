#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Andrej Sýkora'
SITENAME = u'Cubes | Data Brewery'
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
INDEX_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# THEME

THEME = './theme'
THEME_STATIC_PATHS = []

# OUTPUT

OUTPUT_PATH = '../../prod/cubes/'


# Blogroll
LINKS =  False

# Social widget
SOCIAL = False

DEFAULT_PAGINATION = False
