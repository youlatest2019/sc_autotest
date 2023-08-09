#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:34
# @Author   : yangshukun
# @File     : case_1104_kqdb.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_baobiao_common import *
from pageKeyword.keyword_kqdb import *
import sys
from Common.OtherFunc import *


class Rn1104MainProcessTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword,
                            BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword, Rn1104kqdbMainKeyword):

    def test_01_1104_kqdb(self):
        """1104--跨期对比--选择报送内容名称、报送期间、取值方式--刷新--导出"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 01、点击主菜单--报送处理，进入1104跨期对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.into1104KqdbPage()
        # 02、选择报送内容
        self.inputbsnrRn1104kqdb()
        # 03、选择报送期间
        self.inputbsqjRn1104kqdb()
        # 04、选择取值方式
        self.inputqzfsRn1104kqdb()
        # 05、刷新
        self.clickRefreshButtonRn1104kqdb()
        # 06、导出
        self.clickExportButtonRn1104kqdb()