# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Organizations(TeambitionAPI):

    def get(self, id=None):
        """
        获取组织信息

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-get

        :param id: 可选，组织 ID
        :return: 提供 id 返回特定组织信息，否则返回用户相关组织列表
        """
        if id:
            endpoint = 'api/organizations/{0}'.format(id)
        else:
            endpoint = 'api/organizations'
        return self._get(endpoint)

    def create(self, name, description=None, logo=None,
               location=None, website=None):
        """
        创建新组织

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-create

        :param name: 组织名字
        :param description: 可选，描述
        :param logo: 可选，组织 logo
        :param location: 可选，组织所在地
        :param website: 可选，组织网站
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            description=description,
            logo=logo,
            location=location,
            website=website
        )
        return self._post(
            'api/organizations',
            data=data
        )

    def delete(self, id):
        """
        删除组织

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-delete

        :param id: 组织 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/organizations/{0}'.format(id))

    def update(self, id, name=None, description=None, logo=None,
               location=None, website=None):
        """
        更新组织信息

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-update

        :param id: 组织 ID
        :param name: 组织名字
        :param description: 可选，描述
        :param logo: 可选，组织 logo
        :param location: 可选，组织所在地
        :param website: 可选，组织网站
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            description=description,
            logo=logo,
            location=location,
            website=website
        )
        return self._put(
            'api/organizations/{0}'.format(id),
            data=data
        )

    def update_projects(self, id, project_ids):
        """
        更新组织内项目顺序

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-update_projectids

        :param id: 组织 ID
        :param project_ids: 项目 id 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/organizations/{0}/projectIds'.format(id),
            data={
                'projectIds': project_ids
            }
        )

    def add_members(self, id, email):
        """
        添加组织成员

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-add-member

        :param id: 组织 ID
        :param email: 邮箱或邮箱列表
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/organizations/{0}/members'.format(id),
            data={
                'email': email
            }
        )

    create_members = add_members  # Alias for add_members

    def remove_member(self, id, user_id):
        """
        删除组织成员

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-remove-member

        :param id: 组织 ID
        :param user_id: 成员 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/organizations/{0}/members/{1}'.format(id, user_id)
        )

    def get_members(self, id, user_id=None):
        """
        获取组织成员

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-get-member

        :param id: 组织 ID
        :param user_id: 可选，成员 ID
        :return: 返回的 JSON 数据包
        """
        if user_id:
            endpoint = 'api/organizations/{0}/members/{1}'.format(id, user_id)
        else:
            endpoint = 'api/organizations/{0}/members'.format(id)
        return self._get(endpoint)

    def get_recommend_members(self, id):
        """
        获取组织推荐成员列表

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-recommend-members

        :param id: 组织 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/organizations/{0}/recommendMembers'.format(id))

    def update_member_role(self, id, user_id, role_type):
        """
        更新组织成员角色

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-update-member

        :param id: 组织 ID
        :param user_id: 组织成员 ID
        :param role_type: 角色类型, 可选值 member, admin, owner
        """
        return self._put('api/organizations/{0}/members/{1}/{2}'.format(
            id,
            user_id,
            role_type
        ))

    def update_dividers(self, id, dividers):
        """
        更新组织项目分组

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-dividers

        :param id: 组织 ID
        :param dividers: 分组列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/organizations/{0}/dividers'.format(id),
            data={
                'dividers': dividers
            }
        )

    def get_statistic(self, id, base='member', start_date=None, end_date=None):
        """
        获取组织统计数据

        详情请参参考
        http://docs.teambition.com/wiki/orgs#orgs-statistic

        :param id: 组织 ID
        :param base: 可选，统计基于对象，可选值为 member, team, project，默认为 member
        :param start_date: 可选，开始日期，默认为一个月前
        :param end_date: 可选，结束日期，默认为今天
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            base=base,
            startDate=start_date,
            endDate=end_date
        )
        return self._get(
            'api/organizations/{0}/statistic'.format(id),
            params=params
        )

    def get_projects(self, id, project_id=None, is_archived=False):
        """
        获取组织项目

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-projects

        :param id: 组织 ID
        :param project_id: 可选，项目 ID
        :param is_archived: 可选，是否归档，默认为 False
        :return: 返回的 JSON 数据包
        """
        if project_id:
            endpoint = 'api/organizations/{0}/projects/{1}'.format(
                id,
                project_id
            )
        else:
            endpoint = 'api/organizations/{0}/projects'
        return self._get(
            endpoint,
            params={
                'isArchived': is_archived
            }
        )

    def quit(self, id):
        """
        退出组织

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-quit

        :param id: 组织 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/organizations/{0}/quit'.format(id))

    def resend_invitation(self, id, user_id):
        """
        重发邀请邮件

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-resend-invitation

        :param id: 组织 ID
        :param user_id: 成员 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/organizations/{0}/members{1}/resend'.format(id, user_id)
        )

    def get_member_tasks(self, id, member_id, start_date=None, is_done=None,
                         all=False, page=1, count=30):
        """
        获取组织成员任务

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-get-member-tasks

        :param id: 组织 ID
        :param member_id: 成员 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :param is_done: 可选，是否完成，默认为 False
        :param all: 可选，是否返回所有
        :param page:  可选，页码
        :param count: 可选，每页数量，默认为 30
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            startDate=start_date,
            isDone=is_done,
            all=all,
            page=page,
            count=count
        )
        return self._get(
            'api/organizations/{0}/members/{1}/tasks'.format(id, member_id),
            params=params
        )

    def get_member_events(self, id, member_id, start_date=None):
        """
        获取组织成员日程

        详情请参考
        http://docs.teambition.com/wiki/orgs#orgs-get-member-events

        :param id: 组织 ID
        :param member_id: 成员 ID
        :param start_date: 可选，起始日期，默认为当周的起始日期
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(startDate=start_date)
        return self._get(
            'api/organizations/{0}/members/{1}/events'.format(id, member_id),
            params=params
        )

    def get_webhooks(self, id):
        """
        获取组织 Webhook 列表

        :param id: 组织 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/organizations/{0}/hooks'.format(id))

    def create_webhook(self, id, callback_url, active=True, events=None):
        """
        新建组织 webhook

        :param id: 组织 ID
        :param callback_url: 回调地址，Teambition通过HEAD请求进行测试, 有事件被触发将发送POST请求
        :param active: 可选，是否激活，默认为 True
        :param events: 可选，事件列表，默认为空
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            callbackURL=callback_url,
            active=active,
            events=events
        )
        return self._post(
            'api/organizations/{0}/hooks'.format(id),
            data=data
        )

    def update_webhook(self, id, hook_id, callback_url=None, active=True,
                       events=None, add_events=None, remove_events=None):
        """
        更新组织 webhook

        :param id: 组织 ID
        :param hook_id: webhook ID
        :param callback_url: 可选，回调地址，Teambition通过HEAD请求进行测试, 有事件被触发将发送POST请求
        :param active: 可选，是否激活，默认为 True
        :param events: 可选，事件列表，默认为空
        :param add_events: 可选，追加新的事件进去
        :param remove_events: 可选，从原有的事件列表中移除
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            callbackURL=callback_url,
            active=active,
            events=events,
            addEvents=add_events,
            removeEvents=remove_events
        )
        return self._put(
            'api/organizations/{0}/hooks/{1}'.format(id, hook_id),
            data=data
        )

    def delete_webhook(self, id, hook_id):
        """
        删除组织 webhook

        :param id: 组织 ID
        :param hook_id: webhook ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/organizations/{0}/hooks/{1}'.format(id, hook_id)
        )

    def get_supported_webhooks(self):
        """
        获取组织支持的 webhook 列表

        :return: 返回的 JSON 数据包
        """
        return self._get('api/organizations/webhooks')

    def get_webhook_value_format(self, event):
        """
        获取组织 webhook 的返回值格式

        :param event: 事件类型
        :return: 返回的 JSON 数据包
        """
        return self._get('api/organizations/webhooks/{0}'.format(event))
