# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Stages(TeambitionAPI):

    def get(self, tasklist_id):
        """
        获取任务分组的阶段列表

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-get

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

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-create

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

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-delete

        :param id: 阶段 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/stages/{0}'.format(id))

    def update(self, id, name=None, is_locked=None):
        """
        更新阶段

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-update

        :param id: 阶段 ID
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

    def get_tasks(self, id, executor_id=None, is_done=False, all=False,
                  page=1, limit=30, **kwargs):
        """
        获取阶段下得任务列表

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-get-tasks

        :param id: 阶段 ID
        :param executor_id: 可选，执行者 ID
        :param is_done: 可选，是否已完成，默认为 False
        :param all: 可选，所有类型，包括完成与未完成
        :param page: 可选，页码，默认为 1
        :param limit: 可选，每页数量，默认为 30，最大值为 1000
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            isDone=is_done,
            _executorId=executor_id,
            all=all,
            page=page,
            limit=limit,
            **kwargs
        )
        return self._get(
            'api/stages/{0}/tasks'.format(id),
            params=params
        )
