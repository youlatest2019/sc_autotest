#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:34
# @Author   : yangshukun
# @File     : case_rfbs_kqdb.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_baobiao_common import *
from pageKeyword.keyword_kqdb import *
import sys
from Common.OtherFunc import *


class RFBSMainProcessTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword,
                            BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword, RFBSkqdbMainKeyword):

    def test_01_RFBS_DWCKYE_kqdb(self):
        """金数--跨期对比--选择数据日期、取值方式--刷新--单位存款余额--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入金数跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRfbsKqdbPage()
        # 02、选择数据日期
        sjrq = '2022-06-30'
        self.inputsjrqRfbskqdb(sjrq)
        # 03、选择取值方式
        self.inputqzfsRfbskqdb()
        # 04、刷新
        self.clickRefreshButtonRfbsqdb()
        # 05、点击单位存款余额
        self.clickDWCKYEButton()
        # 06、导出
        self.clickExportButtonRfbskqdb()

    def test_02_RFBS_DWCKFSE_kqdb(self):
        """金数--跨期对比--选择数据日期、取值方式--刷新--单位存款发生额--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入金数跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRfbsKqdbPage()
        # 02、选择数据日期
        sjrq = '2022-06-30'
        self.inputsjrqRfbskqdb(sjrq)
        # 03、选择取值方式
        self.inputqzfsRfbskqdb()
        # 04、刷新
        self.clickRefreshButtonRfbsqdb()
        # 05、点击单位存款发生额
        self.clickDWCKFSEButton()
        # 06、导出
        self.clickExportButtonRfbskqdb()

    def test_03_RFBS_JDSJHCXXE_kqdb(self):
        """金数--跨期对比--选择数据日期、取值方式--刷新--极端数据核查信息--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入金数跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRfbsKqdbPage()
        # 02、选择数据日期
        sjrq = '2022-06-30'
        self.inputsjrqRfbskqdb(sjrq)
        # 03、选择取值方式
        self.inputqzfsRfbskqdb()
        # 04、刷新
        self.clickRefreshButtonRfbsqdb()
        # 05、点击极端数据核查信息
        self.clickJDSJHCXXEButton()
        # 06、导出
        self.clickExportButtonRfbskqdb()

    def test_04_RFBS_CLFTY_kqdb(self):
        """金数--跨期对比--选择数据日期、取值方式--刷新--存量非同业单位存款信息大集中数据核对--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入金数跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRfbsKqdbPage()
        # 02、选择数据日期
        sjrq = '2022-06-30'
        self.inputsjrqRfbskqdb(sjrq)
        # 03、选择取值方式
        self.inputqzfsRfbskqdb()
        # 04、刷新
        self.clickRefreshButtonRfbsqdb()
        # 05、点击存量非同业单位存款信息大集中数据核对
        self.clickCLFTYButton()
        # 06、导出
        self.clickExportButtonRfbskqdb()