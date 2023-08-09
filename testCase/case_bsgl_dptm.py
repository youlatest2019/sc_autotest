#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/1 11:27
# @Author   : tangle
# @File     : case_bsgl_dptm.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_bsgl_1104 import *
from data.data_class.common_data import *
import sys
from Common.OtherFunc import *
from pageKeyword.keyword_bsgl_rpbcc import *


class BsglRpbccTest(InitCls, BsglMainKeyword, BsglPubBbmbKeyword, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                    BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword, BsglBsplData, BsglPubBsnrsqKeyword,
                    BsglPubHswhKeyword, BsglPubSjxwhKeyword, ZdysjlxPubSplcKeyword, BsglRpbccBscsKeyword):

    def test_01_dptm_import_module_success(self):
        """dptm压力测试模板导入成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择dptm品种进入压力测试管理界面
        self.switchToBsglBaseFrame()
        self.intoDptmTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导入模板
        self.switchBspzFrame()
        self.importBbmb(self.DPTM_7DAY_JC_XPATH)
        self.GotoSleep(1)
        # 断言导入成功
        res = self.GetTagText(self.MSG_IMPORT_RESULT)
        self.assertEqual(res, '成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_dptm_export_module_success(self):
        """压力测试模板导出成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择压力测试品种进入dptm管理界面
        self.switchToBsglBaseFrame()
        self.intoDptmTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导出模板
        self.switchBspzFrame()
        self.inputBsnrbh("DPTM01007")
        self.refreshBbmbPage()
        self.clickCheckBox(1)
        self.exportBbmb()
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
