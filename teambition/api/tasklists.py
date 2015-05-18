# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from optionaldict import optionaldict

from teambition.api.base import TeambitionAPI


class Tasklists(TeambitionAPI):

    def get(self, id=None, project_id=None):
        """
        获取任务分组列表

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-get

        :param id: 可选，任务分组 ID
        :param project_id: 可选，项目 ID
        :return: 返回的 JSON 数据包
        """
        assert id or project_id
        if id:
            endpoint = 'api/tasklists/{0}'.format(id)
        elif project_id:
            endpoint = 'api/projects/{0}/tasklists'.format(project_id)
        return self._get(endpoint)

    def create(self, project_id, title, description=None):
        """
        新建任务分组

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-create

        :param project_id: 项目 ID
        :param title: 任务列表标题
        :param description: 可选，任务列表描述
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            _projectId=project_id,
            title=title,
            description=description
        )
        return self._post(
            'api/tasklists',
            data=data
        )

    def delete(self, id):
        """
        删除任务分组

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-delete

        :param id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasklists/{0}'.format(id))

    def update(self, id, title=None, description=None, is_archived=None):
        """
        更新任务分组

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-update

        :param id: 任务分组 ID
        :param title: 可选，标题
        :param description: 可选，描述
        :param is_archived: 可选，是否归档
        :return: 返回的 JSON 数据包
        """
        data = optionaldict(
            title=title,
            description=description,
            isArchived=is_archived
        )
        return self._put(
            'api/tasklists/{0}'.format(id),
            data=data
        )

    def update_stage_ids(self, id, stage_ids):
        """
        更新任务分组内阶段顺序

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-update-stageids

        :param id: 任务分组 ID
        :param stage_ids: 阶段 ID 数组
        :return: 返回的 JSON 数据包
        """
        return self._put(
            'api/tasklists/{0}/stageIds'.format(id),
            data={
                'stageIds': stage_ids
            }
        )

    def archive(self, id):
        """
        任务分组存档

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-archive

        :param id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        return self._post('api/tasklists/{0}/archive'.format(id))

    def unarchive(self, id):
        """
        任务分组取消存档

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-unarchive

        :param id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        return self._delete('api/tasklists/{0}/archive'.format(id))

    def get_tasks(self, id, executor_id=None, is_done=False, dump_type='json',
                  all=False, page=1, limit=30, **kwargs):
        """
        获取任务分组任务列表

        详情请参考
        http://docs.teambition.com/wiki/tasklists#tasklists-get-tasks

        :param id: 任务分组 ID
        :param executor_id: 可选，执行者 ID
        :param is_done: 可选，是否已完成，默认为 False
        :param dump_type: 可选，默认为 json，支持 excel
        :param all: 可选，是否所有类型，包含完成和未完成
        :param page: 可选，页码，默认为 1
        :param limit: 可选，每页数量，默认为 30，最大值为 1000
        :return: 返回的 JSON  数据包
        """
        params = optionaldict(
            isDone=is_done,
            _executorId=executor_id,
            dumpType=dump_type,
            all=all,
            page=page,
            limit=limit,
            **kwargs
        )
        return self._get(
            'api/tasklists/{0}/tasks'.format(id),
            params=params
        )

    def get_stages(self, id):
        """
        获取任务分组的阶段列表

        详情请参考
        http://docs.teambition.com/wiki/stages#stages-get

        :param tasklist_id: 任务分组 ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'api/stages',
            params={
                '_tasklistId': tasklist_id
            }
        )
