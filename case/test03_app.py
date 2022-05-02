import pytest
from api.api_app import ApiApp
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.tool import Tool

log = GetLog.get_logger()


class TestApp:
    # 1. 初始化
    def setup_class(self):
        self.app = ApiApp()

    # 2. 调用登录方法
    @pytest.mark.parametrize('mobile,code', read_yaml('app_login.yaml'))
    def test01_app_login(self, mobile, code):
        r = self.app.api_app_login(mobile, code)
        # 获取token
        Tool.common_token(r)
        # 断言
        try:
            Tool.common_assert(r)
        # 捕获异常
        except Exception as e:
            # 日志
            log.info(e)
            # 抛异常
            raise

    # 3. 调用查询文章方法
    @pytest.mark.parametrize('title,content,channel_id,channel', read_yaml('mp_article.yaml'))
    def test02_app_article(self, title, content, channel_id, channel):
        r = self.app.api_app_article(channel_id)
        # 断言
        try:
            Tool.common_assert(r, status_code=200)
        # 捕获异常
        except Exception as e:
            # 日志
            log.info(e)
            # 抛异常
            raise
