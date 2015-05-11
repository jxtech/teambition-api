# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Works(TeambitionAPI):

    def get(self, id=None, parent_id=None, page=None, count=None, all=None):
        """
        获取文件信息

        :param id: 可选，文件 ID
        :param parent_id: 可选，父级 ID
        :param page: 可选，当前页，默认为 1
        :param count: 可选，每页数量，默认为 30
        :param all: 可选，若提供此参数则返回所有
        :return: 返回的 JSON 数据包
        """
        assert id or parent_id

        params = optionaldict(
            page=page,
            count=count,
            all=all
        )
        if id:
            endpoint = 'api/works/{0}'.format(id)
        elif parent_id:
            endpoint = 'api/works'
            params['_parentId'] = parent_id
        return self._get(endpoint, params=params)

    def create(self, parent_id, file_name, file_size, file_type, file_category,
               file_key, image_width=None, image_height=None,
               involve_members=None):
        """
        新建文件

        :param parent_id: 所属目录 ID
        :param file_name: 文件名
        :param file_size: 文件大小
        :param file_type: 文件类型
        :param file_category: 文件类别
        :param file_key: 使用 striker 服务上传后可得
        :param image_width: 可选，图片宽度
        :param image_height: 可选，图片高度
        :param involve_members: 可选
        """
        data = optionaldict(
            _parentId=parent_id,
            fileName=file_name,
            fileSize=file_size,
            fileType=file_type,
            fileCategory=file_category,
            fileKey=file_key,
            imageWidth=image_width,
            imageHeight=image_height,
            involveMembers=involve_members
        )
        return self._post(
            'api/works',
            data=data
        )

    def like(self, id):
        """
        赞文件

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/works/{0}/like'.format(id))

    def update(self, id, file_name):
        """
        更新文件

        :param id: 文件 ID
        :param file_name: 文件名
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/works/{0}'.format(id),
            data=data
        )

    def move(self, id, parent_id):
        """
        移动文件

        :param id: 文件 ID
        :param parent_id: 新的目录 ID
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/works/{0}'.format(id),
            data={
                '_parentId': parent_id
            }
        )

    def delete(self, id):
        """
        删除文件

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/works/{0}'.format(id))

    def update_members(self, id, members):
        """
        更新文件参与者

        :param id: 文件 ID
        :param members: 参与者 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/works/{0}'.format(id),
            data={
                'involveMembers': members
            }
        )

    def get_tags(self, id):
        """
        获取任务标签列表

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/works/{0}/tags'.format(id))

    def create_tag(self, id, name):
        """
        新建标签

        :param id: 文件 ID
        :param name: 标签名称
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/works/{0}/tags'.format(id),
            data={
                'name': name
            }
        )

    def add_tag(self, id, tag_id):
        """
        关联标签

        :param id: 文件 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/works/{0}/tags/{1}'.format(id, tag_id))
