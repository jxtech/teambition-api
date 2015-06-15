# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Works(TeambitionAPI):

    def get(self, id=None, parent_id=None, page=None, count=None, all=None):
        """
        获取文件信息

        详情请参考
        http://docs.teambition.com/wiki/works#works-get

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

        详情请参考
        http://docs.teambition.com/wiki/works#works-create

        :param parent_id: 所属目录 ID
        :param file_name: 文件名
        :param file_size: 文件大小
        :param file_type: 文件类型
        :param file_category: 文件类别
        :param file_key: 使用 striker 服务上传后可得
        :param image_width: 可选，图片宽度
        :param image_height: 可选，图片高度
        :param involve_members: 可选
        :return: 返回的 JSON 数据包
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

        详情请参考
        http://docs.teambition.com/wiki/works#works-like

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/works/{0}/like'.format(id))

    def update(self, id, file_name, description=None):
        """
        更新文件

        详情请参考
        http://docs.teambition.com/wiki/works#works-update

        :param id: 文件 ID
        :param file_name: 文件名
        :param description: 可选，描述
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            fileName=file_name,
            description=description
        )
        return self._put(
            'api/works/{0}'.format(id),
            data=data
        )

    def move(self, id, parent_id):
        """
        移动文件

        详情请参考
        http://docs.teambition.com/wiki/works#works-move

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

        详情请参考
        http://docs.teambition.com/wiki/works#works-delete

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/works/{0}'.format(id))

    def update_members(self, id, members):
        """
        更新文件参与者

        详情请参考
        http://docs.teambition.com/wiki/works#works-update-involvemembers

        :param id: 文件 ID
        :param members: 参与者 ID 列表
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/works/{0}/involveMembers'.format(id),
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

    def remove_tag(self, id, tag_id):
        """
        移除标签

        :param id: 文件 ID
        :param name: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/works/{0}/tags/{1}'.format(id, tag_id))

    def add_tag(self, id, tag_id):
        """
        关联标签

        :param id: 文件 ID
        :param tag_id: 标签 ID
        :return: 返回的 JSON 数据包
        """
        return self._put('api/works/{0}/tags/{1}'.format(id, tag_id))

    def get_objectlinks(self, id):
        """
        获取文件关联的 objectlink 列表

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._get('api/works/{0}/objectlinks'.format(id))

    def create_objectlink(self, id, linked_id, linked_type):
        """
        关联对象

        :param id: 文件 ID
        :param linked_id: 关联对象 ID
        :param linked_type: 关联对象类型
        :return: 返回的 JSON 数据包
        """
        return self._post(
            'api/objectlinks',
            data={
                '_parentId': id,
                'parentType': 'work',
                '_linkedId': linked_id,
                'linkedType': linked_type
            }
        )

    def get_versions(self, id):
        """
        获取文件关联的历史版本信息

        详情请参考
        http://docs.teambition.com/wiki/works-versions#works-versions-list

        :param id: 文件 ID
        :return: 历史版本列表
        """
        return self._get('api/works/{0}/versions'.format(id))

    def get_version(self, id, version_id):
        """
        获取单个历史版本信息

        详情请参考
        http://docs.teambition.com/wiki/works-versions#works-versions-get

        :param id: 文件 ID
        :param version_id: 历史版本 ID
        :return: 历史版本信息
        """
        return self._get('api/works/{0}/versions/{1}'.format(id, version_id))

    def update_version(self, id, version_id, file_name=None, description=None):
        """
        获取单个历史版本信息

        详情请参考
        http://docs.teambition.com/wiki/works-versions#works-versions-update

        :param id: 文件 ID
        :param version_id: 历史版本 ID
        :param file_name: 可选，文件名
        :param description: 可选，描述
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(fileName=file_name, description=description)
        return self._put(
            'api/works/{0}/versions/{1}'.format(id, version_id),
            data=data
        )

    def delete_version(self, id, version_id):
        """
        删除单个历史版本

        详情请参考
        http://docs.teambition.com/wiki/works-versions#works-versions-delete

        :param id: 文件 ID
        :param version_id: 历史版本 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete(
            'api/works/{0}/versions/{1}'.format(id, version_id)
        )

    def create_version(self, id, file_name, file_size, file_type,
                       file_category, file_key, image_width=None,
                       image_height=None, involve_members=None):
        """
        新建文件

        详情请参考
        http://docs.teambition.com/wiki/works-versions#works-versions-post

        :param id: 文件 ID
        :param file_name: 文件名
        :param file_size: 文件大小
        :param file_type: 文件类型
        :param file_category: 文件类别
        :param file_key: 使用 striker 服务上传后可得
        :param image_width: 可选，图片宽度
        :param image_height: 可选，图片高度
        :param involve_members: 可选
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
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
            'api/works/{0}/versions'.format(id),
            data=data
        )

    def link_task(self, id, linked_id):
        """
        关联任务

        :param id: 任务 ID
        :param linked_id: 关联任务 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'task')

    def link_post(self, id, linked_id):
        """
        关联分享

        :param id: 任务 ID
        :param linked_id: 关联分享 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'post')

    def link_event(self, id, linked_id):
        """
        关联日程

        :param id: 任务 ID
        :param linked_id: 关联日程 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'event')

    def link_work(self, id, linked_id):
        """
        关联文件

        :param id: 任务 ID
        :param linked_id: 关联文件 ID
        :return: 返回的 JSON 数据包
        """
        return self.create_objectlink(id, linked_id, 'work')

    def get_activities(self, id):
        """
        获取文件动态

        :param id: 文件 ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/activities',
            params={'_boundToObjectId': id}
        )
