# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import weakref
try:
    import simplejson as json
except ImportError:
    import json
import requests

from teambition import api


class Teambition(object):
    """
    Teambition API 客户端
    """

    API_BASE_URL = 'https://api.teambition.com/'

    def __init__(self, client_id, client_secret, access_token=None):
        """
        初始化 Teambition API Client

        :param client_id: 申请应用时分配的 client_id
        :param client_secret: 申请应用时分配的 client_secret
        :param access_token: 可选，access_token
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = access_token

        weak_self = weakref.proxy(self)
        # API endpoints
        self.oauth = api.OAuth(weak_self)
        self.projects = api.Projects(weak_self)
        self.tasklists = api.Tasklists(weak_self)
        self.stages = api.Stages(weak_self)
        self.tasks = api.Tasks(weak_self)
        self.users = api.Users(weak_self)
        self.organizations = api.Organizations(weak_self)
        self.stagetemplates = api.StageTemplates(weak_self)
        self.teams = api.Teams(weak_self)

    def _request(self, method, endpoint, **kwargs):
        if not endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=endpoint
            )
        else:
            url = endpoint

        if 'params' not in kwargs:
            kwargs['params'] = {}
        if 'access_token' not in kwargs['params'] and self.access_token:
            kwargs['params']['access_token'] = self.access_token
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body

        if 'header' not in kwargs:
            kwargs['header'] = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth2 {0}'.format(self.access_token),
            }

        res = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        res.raise_for_status()
        result = res.json()
        return result

    def get(self, endpoint, **kwargs):
        return self._request('get', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request('post', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request('put', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)

    @property
    def access_token(self):
        """
        获取 access_token

        :return: access_token
        """
        return self._access_token

    @access_token.setter
    def access_token(self, token):
        """
        设置 access_token

        :param token: access_token
        """
        self._access_token = token
