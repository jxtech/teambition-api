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
        # 错误码
        print(e.code)
        # 错误信息
        print(e.message)
        # 当前客户端实例
        e.client
        # 当前接口请求
        e.request
        # 当前接口响应
        e.response

.. module:: teambition.client

.. autoclass:: Teambition
   :members:
