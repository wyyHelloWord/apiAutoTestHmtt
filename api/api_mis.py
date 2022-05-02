import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:
    # 1.初始化
    def __init__(self):
        # 1.登录接口url
        self.url_login = api.hosts + '/mis/v1_0/authorizations'
        log.info('正在初始化后台管理系统 登录url:{}'.format(self.url_login))
        # 2.查询文章接口url
        self.url_search = api.hosts + '/mis/v1_0/articles'
        log.info('正在初始化后台管理系统 查询文章url:{}'.format(self.url_search))
        # 3.审核文章接口url
        self.url_audit = api.hosts + '/mis/v1_0/articles'
        log.info('正在初始化后台管理系统 审核文章url:{}'.format(self.url_audit))

    # 2.登录接口
    def api_mis_login(self, account, password):
        """
        :param account: 账号
        :param password: 密码
        :return: 返回响应对象
        """
        # 1. 请求参数
        data = {'account': account, 'password': password}
        log.info('正在调用后台管理登录接口,请求数据为:{},请求头为:{}'.format(data, api.headers))
        # 2. 调用post请求
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3.查询文章接口
    def api_mis_article_search(self, title, channel):
        """
        :param title: 文章标题
        :param channel: 文章所属频道
        :return: 返回响应对象
        """
        # 1. 请求参数
        data = {'title': title, 'channel': channel}
        log.info('正在调用后台管理查询文章接口,请求数据为:{},请求头为:{}'.format(data, api.headers))
        # 2. 调用get请求
        return requests.get(url=self.url_search, params=data, headers=api.headers)

    # 4.审核文章接口
    def api_mis_article_audit(self):
        """
        :param article_id: 文章id
        :param status: 2: 为审核通过
        :return: 返回响应对象
        """
        # 1. 请求参数
        data = {'article_ids': [api.article_id], 'status': 2}
        log.info('正在调用后台管理审核文章接口,请求数据为:{},请求头为:{}'.format(data, api.headers))
        # 2. 调用put请求
        return requests.put(url=self.url_audit, json=data, headers=api.headers)
