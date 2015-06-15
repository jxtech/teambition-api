# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Activities(TeambitionAPI):

    def get(self, object_id):
        """
        获取动态

        :param object_id: 对象 ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/activities',
            params={'_boundToObjectId': object_id}
        )

    def create(self, content, object_id, object_type,
               attachments=None, mentions=None):
        """
        新建动态

        详情请参考
        http://docs.teambition.com/wiki/activities#activities-comment

        :param content: 内容
        :param object_id: 所属对象 ID
        :param object_type: 所属对象类型，目前仅支持评论: post/task/event/entry/work
        :param attachments: 可选，附件 ID 列表
        :param mentions: 可选，提及，格式为 {"user id": "@username"}
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            content=content,
            _boundToObjectId=object_id,
            boundToObjectType=object_type,
            attachments=attachments,
            mentions=mentions
        )
        return self._post(
            'api/activities',
            data=data
        )

    def update(self, id, content):
        """
        更新动态

        详情请参考
        http://docs.teambition.com/wiki/activities#activities-update_comment

        :param id: 动态 ID
        :param content: 内容
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/activities/{0}'.format(id),
            data={
                'content': content
            }
        )

    def delete(self, id):
        """
        删除动态

        详情请参考
        http://docs.teambition.com/wiki/activities#activities-delete

        :param id: 动态 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/activities/{0}'.format(id))
