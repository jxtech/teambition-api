# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from teambition.api.base import TeambitionAPI


class EntryCategories(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取账目分类

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entrycategory#bookkeeping-entrycategory-get

        :param id: 可选，账目分类 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        assert id or project_id
        params = {}
        if id:
            endpoint = 'api/entrycategories/{0}'.format(id)
        elif project_id:
            endpoint = 'api/entrycategories'
            params['_projectId'] = project_id
        return self._get(endpoint, params=params)

    def create(self, project_id, title, type):
        """
        新建账目分类

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entrycategory#bookkeeping-entrycategory-create

        :param project_id: 项目 ID
        :param title: 标题
        :param type: 账目类型，1 为收入，-1 为支出
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/entrycategories',
            data={
                '_projectId': project_id,
                'title': title,
                'type': type
            }
        )

    def delete(self, id):
        """
        删除账目分类 只允许删除非默认分类

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entrycategory#bookkeeping-entrycategory-delete

        :param id: 账目分类 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/entrycategories/{0}'.format(id))

    def update(self, id, title):
        """
        更新账目分类

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entrycategory#bookkeeping-entrycategory-update

        :param id: 账目分类 ID
        :param title: 标题
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/entrycategories/{0}'.format(id),
            data={
                'title': title
            }
        )
