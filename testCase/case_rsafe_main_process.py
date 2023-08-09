#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/15 11:44
# @Author   : tangle
# @File     : case_rsafe_main_process.py
from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_mingxi_common import *
import sys
from Common.OtherFunc import *
from pageKeyword.keyword_rmbtd_hedui import *
from pageKeyword.keyword_oracle_common import *


class RsafeMainProcessTest(InitCls, BsclMainKeyword, PubKeywordHdDataListPageForMx, PubKeywordHdPageForMx,
                           PubKeywordSpPageForMx, PubKeywordSbPageForMx,
                           PubKeywordCxPageForMx, BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSplcKeyword,
                           BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword, PubKeywordMbtdAddPage):

    def test_01_rsafe_main_process(self):
        """外管局--建立分组->授权->新增报送任务-->核对提交->审批通过->上报下载，批量上传,主流程案例(批量上传注意要先配置FTP)"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入利率报备管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送分组管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 编辑管理员分组，把登录用户添加为管理员
        self.addUserForAdminGroup()
        # 6、新增分组
        group_name = "rsafe自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, user_chinese_name, "自动化测试_rsafe自动化分组描述")
        # 7、分组授权
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 8、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("账户收支余信息")
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
        self.batchUpdateSplc("外管局账户收支余审批")
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.bsglMainFrame()
        self.closeBatchAlertSplc()
        # 14、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 15、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        # 16、切换到品种管理frame
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        bsnr_no = "REP00029"
        bsqj_no = "20220630"
        bsqj_date = "2022年06月30日"
        report_no = bsnr_no + "-" + bsqj_no
        response = self.queryBsrw(bsqj_date, "账户收支余信息")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("rsafe任务自动化废弃")
        # 17、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 18、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type="day")
        self.addBsrwSave()
        # 19、点击主菜单--报送处理，进入外管局核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeHdPage()
        # 20、输入报送期间，报送任务编号查询
        self.choiceHdReportDateForMx(bsqj_date)
        self.inputHdReportNoForMx(report_no)
        self.refreshHdDataForMx()
        # 21、选择报送任务，点击提交
        self.QuiteFrame()
        self.SwitchFrame(self.RSAFE_HD_MAIN_FRAME)
        self.tickAllBoxAllPageForMx()
        self.submitHdForMx()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForMx()
        # 22、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeSpPage()
        self.entringHandleForMx(biz_flow_name="外管局账户收支余审批")
        # 23、搜索对应的报送任务，全选，审批通过
        self.choiceSpReportDateForMx(bsqj_date)
        self.inputSpReportNoForMx(report_no)
        self.refreshSpDataForMx()
        self.tickAllBoxAllPageForMx()
        self.inputAuditResonSpDataForMx("自动化rsafe审批通过")
        self.agreeSpDataForMx()
        self.GotoSleep(2)
        res2 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("审批成功", res2)
        self.clickAlertConfirmButtonForMx()
        # 24、进入上报页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeSbPage()
        # 25、搜索对应报送任务，全选，打包下载，
        start_date = '2022-06-30'
        end_date = '2022-06-30'
        self.inputSbSjrqForMx(start_date, end_date)
        self.inputSbReportNoForMx(report_no)
        self.refreshSbDataForMx()
        self.tickAllBoxAllPageForMx()
        self.downLoadSbDataForMx1()
        # self.refreshSbDataForMx()
        # 26.批量上传（先配置FTP！！！）
        self.Click(self.BUTTON_PUB_SB_PLSC_WGJ)
        # 27、进入查询页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeCxPage()
        # 28、搜索对应报送任务，批量导出
        start_date = '2022-06-30'
        end_date = '2022-06-30'
        self.inputCxSjrqForMx(start_date, end_date)
        # # self.choiceCxReportStatusMX("待反馈")
        self.refreshCxDataForMx()
        self.inputCxReportNoForMx(report_no)
        self.refreshCxDataForMx()
        self.tickAllBoxAllPageForMx()
        self.downLoadCxDataForMx()
        time.sleep(1.5)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_rsafe_audit_refused(self):
        """外管局--审批驳回后，核对页面可正常查看报送任务，且驳回意见正确"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入征信管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 编辑管理员分组，把登录用户添加为管理员
        self.addUserForAdminGroup()
        # 进入报送任务页面，添加报送任务
        self.SwitchFatherFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        bsnr_no = "REP00029"
        bsqj_no = "20220630"
        bsqj_date = "2022年06月30日"
        report_no = bsnr_no + "-" + bsqj_no
        response = self.queryBsrw(bsqj_date, "账户收支余信息")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("rsafe任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 7、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type='day')
        self.addBsrwSave()
        # 8、点击主菜单--报送处理，进入外管局核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeHdPage()
        # 9、输入报送期间，报送任务编号查询
        self.choiceHdReportDateForMx(bsqj_date)
        self.inputHdReportNoForMx(report_no)
        self.refreshHdDataForMx()
        # 10、选择报送任务，点击提交
        self.QuiteFrame()
        self.SwitchFrame(self.RSAFE_HD_MAIN_FRAME)
        self.tickAllBoxAllPageForMx()
        self.submitHdForMx()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForMx()
        # 11、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeSpPage()
        self.entringHandleForMx(biz_flow_name="外管局账户收支余审批")
        # 12、搜索对应的报送任务，全选，审批驳回
        self.choiceSpReportDateForMx(bsqj_date)
        self.inputSpReportNoForMx(report_no)
        self.refreshSpDataForMx()
        self.tickAllBoxAllPageForMx()
        self.inputAuditResonSpDataForMx("自动化rsafe审批驳回")
        self.rejectSpDataForMx()
        res2 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("审批成功", res2)
        self.clickAlertConfirmButtonForMx()
        # 13、点击主菜单--报送处理，进入rsafe核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeHdPage()
        # 14、输入报送期间，报送任务编号查询
        self.choiceHdReportDateForMx(bsqj_date)
        self.inputHdReportNoForMx(report_no)
        self.refreshHdDataForMx()
        # 断言驳回成功，且驳回意见与审批一致
        res3 = self.GetElementAttrbute(self.DATA_PUB_REFUSE_RESON_MX, "value")
        self.assertEqual("自动化rsafe审批驳回", res3)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_rsafe_go_back_task(self):
        """外管局--上报页面退回上报数据，用户在核对页面可正常查看退回的任务，且退回意见正确"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局品种进入征信管理界面
        self.intoRsafeTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 编辑管理员分组，把登录用户添加为管理员
        self.addUserForAdminGroup()
        # 进入报送任务页面，添加报送任务
        self.SwitchFatherFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        bsnr_no = "REP00029"
        bsqj_no = "20220630"
        bsqj_date = "2022年06月30日"
        report_no = bsnr_no + "-" + bsqj_no
        response = self.queryBsrw(bsqj_date, "账户收支余信息")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("rsafe任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 7、选择外管局品种进入外管局管理界面
        self.intoRsafeTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type='day')
        self.addBsrwSave()
        # 8、点击主菜单--报送处理，进入rsafe核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeHdPage()
        # 9、输入报送期间，报送任务编号查询
        self.choiceHdReportDateForMx(bsqj_date)
        self.inputHdReportNoForMx(report_no)
        self.refreshHdDataForMx()
        # 10、选择报送任务，点击提交
        self.QuiteFrame()
        self.SwitchFrame(self.RSAFE_HD_MAIN_FRAME)
        self.tickAllBoxAllPageForMx()
        self.submitHdForMx()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("提交成功", res1)
        self.clickAlertConfirmButtonForMx()
        # 11、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeSpPage()
        self.entringHandleForMx(biz_flow_name="外管局账户收支余审批")
        # 12、搜索对应的报送任务，全选，审批通过
        self.choiceSpReportDateForMx(bsqj_date)
        self.inputSpReportNoForMx(report_no)
        self.refreshSpDataForMx()
        self.tickAllBoxAllPageForMx()
        self.inputAuditResonSpDataForMx("自动化rsafe审批通过")
        self.agreeSpDataForMx()
        res2 = self.GetTagText(self.MSG_PUB_MX)
        self.assertIn("审批成功", res2)
        time.sleep(3)
        self.clickAlertConfirmButtonForMx()
        # 13、进入上报页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeSbPage()
        # 14、搜索对应报送任务
        start_date = '2022-06-30'
        end_date = '2022-06-30'
        self.inputSbSjrqForMx(start_date, end_date)
        self.inputSbReportNoForMx(report_no)
        self.refreshSbDataForMx()
        # 进入报送任务详情页面
        self.intoReportInformationSbForMx()
        self.changeToModulePageFrame()
        # 退回全部分组子任务
        self.goBackAllGroupSbForMx("Rsafe自动化上报页面退回")
        # 15、点击主菜单--报送处理，进入外管局核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRsafeHdPage()
        # 16、输入报送期间，报送任务编号查询
        self.choiceHdReportDateForMx(bsqj_date)
        self.inputHdReportNoForMx(report_no)
        self.refreshHdDataForMx()
        # 断言驳回成功，且驳回意见与审批一致
        res3 = self.GetElementAttrbute(self.DATA_PUB_REFUSE_RESON_MX, "value")
        self.assertEqual("Rsafe自动化上报页面退回", res3)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))