#! -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
#用例路径
case_path = os.path.join(os.getcwd(), "case")  # os.getcwd "获取当前工作目录，os.path.join
print(os.getcwd())
#报告路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():
    discover = unittest.defaultTestLoader.discover(
        start_dir=case_path,
        pattern='test*.py',
        top_level_dir=None
    )
    return discover #返回所有的用例

if __name__=='__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    report_abspath = os.path.join(report_path, "result.html")
    with  open(report_abspath, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title='walker自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')
        runner.run((all_case()))