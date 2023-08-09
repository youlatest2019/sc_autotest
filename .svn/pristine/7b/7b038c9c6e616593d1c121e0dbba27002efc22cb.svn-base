#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/15 11:44
# @Author   : tangle
# @File     : case_bsgl_js.py
from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_js import *
from pageKeyword.keyword_ptsz import *
from utils.operationXml import *
import sys
from baseOperation.init_self import *
from pageKeyword.keyword_bsgl_common import *
from data.data_class.bsgl_js_data import *
from Common.OtherFunc import *


class PtszBSJGXXTest(InitCls, PTSZMainKeyword, CWGSMainKeyword, JTGSMainKeyword, OperationXml, ZdysjlxPubSplcKeyword):

    def test_01_XZ_cwgs_success(self):
        """新增财务公司信息"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入平台设置主界面
        self.intoPtszMainMenu()
        self.switchToPTSZBaseFrame()
        # 3、选择报送机构信息
        self.intoBsjgxxTab()
        # 4、选择财务公司界面
        self.switchGSYQFrame()
        self.swithToCwgs()
        # 5、新增财务公司信息
        sjkzr_name = '名称' + get_now_time_to_str()
        sjzkr_no = '888' + get_now_time_to_str()
        cwgsgdxx_zjhm = '222' + get_now_time_to_str()
        self.addCwgs_ggxx(sjkzr_name, sjzkr_no, cwgsgdxx_zjhm)
        # 6、保存
        self.SaveCWGS()

    def test_02_jtgs_success(self):
        """新增集团公司信息"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入平台设置主界面
        self.intoPtszMainMenu()
        self.switchToPTSZBaseFrame()
        # 3、选择报送机构信息
        self.intoBsjgxxTab()
        # 4、选择集团公司界面
        self.switchGSYQFrame()
        self.swithToJtgs()
        # 5、新增集团公司信息
        self.addJtgs_ggxx()
        # 6、保存
        self.SaveCWGS()
