#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/10/31 17:40
# @Author   : tangle
# @File     : keyword_dataset_sq.py
from pageElement.page_dataset_sq import *
from baseOperation.WebOperation import *


class DataSetSqPageKeyword(DataSetSqFrame, DataSetSqMainPage, WebDriver):
    """数据集授权页面关键字"""

    def changeToMainFrameForDataSq(self):
        """切换到数据集授权主FRAME"""
        self.SwitchFrame(self.FRAME_SQ_PAGE)

    def choiceDataSqUserXm(self, user_name):
        """数据集授权-人员名称下拉框输入并选择"""
        self.Click(self.BUTTON_USERXM)
        self.Input(user_name, self.INPUT_USERXM)
        self.Click(self.SELECT_USERXM.format(user_name))

    def choiceDataSqSjjFz(self, group_name):
        """数据集授权--权限项--勾选数据集分组名称复选框"""
        self.Click(self.SELECT_SJJFZ_ALL_SQ.format(group_name))

    def saveDataSetSq(self):
        """点击保存按钮"""
        self.Click(self.BUTTON_SAVE_SQ)

    def refreshDataSetSq(self):
        """点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_SQ)

    def clickUserQuery(self):
        """点击人员权限查询按钮"""
        self.Click(self.BUTTON_USERQUERY)

    def changeToFrameForUserQuery(self):
        """切换到人员权限查询页面frame"""
        self.SwitchFrameByElement(self.FRAME_USERQUERY_PAGE)

    def refreshUserQuery(self):
        """人员权限页面-刷新按钮"""
        self.Click(self.REFRESH_USERQUERY)

    def closeUserQuery(self):
        """关闭人员权限查询页面"""
        self.Click(self.CLOSE_USERQUERY)

    def choiceDataSqRole(self, role_name):
        """数据集授权-点击角色下拉框输入并选择"""
        self.Click(self.BUTTON_ROLE)
        self.Input(role_name, self.INPUT_ROLE)
        self.Click(self.SELECT_ROLE.format(role_name))
