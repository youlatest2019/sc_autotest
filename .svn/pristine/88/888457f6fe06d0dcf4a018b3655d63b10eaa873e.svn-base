#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/6/16 17:46
# @Author   : yangshukun
# @File     : case_ywbl_common.py
from baseOperation.init_cls import *
from pageKeyword.keyword_login import *
from pageKeyword.keyword_ywbl import *
from utils.operationXml import *
import sys


class YwblCommonTest(InitCls, YwblKeyword, OperationXml):

    def test_export_excel_success(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        '''测试全选导出EXCEL成功'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CWXX)
        self.choiceYwmx(self.YWMX_KJKM)
        self.ywblRefresh()
        # 4、复选框全选
        self.checkBoxControl(self.CHECKBOX_ALL)
        # 5、导出EXCEL
        self.exportData(self.EXPORT_EXCEL)
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_export_csv_success(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        '''测试全选导出EXCEL成功'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CWXX)
        self.choiceYwmx(self.YWMX_KJKM)
        self.ywblRefresh()
        # 4、复选框全选
        self.checkBoxControl(self.CHECKBOX_ALL)
        # 5、导出EXCEL
        self.exportData(self.EXPORT_CSV)
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_add_ygxx_and_del_success(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        '''测试新增员工信息并删除成功'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_YGXX)
        self.ywblRefresh()
        # 4、操作新增员工信息
        self.addYgxxMainTable()
        # 5、断言保存成功
        res = self.getAlertText()
        self.assertEqual("保存成功", res)
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

