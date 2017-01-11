# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tasks(TeambitionAPI):

    def get(self, id, detail_type=None):
        """
        获取任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-get-by-id

        :param id: 任务 ID
        :param detail_type: 可选值complete, 则会包含子任务详细信息
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            detailType=detail_type
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

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-create

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
            tagIds=tag_ids
        )
        return self._post(
            'api/tasks',
            data=data
        )

    def delete(self, id):
        """
        删除任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-delete

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasks/{0}'.format(id))

    def update(self, id, content=None, tasklist_id=None, stage_id=None,
               executor_id=None, involve_members=None, due_date=None,
               priority=None, recurrence=None, is_done=None, note=None):
        """
        更新任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update

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

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-like

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasks/{0}/like'.format(id))

    def fork(self, id, stage_id, do_link=False, do_linked=False):
        """
        复制任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-fork

        :param id: 任务 ID，任务 ID
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

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-move

        :param id: 任务 ID
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

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-archive

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasks/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档任务

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-unarchive

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasks/{0}/archive'.format(id))

    def update_subtasks(self, id, subtask_ids):
        """
        更新任务内子任务顺序

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update-subtaskids

        :param id: 任务 ID
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

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update-tags

        :param id: 任务 ID
        :param tag_ids: 标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/tagIds'.format(id),
            data={
                'tagIds': tag_ids
            }
        )

    def update_content(self, id, content):
        """
        更新任务内容

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update_content

        :param id: 任务 ID
        :param content: 任务内容
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/content'.format(id),
            data={
                'content': content
            }
        )

    def update_note(self, id, note):
        """
        更新任务备注

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update_note

        :param id: 任务 ID
        :param note: 任务备注
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/note'.format(id),
            data={
                'note': note
            }
        )

    def update_executor(self, id, executor_id):
        """
        更新任务执行者

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update_executor

        :param id: 任务 ID
        :param executor_id: 执行者 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/_executorId'.format(id),
            data={
                '_executorId': executor_id
            }
        )

    def update_status(self, id, is_done):
        """
        更新任务状态

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update_status

        :param id: 任务 ID
        :param is_done: 是否已经完成
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/isDone'.format(id),
            data={
                'isDone': is_done
            }
        )

    def update_duedate(self, id, duedate):
        """
        更新截止日期

        详情请参考
        http://docs.teambition.com/wiki/tasks#tasks-update_duedate

        :param id: 任务 ID
        :param duedate: 截止日期，请使用 ISOString 格式，置空请传 None
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasks/{0}/dueDate'.format(id),
            data={
                'dueDate': duedate
            }
        )

    def get_subtasks(self, id):
        """
        获取子任务列表

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/{0}/subtasks'.format(id))

    def get_tags(self, id):
        """
        获取任务标签列表

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/{0}/tags'.format(id))

    def remove_tag(self, id, tag_id):
        """
        移除标签

        :param id: 任务 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasks/{0}/tags/{1}'.format(id, tag_id))

    def add_tag(self, id, tag_id):
        """
        关联标签

        :param id: 任务 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/tasks/{0}/tags/{1}'.format(id, tag_id))

    def get_objectlinks(self, id):
        """
        获取任务关联的 objectlink 列表

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/{0}/objectlinks'.format(id))

    def create_objectlink(self, id, linked_id, linked_type):
        """
        关联对象

        :param id: 任务 ID
        :param linked_id: 关联对象 ID
        :param linked_type: 关联对象类型
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/objectlinks',
            data={
                '_parentId': id,
                'parentType': 'task',
                '_linkedId': linked_id,
                'linkedType': linked_type
            }
        )

    def link_task(self, id, linked_id):
        """
        关联任务

        :param id: 任务 ID
        :param linked_id: 关联任务 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'task')

    def link_post(self, id, linked_id):
        """
        关联分享

        :param id: 任务 ID
        :param linked_id: 关联分享 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'post')

    def link_event(self, id, linked_id):
        """
        关联日程

        :param id: 任务 ID
        :param linked_id: 关联日程 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'event')

    def link_work(self, id, linked_id):
        """
        关联文件

        :param id: 任务 ID
        :param linked_id: 关联文件 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'work')

    def get_activities(self, id):
        """
        获取任务动态

        :param id: 任务 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/{0}/activities'.format(id))

    def import_tasks(self, tasklist_id, tasks, stage_id=None, executor_id=None,
                     involve_members=None, due_date=None, visiable=None):
        """
        批量导入任务

        一次允许50条, 仅支持任务标题列表

        :param tasklist_id: 任务分组 ID
        :param tasks: 任务内容列表
        :param stage_id: 可选，阶段 ID，默认分组的第一个阶段
        :param executor_id: 可选，执行者 ID
        :param involve_members: 可选，参与者列表
        :param due_date: 可选，截止日期
        :param visiable: 可选，可见状态
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            tasks=tasks,
            _stageId=stage_id,
            _executorId=executor_id,
            involveMembers=involve_members,
            dueDate=due_date,
            visiable=visiable,
        )
        return self._post(
            'api/tasklists/{0}/import_tasks'.format(tasklist_id),
            data=data
        )
