# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Collections(TeambitionAPI):

    def get(self, id=None, parent_id=None):
        """
        获取文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-get

        :param id: 可选，文件集 ID
        :param parent_id: 可选，父级 ID
        :return: 返回的 JSON 数据包
        """
        params = {}
        if id:
            endpoint = 'api/collections/{0}'.format(id)
        elif parent_id:
            endpoint = 'api/collections'
            params['_parentId'] = parent_id
        return self._get(endpoint, params=params)

    def create(self, title, project_id, parent_id=None, description=None,
               color=None):
        """
        新建文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-create

        :param title: 文件集标题
        :param project_id: 项目 ID
        :param parent_id: 可选，父级 ID，默认为项目 ID
        :param description: 可选，描述
        :param color: 可选，颜色，默认为空
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            _projectId=project_id,
            _parentId=parent_id or project_id,
            description=description,
            color=color
        )
        return self._post(
            'api/collections',
            data=data
        )

    def delete(self, id):
        """
        删除文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-delete

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/collections/{0}'.format(id))

    def update(self, id, title=None, parent_id=None, description=None,
               color=None):
        """
        更新文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-update

        :param id: 文件集 ID
        :param title: 可选，文件集标题
        :param parent_id: 可选，父级 ID
        :param description: 可选，描述
        :param color: 可选，颜色，默认为空
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

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-archive

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/collections/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        归档文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-unarchive

        :param id: 文件集 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/collections/{0}/archive'.format(id))

    def move(self, id, parent_id):
        """
        移动文件集

        详情请参考
        http://docs.teambition.com/wiki/collections#collections-move

        :param id: 文件集 ID
        :param parent_id: 新的父级目录 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/collections/{0}/move'.format(id),
            data={
                '_parentId': parent_id
            }
        )
