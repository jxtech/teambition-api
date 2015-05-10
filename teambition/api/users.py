# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Users(TeambitionAPI):

    def me(self):
        """
        获取个人信息
        :return: 返回的 JSON 数据包
        """
        return self._get('api/users/me')

    def update(self, name=None, avatar_url=None, title=None, birthday=None,
               location=None, phone=None, website=None):
        """
        更新个人信息

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
