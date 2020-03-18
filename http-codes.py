# -*- coding: UTF-8 -*-
"""
http-codes.py - HTTP status code lookup module for Sopel
Copyright 2016, dgw
Licensed under the GPL v3.0 or later
"""

from __future__ import unicode_literals
from sopel.module import commands, example
import bleach
from lxml import etree
import requests
import re

api_url = 'https://httpstatuses.com/%s'


@commands('http')
@example('.http 418')
def http_code(bot, trigger):
    query = trigger.group(3) or None
    bot.say("[HTTP Status] %s" % fetch_result(query))


def fetch_result(query):
    if not query:
        return "You must provide a HTTP status code to look up."
    if not re.match('^[1-5]\\d{2}$', query):
        return "Invalid HTTP status code: %s" % query
    url = api_url % query
    try:
        r = requests.get(url=url, timeout=(10.0, 4.0))
    except requests.exceptions.ConnectTimeout:
        return "Connection timed out."
    except requests.exceptions.ConnectionError:
        return "Couldn't connect to server."
    except requests.exceptions.ReadTimeout:
        return "Server took too long to send data."
    if r.status_code == 404:
        return "Unknown HTTP status code: %s" % query
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "HTTP error: " + e.message

    page = etree.HTML(r.content)
    title = bleach.clean(etree.tostring(page.xpath('/html/body/article/h1[1]')[0], encoding='unicode'), tags=[], strip=True)
    summary = bleach.clean(
        re.sub('<a href="#ref-\\d+">.*?<\\/a>', '', etree.tostring(page.xpath('/html/body/article/p[1]')[0], encoding='unicode')), tags=[],
        strip=True)
    return "{title}: {summary} — {link}".format(title=title, summary=summary, link=url)
