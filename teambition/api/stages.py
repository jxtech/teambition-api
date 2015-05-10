# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Stages(TeambitionAPI):

    def get(self, tasklist_id):
        """
        获取任务分组的阶段列表

        :param tasklist_id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/stages',
            params={
                '_tasklistId': tasklist_id
            }
        )

    def create(self, name, tasklist_id, prev_id):
        """
        新建阶段

        :param name: 阶段名称
        :param tasklist_id: 任务分组 ID
        :param prev_id: 前一个阶段的 ID
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/stages',
            data={
                'name': name,
                '_tasklistId': tasklist_id,
                '_prevId': prev_id
            }
        )

    def delete(self, id):
        """
        删除阶段（流程模式下，最后一个阶段无法被删除）

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/stages/{0}'.format(id))

    def update(self, id, name=None, is_locked=None):
        """
        更新阶段

        :param id: 路径参数
        :param name: 阶段名称
        :param is_locked: 锁定最后一个阶段
        """
        data = optionaldict(
            name=name,
            isLocked=is_locked
        )
        return self._put(
            'api/stages/{0}'.format(id),
            data=data
        )
