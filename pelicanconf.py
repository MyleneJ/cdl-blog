#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Toulibre'
SITENAME = u'Capitole du Libre - le blog'
SITEURL = 'http://localhost:8000'
SITEDESCRIPTION = u'L\'événement du Logiciel Libre à Toulouse'

# CDL infos
CDL_DATE = u'19-20 novembre 2016'
CDL_YEAR = u"2016"
CDL_TAG = u'#cdl%s' % CDL_YEAR
CDL_URL_BASE = 'https://%s.capitoledulibre.org/' % CDL_YEAR

# Theme
THEME = 'cdltheme-blog'
CSS_FILE = 'styles.min.css'

PATH = 'src'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['md_inline_extension']


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['liens']


ARTICLE_URL = '{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}-{date:%d}-{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}-{date:%d}-{slug}-{lang}.html'

# static paths will be copied under the same name
STATIC_PATHS = ["blog", "photos",]

# Menus
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Accueil', CDL_URL_BASE),
    ('Programme', '%sprogramme.html' % CDL_URL_BASE),
    ('Animations', '%s#animations' % CDL_URL_BASE),
    ('Partenaires', '%s#partenaires' % CDL_URL_BASE),
    ('Venir', '%s#venir' % CDL_URL_BASE),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  (
    ('Toulibre', 'http://www.toulibre.org/'),
    ('Ubuntu-fr', 'http://www.ubuntu-fr.org/'),
         )

# Social widget
SOCIAL = (
          ('Identica', 'identica', 'http://identi.ca/toulibreorg'),
          ('Twitter', 'twitter', 'https://twitter.com/toulibreorg'),
          ('Google+', 'google', 'https://plus.google.com/b/109128243242581226442/109128243242581226442/posts'),
          ('Lanyrd', 'lanyrd', 'http://lanyrd.com/2013/capitole-du-libre/'),
         )

TWITTER_USERNAME = 'Toulibreorg'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
