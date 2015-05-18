# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import hashlib

from teambition.utils import to_binary
from teambition.api.base import TeambitionAPI


class Webhooks(TeambitionAPI):

    def verify_signature(self, sign, timestamp, nonce):
        """
        校验 webhook 签名

        :param sign: 签名
        :param timestamp: 时间戳
        :param nonce: nonce
        :return: 验证通过返回 True 否则 False
        """
        keys = [
            to_binary(self.client_secret),
            to_binary(timestamp),
            to_binary(nonce),
        ]
        keys.sort()
        keys_str = b''.join(keys)
        signature = hashlib.sha1(keys_str).hexdigest()
        return to_binary(sign) == signature
