# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tasks(TeambitionAPI):

    def get(self, id, is_done=False, all=None,
            page=1, count=30, due_date=None):
        """
        获取任务

        :param id: 路径参数
        :param is_done: 可选，是否已完成，默认为 False
        :param all: 可选，若提供此参数则抓取所以符合条件的任务
        :param page: 可选，页码，与 count 配合使用
        :param count: 可选，每页数据数量，默认为 30
        :param due_date: 可选，截止日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            isDone=is_done,
            all=all,
            page=page,
            count=count,
            dueDate=due_date
        )
        return self._get(
            'api/tasks/{0}'.format(id),
            params=params
        )

    def create(self, content, tasklist_id, stage_id=None, executor_id=None,
               involve_members=None, due_date=None, priority=None,
               recurrence=None, tag_ids=None):
        """
        创建任务

        :param content: 任务内容
        :param tasklist_id: 任务分组 ID
        :param stage_id: 可选，阶段 ID，默认为任务分组的第一个阶段
        :param executor_id: 可选，执行者 ID，默认为空
        :param involve_members: 可选，参与者 ID 数组，默认为创建者和执行者
        :param due_date: 可选，截止日期
        :param priority: 可选，优先级，可选值为 0，1，2，对应普通、紧急、非常紧急
        :param recurrence: 可选，重复规则列表
        :param tag_ids: 可选，标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            content=content,
            _tasklistId=tasklist_id,
            _stageId=stage_id,
            _executorId=executor_id,
            involveMembers=involve_members,
            dueDate=due_date,
            priority=priority,
            recurrence=recurrence,
            tag_ids=tag_ids
        )
        return self._post(
            'api/tasks',
            data=data
        )

    def delete(self, id):
        """
        删除任务

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasks/{0}'.format(id))

    def update(self, id, content=None, tasklist_id=None, stage_id=None,
               executor_id=None, involve_members=None, due_date=None,
               priority=None, recurrence=None, is_done=None, note=None):
        """
        更新任务

        :param content: 任务内容
        :param tasklist_id: 任务分组 ID
        :param stage_id: 可选，阶段 ID，默认为任务分组的第一个阶段
        :param executor_id: 可选，执行者 ID，默认为空
        :param involve_members: 可选，参与者 ID 数组，默认为创建者和执行者
        :param due_date: 可选，截止日期
        :param priority: 可选，优先级，可选值为 0，1，2，对应普通、紧急、非常紧急
        :param recurrence: 可选，重复规则列表
        :param is_done: 可选，完成状态
        :param note: 可选，笔记
        """
        data = optionaldict(
            content=content,
            _tasklistId=tasklist_id,
            _stageId=stage_id,
            _executorId=executor_id,
            involveMembers=involve_members,
            dueDate=due_date,
            priority=priority,
            recurrence=recurrence,
            isDone=is_done,
            note=note
        )
        return self._put(
            'api/tasks/{0}'.format(id),
            data=data
        )

    def like(self, id):
        """
        赞任务

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasks/{0}/like'.format(id))

    def fork(self, id, stage_id, do_link=False, do_linked=False):
        """
        复制任务

        :param id: 路径参数，任务 ID
        :param stage_id: 目的阶段 ID
        :param do_link: 可选，是否关联复制出的任务，默认为 False
        :param do_linked: 可选，是否会被复制出的任务关联，默认为 False
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _stageId=stage_id,
            doLink=do_link,
            doLinked=do_linked
        )
        return self._put(
            'api/tasks/{0}/fork'.format(id),
            data=data
        )

    def move(self, id, stage_id):
        """
        移动任务

        :param id: 路径参数
        :param stage_id: 目的阶段 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/move'.format(id),
            data={
                '_stageId': stage_id
            }
        )

    def archive(self, id):
        """
        归档任务

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasks/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档任务

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasks/{0}/archive'.format(id))

    def update_subtasks(self, id, subtask_ids):
        """
        更新任务内子任务顺序

        :param id: 路径参数
        :param subtask_ids: 子任务 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/subtaskIds'.format(id),
            data={
                'subtaskIds': subtask_ids
            }
        )

    def update_tags(self, id, tag_ids):
        """
        更新任务标签

        :param id: 路径参数
        :param tag_ids: 标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/tagIds'.format(id),
            data={
                'tagIds': tag_ids
            }
        )
