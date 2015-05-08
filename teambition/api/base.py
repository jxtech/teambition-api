# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class TeambitionAPI(object):

    def __init__(self, client):
        self._client = client

    def get(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.get(url, **kwargs)

    def post(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, **kwargs)

    def put(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.put(url, **kwargs)

    def delete(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.delete(url, **kwargs)

    @property
    def access_token(self):
        return self._client.access_token

    @property
    def client_id(self):
        return self._client.client_id

    @property
    def client_secret(self):
        return self._client.client_secret
