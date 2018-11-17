#! -*- coding:utf-8 -*-
"""
http://www.cnblogs.com/weke/articles/6271206.html
前置和后置
1.setUp：在写测试用例的时候，每次操作其实都是基于打开浏览器输入对应网址这些操作，这个就是执行用例的前置条件。在执行每个用例前执行的
2.tearDown：执行完用例后，为了不影响下一次用例的执行，一般有个数据还原的过程，这就是执行用例的后置条件:在执行每个用例后要执行的
unittest执行顺序是 每个    用例前会执行setup,用例后会执行teardown
使用run_all_case时必须时，文件夹下必须有__init__文件才可以识别该目录下的用例
3 生成报告Download下HTMLTestRunner.py文件就是需要下载的包。
4 .下载后手动拖到python安装文件的Lib目录下
"""
import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    @classmethod
    def setUpclass(cls):
        print("start\n")
    @classmethod
    def tearDown(cls):
        print('stop')

    def testAdd(self):  # test method names begin 'test*'：unittest模块，测试方法必须以test开头才可以执行
        print("testadd888")
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)


    def testMultiply(self):
        print("testmulgiply999")
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
if __name__=='__main__':
    unittest.main()
