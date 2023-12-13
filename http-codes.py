"""
http-codes.py - HTTP status code lookup module for Sopel

Copyright 2016-2023, dgw
Portions based on code by SnoopJ, used with permission.

Licensed under the GPL v3.0 or later
"""
from __future__ import annotations

# Python 3.5+ required
from http import HTTPStatus
import random

# Sopel 7.1+ required
from sopel import plugin


@plugin.command('http')
@plugin.example('.http 418')
@plugin.output_prefix('[http-codes] ')
def http_code(bot, trigger):
    status = trigger.group(3)

    try:
        if not status:
            raise ValueError("Empty argument.")
        if len(status) != 3:
            raise ValueError("Incorrect length.")
        status = int(trigger.group(3))
    except ValueError:
        bot.reply(
            "{} is clearly not a valid HTTP status code."
            .format(status)
        )
        return

    try:
        status = HTTPStatus(status)
    except ValueError:
        bot.reply(
            "{} seems not to be a known HTTP status code."
            .format(status)
        )
        return

    desc = status.description
    if desc and not desc.endswith('.'):
        # stdlib is frustratingly inconsistent about punctuating the description
        desc += '.'

    bot.say("HTTP {code} — {title}{summary} https://http.{animal}/{code}.jpg".format(
        code=status.value,
        title=status.phrase,
        summary=(': ' + desc if desc else '.'),
        animal=random.choice(('cat', 'dog')),
    ))
