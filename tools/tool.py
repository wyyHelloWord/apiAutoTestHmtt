import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    # 1. 提取token
    @classmethod
    def common_token(cls, response):
        token = response.json().get('data').get('token')
        api.headers['Authorization'] = 'Bearer ' + token
        log.info('正在提取token,提取的token为:{},添加token后的headers为:{}'.format(token, api.headers))
        print('添加的token为:{},添加token后的headers为{}'.format(token, api.headers))

    # 2. 断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info('正在调用公共断言方法')
        # 断言状态码
        log.info('正在判断{} == {}'.format(status_code, response.status_code))
        assert status_code == response.status_code
        # 断言响应信息
        log.info('正在判断 OK == {}'.format(response.json().get('message')))
        assert 'OK' == response.json().get('message')
