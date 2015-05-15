# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Users(TeambitionAPI):

    def me(self):
        """
        获取个人信息

        详情请参考
        http://docs.teambition.com/wiki/me#me-get

        :return: 返回的 JSON 数据包
        """
        return self._get('api/users/me')

    def update(self, name=None, avatar_url=None, title=None, birthday=None,
               location=None, phone=None, website=None):
        """
        更新个人信息

        详情请参考
        http://docs.teambition.com/wiki/me#me-update-info

        :param name: 可选，姓名
        :param avatar_url: 可选，头像地址
        :param title: 可选，职位
        :param birthday: 可选，出生日期
        :param location: 可选，所在地
        :param phone: 可选，手机号码
        :param website: 可选，个人站点
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            name=name,
            avatarUrl=avatar_url,
            title=title,
            birthday=birthday,
            location=location,
            phone=phone,
            website=website
        )
        return self._put(
            'api/users',
            data=data
        )

    def add_email(self, email):
        """
        添加新邮箱

        详情请参考
        http://docs.teambition.com/wiki/me#me-update-emails

        :param email: 邮箱地址
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/users/email',
            data={
                'email': email
            }
        )

    def update_preferences(self, id, notification):
        """
        更新通知设置

        详情请参考
        http://docs.teambition.com/wiki/me#me-update-notification

        :param id: 用户 ID
        :param notification: 新通知设置，dict 类型
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/preferences/{0}'.format(id),
            data={
                'notification': notification
            }
        )

    def send_verification_email(self, email_id):
        """
        发送邮箱验证邮件

        详情请参考
        http://docs.teambition.com/wiki/me#me-send-verify-email

        :param email_id: 邮箱唯一标识 ID，可以从 emails 属性中获得
        :return: 返回的 JSON 数据包
        """
        return self._post('api/users/email/{0}/send'.format(email_id))

    def delete_email(self, email_id):
        """
        删除关联邮箱

        详情请参考
        http://docs.teambition.com/wiki/me#me-delete-email

        :param email_id: 邮箱唯一标识 ID，可以从 emails 属性中获得
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/users/email/{0}/send'.format(email_id))

    def get_my_tasks(self, page=1, count=30):
        """
        获取执行者为我的任务

        详情请参考
        http://docs.teambition.com/wiki/me#me-tasks

        :param page: 可选，当前页码
        :param count: 可选，每页数量，默认为 30
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/me')

    def get_involved_tasks(self, page=1, count=30):
        """
        获取我参与的任务

        详情请参考
        http://docs.teambition.com/wiki/me#me-involves

        :param page: 可选，当前页码
        :param count: 可选，每页数量，默认为 30
        :return: 返回的 JSON 数据包
        """
        return self._get('api/tasks/involves')

    def get_today_count(self):
        """
        获取今日待处理事项总数

        详情请参考
        http://docs.teambition.com/wiki/me#me-today

        :return: 今日待处理事项数量
        """
        res = self._get('api/users/todayCount')
        return res['todayCount']
