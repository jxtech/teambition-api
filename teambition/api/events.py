# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Events(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-get

        :param id: 可选，日程 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        endpoint = 'api/events'
        if id:
            endpoint = 'api/events/{0}'.format(id)
        elif project_id:
            endpoint = 'api/projects/{0}/events'.format(project_id)
        return self._get(endpoint)

    def create(self, project_id, title, start_date, end_date, location=None,
               status=None, reminders=None, content=None, recurrence=None,
               source_id=None, mode=None, visiable='members', tag_ids=None):
        """
        新建日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-create

        :param project_id: 项目 ID
        :param title: 内容
        :param start_date: 开始时间
        :param end_date: 结束时间
        :param location: 可选，地点
        :param status: 可选，状态
        :param reminders: 可选，提醒
        :param content: 可选，备注
        :param recurrence: 可选，重复日程规则列表
        :param source_id: 可选，需要派生的重复日程
        :param mode: 可选，新建模式，可选值为 single, after
        :param visiable: 可选，可见范围，默认为 members，可选 involves
        :param tag_ids: 可选，标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _projectId=project_id,
            title=title,
            startDate=start_date,
            endDate=end_date,
            location=location,
            status=status,
            reminders=reminders,
            content=content,
            recurrence=recurrence,
            _sourceId=source_id,
            mode=mode,
            visiable=visiable,
            tagIds=tag_ids
        )
        return self._post(
            'api/events',
            data=data
        )

    def delete(self, id):
        """
        删除日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-delete

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/events/{0}'.format(id))

    def update(self, id, title=None, start_date=None, end_date=None,
               location=None, status=None, reminders=None, content=None):
        """
        更新日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-update

        :param id: 日程 ID
        :param title: 内容
        :param start_date: 开始时间
        :param end_date: 结束时间
        :param location: 可选，地点
        :param status: 可选，状态
        :param reminders: 可选，提醒
        :param content: 可选，备注
        """
        data = optionaldict(
            title=title,
            startDate=start_date,
            endDate=end_date,
            location=location,
            status=status,
            reminders=reminders,
            content=content
        )
        return self._put(
            'api/events/{0}'.format(id),
            data=data
        )

    def like(self, id):
        """
        赞日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-like

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/events/{0}/like'.format(id))

    def archive(self, id):
        """
        归档日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-archive

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/events/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档日程

        详情请参考
        http://docs.teambition.com/wiki/events#events-unarchive

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/events/{0}/archive'.format(id))

    def update_tags(self, id, tag_ids):
        """
        更新日程标签

        详情请参考
        http://docs.teambition.com/wiki/events#events-update-tags

        :param id: 日程 ID
        :param tag_ids: 标签 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/events/{0}/tagIds'.format(id),
            data={
                'tagIds': tag_ids
            }
        )

    def get_tags(self, id):
        """
        获取日程标签列表

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/events/{0}/tags'.format(id))

    def remove_tag(self, id, tag_id):
        """
        移除标签

        :param id: 日程 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/events/{0}/tags/{1}'.format(id, tag_id))

    def add_tag(self, id, tag_id):
        """
        关联标签

        :param id: 日程 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/events/{0}/tags/{1}'.format(id, tag_id))

    def get_objectlinks(self, id):
        """
        获取日程关联的 objectlink 列表

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/events/{0}/objectlinks'.format(id))

    def create_objectlink(self, id, linked_id, linked_type):
        """
        关联对象

        :param id: 日程 ID
        :param linked_id: 关联对象 ID
        :param linked_type: 关联对象类型
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/objectlinks',
            data={
                '_parentId': id,
                'parentType': 'event',
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
        获取日程动态

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/activities',
            params={'_boundToObjectId': id}
        )
