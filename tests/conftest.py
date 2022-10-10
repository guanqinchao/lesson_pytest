# Author:qinchao
# Email:1424185332@qq.com
import pytest

#声明一个夹具，这个夹具就是一个函数
@pytest.fixture()
def fixt():
    print("setUp ，每次执行一个测试用例都会执行的！")
    #yield 之前就是setUp 前置； 之后就是tearDown 后置。
    yield
    # 这个是 tearDown
    print("tearDown，每个测试用例执行之后都会执行的。")
