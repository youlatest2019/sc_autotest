#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:50
# @Author   : yangshukun
# @File     : keyword_1104_hedui.py

from pageElement.page_1104_hedui import *
from baseOperation.WebOperation import *


class Rn1104HdMainKeyword(Rn1104HdMainPage, WebDriver):

    def inputSjrqRn1104Hd(self, start_date, end_date):
        """1104核对页面，数据日期输入"""
        self.Click(self.INPUT_START_DATE_RN1104_HD)
        self.Input(start_date, self.INPUT_START_DATE_RN1104_HD)
        self.Click(self.INPUT_END_DATE_RN1104_HD)
        self.Input(end_date, self.INPUT_END_DATE_RN1104_HD)

    def clickRefreshButtonRn1104Hd(self):
        """1104核对页面，点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_RN1104_HD)
