# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tags(TeambitionAPI):

    def get(self, id):
        """
        获取标签信息

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-get

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}'.format(id))

    def create(self, name, project_id):
        """
        新建标签

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-create

        :param name: 标签名称
        :param project_id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/tags',
            data={
                'name': name,
                '_projectId': project_id
            }
        )

    def delete(self, id):
        """
        删除标签

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-delete

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tags/{0}'.format(id))

    def update(self, id, name, color=None):
        """
        更新标签

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-update

        :param id: 标签 ID
        :param name: 标签名称
        :param color: 可选，颜色标记
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            color=color
        )
        return self._put(
            'api/tags/{0}'.format(id),
            data=data
        )

    def archive(self, id):
        """
        归档标签

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-archive

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tags/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档标签

        详情请参考
        http://docs.teambition.com/wiki/tags#tags-unarchive

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tags/{0}/archive'.format(id))

    def get_tasks(self, id):
        """
        获取标签关联的任务

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}/tasks'.format(id))

    def get_posts(self, id):
        """
        获取标签关联的分享

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}/posts'.format(id))

    def get_events(self, id):
        """
        获取标签关联的日程

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}/events'.format(id))

    def get_works(self, id):
        """
        获取标签关联的文件

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}/works'.format(id))
