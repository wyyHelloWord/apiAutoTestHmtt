import os
import yaml
from config import BASE_PATH
from tools.get_log import GetLog

log = GetLog.get_logger()


def read_yaml(filename):
    yaml_filepath = BASE_PATH + os.sep + 'data' + os.sep + filename
    arrays = []
    with open(yaml_filepath, 'r', encoding='utf-8') as f:
        # return yaml.safe_load(f).get('mp_login001').get('mobile')  # 13812345678
        for datas in yaml.safe_load(f).values():
            arrays.append(tuple(datas.values()))
    log.info('正在调用读取yaml文件方法,读取的文件为:{},读取到的数据为:{}'.format(yaml_filepath, arrays))
    return arrays


if __name__ == '__main__':
    print(type(read_yaml('mp_article.yaml')))
    print(read_yaml('mp_article.yaml')[0][0])
    print(type(read_yaml('mp_article.yaml')[0][0]))
    print(read_yaml('mp_article.yaml')[0][1])
    print(type(read_yaml('mp_article.yaml')[0][1]))
    print(read_yaml('mp_article.yaml')[0][2])
    print(type(read_yaml('mp_article.yaml')[0][2]))
    print(read_yaml('mp_article.yaml')[0][3])
    print(type(read_yaml('mp_article.yaml')[0][3]))
    print(read_yaml('mp_article.yaml')[:])
