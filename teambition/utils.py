# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime
try:
    import simplejson as json
except ImportError:
    import json

import six
import dateutil.parser


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.date):
            encoded = obj.isoformat()
        elif isinstance(obj, datetime.datetime):
            encoded = obj.isoformat()
        else:
            encoded = super(JSONEncoder, self).default(obj)
        return encoded


class JSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        kwargs['object_hook'] = self.datetime_object_hook
        super(JSONDecoder, self).__init__(*args, **kwargs)

    def datetime_object_hook(self, obj):
        for key, value in six.iteritems(obj):
            if not isinstance(value, six.string_types):
                continue
            # TODO: a better way to identify ISO datetime
            if len(value) not in (10, 18, 20, 22, 24, 25, 26):
                continue
            try:
                value = dateutil.parser.parse(value)
            except (TypeError, ValueError, OverflowError):
                continue
            obj[key] = value
        return obj


def to_text(value, encoding='utf-8'):
    """Convert value to unicode, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return ''
    if isinstance(value, six.text_type):
        return value
    if isinstance(value, six.binary_type):
        return value.decode(encoding)
    return six.text_type(value)


def to_binary(value, encoding='utf-8'):
    """Convert value to binary string, default encoding is utf-8

    :param value: Value to be converted
    :param encoding: Desired encoding
    """
    if not value:
        return b''
    if isinstance(value, six.binary_type):
        return value
    if isinstance(value, six.text_type):
        return value.encode(encoding)
    return six.binary_type(value)
