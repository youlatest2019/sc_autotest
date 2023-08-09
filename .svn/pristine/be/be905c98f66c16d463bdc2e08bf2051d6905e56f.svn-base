#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 16:40
# @Author   : yangshukun
# @File     : keyword_bsgl_1104.py
from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class Rn1104BsrypzKeyword(BsglElementMain, BsglElementFrame, WebDriver, Rn1104ElementBsrypzElement):
    """"报送人员配置界面关键字"""

    def choiceBspl(self, bspl_name):
        """选择报送频率"""
        self.Click(self.INPUT_BSPL_BSRYPZ.format(bspl_name))

    def inputBbbh(self, bbbh_name):
        """输入报表编号"""
        self.Input(bbbh_name, self.INPUT_BBBH)

    def inputBbmc(self, bbmc_name):
        """输入报表名称"""
        self.Input(bbmc_name, self.INPUT_BBMC)

    def choiceBbfz(self, bbfz_name):
        """选择报表分组"""
        self.Click(self.INPUT_BBFZ.format(bbfz_name))

    def refreshBsrypz(self):
        """报送人员配置页面刷新按钮"""
        self.Click(self.BUTTON_REFRESH)

    def checkAllBsrypz(self):
        """报送人员配置页面，全选"""
        self.Click(self.BOX_ALL)

    def checkAloneBsrypz(self):
        """报送人员配置页面，单选"""
        self.Click(self.BOX_ALONE)

    def batchUpdate(self, user_type, user_name):
        """批量编辑"""
        self.Click(self.BUTTON_EDIT_MANY)
        self.QuiteFrame()
        self.SwitchFrame(self.RN1104_BSRYPZ_BATCH_UPDATE_FRAME)
        self.Click(self.INPUT_RYLX.format(user_type))
        self.Input(user_name, self.INPUT_NAME)
        self.Click(self.BUTTON_CONFIRM)

    def saveBsrypz(self):
        """报送人员配置页面，保存"""
        self.Click(self.BUTTON_SAVE)

    def updateUserForTable(self, tbr_name, fhr_name, fzr_name):
        """主页面修改填表人，复核人，负责人"""
        self.ClearData(self.INPUT_TBR)
        self.ClearData(self.INPUT_FHR)
        self.ClearData(self.INPUT_FZR)
        self.Input(tbr_name, self.INPUT_TBR)
        self.Input(fhr_name, self.INPUT_FHR)
        self.Input(fzr_name, self.INPUT_FZR)


class BscsRN1104Keyword(BsglElementFrame, RN1104BscsElement, WebDriver):
    """1104报送参数界面关键字"""

    def RN1104BscsFrame(self):
        self.SwitchFrame(self.BSGL_TAB_FRAME)

    def set1104QZSJJJKGYes(self):
        """强制数据校验开关--是"""
        self.Click(self.SET_QZSJJJKG_YES)

    def set1104QZSJJJKGNo(self):
        """强制数据校验开关--否"""
        self.Click(self.SET_QZSJJJKG_NO)

    def set1104BJQSYes(self):
        """表间取数数据变化时重新审批开关--是"""
        self.Click(self.SET_BJQS_YES)

    def set1104BJQSNo(self):
        """表间取数数据变化时重新审批开关--否"""
        self.Click(self.SET_BJQS_NO)

    def set1104SbspYes(self):
        """设置上报审批--是"""
        self.Click(self.SET_SBSP_YES)

    def set1104SbspNo(self):
        """设置上报审批--否"""
        self.Click(self.SET_SBSP_NO)

    def save(self):
        """保存设置"""
        self.Click(self.BUTTON_SAVE_1104)
