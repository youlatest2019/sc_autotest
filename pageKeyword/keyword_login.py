#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/6/15 10:24
# @Author   : yangshukun
# @File     : keyword_login.py
from pageElement.page_login import *
from Common.getconf import *
from baseOperation.WebOperation import *


class Login(WebDriver, PageLoginElement):

    def typeUserName(self, username):
        self.FindElement(self.username_loc).send_keys(username)

    def typePassword(self, password):
        self.FindElement(self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.FindElement(self.login_loc).click()

    def login(self):
        conf = Config()
        username = conf.get('BaseUrl', 'user')
        self.typeUserName(username)
        self.clickLogin()

    # @property
    # def getLoginError(self):
    #     '''获取错误信息'''
    #     return self.FindElement(*self.loginError_loc).text
