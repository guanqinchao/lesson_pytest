import unittest
import requests
import json
from common.read_excel import read_excel_dict
from setting import config
from ddt import ddt, data
from common.logger import my_log

# file = r'D:\自动化测试学习\Study_unittest\Lesson_21\data\cases.xlsx'
# 得到测试数据
cases = read_excel_dict (file=config.case_file, sheet_name='register')


@ddt
class TestRegister (unittest.TestCase):

    @data (*cases)
    def test_register(self, info):
        '''步骤
          1、 准备测试用例
          2、 发送接口请求，得到实际
          3、预期结果和实际结果的断言
        TODO: 域名和端口，环境变化时更方便的修改
        :param info:
        :return:
        '''
        # 1、准备测试数据
        my_log.info (f'正在进行测试{info}')
        url = config.host + info['url']  # str
        method = info['method']  # str
        # 将 json 格式转化成字典 因为requests.request 需要字典格式  传str字符串  json 格式 会报错
        headers = json.loads (info['headers'])
        json_data = json.loads (info['json'])  # 注意命名为 json_data   不用命名  json
        excepted = json.loads (info['excepted'])
        # 序列化（ json.dumps  字典-> json） 、#   反序列化( json.loads   json ->  字典)
        # dict_data =  json.loads(json_data)

        # 2、 发送接口请求， 得到实际结果
        response = requests.request (url=url, headers=headers, json=json_data, method=method)
        actual = response.json ()
        # 3、预期结果 和 实际结果的断言
        self.assertEqual (actual, excepted)
