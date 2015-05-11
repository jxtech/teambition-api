# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from teambition.api.base import TeambitionAPI


class Tags(TeambitionAPI):

    def get(self, id):
        """
        获取标签信息

        :param id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tags/{0}'.format(id))

    def create(self, name, project_id):
        """
        新建标签

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
