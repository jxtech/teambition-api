# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Collections(TeambitionAPI):

    def get(self, id=None, parent_id=None):
        """
        获取文件集

        :param id: 可选，文件集 ID
        :param parent_id: 可选，父级 ID
        :return: 返回的 JSON 数据包
        """
        if id:
            endpoint = 'api/collections/{0}'.format(id)
            params = {}
        elif parent_id:
            endpoint = 'api/collections'
            params = {'_parentId': parent_id}
        return self._get(endpoint, params=params)

    def create(self, title, project_id, parent_id=None, description=None,
               collection_type=None, color=None):
        """
        新建文件集

        :param title: 文件集标题
        :param project_id: 项目 ID
        :param parent_id: 可选，父级 ID，默认为项目 ID
        :param description: 可选，描述
        :param collection_type: 可选，类型，默认为空，保留字段：default, root
        :param color: 可选，颜色，默认为空
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            _projectId=project_id,
            _parentId=parent_id or project_id,
            description=description,
            collectionType=collection_type,
            color=color
        )
        return self._post(
            'api/collections',
            data=data
        )

    def delete(self, id):
        """
        删除文件集

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/collections/{0}'.format(id))

    def update(self, id, title=None, parent_id=None, description=None,
               color=None, is_archived=None):
        """
        更新文件集

        :param id: 文件集 ID
        :param title: 可选，文件集标题
        :param parent_id: 可选，父级 ID
        :param description: 可选，描述
        :param color: 可选，颜色，默认为空
        :param is_archived: 可选，是否归档
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            _parentId=parent_id,
            description=description,
            color=color,
            isArchived=is_archived
        )
        return self._put(
            'api/collections/{0}'.format(id),
            data=data
        )

    def archive(self, id):
        """
        归档文件集

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/collections/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        归档文件集

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/collections/{0}/archive'.format(id))
