"""
多参少参怎么测试
我的思路是定义一个多参的方法/少参方法
然后进行判断,如果是多参,调用多参方法
如果是少参,调用少参方法

"""
import requests
import api
from tools.get_log import GetLog

log = GetLog.get_logger()


class ApiMp:
    # 初始化
    def __init__(self):
        self.url_login = api.hosts + '/mp/v1_0/authorizations'
        log.info('正在初始化自媒体登录url:{}'.format(self.url_login))
        # self.url_article = api.hosts + '/mp/v1_0/channels'
        self.url_article = api.hosts + '/mp/v1_0/articles'
        # self.url_article = api.hosts + '/mp/v1_0/articles?draft=false'
        log.info('正在初始化自媒体发布文章url:{}'.format(self.url_article))

    # 登录接口
    def api_mp_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 返回响应对象
        """
        # 1.请求参数
        data = {"mobile": mobile, "code": code}
        # 2.调用post方法
        log.info('正在调用自媒体登录接口,请求数据为:{},请求头为:{}'.format(data, api.headers))
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 发布文章接口
    def api_mp_article(self, title, content, channel_id):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道id
        :param cover: 封面 0: 为自动
        :return: 返回响应对象
        """
        # 1.请求参数
        data = {'title': title, 'content': content, 'channel_id': channel_id, 'cover': {"type": 0, "images": []}}
        # 2.调用post方法
        log.info('正在调用自媒体发布文章接口,请求数据为:{},请求头为:{}'.format(data, api.headers))
        return requests.post(url=self.url_article, json=data, headers=api.headers)


if __name__ == '__main__':
    mp_login = ApiMp().api_mp_login('13911111111', '246810')
    print(mp_login.json().get('data').get('token'))
    print(mp_login.status_code)
    print(mp_login.json().get('message'))
    print(type(mp_login.status_code))
    assert 201 == mp_login.status_code
    assert 'OK' == mp_login.json().get('message')
    print(api.article_id)

