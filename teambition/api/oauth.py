# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import requests
from furl import furl

from teambition.api.base import TeambitionAPI


class TeambitionOAuth(TeambitionAPI):

    def get_authorize_url(self, redirect_uri, state='', lang='zh'):
        oauth2_url = furl('https://account.teambition.com/oauth2/authorize')
        oauth2_url.add(args={
            'client_id': self.client_id,
            'redirect_uri': redirect_uri,
            'state': state,
            'lang': lang
        })
        return oauth2_url.url

    def fetch_access_token(self, code, grant_type='code'):
        res = self.post(
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
