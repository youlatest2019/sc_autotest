#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/18 11:20
# @Author   : yangshukun
# @File     : case_bsgl_rpbcc.py
import time

from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from data.data_class.common_data import *
import sys
from Common.OtherFunc import *
from pageKeyword.keyword_bsgl_rpbcc import *


class BsglRpbccTest(InitCls, BsglMainKeyword, BsglPubBbmbKeyword, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                    BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword, BsglBsplData, BsglPubBsnrsqKeyword,
                    BsglPubHswhKeyword, BsglPubSjxwhKeyword, ZdysjlxPubSplcKeyword, BsglRpbccBscsKeyword,
                    XsjdpzPubSplcKeyword, PubLsbbKeyword):

    def test_01_rpbcc_import_module_success(self):
        """RPBCC人行报表模板导入成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择rpbcc品种进入rpbcc管理界面
        self.switchToBsglBaseFrame()
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导入模板
        self.switchBspzFrame()
        self.importBbmb(self.RPBCC_A1302_PATH)
        self.GotoSleep(1)
        # 断言导入成功
        res = self.GetTagText(self.MSG_IMPORT_RESULT)
        self.assertEqual(res, '成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_rpbcc_export_module_success(self):
        """RPBCC报表模板导出成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.switchToBsglBaseFrame()
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导出模板
        self.switchBspzFrame()
        self.inputBsnrbh("A1302")
        self.refreshBbmbPage()
        self.clickCheckBox(1)
        self.exportBbmb()
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_add_bsrw_rpbcc_success(self):
        """rpbcc废弃报送任务+报送任务新增成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        self.switchBspzFrame()
        # 判断报送任务是否存在，存在则废弃
        response = self.queryBsrw("2021年第一季度", "A1302")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("rpbcc任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRpbccTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("A1302", "2021")
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 7、断言新增成功
        self.GotoSleep(1)
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功")
        self.closeXzrw_success()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_rpbcc_bsfw_success(self):
        """rpbcc报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择rpbcc品进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("按季", "A1302")
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        self.clickOkAlert()
        # 6、查询并点击是否报送按钮(是)
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_change_rpbcc_bsfw_success(self):
        """rpbcc报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并修改单个报送内容设置
        self.bsglMainFrame()
        self.queryBsnr(self.PL_SEASON, "A1302")
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 45 /1 * * ?", "15", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_add_edit_del_group_rpbcc_success(self):
        """rpbcc分组管理--新增分组，编辑，删除，成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToFzgl()
        # 6、新增分组并断言成功
        self.bsglMainFrame()
        group_name = "rpbcc自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限1", "自动化测试_rpbcc分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        self.editeGroup(group_name, group_name + "_修改", "自动化测试_rpbcc分组描述_修改")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 8查询修改后的名称正确
        self.searchGroupName(group_name + "_修改")
        self.refreshGroupPage()
        res = self.GetTagText(self.DATA_FIRST_GROUP.format(1))
        self.assertEqual(res, group_name + "_修改")
        # 删除分组
        self.delGroup(group_name + "_修改")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_bssq_success(self):
        """rpbcc报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rpbcc自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限1", "自动化测试_rpbcc授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("A1302")
        self.refreshBssqPage()
        # 8、勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.tickSbqx()
        self.tickCxqx()
        self.tickCcqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入分组管理
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 10、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_rpbcc_splc_batch_update_success(self):
        """rpbcc审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rpbcc自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限1", "自动化测试_rpbcc授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("A1302")
        self.refreshBssqPage()
        # 8、勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入审批流程页面
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshSplcPage()
        # 11、勾选报送内容，批量修改,并断言修改成功
        self.tickBoxAll()
        self.batchUpdateSplc("人行报表审批")
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.bsglMainFrame()
        res = self.GetTagText(self.MSG_BATCH_ALERT_SPLC)
        self.assertEqual(res, "保存成功")
        self.closeBatchAlertSplc()
        # 进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_09_rpbcc_bsnrsq_edit_all_success(self):
        """rpbcc报送内容授权--编辑全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rpbcc分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rpbcc授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("A1302")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("A1302")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("A1302-监管类指标季报表1（人民币）")
        # 12、点击编辑全部，进行授权
        self.clickEditAllBsnrsq()
        self.AlertAccept()
        # 13、断言编辑全部授权后，检查编辑权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("A1302-监管类指标季报表1（人民币）", 1)).split("(")[1].split(")")[
            0]
        self.assertGreater(int(res), 0)
        # 14、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 15、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_rpbcc_bsnrsq_trace_all_success(self):
        """rpbcc报送内容授权--追溯全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rpbcc分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rpbcc授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("A1302")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("A1302")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("A1302-监管类指标季报表1（人民币）")
        # 12、点击追溯全部，进行授权
        self.clickTraceAllBsnrsq()
        self.AlertAccept()
        # 13、断言追溯全部授权后，检查追溯权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("A1302-监管类指标季报表1（人民币）", 2)).split("(")[1].split(")")[
            0]
        self.assertGreater(int(res), 0)
        # 14、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 15、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_11_rpbcc_bsnrsq_cancel_all_success(self):
        """rpbcc报送内容授权--取消全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rpbcc分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rpbcc授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("A1302")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("A1302")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("A1302-监管类指标季报表1（人民币）")
        # 12、点击追溯全部，进行授权
        self.clickTraceAllBsnrsq()
        self.AlertAccept()
        # 13、断言追溯全部授权后，检查追溯权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("A1302-监管类指标季报表1（人民币）", 2)).split("(")[1].split(")")[
            0]
        self.assertGreater(int(res), 0)
        # 14、取消全部授权，断言取消后权限项为0
        self.choiceBoxByNameBsnrsq("A1302-监管类指标季报表1（人民币）")
        self.clickCancelAllBsnrsq()
        self.AlertAccept()
        res1 = \
            self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("A1302-监管类指标季报表1（人民币）", 2)).split("(")[1].split(")")[0]
        self.assertEqual(int(res1), 0)
        res2 = \
            self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("A1302-监管类指标季报表1（人民币）", 1)).split("(")[1].split(")")[0]
        self.assertEqual(int(res2), 0)
        # 15、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 16、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_12_rpbcc_hswh_add_function_success(self):
        """rpbcc函数维护--新增函数成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入函数维护页面，点击新增进入新增页面
        self.swithToHswh()
        self.bsglMainFrame()
        self.addHswhMainPage()
        self.switchToDetailFrame()
        # 6、输入函数基础信息
        hsmc = "rpbcc自动化测试函数" + get_now_time_to_str()
        self.inputHsmcHswhDetailPage(hsmc)
        self.inputHslbHswhDetailPage(self.HSLB_DKYE)
        self.inputHsmsHswhDetailPage("rpbcc自动化测试-函数描述")
        self.inputResTypeHswhDetailPage(self.RES_ZS)
        self.inputSqlHswhDetailPage("select @1 from dual")
        # 7、点击解析参数，并输入参数名称、类型、参数值
        self.clickAnalParamHswhDetailPage()
        self.makeParamsInfoHswhDetailPage("rpbcc自动化测试参数", self.PARAMS_TEXT, "1")
        # 8、点击测试,并断言测试sql成功,退出测试界面
        self.clickTestHswhDetailPage()
        res = self.GetTagText(self.MSG_DETAIL_HSWH)
        self.assertEqual(res, "SQL预执行成功，语法正确！")
        self.closeAlertTestHswhDetailPage()
        self.closeTestHswhDetailPage()
        # 9、切换到详情frame，点击保存，并断言保存成功
        self.switchToDetailFrame()
        self.clickSaveHswhDetailPage()
        res1 = self.GetTagText(self.MSG_DETAIL_HSWH)
        self.assertEqual(res1, "保存成功")
        self.closeHswhAlert()
        self.closeHswhDetailMainPage()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_13_rpbcc_sjxwh_add_data_success(self):
        """rpbcc数据项维护维护--新增数据项成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入数据项维护页面，点击新增按钮
        self.swithToSjxwh()
        self.switchBspzFrame()
        self.clickSjxwhAddButton()
        # 6、输入数据项基本信息
        sjx_name = "rpbcc自动化数据项名称" + get_now_time_to_str()
        self.inputSjxwhInfo(sjx_name, "rpbcc自动化数据项描述", self.GROUP_SEASON_ONE, "A2333-涉农贷款季报表")
        # 7、添加函数并插入
        self.choiceSjxwhFuncDataAndInster("6")
        # 8、添加数据项并插入
        self.choiceSjxwhItemsDataAndInster("A1463.12D47_人民币")
        # 9、保存
        self.clickSjxwhSaveButton()
        res2 = self.GetTagText(self.MSG_FUNC_FORM_SJXWH)
        self.assertEqual(res2, "保存成功！")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_14_rpbcc_bscs_change_success(self):
        """rpbcc报送参数--修改报送参数成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送参数页面
        self.swithToBscs()
        self.switchBspzFrame()
        # 6、输入参数值并保存成功
        self.changeRpbccBscsJgldm("001")
        self.changeRpbccBscsDqdm("81045")
        self.changeRpbccBscsFile()
        self.changeRpbccBscsSbsp()
        self.changeRpbccBscsSave()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_15_rpbcc_set_zdysjlx_success(self):
        """设置rpbcc-自定义数据类型"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入自定义数据类型页签
        self.swithToZdysjlx()
        self.ZdysjlxFrame()
        # 新增数据类型-编辑数据类型-新增数据类型明细-编辑数据类型明细-删除数据类型失败（该自定义类型已被引用，不可删除！）--删除数据类型明细后（删除成功！）--删除数据类型成功（删除成功！）
        # 6、数据类型-新增按钮
        self.addSjlxButton()
        # 7、数据类型-新增-编号
        bh = "zdy" + get_now_time_to_str()
        self.addSjlxBh(bh)
        # 8、数据类型-新增-名称
        base_name = "rpbcc自定义" + get_now_time_to_str()
        add_name = base_name + "-新增"
        edit_name = base_name + "-编辑"
        self.addSjlxName(add_name)
        # 9、数据类型-新增-说明
        self.addSjlxSm(add_name + "说明")
        # 10、数据类型-新增-保存按钮
        self.addSjlxSave()
        # 11、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 12、数据类型-选择点击数据行
        self.choiceSjlxClick(bh)
        # 13、数据类型-编辑按钮
        self.editSjlxButton()
        # 14、数据类型-编辑-名称
        self.editSjlxName(edit_name)
        # 15、数据类型-编辑-说明
        self.editSjlxSm(edit_name + "说明")
        # 16、数据类型-编辑-保存按钮
        self.editSjlxSave()
        # 17、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 18、数据类型-选择点击数据行
        self.choiceSjlxClick(bh)
        # 19、数据类型明细-新增按钮
        self.addSjlxMxButton()
        # 20、数据类型明细-新增-名称
        self.addSjlxMxName("数据类型明细-新增名称")
        # 21、数据类型明细-新增-参数值
        self.addSjlxMxCsz("数据类型明细-新增参数值")
        # 22、数据类型明细-新增-保存按钮
        self.addSjlxMxSave()
        # 23、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 24、数据类型明细-勾选第一行
        self.SelectSjlxMxFrist()
        # 25、数据类型明细-编辑按钮
        self.editSjlxMxButton()
        # 26、数据类型-编辑-名称
        self.editSjlxMxName("数据类型明细-编辑名称")
        # 27、数据类型-编辑-说明
        self.editSjlxMxCsz("数据类型明细-编辑参数值")
        # 28、数据类型-编辑-保存按钮
        self.editSjlxMxSave()
        # 29、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 30、数据类型-删除按钮
        self.delSjlxButton()
        # 31、断言 -数据类型-删除按钮-删除失败-该自定义类型已被引用，不可删除！
        res = self.GetTagText(self.MSG_SJLX_RESULT_SUCCESS)
        self.assertEqual(res, '该自定义类型已被引用，不可删除！')
        # 32、数据类型--删除失败--确定
        self.delSjlxFail()
        # 33、数据类型明细复选框全选
        self.SelectSjlxMxAll()
        # 34、数据类型明细-删除按钮
        self.delSjlxMxButton()
        # 35、断言 -数据类型明细-删除按钮-删除成功
        res = self.GetTagText(self.MSG_SJLXMX_RESULT_SUCCESS)
        self.assertEqual(res, '删除成功！')
        # 36、关闭删除成功弹窗
        self.delSjlxMxSuccessClose()
        # 37、数据类型-删除按钮
        self.delSjlxButton()
        # 38、断言 -数据类型-删除按钮-删除成功
        res = self.GetTagText(self.MSG_SJLX_RESULT_SUCCESS)
        self.assertEqual(res, '删除成功！')
        # 39、关闭删除成功弹窗
        self.delSjlxSuccessClose()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_16_rpbcc_xsjdpz_change_success(self):
        """rpbcc小数精度配置--配置小数精度成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表品种进入rpbcc管理界面
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 进入报表模板管理页签
        self.swithToBbmb()
        # 导入模板
        self.switchBspzFrame()
        self.importBbmb(self.RPBCC_A1302_PATH)
        self.GotoSleep(1)
        # 断言导入成功
        res = self.GetTagText(self.MSG_IMPORT_RESULT)
        self.assertEqual(res, '成功')
        # 5、进入小数精度配置页面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRpbccTab()
        self.switchBspzFrame()
        self.swithToXsjdpz()
        self.switchBspzFrame()
        # 6、点击通用小数位数配置
        self.clickTyxswspz()
        # 7、切换到通用小数位数frame
        self.changeTyxswspzframe()
        # 8、修改通用小数位数--数值-通用计算、显示小数位数；百分比-通用计算、显示小数位数
        ty_szjsxs = "4"
        ty_szxsxs = "2"
        ty_bfbjsxs = "3"
        ty_bfbxsxs = "2"
        ty_jejsxs = "5"
        ty_jexsxs = "2"
        ty_llbjsxs = "2"
        ty_llbxsxs = "2"
        self.inputTyxswspzJeJs(ty_jejsxs)
        self.inputTyxswspzJeXs(ty_jexsxs)
        self.inputTyxswspzSzJs(ty_szjsxs)
        self.inputTyxswspzSzXs(ty_szxsxs)
        self.inputTyxswspzBfbJs(ty_bfbjsxs)
        self.inputTyxswspzBfbXs(ty_bfbxsxs)
        self.inputTyxswspzLlJs(ty_llbjsxs)
        self.inputTyxswspzLlXs(ty_llbxsxs)
        # 9、通用小数位数配置-点击保存
        self.saveTyxswspz()
        # 断言 -通用小数位数配置-点击保存-保存成功
        res = self.GetTagText(self.MSG_TYXSWSPZ_SAVE_SUCCESS)
        self.assertEqual(res, '保存成功')
        # 10、通用小数位数配置-关闭保存成功弹窗
        self.closeTyxswspzSaveSuccess()
        # 通用小数位数配置 - 关闭通用小数位数配置页面
        self.QuiteFrame()
        self.closeTyxswspz()
        # 11、切换frame
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        # 12、断言--修改通用小数位数在数据列表表头是否显示正确
        msg = "品种通用小数位数" + "\n" + "显示小数位数（金额：" + ty_jexsxs + "位；数值：" + ty_szxsxs + "位；百分比：" + ty_bfbxsxs + "位；利率：" + ty_llbxsxs + "位）" + "\n" + "计算小数位数（金额：" + ty_jejsxs + "位；数值：" + ty_szjsxs + "位；百分比：" + ty_bfbjsxs + "位；利率：" + ty_llbjsxs + "位）"
        res = self.GetElementAttrbute(self.MSG_TYXSWSPZ_SJLBXS, "title")
        self.assertEqual(res, msg)
        # 13、输入报送内容名称
        self.inputXsjdpzBsnrmc("A1302")
        # 14、刷新页面
        self.refeshXsjdpzPage()
        # 15、点击编辑按钮-进入小数精度批量配置页面
        self.clickXsjdpzEdit()
        # 进入小数精度批量配置页面-切换窗口句柄传递权利
        self.get_window_handle()
        # 16、小数精度批量配置页面-刷新
        self.refeshXsjdplpzPage()
        # 17、小数精度批量配置-未勾选单元格-点击修改小数位数
        self.alterXsjdplpz("修改单元格小数位数")
        # 断言--请选择需要修改的数据项。
        res = self.GetTagText(self.MSG_XSJDPLPZ_ALTER_NULL)
        self.assertEqual(res, '请选择需要修改的数据项。')
        # 点击提示框确定按钮
        self.okXsjdplpzAlterNull()
        # 18、小数精度批量配置-单元格frame
        self.changeXsjdplpzDygframe()
        # 19、小数精度批量配置 - 选中单元格
        ri = "6"  # 6行
        ci = "3"  # 3列
        self.chooseXsjdplpzDyg(ri, ci)
        # 20、点击修改小数位数,切换修改小数位数frame
        self.QuiteFrame()
        self.alterXsjdplpz("修改单元格小数位数")
        self.changeAlterDygxswsframe()
        # 21、小数精度批量配置-修改小数位数-选择数据类型
        self.chooseXsjdplpzAlterSjlx(self.ALTER_SJXLX_SZ)  # 数值
        # 22、小数精度批量配置-修改小数位数-计算小数位数
        self.inputXsjdplpzAlterJsxsws(3)  # 3位
        # 23、小数精度批量配置-修改小数位数-显示小数位数
        self.inputXsjdplpzAlterXsxsws(2)  # 2位
        # 24、小数精度批量配置-修改小数位数-保存按钮
        self.clickXsjdplpzAlterSave()
        self.QuiteFrame()
        # 25、关闭小数精度批量配置窗口
        self.driver.close()
        time.sleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_17_import_lsmodule_success(self):
        """人行报表历史报表导入成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择1104品种进入1104管理界面
        self.switchToBsglBaseFrame()
        self.intoRpbccTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入历史报表管理页签
        self.swithToLsbb()
        # 6、选择报送频率和报送日期
        self.switchBspzFrame()
        self.changeLsbbBspl("按月")
        self.changeLsbbBsrq("2025-06-30")
        self.changeLsbbRefresh()
        self.changeLsbbImport(self.A1411_PATH)
        self.GotoSleep(3)
        # 断言导入成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '导入成功!')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
