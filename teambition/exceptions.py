# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import six
from requests import RequestException


class TeambitionException(RequestException):

    def __str__(self):
        if six.PY2:
            return self.response.content
        else:
            return self.response.text

    __repr__ = __str__
