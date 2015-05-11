# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Events(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取日程

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

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/events/{0}'.format(id))

    def update(self, id, title=None, start_date=None, end_date=None,
               location=None, status=None, reminders=None, content=None):
        """
        更新日程

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

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/events/{0}/like'.format(id))

    def archive(self, id):
        """
        归档日程

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/events/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        取消归档日程

        :param id: 日程 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/events/{0}/archive'.format(id))

    def update_tags(self, id, tag_ids):
        """
        更新日程标签

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
