#! -*- coding:utf-8 -*-
import unittest
class Testone(unittest.TestCase):
    def setUp(self):
       pass
    def tearDown(self):
        pass
    def test01(self):
      print("测试百度01")
      assert 2==3
    def test02(self):
        print("测试百度02")
if __name__=='__main__':
    unittest.main()