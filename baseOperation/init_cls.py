#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/6/15 9:51
# @Author   : yangshukun
# @File     : init_cls.py
import unittest
from selenium import webdriver
from pageKeyword.keyword_login import *
from Common.log import mylog


class InitCls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mylog.info('\n----------【用例开始执行】----------')
        conf = Config()
        username = conf.get('BaseUrl', 'user')
        url = conf.get('BaseUrl', 'url')
        driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        # option.add_argument('disable-infobars')
        DOWNLOAD_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'result')
        chrome_options.add_experimental_option('prefs', {
            'download.default_directory': DOWNLOAD_PATH,  # 设置下载路径，路径不存在会自动创建
            'download.prompt_for_download': False,  # 是否弹窗询问
            'safebrowsing.enabled': False,  # 是否提示安全警告
            # Boolean that records if the download directory was changed by an
            # upgrade a unsafe location to a safe location.
            'download.directory_upgrade': False  # 记录下载目录是否被更改？
        })
        cls.driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.driver.find_element(By.ID, "userno").send_keys(username)
        cls.driver.find_element(By.XPATH, "//*[@id='submitA']/img").click()

    @classmethod
    def tearDownClass(cls):
        mylog.info('\n----------【用例执行结束】----------')
        cls.driver.quit()
