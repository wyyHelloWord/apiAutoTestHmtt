import logging.handlers
import os

from config import BASE_PATH


class GetLog:
    __logger = None

    # 获取日志器
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            cls.__logger = logging.getLogger()
            # 修改日志级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器
            log_filepath = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt.log'
            th = logging.handlers.TimedRotatingFileHandler(filename=log_filepath,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 设置格式器
            fmt = logging.Formatter(
                '%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s')
            th.setFormatter(fmt)
            # 将处理器添加到日志器
            cls.__logger.addHandler(th)
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info('a hahahaha')
