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
