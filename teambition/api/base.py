# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import weakref


class APIDescriptor(object):

    def __init__(self, api):
        self.api = api

    def __get__(self, instance, instance_type=None):
        if instance is not None:
            if self.api._client is None:
                self.api._client = weakref.proxy(instance)
        return self.api


class TeambitionAPI(object):

    def __init__(self, client=None):
        self._client = client

    def _get(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.get(url, **kwargs)

    def _post(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(url, **kwargs)

    def _put(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.put(url, **kwargs)

    def _delete(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.delete(url, **kwargs)

    @property
    def access_token(self):
        return self._client.access_token

    @access_token.setter
    def access_token(self, value):
        self._client.access_token = value

    @property
    def client_id(self):
        return self._client.client_id

    @property
    def client_secret(self):
        return self._client.client_secret

    def add_to_class(self, klass, name):
        klass._api_endpoints[name] = self
        setattr(klass, name, APIDescriptor(self))
