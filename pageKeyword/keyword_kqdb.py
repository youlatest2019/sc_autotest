#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:50
# @Author   : yangshukun
# @File     : keyword_1104_kqdb.py

from pageElement.page_kqdb import *
from baseOperation.WebOperation import *


class Rn1104kqdbMainKeyword(Rn1104kqdbMainPage, WebDriver):

    def inputbsnrRn1104kqdb(self):
        """1104跨期对比页面，选择报送内容名称"""
        self.Click(self.BUTTON_BSNRMC1)
        self.Click(self.SELECT_BSNRMC1)

    def inputbsqjRn1104kqdb(self):
        """1104跨期对比页面，选择报报送期间"""
        self.Click(self.BUTTON_BSQJ1)
        self.Click(self.SELECT_BSQJ1)

    def inputqzfsRn1104kqdb(self):
        """1104跨期对比页面，选择取值方式"""
        self.Click(self.BUTTON_QZFS)
        self.Click(self.SELECT_QZFS_BQZHYICBS)    #选择取值方式-本期最后一次报送
        #self.Click(self.SELECT_QZFS_BQSCBS)      #选择取值方式-本期首次报送

    def clickRefreshButtonRn1104kqdb(self):
        """1104跨期对比页面，点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_RN1104_KQDB)

    def clickExportButtonRn1104kqdb(self):
        """1104跨期对比页面，点击导出按钮"""
        self.Click(self.BUTTON_EXPORT_RN1104_KQDB)


class RPbcckqdbMainKeyword(RPBCCkqdbMainPage, WebDriver):

    def inputbsnrRpbcckqdb(self):
        """人行大集中跨期对比页面，选择报送内容名称"""
        self.Click(self.BUTTON_BSNRMC2)
        self.Click(self.SELECT_BSNRMC2)

    def inputbsqjRpbcckqdb(self):
        """人行大集中跨期对比页面，选择报报送期间"""
        self.Click(self.BUTTON_BSQJ2)
        self.Click(self.SELECT_BSQJ2)

    def inputqzfsRpbcckqdb(self):
        """人行大集中跨期对比页面，选择取值方式"""
        self.Click(self.BUTTON_QZFS)
        self.Click(self.SELECT_QZFS_BQZHYICBS)    #选择取值方式-本期最后一次报送
        #self.Click(self.SELECT_QZFS_BQSCBS)      #选择取值方式-本期首次报送

    def clickRefreshButtonRpbcckqdb(self):
        """人行大集中跨期对比页面，点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_RPBCC_KQDB)

    def clickExportButtonRpbcckqdb(self):
        """人行大集中跨期对比页面，点击导出按钮"""
        self.Click(self.BUTTON_EXPORT_RPBCC_KQDB)


class RFBSkqdbMainKeyword(RFBSkqdbMainPage, WebDriver):

    def inputsjrqRfbskqdb(self, sjrq):
        """金数跨期对比页面，选择数据日期"""
        self.Click(self.INPUT_PUB_SJRQ)
        self.Input(sjrq, self.INPUT_PUB_SJRQ)

    def inputqzfsRfbskqdb(self):
        """金数跨期对比页面，选择取值方式"""
        self.Click(self.BUTTON_QZFS)
        self.Click(self.SELECT_QZFS_BQZHYICBS)

    def clickRefreshButtonRfbsqdb(self):
        """金数跨期对比页面，点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_RFBS_KQDB)

    def clickExportButtonRfbskqdb(self):
        """金数跨期对比页面，点击导出按钮"""
        self.Click(self.BUTTON_EXPORT_RFBS_KQDB)

    def clickDWCKYEButton(self):
        """单位存款余额"""
        self.Click(self.BUTTNO_DWCKYE)

    def clickDWCKFSEButton(self):
        """单位存款发生额"""
        self.Click(self.BUTTNO_DWCKFSE)

    def clickJDSJHCXXEButton(self):
        """极端数据核查信息"""
        self.Click(self.BUTTNO_JDSJHCXXE)

    def clickCLFTYButton(self):
        """存量非同业单位存款信息大集中数据核对"""
        self.Click(self.BUTTNO_CLFTY)