import pytest
from api.api_mis import ApiMis
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
from tools.tool import Tool

log = GetLog.get_logger()


class TestMis:
    # 初始化ApiMis对象
    def setup_class(self):
        self.mis = ApiMis()

    # 调用登录方法
    @pytest.mark.parametrize('account,password', read_yaml('mis_login.yaml'))
    def test01_mis_login(self, account, password):
        r = self.mis.api_mis_login(account, password)
        # 获取 token
        Tool.common_token(r)
        # 断言
        try:
            Tool.common_assert(r)
        except Exception as e:
            # 1. 写日志
            log.error(e)
            # 2. 抛异常
            raise

    # 调用查询文章方法
    @pytest.mark.parametrize('title,content,channel_id,channel', read_yaml('mp_article.yaml'))
    def test02_mis_search(self, title, content, channel_id, channel):
        r = self.mis.api_mis_article_search(title, channel)
        # 断言
        try:
            Tool.common_assert(r, status_code=200)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 调用审核文章方法
    def test03_mis_audit(self):
        r = self.mis.api_mis_article_audit()
        # 断言
        try:
            Tool.common_assert(r)
        # 捕获异常
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise
