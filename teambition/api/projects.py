# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime

import pytz
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Projects(TeambitionAPI):

    def get(self, id=None, team_id=None, is_archived=False):
        """
        获取项目信息

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-get

        :param id: 可选，不提供则返回用户所在的项目
        :param team_id: 可选，团队 ID，提供可获取团队所在项目
        :param is_archived: 返回归档的项目，默认为 False
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            _teamId=team_id,
            isArchived=is_archived
        )
        if id is None:
            endpoint = 'api/projects'
        else:
            endpoint = 'api/projects/{0}'.format(id)

        return self._get(
            endpoint,
            params=params
        )

    def create(self, name, description=None, logo=None, categroy=None,
               divider_index=None, organization_id=None):
        """
        新建项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-create

        :param name: 项目名称
        :param description: 可选，项目描述
        :param logo: 可选，项目 logo
        :param category: 可选，项目类别
        :param divider_index: 可选，dividers 中得 index，仅对拥有者有效
        :param organization_id: 可选，组织 ID，创建组织项目时需要提供此参数
        :return: 新建的项目信息
        """
        data = optionaldict(
            name=name,
            description=description,
            logo=logo,
            category=categroy,
            dividerIndex=divider_index,
            _organizationId=organization_id
        )
        return self._post(
            'api/projects',
            data=data
        )

    def delete(self, id):
        """
        删除项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-delete

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/projects/{0}'.format(id))

    def update(self, id, name=None, description=None, logo=None,
               category=None, is_archived=None, is_public=None):
        """
        更新项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-update

        :param id: 路径参数
        :param name: 项目名称
        :param description: 可选，项目描述
        :param logo: 可选，项目 logo
        :param category: 可选，项目类别
        :param is_archived: 可选，是否归档
        :param is_public: 是否公开，需要拥有者权限
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            description=description,
            logo=logo,
            category=category,
            isArchived=is_archived,
            isPublic=is_public
        )
        return self._put(
            'api/projects/{0}'.format(id),
            data=data
        )

    def star(self, id):
        """
        项目加星

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-star

        :param id: 路径参数
        """
        return self._put('api/projects/{0}/star'.format(id))

    def unstar(self, id):
        """
        取消项目加星

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-star

        :param id: 路径参数
        """
        return self._delete('api/projects/{0}/star'.format(id))

    def copy(self, id, name, organization_id=None, is_public=False):
        """
        复制项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-copy

        :param id: 路径参数
        :param name: 新项目名称
        :param organization_id: 可选，所属组织 ID，若为空则属于个人
        :param is_public: 可选，是否公开，默认为 False
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            _organizationId=organization_id,
            isPublic=is_public
        )
        return self._put(
            'api/projects/{0}/copy'.format(id),
            data=data
        )

    def get_posts(self, id):
        """
        获取项目分享列表

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/{0}/posts'.format(id))

    def get_tags(self, id):
        """
        获取项目标签列表

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/{0}/tags'.format(id))

    def update_navigation(self, id, navigation):
        """
        更新项目应用导航

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-update-apps

        :param id: 项目 ID
        :param navigation: 字典，新的应用顺序
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/projects/{0}/navigation'.format(id),
            data={
                'navigation': navigation
            }
        )

    def add_members(self, id, email):
        """
        添加项目成员

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-add-member

        :param id: 项目 ID
        :param email: 邮箱或邮箱列表
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/projects/{0}/members'.format(id),
            data={
                'email': email
            }
        )

    create_members = add_members  # Alias for add_members

    def remove_member(self, id, user_id):
        """
        删除项目成员

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-remove-member

        :param id: 项目 ID
        :param user_id: 成员 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/projects/{0}/members/{1}'.format(id, user_id)
        )

    def get_members(self, id, user_id=None):
        """
        获取项目成员

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-get-members

        :param id: 项目 ID
        :param user_id: 可选，成员 ID
        :return: 返回的 JSON 数据包
        """
        if user_id:
            endpoint = 'api/projects/{0}/members/{1}'.format(id, user_id)
        else:
            endpoint = 'api/projects/{0}/members'.format(id)
        return self._get(endpoint)

    def get_recommend_members(self, id):
        """
        获取项目推荐成员列表

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-recommend-members

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/{0}/recommendMembers'.format(id))

    def update_member_role(self, id, user_id, role_type):
        """
        更新项目成员角色

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-update-member

        :param id: 项目 ID
        :param user_id: 成员 ID
        :param role_type: 角色类型, 可选值 member, admin, owner
        :return: 返回的 JSON  数据包
        """
        return self._put('api/projects/{0}/members/{1}/{2}'.format(
            id,
            user_id,
            role_type
        ))

    def transfer(self, id, organization_id=None):
        """
        移交项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-transfer

        :param id: 项目 ID
        :param organization_id: 目的组织 ID
        """
        return self._put(
            'api/projects/{0}/transfer'.format(id),
            data={
                '_organizationId': organization_id
            }
        )

    def get_statistic(self, id, today=True):
        """
        获取项目统计数据

        详情请参参考
        http://docs.teambition.com/wiki/projects#projects-statistic

        :param id: 项目 ID
        :param today: 可选，默认为今天，以该日期为准，退后五天内每天的任务完成数
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/projects/{0}/statistic'.format(id),
            params={
                'today': today
            }
        )

    def quit(self, id):
        """
        退出项目

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-quit

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/projects/{0}/quit'.format(id))

    def resend_invitation(self, id, user_id):
        """
        重发邀请邮件

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-resend-invitation

        :param id: 项目 ID
        :param user_id: 成员 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/projects/{0}/members{1}/resend'.format(id, user_id)
        )

    def reset_invitation(self, id):
        """
        重置项目邀请链接

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-reset-invitelink

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/projects/{0}/invitelink'.format(id))

    def update_tasklists(self, id, tasklist_ids):
        """
        自定义项目内任务分组排序

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-update-tasklistIds

        :param id: 项目 ID
        :param tasklist_ids: 所有未归档的任务分组 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/projects/{0}/tasklistIds',
            data={
                'tasklistIds': tasklist_ids
            }
        )

    def get_activities(self, id, start_date=None, end_date=None, limit=30):
        """
        获取主页动态

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-home-activities

        :param id: 项目 ID
        :param start_date: 可选，开始时间，默认为当天的开始
        :param end_date: 可选，结束时间，默认为当天的 23 时 59 分 59 秒
        :param limit: 可选，数量限制，默认为 30
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            startDate=start_date,
            endDate=end_date,
            limit=limit
        )
        return self._get(
            'api/projects/{0}/activities'.format(id),
            params=params
        )

    def get_reviews(self, id, start_date=None, end_date=None):
        """
        获取项目历史动态

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-reviews

        :param id: 项目 ID
        :param start_date: 可选，开始时间，默认为当天的开始
        :param end_date: 可选，结束时间，默认为当天的 23 时 59 分 59 秒
        :return: 返回的 JSON 数据包
        """
        params = optionaldict(
            startDate=start_date,
            endDate=end_date
        )
        return self._get(
            'api/projects/{0}/reviews'.format(id),
            params=params
        )

    def get_tasks(self, id=None, executor_id=None, fields=None,
                  subtask_fields=None, with_tasklist=False, with_subtasks=False,
                  with_tags=False, with_executor=False, is_done=False, all=False,
                  page=1, limit=30, **kwargs):
        """
        获取项目任务

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-get-tasks

        :param id: 可选，项目 ID
        :param executor_id: 可选，执行者 ID
        :param field: 可选，属性列表, 如: _id,_projectId,isDone,content
        :param subtask_fields: 可选，子任务属性列表，有: _id, _taskId, _executorId, content, order
        :param with_tasklist: 可选，是否包含任务分组信息，默认为 False
        :param with_subtasks: 可选，是否包含子任务信息，默认为 False
        :param with_tags: 可选，是否包含标签信息，默认为 False
        :param with_executor: 可选，是否包含执行者信息，默认为 False
        :param is_done: 可选，是否完成，默认为 False
        :param all: 可选，是否包含所有类型，包括完成与未完成，默认为 False
        :param page: 可选，页码，默认为 1
        :param limit: 可选，每页数量，默认为 30 ，最大为 1000
        :return: 返回的 JSON 数据包
        """
        if id:
            endpoint = 'api/projects/{0}/tasks'.format(id)
        else:
            endpoint = 'api/projects/tasks'

        if isinstance(fields, (tuple, list)):
            fields = ','.join(fields)
        if isinstance(subtask_fields, (tuple, list)):
            subtask_fields = ','.join(subtask_fields)

        params = optionaldict(
            _executorId=executor_id,
            fields=fields,
            subtaskFields=subtask_fields,
            withTasklist=with_tasklist,
            withSubtasks=with_subtasks,
            withTags=with_tags,
            withExecutor=with_executor,
            isDone=is_done,
            all=all,
            page=page,
            limit=limit,
            **kwargs
        )
        return self._get(endpoint, params=params)

    def get_events(self, id=None, start_date=None, end_date=None):
        """
        获取项目日程

        详情请参考
        http://docs.teambition.com/wiki/projects#projects-get-events

        :param id: 可选，项目 ID
        :param start_date: 可选，起始日期
        :param end_date: 可选，截止日期
        :return: 返回的 JSON 数据包
        """
        start_date = start_date or datetime.utcnow().replace(tzinfo=pytz.utc)
        if id:
            endpoint = 'api/projects/{0}/events'.format(id)
        else:
            endpoint = 'api/projects/events'
        params = optionaldict(
            start_date=start_date,
            end_date=end_date
        )
        return self._get(endpoint, params=params)

    def get_tasklists(self, id):
        """
        获取项目任务分组列表

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-get

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/{0}/tasklists'.format(id))

    def get_webhooks(self, id):
        """
        获取项目 Webhook 列表

        :param id: 项目 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/{0}/hooks'.format(id))

    def create_webhook(self, id, callback_url, active=True, events=None):
        """
        新建项目 webhook

        :param id: 项目 ID
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
            'api/projects/{0}/hooks'.format(id),
            data=data
        )

    def update_webhook(self, id, hook_id, callback_url=None, active=True,
                       events=None, add_events=None, remove_events=None):
        """
        更新项目 webhook

        :param id: 项目 ID
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
            'api/projects/{0}/hooks/{1}'.format(id, hook_id),
            data=data
        )

    def delete_webhook(self, id, hook_id):
        """
        删除项目 webhook

        :param id: 项目 ID
        :param hook_id: webhook ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/projects/{0}/hooks/{1}'.format(id, hook_id))

    def get_supported_webhooks(self):
        """
        获取项目支持的 webhook 列表

        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/webhooks')

    def get_webhook_value_format(self, event):
        """
        获取项目 webhook 的返回值格式

        :param event: 事件类型
        :return: 返回的 JSON 数据包
        """
        return self._get('api/projects/webhooks/{0}'.format(event))
