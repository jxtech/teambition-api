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


接口调用发生错误时，可以捕获 ``TeambitionException``::

    from teambition import Teambition, TeambitionException

    tb = Teambition('key', 'secret', access_token='123456')
    try:
        tb.projects.get()
    except TeambitionException as e:
        # do something useful
        pass

.. module:: teambition.client

.. autoclass:: Teambition
   :members:
