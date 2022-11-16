# -*- coding: UTF-8 -*-
"""
http-codes.py - HTTP status code lookup module for Sopel
Copyright 2016-2022, dgw
Licensed under the GPL v3.0 or later
"""
# Python 3.5+ required
import http
import re

# Sopel 7.1+ required
from sopel import plugin


def setup(bot):
    bot.memory['http_codes_map'] = {code.value: code.name for code in http.HTTPStatus}


def shutdown(bot):
    try:
        del bot.memory['http_codes_map']
    except KeyError:
        pass


@plugin.command('http')
@plugin.example('.http 418')
@plugin.output_prefix('[http-codes] ')
def http_code(bot, trigger):
    try:
        query = int(trigger.group(3))
    except ValueError:
        bot.reply("That doesn't seem to be a valid number.")
        return

    mapping = bot.memory['http_codes_map']

    if query not in mapping:
        bot.reply("I don't recognize that status code.")
        return

    code = getattr(http.HTTPStatus, mapping[query])

    bot.say("HTTP {code} {title}: {summary}".format(
        code=code.value, title=code.phrase, summary=code.description
    ))
