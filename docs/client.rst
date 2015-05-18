Teambition API 客户端
=========================

`Teambition` 基本使用方法::

    from teambition import Teambition

    tb = Teambition('key', 'secret')
    authorize_url = tb.oauth.get_authorize_url('http://localhost')
    me = tb.users.me()
    # 以此类推，参见 API 详细说明
    # tb.projects.xxx()
    # tb.tasks.xxx()

.. module:: teambition.client

.. autoclass:: Teambition
   :members:
