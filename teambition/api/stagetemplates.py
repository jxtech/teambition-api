# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class StageTemplates(TeambitionAPI):

    def get(self):
        """
        获取用户自定义的阶段模板

        详情请参考
        http://docs.teambition.com/wiki/stages-template#stages-template-get

        :return: 返回的 JSON 数据包
        """
        return self._get('api/stagetemplates')

    def create(self, title, stages):
        """
        新建模板

        详情请参考
        http://docs.teambition.com/wiki/stages-template#stages-template-create

        :param title: 模板标题
        :param stages: 阶段名称列表，至少两个阶段
        :return: 返回的 JSON 数据包
        """
        if isinstance(stages, (tuple, list)):
            stages = ','.join(stages)
        return self._post(
            'api/stagetemplates',
            data={
                'title': title,
                'stages': stages
            }
        )

    def delete(self, id):
        """
        删除模板

        详情请参考
        http://docs.teambition.com/wiki/stages-template#stages-template-delete

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/stagetemplates/{0}'.format(id))

    def update(self, id, title=None, stages=None):
        """
        更新模板

        详情请参考
        http://docs.teambition.com/wiki/stages-template#stages-template-update

        :param id: 路径参数
        :param title: 可选，模板标题
        :param stages: 可选，阶段名称列表，至少两个阶段
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            stages=stages
        )
        return self._put(
            'api/stagetemplates/{0}'.format(id),
            data=data
        )
