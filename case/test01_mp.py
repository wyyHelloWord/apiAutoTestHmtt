import pytest
import api
from api.api_mp import ApiMp
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.tool import Tool

log = GetLog.get_logger()


class TestMp:
    # 初始化
    def setup_class(self):
        self.mp = ApiMp()

    # 登录接口测试方法
    @pytest.mark.parametrize('mobile,code', read_yaml('mp_login.yaml'))
    def test01_mp_login(self, mobile, code):
        r = self.mp.api_mp_login(mobile, code)
        # 异常
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        # 捕获异常
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛出异常
            raise

    # 发布文章测试方法
    @pytest.mark.parametrize('title,content,channel_id,channel', read_yaml('mp_article.yaml'))
    def test02_mp_article(self, title, content, channel_id, channel):
        r = self.mp.api_mp_article(title, content, channel_id)
        # 查看响应信息
        print(r.json())
        print(r.status_code)
        # print(r.json().get('data').get('channels')[0].get('id'))
        # print('文章id为:', r.json().get('data').get('results')[0].get('id'))
        # 获取文章id
        api.article_id = r.json().get('data').get('id')
        print('获取到的文章id为:', api.article_id)
        # print(api.headers)
        # 断言
        try:
            Tool.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise


if __name__ == '__main__':
    TestMp()
