import unittest
import time

from script.test_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner



# 定义一个测试套件
suite = unittest.TestSuite()

# 添加测试用例

suite.addTest(unittest.makeSuite(TestLogin))

# 定义测试报告路径
report_path = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流

with open(report_path, "wb") as f:
    # 创建运行期
    runner = HTMLTestRunner(f, title="Tpshop接口测试报告", description="这是第一次测试")
    # 执行测试套间
    runner.run(suite)
