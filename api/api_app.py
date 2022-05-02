import time
import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:

    # 初始化
    def __init__(self):
        # 1.登录url
        self.url_login = api.hosts + '/app/v1_0/authorizations'
        log.info('正在初始化app登录url:{}'.format(self.url_login))
        # 2.查询文章url
        self.url_article = api.hosts + '/app/v1_1/articles'
        log.info('正在初始化app查询文章url:{}'.format(self.url_article))
        # 登录接口

    def api_app_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 返回响应对象
        """
        # 1. 请求参数
        data = {'mobile': mobile, 'code': code}
        # 2. 调用post请求方法
        log.info('正在调用app登录接口方法,请求参数为:{},请求头为:{}'.format(data, api.headers))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 查询文章接口
    def api_app_article(self, channel_id):
        """
        :param channel_id: 文章id, 来自发布文章以后
        :param timestamp: 时间戳,单位毫秒
        :param with_top: 置顶文章: 1: 为包含, 0: 不包含
        :return: 返回响应对象
        """
        # 1. 请求参数
        data = {'channel_id': channel_id, 'timestamp': int(time.time()), 'with_top': 1}
        # 2. 调用get请求方法
        log.info('正在调用app查询指定频道下所有文章接口方法,请求参数为:{},请求头为:{}'.format(data, api.headers))
        return requests.get(url=self.url_article, params=data, headers=api.headers)
