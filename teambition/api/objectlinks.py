# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from teambition.api.base import TeambitionAPI


class ObjectLinks(TeambitionAPI):

    def get(self, parent_id, parent_type):
        """
        获取对象关联的 objectlink 列表

        详情请参考
        http://docs.teambition.com/wiki/objectlinks#objectlinks-get

        :param parent_id: 主体对象 ID
        :param parent_type: 主体对象类型
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/objectlinks',
            params={
                '_parentId': parent_id,
                'parentType': parent_type
            }
        )

    def create(self, parent_id, parent_type, linked_id, linked_type):
        """
        新建关联

        详情请参考
        http://docs.teambition.com/wiki/objectlinks#objectlinks-create

        :param parent_id: 主体对象 ID
        :param parent_type: 主体对象类型
        :param linked_id: 关联对象 ID
        :param linked_type: 关联对象类型
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/objectlinks',
            data={
                '_parentId': parent_id,
                'parentType': parent_type,
                '_linkedId': linked_id,
                'linkedType': linked_type
            }
        )

    def delete(self, id):
        """
        删除关联

        详情请参考
        http://docs.teambition.com/wiki/objectlinks#objectlinks-delete

        :param id: 关联 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/objectlinks/{0}'.format(id))
