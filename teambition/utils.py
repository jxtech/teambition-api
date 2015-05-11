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
        kwargs[b'object_hook'] = self.datetime_object_hook
        super(JSONDecoder, self).__init__(*args, **kwargs)

    def datetime_object_hook(self, obj):
        for key, value in six.iteritems(obj):
            if not isinstance(value, six.string_types):
                continue
            if len(value) not in (10, 18, 22, 24, 26):
                continue
            try:
                value = dateutil.parser.parse(value)
            except ValueError:
                continue
            obj[key] = value
        return obj
