# Author:qinchao
# Email:1424185332@qq.com
import pytest
# from  fixtures import fixt
class TestFixture2:
    def test_fixture(self,fixt):
        assert 1+1==2

    def test_fixture1(self,fixt):
        actual=1
        excepted =1
        assert actual==excepted

    def test_fixture2(self,fixt):
        assert 1+2==2
