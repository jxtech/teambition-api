# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Teams(TeambitionAPI):

    def get(self, id=None, organization_id=None, project_id=None):
        """
        获取团队

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get

        :param id: 可选，团队 ID
        :param organization_id: 可选，组织 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        if id:
            endpoint = 'api/teams/{0}'.format(id)
        else:
            endpoint = 'api/teams'

        params = optionaldict(
            _organizationId=organization_id,
            _projectId=project_id
        )
        return self._get(endpoint, params=params)

    def create(self, name, organization_id=None):
        """
        新建团队

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-create

        :param name: 团队名称
        :param organization_id: 可选，组织ID
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            _organizationId=organization_id
        )
        return self._post(
            'api/teams',
            data=data
        )

    def delete(self, id):
        """
        删除团队

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-delete

        :param id: 团队 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/teams/{0}'.format(id))

    def update(self, id, name):
        """
        更新团队

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-update

        :param id: 团队 ID
        :param name: 团队名称
        """
        return self._put(
            'api/teams/{0}'.format(id),
            data={
                'name': name
            }
        )

    def bind_project(self, id, project_id):
        """
        关联团队与项目

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-bind-project

        :param id: 团队 ID
        :param project_id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/teams/{0}/projects/{1}'.format(id, project_id))

    def unbind_project(self, id, project_id):
        """
        取消关联团队与项目

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-unbind-project

        :param id: 团队 ID
        :param project_id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/teams/{0}/projects/{1}'.format(id, project_id)
        )

    def add_members(self, id, email):
        """
        添加团队成员

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-add-member

        :param id: 团队 ID
        :param email: 邮箱或邮箱列表
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/teams/{0}/members'.format(id),
            data={
                'email': email
            }
        )

    create_members = add_members

    def remove_member(self, id, user_id):
        """
        删除团队成员

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-remove-member

        :param id: 团队 ID
        :param user_id: 成员 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/teams/{0}/members/{1}'.format(id, user_id)
        )

    def get_members(self, id, user_id=None):
        """
        获取团队成员

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get-member

        :param id: 团队 ID
        :param user_id: 可选，用户 ID
        :return: 返回的 JSON 数据包
        """
        if user_id:
            endpoint = 'api/teams/{0}/members/{1}'.format(id, user_id)
        else:
            endpoint = 'api/teams/{0}/members'.format(id)
        return self._get(endpoint)

    def quit(self, id):
        """
        退出团队

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-quit

        :param id: 团队 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/teams/{0}/quit'.format(id))

    def get_memeber_tasks(self, id, member_id, start_date=None):
        """
        获取团队成员任务

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get-team-member-tasks

        :param id: 团队 ID
        :param member_id: 成员 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(startDate=start_date)
        return self._get(
            'api/teams/{0}/members/{1}/tasks'.format(id, member_id),
            params=params
        )

    def get_member_events(self, id, member_id, start_date=None):
        """
        获取团队成员日程

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get-team-member-events

        :param id: 团队 ID
        :param member_id: 成员 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(startDate=start_date)
        return self._get(
            'api/teams/{0}/members/{1}/events'.format(id, member_id),
            params=params
        )

    def get_tasks(self, id, start_date=None):
        """
        获取团队周任务

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get-team-week-tasks

        :param id: 团队 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(startDate=start_date)
        return self._get(
            'api/teams/{0}/tasks'.format(id),
            params=params
        )

    def get_events(self, id, start_date=None):
        """
        获取团队周日程

        详情请参考
        http://docs.teambition.com/wiki/teams#teams-get-team-week-events

        :param id: 团队 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(startDate=start_date)
        return self._get(
            'api/teams/{0}/events'.format(id),
            params=params
        )
