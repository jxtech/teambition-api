# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class TeambitionProjects(TeambitionAPI):

    def get(self, id=None, is_archived=False):
        """
        获取项目信息

        :param id: 可选，不提供则返回用户所在的项目
        :param is_archived: 返回归档的项目，默认为 False
        :return: 返回的 JSON 数据包
        """
        if id is None:
            endpoint = 'api/projects'
        else:
            endpoint = 'api/projects/{0}'.format(id)

        return self._get(
            endpoint,
            params={
                'isArchived': is_archived
            }
        )

    def create(self, name, description=None, logo=None, categroy=None,
               divider_index=None, organization_id=None):
        """
        新建项目

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

        :param id: 路径参数
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/projects/{0}'.format(id))

    def update(self, id, name=None, description=None, logo=None,
               category=None, is_archived=None, is_public=None):
        """
        更新项目

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

        :param id: 路径参数
        """
        return self._put('api/projects/{0}/star'.format(id))

    def unstar(self, id):
        """
        项目加星

        :param id: 路径参数
        """
        return self._delete('api/projects/{0}/star'.format(id))

    def copy(self, id, name, organization_id=None, is_public=False):
        """
        复制项目

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
