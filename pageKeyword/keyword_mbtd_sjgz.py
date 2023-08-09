#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/8 14:06
# @Author   : yangshukun
# @File     : keyword_mingxi_common.py

from pageElement.page_mbtd_sjgz import *
from baseOperation.WebOperation import *
from pageElement.page_bscl_common import *


class RmbtdDataModifypage(WebDriver, RmbtdDataModifyElementMain, PubBbBspzElement):  # 征信数据更正页面公共关键字

    def inputBusiName(self, name):
        """企业名称/债务人名称输入框"""
        self.Input(name, self.BUSINESS_NAME)
        self.Click(self.BUTTON_PUB_REFRESH_BB)

    def buttonModify(self, name):
        """整笔更正-更正按钮+修改数据"""
        self.Click(self.BUTTON_MODIFY)
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.BUSINESS_INFO_FRAME)
        self.ClearData(self.INPUT_BUSINESS_NAME)
        self.Input(name, self.INPUT_BUSINESS_NAME)

    def buttonSubmit(self):
        """提交按钮"""
        self.Click(self.BUTTON_SUBMIT)

    def buttonFxkAllMBTDGZ(self):
        """勾选全部复选框"""
        self.Click(self.FXK_ALL_MBTDGZ)

    def buttonDeleteMbtdGz(self):
        """整笔删除按钮"""
        self.Click(self.BUTTON_DELETE_MBTDGZ)
        self.Click(self.BUTTON_OK_DELETE)
        self.Click(self.BUTTON_OK_DELETE)

    def buttonModifypart(self, name):
        """按段更正-更正按钮+修改数据"""
        self.Click(self.BUTTON_MODIFY)
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.QYDB_INFO_FRAME)
        self.ClearData(self.INPUT_DEBTOR_NAME)
        self.Input(name, self.INPUT_DEBTOR_NAME)

    def inputGroup(self, group):
        """分组"""
        self.Click(self.INPUT_GROUP.format(group))

    def buttonDeleteMbtdGzPart(self, passage):
        """按段删除-更正按钮+删除数据"""
        self.Click(self.BUTTON_MODIFY)
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.QYDB_INFO_FRAME)
        self.Click(self.BUTTON_DELETE_INFO_ZX.format(passage))
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.AD_ALERT_DELETE_FRAME)
        self.Click(self.SJ_DATE_ZXSJGZ)
        self.Click(self.SJ_DATE_ZXSHGZ_ALL)
        self.Click(self.BUTTON_OK_ZX)
        self.Click(self.ALERT_DELETE_OK)
        self.Click(self.ALERT_TIPS_OK)
