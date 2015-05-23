# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import six
from requests import RequestException


class TeambitionException(RequestException):

    def __init__(self, code=-1, message=None, client=None, *args, **kwargs):
        super(TeambitionException, self).__init__(*args, **kwargs)
        self.code = code
        self.message = message
        self.client = client

    def __str__(self):
        if six.PY2:
            return self.response.content
        else:
            return self.response.text

    __repr__ = __str__
