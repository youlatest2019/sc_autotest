#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/1
# @Author   : tangle
# @File     : keyword_bsgl_ramllt.py
from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRamlltBscsKeyword(RAMLLTBscsElement, WebDriver):
    """反洗钱大额报送参数关键字"""

    def inputBscsRamlltCsz(self, csz):
        """反洗钱大额报送参数-报告机构编码-参数值"""
        self.ClearData(self.INPUT_BGJGBM_CSZ)
        self.Input(csz, self.INPUT_BGJGBM_CSZ)

    def clickBscsRamlltSave(self):
        """反洗钱报送参数-点击保存按钮"""
        self.Click(self.BUTTON_SAVE)


class BsglRamlltJkzbSzKeyword(RAMLLTJkzbSzElement, WebDriver):
    """反洗钱大额监控指标设置"""

    def CutJczbmsRamllt(self, jczbbm):
        """反洗钱大额监控指标设置-监测指标描述-剪切"""
        self.CutData(self.INPUT_JCZBMS.format(jczbbm))

    def InputJczbmsRamllt(self, jczbms_new, jczbbm):
        """反洗钱大额监控指标设置-监测指标描述-输入"""
        self.Input(jczbms_new, self.INPUT_JCZBMS.format(jczbbm))

    def PasteJczbmsRamllt(self, jczbbm):
        """反洗钱大额监控指标设置-监测指标描述-粘贴"""
        self.AllChoiceData(self.INPUT_JCZBMS.format(jczbbm))
        self.PasteData(self.INPUT_JCZBMS.format(jczbbm))

    def SaveJkzbSzRamllt(self):
        """反洗钱大额监控指标设置-保存"""
        self.Click(self.BUTTON_SAVEMONITOR)

    def clickSbfwCszRamllt(self, jczbbm, ):
        """反洗钱大额监控指标设置-上报范围-点击参数值下拉列表"""
        self.Click(self.BUTTON_SBFW_CSZ.format(jczbbm))

    def inputSbfwCszRamllt(self, jczbbm, sbfw_csz):
        """反洗钱大额监控指标设置-上报范围-点击参数值下拉列表"""
        self.Click(self.BUTTON_SBFW_CSZ.format(jczbbm))

    def choiceSbfwCszRamllt(self, jczbbm, sbfw_csz):
        """反洗钱大额监控指标设置-上报范围-点击参数值下拉列表-输入选择参数值"""
        self.Click(self.BUTTON_SBFW_CSZ.format(jczbbm))
        self.Input(sbfw_csz, self.INPUT_SBFW_CSZ.format(jczbbm))
        self.Click(self.SELECT_INPUT_SBFW_CSZ.format(jczbbm, sbfw_csz))
        self.Click(self.BUTTON_SBFW_CSZ.format(jczbbm))

    def delSbfwCszRamllt(self, jczbbm, sbfw_csz):
        """反洗钱大额监控指标设置-上报范围-删除参数值"""
        self.Click(self.DEL_SBFW_CSZ.format(jczbbm, sbfw_csz))

    def inputLjjyjeCnyCszRamllt(self, jczbbm, cny_ljje):
        """反洗钱大额监控指标设置-累计交易金额（人民币）-输入参数值"""
        self.ClearData(self.INPUT_LJJYJE_CNY_CSZ.format(jczbbm))
        self.Input(cny_ljje, self.INPUT_LJJYJE_CNY_CSZ.format(jczbbm))

    def inputDbjyjeCnyCszRamllt(self, jczbbm, cny_dbje):
        """反洗钱大额监控指标设置-单笔交易金额（人民币）-输入参数值"""
        self.ClearData(self.INPUT_DBJYJE_CNY_CSZ.format(jczbbm))
        self.Input(cny_dbje, self.INPUT_DBJYJE_CNY_CSZ.format(jczbbm))

    def inputLjjyjeUsaCszRamllt(self, jczbbm, usa_ljje):
        """反洗钱大额监控指标设置-累计交易金额（人民币）-输入参数值"""
        self.ClearData(self.INPUT_LJJYJE_USA_CSZ.format(jczbbm))
        self.Input(usa_ljje, self.INPUT_LJJYJE_USA_CSZ.format(jczbbm))

    def inputDbjyjeUsaCszRamllt(self, jczbbm, usa_dbje):
        """反洗钱大额监控指标设置-单笔交易金额（人民币）-输入参数值"""
        self.ClearData(self.INPUT_DBJYJE_USA_CSZ.format(jczbbm))
        self.Input(usa_dbje, self.INPUT_DBJYJE_USA_CSZ.format(jczbbm))

    def changeQyRamllt(self, jczbbm):
        """反洗钱大额监控指标设置-启用"""
        self.Click(self.BUTTON_CZ_QY.format(jczbbm))
