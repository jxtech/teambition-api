# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Messages(TeambitionAPI):

    def get(self):
        """
        获取消息列表

        详情请参考
        http://docs.teambition.com/wiki/messages#messages-get

        :return: 返回的 JSON 数据包
        """
        return self._get('api/v2/messages')

    def update(self, id, is_archived=None, is_read=None):
        """
        更新消息，标记已读/归档

        详情请参考
        http://docs.teambition.com/wiki/messages#messages-update

        :param id: 消息 ID
        :param is_archived: 可选，是否归档
        :param is_read: 可选，是否已读
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            isArchived=is_archived,
            isRead=is_read
        )
        return self._put(
            'api/messages/{0}'.format(id),
            data=data
        )

    def mark_all_read(self):
        """
        标记所有未读消息为已读

        详情请参考
        http://docs.teambition.com/wiki/messages#messages-update-markallread

        :return: 返回的 JSON 数据包
        """
        return self._put('api/messages/markallread')

    def delete(self, id):
        """
        删除单条消息

        详情请参考
        http://docs.teambition.com/wiki/messages#messages-delete

        :param id: 消息 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/messages/{0}'.format(id))

    def archive_all(self):
        """
        归档所有已读消息

        详情请参考
        http://docs.teambition.com/wiki/messages#messages-delete

        :return: 返回的 JSON 数据包
        """
        return self._delete('api/messages')
