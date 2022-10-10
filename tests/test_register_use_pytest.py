# Author:qinchao
# Email:1424185332@qq.com
import  requests


class TestRegister:
    def test_register(self,fixt):
        '''步骤
         1、准备测试用例
         2、发送接口请求，得到实际
          3、预期结果和实际结果的断言
        :return:
        '''
        url = 'http://api.lemonban.com:8766/futureloan/member/register'
        headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        method = 'post'
        json_data = {
            "mobile_phone": "",
            "reg_name": "大柠31",
            "pwd": "qaq123456"
        }
        excepted = {
            "code": 1,
            "msg": "手机号为空",
            "data": None,
            "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
        }
        response = requests.request (url=url, headers=headers, json=json_data, method=method)
        actual = response.json ()
        assert (actual, excepted)

    def test_register_two(self,fixt):
        '''步骤
         1、准备测试用例
         2、发送接口请求，得到实际
          3、预期结果和实际结果的断言
        :return:
        '''
        url = 'http://api.lemonban.com:8766/futureloan/member/register'
        headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        method = 'post'
        json_data = {"mobile_phone": "13588123465", "reg_name": "uuu柠檬", "pwd": "222"}
        excepted = {
            "code": 2,
            "msg": "密码格式为8到16位",
            "data": None,
            "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
        }
        response = requests.request (url=url, headers=headers, json=json_data, method=method)
        actual = response.json ()
        assert(actual, excepted)
