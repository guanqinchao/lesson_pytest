import unittest
# import unittestreport
import  time
from datetime import datetime
from BeautifulReport import BeautifulReport
# discover 的参数：在该目录下找到test_*.py , 用例所在的包
suite = unittest.defaultTestLoader.discover ('tests')
#
# ut = unittestreport.TestRunner(suite)
ut = BeautifulReport (suite)
# 获取现在的时间戳 ts   time.time()
# 字符串拼接 f'reports/report-{ts}.html'
# ut.run()
#ut.report ('测试',filename='reports/report'+str(time.time())+'.html')
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
ut.report ('测试',filename='reports/report'+ts+'.html')