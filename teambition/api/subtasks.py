# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Subtasks(TeambitionAPI):

    def get(self, id=None, task_id=None):
        """
        获取子任务，子任务 ID 和任务 ID 参数只能有一个存在

        :param id: 可选，子任务 ID
        :param task_id: 可选，任务 ID
        :return: 返回的 JSON 数据包
        """
        assert id or task_id, 'id 和 task_id 必须提供其中之一'
        if id:
            endpoint = 'api/subtasks/{0}'.format(id)
        elif task_id:
            endpoint = 'api/tasks/{0}/subtasks'.format(task_id)
        return self._get(endpoint)

    def create(self, content, task_id, executor_id=None):
        """
        新建子任务

        :param content: 子任务内容
        :param task_id: 任务 ID
        :param executor_id: 可选，执行者 ID，默认为空
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            content=content,
            _taskId=task_id,
            _executorId=executor_id
        )
        return self._post(
            'api/subtasks',
            data=data
        )

    def delete(self, id):
        """
        删除子任务

        :param id: 子任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/subtasks/{0}'.format(id))

    def update(self, id, content=None, is_done=None, executor_id=None):
        """
        更新子任务

        :param id: 子任务 ID
        :param content: 可选，子任务内容
        :param is_done: 可选，子任务完成状态
        :param executor_id: 可选，执行者 ID
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            content=content,
            isDone=is_done,
            _executorId=executor_id
        )
        return self._put(
            'api/subtasks/{0}'.format(id),
            data=data
        )

    def transform(self, id, do_link=False, do_linked=False):
        """
        转换成任务

        :param id: 子任务 ID
        :param do_link: 是否关联转出的任务，默认为 False
        :param do_linked: 是否会被转出的任务关联，默认为 False
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            doLink=do_link,
            doLinked=do_linked
        )
        return self._put(
            'api/subtasks/{0}/transform',
            data=data
        )
