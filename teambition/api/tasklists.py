# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class TeambitionTasklists(TeambitionAPI):

    def get(self, id):
        """
        获取任务分组列表

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasklists/{0}'.format(id))

    def create(self, project_id, title, description=None):
        """
        新建任务分组

        :param project_id: 项目 ID
        :param title: 任务列表标题
        :param description: 可选，任务列表描述
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _projectId=project_id,
            title=title,
            description=description
        )
        return self._post(
            'api/tasklists',
            data=data
        )

    def delete(self, id):
        """
        删除任务分组

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasklists/{0}'.format(id))

    def update(self, id, title=None, description=None, is_archived=None):
        """
        更新任务分组

        :param id: 路径参数
        :param title: 可选，标题
        :param description: 可选，描述
        :param is_archived: 可选，是否归档
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            description=description,
            isArchived=is_archived
        )
        return self._put(
            'api/tasklists/{0}'.format(id),
            data=data
        )

    def update_stage_ids(self, id, stage_ids):
        """
        更新任务分组内阶段顺序

        :param id: 路径参数
        :param stage_ids: 阶段 ID 数组
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasklists/{0}/stageIds'.format(id),
            data={
                'stageIds': stage_ids
            }
        )

    def archive(self, id):
        """
        任务分组存档

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasklists/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        任务分组取消存档

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasklists/{0}/archive'.format(id))
