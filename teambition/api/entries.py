# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Entries(TeambitionAPI):

    def get(self, id=None, project_id=None, category_id=None):
        """
        获取账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-get

        :param id: 可选，账目 ID
        :param project_id: 可选，项目 ID
        :param category_id: 可选，账目类别 ID
        :return: 返回的 JSON 数据包
        """
        assert id or project_id or category_id
        params = {}
        if id:
            endpoint = 'api/entries/{0}'.format(id)
        elif project_id:
            endpoint = 'api/entries'
            params['_projectId'] = project_id
        elif category_id:
            endpoint = 'api/entries'
            params['_entryCategoryId'] = category_id
        return self._get(endpoint, params=params)

    def create(self, project_id, category_id, content, amount, type,
               note=None, visiable=None, tag_ids=None, involve_members=None):
        """
        新建账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-create

        :param project_id: 项目 ID
        :param category_id: 账目分类 ID
        :param content: 内容
        :param amount: 金额
        :param type: 类型，1 为收入，-1 为支出
        :param note: 可选，备注
        :param visiable: 可选，可见范围
        :param tag_ids: 可选，标签 ID 列表
        :param involve_members: 可选，参与者 ID 列表
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _projectId=project_id,
            _entryCategoryId=category_id,
            content=content,
            amount=amount,
            type=type,
            note=note,
            visiable=visiable,
            tagIds=tag_ids,
            involveMembers=involve_members
        )
        return self._post(
            'api/entries',
            data=data
        )

    def delete(self, id):
        """
        删除账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-delete

        :param id: 账目 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/entries/{0}'.format(id))

    def update(self, id, content, amount, note=None):
        """
        更新账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-update

        :param id: 账目 ID
        :param content: 内容
        :param amount: 金额
        :param note: 可选，备注
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            content=content,
            amount=amount,
            note=note
        )
        return self._put(
            'api/entries/{0}'.format(id),
            data=data
        )

    def approval(self, id):
        """
        审批账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-approval

        :param id: 账目 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/entries/{0}/approval'.format(id))

    def unapproval(self, id):
        """
        取消审批账目

        详情请参考
        http://docs.teambition.com/wiki/bookkeeping-entry#bookkeeping-entry-cancel_the_approval

        :param id: 账目 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/entries/{0}/approval'.format(id))
