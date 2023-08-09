#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:34
# @Author   : yangshukun
# @File     : case_pbcc_kqdb.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_baobiao_common import *
from pageKeyword.keyword_kqdb import *
import sys
from Common.OtherFunc import *


class RpbccMainProcessTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword,
                            BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword, RPbcckqdbMainKeyword):

    def test_01_PBCC_kqdb(self):
        """人行大集中--跨期对比--选择报送内容名称、报送期间、取值方式--刷新--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入人行大集中跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intopbccKqdbPage()
        # 02、选择报送内容
        self.inputbsnrRpbcckqdb()
        # 03、选择报送期间
        self.inputbsqjRpbcckqdb()
        # 04、选择取值方式
        self.inputqzfsRpbcckqdb()
        # 05、刷新
        self.clickRefreshButtonRpbcckqdb()
        # 06、导出
        self.clickExportButtonRpbcckqdb()