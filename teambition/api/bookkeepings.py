# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class BookKeepings(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取账簿信息

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping#bookkeeping-get

        :param id: 可选，账簿 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        assert id or project_id
        params = {}
        if id:
            endpoint = 'api/bookkeepings/{0}'.format(id)
        elif project_id:
            endpoint = 'api/bookkeepings'
            params['_projectId'] = project_id
        return self._get(endpoint, params=params)

    def update(self, id, approver_ids=None, display_fields=None):
        """
        更新账簿信息

        :param id: 账簿 ID
        :param approver_ids: 可选，审批者 ID 列表
        :param display_fields: 可选，字段列表
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _approverIds=approver_ids,
            displayFields=display_fields
        )
        return self._put(
            'api/bookkeepings/{0}'.format(id),
            data=data
        )
