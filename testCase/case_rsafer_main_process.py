#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:34
# @Author   : yangshukun
# @File     : case_1104_main_process.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_baobiao_common import *
import sys
from Common.OtherFunc import *


class RsaferMainProcessTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubFzglKeyword, BsglPubBssqKeyword,
                            BsglPubSplcKeyword,
                            BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword):

    def test_01_rsafer_main_process(self):
        """外管局报表--建立分组->授权->导入模板->新增报送任务->核对提交->审批通过->上报下载，确认上报->查询，主流程案例"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToFzgl()
        # 6、新增分组
        self.bsglMainFrame()
        group_name = "外管局报表自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "征信权限1", "自动化测试_外管局报表分组描述")
        # 7、分组授权
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 8、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
        self.refreshBssqPage()
        # 9、勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.tickSbqx()
        self.tickCxqx()
        self.tickCcqx()
        self.saveBssq()
        # 10、进入审批流程页面
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 11、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshSplcPage()
        # 12、勾选报送内容，批量修改,并断言修改成功
        self.tickBoxAll()
        self.batchUpdateSplc("外管局报表审批")
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.bsglMainFrame()
        self.closeBatchAlertSplc()
        # 13、进入报表模板页面，导入模板
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToBbmb()
        self.switchBspzFrame()
        self.importBbmb(self.RSAFER_P02_PATH)
        self.GotoSleep(1)
        # 14、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 15、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 16、切换到品种管理frame
        bsnr_name = "P02-大额结售汇交易统计表"
        bsqj = "2022年06月30日"
        bbbh = "P02"
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.queryBsrw(bsqj, bsnr_name)
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("外管局报表任务自动化废弃")
        # 17、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 18、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bbbh, "20220630", type="day", qssd_index=3)
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 19、点击主菜单--报送处理，进入外管局报表核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferHdPage()
        # 20、输入报送期间，和报表编号查询
        self.choiceReportDateForBb(bsqj)
        self.inputReportNoForBb(bbbh)
        self.clickRefreshButtonForBb()
        # 21、选择报送任务，点击提交
        self.tickAllBoxForBb()
        self.submitForBb()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForBb()
        # 22、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferSpPage()
        self.entringHandleForBb(biz_flow_name="外管局报表审批")
        # 23、搜索对应的报送任务，全选，审批通过
        self.choiceReportDateForBb(bsqj)
        self.inputReportNoForBb(bbbh)
        self.clickRefreshButtonForBb()
        self.tickAllBoxForBb()
        self.inputAuditReasonForBb("自动化外管局报表审批通过")
        self.clickAuditAgreeForBb()
        res2 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("审批成功", res2)
        self.clickAlertConfirmButtonForBb()
        # 24、进入上报页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferSbPage()
        # 25、搜索对应报送任务，全选，打包下载，确认成功
        self.inputSbSjrqForBb("ifrRMM031503")
        self.choiceReportDateForBb(bsqj)
        self.inputReportNoForBb(bbbh)
        self.clickRefreshButtonForBb()
        self.tickAllBoxForBb()
        self.clickDownloadButtonForBb()
        self.clickQrcgButtonForBb()
        res3 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("上报成功", res3)
        self.clickAlertConfirmButtonForBb()
        # 26、进入查询页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferCxPage()
        # 27、搜索对应报送任务，批量导出
        self.inputCxSjrqForBb("ifrRMM031504")
        self.choiceReportDateForBb(bsqj)
        self.inputReportNameForBb(bbbh)
        self.clickRefreshButtonForBb()
        self.tickAllBoxCxPageForBb()
        self.exportBatchForBb()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_rsafer_audit_refused(self):
        """外管局报表--审批驳回后，核对页面可正常查看报送任务，且驳回意见正确"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入rsafer管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 编辑管理员分组，把登录用户添加为管理员
        self.addUserForAdminGroup()
        # 13、进入报表模板页面，导入模板
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToBbmb()
        self.switchBspzFrame()
        self.importBbmb(self.RSAFER_P02_PATH)
        self.GotoSleep(1)
        # 14、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 15、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 16、切换到品种管理frame
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.queryBsrw("2030年10月12日", "P02-大额结售汇交易统计表")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("外管局报表任务自动化废弃")
        # 17、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 18、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("P02", "20301012", type="day", qssd_index=3)
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 19、点击主菜单--报送处理，进入外管局报表核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferHdPage()
        # 20、输入报送期间，和报表编号查询
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        # 21、选择报送任务，点击提交
        self.tickAllBoxForBb()
        self.submitForBb()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForBb()
        # 22、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferSpPage()
        self.entringHandleForBb(biz_flow_name="外管局报表审批")
        # 23、搜索对应的报送任务，全选，审批通过
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        self.tickAllBoxForBb()
        self.inputAuditReasonForBb("自动化外管局报表报表审批驳回")
        self.clickAuditRefuseForBb()
        res2 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("审批成功", res2)
        self.clickAlertConfirmButtonForBb()
        # 19、点击主菜单--报送处理，进入外管局报表核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferHdPage()
        # 20、输入报送期间，和报表编号查询
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        # 断言驳回成功，且驳回意见与审批一致
        res3 = self.GetTagText(self.DATA_PUB_TABLE_NO_BB)
        self.assertEqual("P02", res3)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_rsafer_go_back_task(self):
        """外管局报表--上报页面退回上报数据，用户在核对页面可正常查看退回的任务，且退回意见正确"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 编辑管理员分组，把登录用户添加为管理员
        self.addUserForAdminGroup()
        # 13、进入报表模板页面，导入模板
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToBbmb()
        self.switchBspzFrame()
        self.importBbmb(self.RSAFER_P02_PATH)
        self.GotoSleep(1)
        # 14、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 15、选择rsafer品种进入rsafer管理界面
        self.intoRsaferTab()
        # 16、切换到品种管理frame
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.queryBsrw("2030年10月12日", "P02-大额结售汇交易统计表")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("外管局报表任务自动化废弃")
        # 17、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 18、选择rsafer品种进入rsafer管理界面
        self.intoRsaferTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("P02", "20301012", type="day", qssd_index=3)
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 19、点击主菜单--报送处理，进入rsafer核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferHdPage()
        # 20、输入报送期间，和报表编号查询
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        # 21、选择报送任务，点击提交
        self.tickAllBoxForBb()
        self.submitForBb()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForBb()
        # 22、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferSpPage()
        self.entringHandleForBb(biz_flow_name="外管局报表审批")
        # 23、搜索对应的报送任务，全选，审批通过
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        self.tickAllBoxForBb()
        self.inputAuditReasonForBb("自动化外管局报表审批通过")
        self.clickAuditAgreeForBb()
        res2 = self.GetTagText(self.MSG_PUB_BB_1)
        self.assertIn("审批成功", res2)
        self.clickAlertConfirmButtonForBb()
        # 24、进入上报页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferSbPage()
        # 25、搜索对应报送任务，全选，打包下载，确认成功
        self.inputSbSjrqForBb("ifrRMM031503")
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        # 获取主系统窗口handle
        main_handle = self.GetNowHandle()
        # 进入报送任务详情页面
        self.clickBbxqButtonForBb()
        # 获取报表详情窗口handle，切换到报表详情窗口
        all_handle = self.GetAllHandle()
        for handle in all_handle:
            if handle != main_handle:
                bb_handle = handle
                self.SwitchHandle(bb_handle)
                # 报表详情点击退回按钮
                self.clickGoBackButtonForBb()
                self.goBackSuccForBb("外管局报表自动化退回")
        self.SwitchHandle(main_handle)
        # 19、点击主菜单--报送处理，进入rsafer核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsaferHdPage()
        # 20、输入报送期间，和报表编号查询
        self.choiceReportDateForBb("2030年10月12日")
        self.inputReportNoForBb("P02")
        self.clickRefreshButtonForBb()
        # 断言驳回成功，且驳回意见与审批一致
        res3 = self.GetTagText(self.DATA_PUB_TABLE_NO_BB)
        self.assertEqual("P02", res3)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
