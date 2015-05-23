# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import copy
try:
    import simplejson as json
except ImportError:
    import json

import requests

from teambition import api
from teambition.api.base import TeambitionAPI
from teambition.utils import JSONEncoder, JSONDecoder
from teambition.exceptions import TeambitionException


class Teambition(object):
    """
    Teambition API 客户端
    """

    API_BASE_URL = 'https://api.teambition.com/'

    # API endpoints
    oauth = api.OAuth()
    """:doc:`oauth`"""
    projects = api.Projects()
    """:doc:`projects`"""
    tasklists = api.Tasklists()
    """:doc:`tasklists`"""
    stages = api.Stages()
    """:doc:`stages`"""
    tasks = api.Tasks()
    """:doc:`tasks`"""
    users = api.Users()
    """:doc:`users`"""
    organizations = api.Organizations()
    """:doc:`organizations`"""
    stagetemplates = api.StageTemplates()
    """:doc:`stagetemplates`"""
    teams = api.Teams()
    """:doc:`teams`"""
    subtasks = api.Subtasks()
    """:doc:`subtasks`"""
    messages = api.Messages()
    """:doc:`messages`"""
    posts = api.Posts()
    """:doc:`posts`"""
    collections = api.Collections()
    """:doc:`collections`"""
    works = api.Works()
    """:doc:`works`"""
    events = api.Events()
    """:doc:`events`"""
    tags = api.Tags()
    """:doc:`tags`"""
    objectlinks = api.ObjectLinks()
    """:doc:`objectlinks`"""
    activities = api.Activities()
    """:doc:`activities`"""
    webhooks = api.Webhooks()
    """:doc:`webhooks`"""
    bookkeepings = api.BookKeepings()
    """:doc:`bookkeepings`"""
    entrycategories = api.EntryCategories()
    """doc:`entrycategories`"""
    entries = api.Entries()
    """:doc:`entries`"""

    def __new__(cls, *args, **kwargs):
        self = super(Teambition, cls).__new__(cls)
        for name, tb_api in self.__class__.__dict__.items():
            if isinstance(tb_api, TeambitionAPI):
                tb_api = copy.deepcopy(tb_api)
                tb_api._client = self
                setattr(self, name, tb_api)
        return self

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

    def _request(self, method, endpoint, **kwargs):
        if not endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=endpoint
            )
        else:
            url = endpoint

        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(
                kwargs['data'],
                ensure_ascii=False,
                cls=JSONEncoder
            )
            body = body.encode('utf-8')
            kwargs['data'] = body

        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
        if 'Authorization' not in kwargs['headers']:
            kwargs['headers']['Authorization'] = 'OAuth2 {0}'.format(
                self.access_token
            )

        res = requests.request(
            method=method,
            url=url,
            **kwargs
        )
        # Error handling, reraise RequestException as TeambitionException
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            code = -1
            message = None
            if reqe.response.text:
                try:
                    errinfo = json.loads(reqe.response.text)
                    code = errinfo['code']
                    message = errinfo['message']
                except ValueError:
                    pass
            raise TeambitionException(
                code=code,
                message=message,
                client=self,
                request=reqe.request,
                response=reqe.response
            )

        result = res.json(cls=JSONDecoder)
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
