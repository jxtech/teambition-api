# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import requests
from furl import furl

from teambition.api.base import TeambitionAPI


class OAuth(TeambitionAPI):

    def get_authorize_url(self, redirect_uri, state='', lang='zh'):
        """
        获取授权地址

        详情请参考
        http://docs.teambition.com/wiki/oauth2#oauth2-authorize

        :param redirect_uri: 授权回调地址
        :param state: 原样返回给客户端
        :param lang: 语言类型，可选 zh, en，默认为 zh
        :return: 授权地址
        """
        oauth2_url = furl('https://account.teambition.com/oauth2/authorize')
        oauth2_url.add(args={
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'state': state,
            'lang': lang
        })
        return oauth2_url.url

    def fetch_access_token(self, code, grant_type='code'):
        """
        根据 code 获取 access_token

        详情请参考
        http://docs.teambition.com/wiki/oauth2#oauth2-access_token

        :param code: 授权完成返回的 code 参数值
        :param grant_type: 固定值为 code
        :return: access_token 值
        """
        res = self._post(
            'oauth2/access_token',
            data={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': code,
                'grant_type': grant_type
            }
        )
        token = res['access_token']
        self._client._access_token = token
        return token

    get_access_token = fetch_access_token  # Alias

    def check(self, access_token=None):
        """
        验证 access_token 是否合法

        详情请参考
        http://docs.teambition.com/wiki/oauth2#oauth2-check

        :param access_token: 可选，access_token
        :return: 返回的 JSON 数据包
        """
        token = access_token or self.access_token
        headers = {
            'Authorization': 'OAuth2 {0}'.format(token),
        }
        valid = True
        try:
            self._get(
                'api/applications/{0}/tokens/check'.format(self.client_id),
                headers=headers
            )
        except requests.HTTPError:
            valid = False

        return valid
