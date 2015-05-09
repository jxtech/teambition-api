# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pickle
import unittest
try:
    import simplejson as json
except ImportError:
    import json

from teambition.utils import OptionalDict


class OptionalDictTestCase(unittest.TestCase):

    def test_init_with_none(self):
        d = OptionalDict(
            a=1,
            b=None
        )
        self.assertEqual(1, d['a'])
        self.assertNotIn('b', d)

    def test_init_with_dict_contains_none(self):
        d1 = {
            'a': 1,
            'b': None
        }
        d = OptionalDict(d1)
        self.assertEqual(1, d['a'])
        self.assertNotIn('b', d)

    def test_setitem_with_none(self):
        d = OptionalDict()
        d['a'] = 1
        d['b'] = None
        self.assertEqual(1, d['a'])
        self.assertNotIn('b', d)

    def test_setdefault_with_none(self):
        d = OptionalDict()
        d.setdefault('a', 1)
        d.setdefault('b', None)
        self.assertEqual(1, d['a'])
        self.assertNotIn('b', d)

    def test_json_dumps(self):
        d = OptionalDict(
            a=1,
            b=None
        )
        json.dumps(d)

    def test_pickle_dumps(self):
        d = OptionalDict(
            a=1,
            b=None
        )
        pickle.dumps(d)

    def test_pickle_loads(self):
        d = OptionalDict(
            a=1,
            b=None
        )
        s = pickle.dumps(d)
        pickle.loads(s)
