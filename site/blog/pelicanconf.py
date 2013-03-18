#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys

AUTHOR = u'Andrej Sýkora'
SITENAME = u'Blog | Data Brewery'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_PAGES_ON_MENU = False

# PATHS


# URLS TO STATIC PAGES

AUTHOR_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORY_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# PAGINATIOn

DEFAULT_PAGINATION = 5

# THEME

THEME = '../_global/theme'
THEME_STATIC_PATHS = ['static']
EXTRA_TEMPLATES_PATHS=['theme/templates']

# OUTPUT

OUTPUT_PATH = '../../prod/blog/'


# Blogroll
LINKS =  False

# Social widget
SOCIAL = False

#PLUGIN_PATH = '../plugins'
#PLUGINS = ['textbox']
#sys.path.insert(0, PLUGIN_PATH)

