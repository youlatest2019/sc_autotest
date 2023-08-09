#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/5 17:52
# @Author   : yangshukun
# @File     : case_bsgl_rsafe.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_bsgl_rsafe import *
from utils.operationXml import *
import sys
from Common.OtherFunc import *


class BsglRsafeTest(InitCls, BsglMainKeyword, OperationXml, RsafeZhxzwhKeyword, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                    BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSjsqKeyword, RsafeBscsKeyword, RsafeJybmwhKeyword,
                    BsglPubSplcKeyword, RsafeTbrwhKeyword):

    def test_01_add_zhxz_and_delete_success(self):
        """外管局--新增账户性质并删除成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择外管局品种进入外管局接口管理界面
        self.switchToBsglBaseFrame()
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入账户性质维护管理页签
        self.swithToZhxzwh()
        # 6、新增账户性质数据
        self.switchBspzFrame()
        self.addZhxzwh("5001", "自动化测试账户性质名称")
        self.saveZhxzwh()
        self.GotoSleep(1)
        # 7、删除数据
        self.delZhxzwh("5001")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_add_bsrw_rsafe_success(self):
        """外管局报送任务新增报送任务并废弃成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        # 6、新增报送任务
        self.switchBspzFrame()
        self.addBsrw("REP00028", "20210629", type="day")
        self.addBsrwSave()
        # 7、断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功")
        self.closeXzrw_success()
        # 废弃报送任务
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.switchBspzFrame()
        self.queryBsrw("2021年06月29日", "账户开关户信息")
        self.abandonBsrw("外管局任务自动化废弃")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_sfbs_bsfw_success(self):
        """外管局报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("按日", "账户开关户信息")
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

    def test_04_change_bsfw_success(self):
        """外管局报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、修改单个报送内容设置
        self.bsglMainFrame()
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 0 6 * * ?", "15", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_add_group_east_success(self):
        """外管局分组管理--新增分组+删除分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签
        self.swithToFzgl()
        # 6、新增分组并断言成功
        self.bsglMainFrame()
        group_name = "外管局自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "征信权限1", "自动化测试_外管局分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        self.editeGroup(group_name, group_name + "_修改", "自动化测试_外管局分组描述_修改")
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

    def test_06_bssq_success(self):
        """外管局报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "外管局自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "征信权限1", "自动化测试_外管局分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("账户收支余信息")
        self.refreshBssqPage()
        # 勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.tickSbqx()
        self.tickCxqx()
        self.tickCcqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 进入分组管理
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_change_power_east_success(self):
        """外管局数据授权--修改授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签,新增分组并断言成功
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "外管局自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "征信权限1", "自动化测试_外管局分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面选择分组
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("账户收支余信息")
        self.refreshBssqPage()
        # 7、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 8、进入数据授权页面,选择分组
        self.SwitchFatherFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        self.searchGroupNameSjsq(group_name)
        self.searchBsnrSjsq("账户收支余信息")
        self.refreshSjsqPage()
        # 9、点击全部，修改权限为按字段筛选+下拉框并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("操作类型")
        self.clickZdTwoBssqPage("A-新建")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 10、进入报送管理主界面，选择外管局品种进入外管局管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 11、点击数据范围按钮，修改权限为按字段筛选+输入值并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("账号")
        self.inputZdBssqPage("自动化外管局1")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 12、进入报送管理主界面，选择外管局品种进入外管局管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 13、点击数据范围按钮，修改权限为全部并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.clickAllSjsq()
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 14、进入报送管理主界面，选择外管局品种进入外管局管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 15、清除查询条件并断言成功
        self.clearDataBssqPage()
        res = self.GetElementAttrbute(self.INPUT_BSNR_SJSQ, "value")
        self.assertEqual(res, "")
        # 进入分组管理删除分组
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_splc_batch_update_success(self):
        """外管局审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "外管局自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "征信权限1", "自动化测试_外管局分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("账户收支余信息")
        self.refreshBssqPage()
        # 8、勾选核对权限
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
        self.batchUpdateSplc("外管局账户收支余审批")
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

    def test_09_bscs_update_success(self):
        """外管局报送参数修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、修改报送参数并保存成功
        self.swithToBscs()
        self.bsglMainFrame()
        self.changeRsafeBscsYhfzjgdm("changeRsafeBscsYhfzjgdm")
        self.changeRsafeBscsYhfzjgmc("外管局-自动化")
        self.changeRsafeBscsWbzhkmh("1001")
        self.changeRsafeBscsHlzsgz()
        self.changeRsafeBscsWgjsbhm("1213")
        self.changeRsafeBscsSave()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_jybmwh_add_success(self):
        """外管局交易编码维护新增+删除成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、新增交易编码维护并保存成功
        self.swithToJybmwh()
        self.bsglMainFrame()
        self.changeRsafeJybmwhAdd()
        self.changeRsafeJybmwhJybm("001")
        self.changeRsafeJybmwhJymc("自动化测试")
        self.changeRsafeJybmwhSave()
        self.AlertAccept()
        # 6、删除新增的交易编码
        self.changeRsafeJybmwhFxkOne("001")
        self.changeRsafeJybmwhDelete()
        self.AlertAccept()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_11_add_tbrwh_and_delete_success(self):
        """外管局--新增填报人维护并删除成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择外管局品种进入外管局接口管理界面
        self.switchToBsglBaseFrame()
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入账户性质维护管理页签
        self.swithToTbrwh()
        # 6、新增填报人维护数据
        self.switchBspzFrame()
        self.addTbrwh("填报人账号" + get_now_time_to_str(), "填报人名称" + get_now_time_to_str(), "填报人电话" + get_now_time_to_str() )
        self.saveTbrwh()
        self.GotoSleep(1)
        # 7、删除数据
        self.delTbrwh()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))