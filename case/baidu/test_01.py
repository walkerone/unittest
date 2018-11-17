#! -*- coding:utf-8 -*-
import unittest
import time
from  selenium import webdriver
class Testone(unittest.TestCase):
    def setUp(self):
       pass
    def tearDown(self):
        pass
    def test01(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        time.sleep(1)
        driver.quit

    def test02(self):
        driver = webdriver.Chrome()
        driver.get("https://www.cnblogs.com/")
        time.sleep(1)
        driver.quit()

if __name__=='__main__':
    unittest.main()

