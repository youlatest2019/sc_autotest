#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/5 17:39
# @Author   : yangshukun
# @File     : keyword_bsgl_rsafe.py

from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class RsafeZhxzwhKeyword(BsglElementMain, BsglElementFrame, RsafeZhxzwhElement, WebDriver):
    """账户性质维护页面关键字"""

    def addZhxzwh(self, bh_number, name):
        """新增账户性质数据"""
        self.Click(self.BUTTON_ADD)
        self.Input(bh_number, self.INPUT_ZHXZBH)
        self.Input(name, self.INPUT_ZHXZMC)

    def saveZhxzwh(self):
        """保存数据，并处理弹窗"""
        self.Click(self.BUTTON_SAVE)
        self.AlertAccept()

    def delZhxzwh(self, bh_number):
        """删除数据并处理弹窗"""
        self.Click(self.BOX_DEL_DATA.format(bh_number))
        self.Click(self.BUTTON_DEL)
        self.AlertAccept()


class RsafeBscsKeyword(BsglElementMain, BsglElementFrame, RsafeBscsElement, WebDriver):
    """报送参数页面关键字"""

    def changeRsafeBscsSave(self):
        """外管局修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_WGJ)

    def changeRsafeBscsYhfzjgdm(self, text):
        """外管局修改报送参数-银行分支机构代码"""
        self.ClearData(self.INPUT_YHFZJGDM_WGJ)
        self.Input(text, self.INPUT_YHFZJGDM_WGJ)

    def changeRsafeBscsYhfzjgmc(self, text):
        """外管局修改报送参数-银行分支机构名称"""
        self.ClearData(self.INPUT_YHFZJGMC_WGJ)
        self.Input(text, self.INPUT_YHFZJGMC_WGJ)

    def changeRsafeBscsWbzhkmh(self, text):
        """外管局修改报送参数-外币账户科目号"""
        self.ClearData(self.INPUT_WBZHKMH_WGJ)
        self.Input(text, self.INPUT_WBZHKMH_WGJ)

    def changeRsafeBscsHlzsgz(self):
        """外管局修改报送参数-汇率折算规则"""
        self.Click(self.INPUT_HLZSGZ_WGJ)

    def changeRsafeBscsWgjsbhm(self, text):
        """外管局修改报送参数-外管局申报号码"""
        self.ClearData(self.INPUT_WGJSBHM)
        self.Input(text, self.INPUT_WGJSBHM)


class RsafeJybmwhKeyword(BsglElementMain, BsglElementFrame, RsafeJybmwhElement, WebDriver):
    """交易编码维护页面关键字"""

    def changeRsafeJybmwhSave(self):
        """外管局交易编码维护-保存"""
        self.Click(self.BUTTON_SAVE_JYBMWH)

    def changeRsafeJybmwhAdd(self):
        """外管局交易编码维护-新增"""
        self.Click(self.BUTTON_ADD_WGJ)

    def changeRsafeJybmwhJybm(self, text):
        """外管局交易编码维护-交易编码"""
        self.Input(text, self.INPUT_JYBM_WGJ)

    def changeRsafeJybmwhJymc(self, text):
        """外管局交易编码维护-交易名称"""
        self.Input(text, self.INPUT_JYMC_WGJ)

    def changeRsafeJybmwhCloseX(self):
        """外管局交易编码维护-X按钮"""
        self.Click(self.BUTTON_CLOSE_WGJ)

    def changeRsafeJybmwhDelete(self):
        """外管局交易编码维护-删除"""
        self.Click(self.BUTTON_DELETE_JYBMWH)

    def changeRsafeJybmwhFxkAll(self):
        """外管局交易编码维护-全选复选框"""
        self.Click(self.CHECK_BOX_ALL_WGJ)

    def changeRsafeJybmwhFxkOne(self, text):
        """外管局交易编码维护-单选复选框"""
        self.Click(self.CHECK_BOX_ONE_WGJ.format(text))

class RsafeTbrwhKeyword(BsglElementMain, BsglElementFrame, RSAFEtbrwhElement, WebDriver):
    """填报人维护页面关键字"""

    def addTbrwh(self, tbrzh, tbrmc ,tbrdh):
        """新增填报人数据"""
        self.Click(self.RSAFEtbrwhXZ)
        self.Input(tbrzh, self.INPUT_TBRZH)
        self.Input(tbrmc, self.INPUT_TBRMC)
        self.Input(tbrdh, self.INPUT_TBRDH)

    def saveTbrwh(self):
        """保存数据，并处理弹窗"""
        self.Click(self.RSAFEtbrwh_ALL)
        self.Click(self.RSAFEtbrwhBC)
        self.AlertAccept()

    def delTbrwh(self):
        """删除数据并处理弹窗"""
        self.Click(self.RSAFEtbrwh_ALL)
        self.Click(self.RSAFEtbrwhSC)
        self.AlertAccept()
