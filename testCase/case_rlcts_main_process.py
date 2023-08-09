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


class RlctsMainProcessTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubFzglKeyword, BsglPubBssqKeyword,
                           BsglPubSplcKeyword,
                           BsglPubBsrwKeyword, BsglMainKeyword, BsglPubBbmbKeyword, BsglPubBsfwKeyword,
                           BsglPubSjsqKeyword, OperationXml,
                           BsglPubBssqDeFxqKeyword, BsglPubSplcDeFxqKeyword, PubMxBspzElement, PubBbBspzElement):

    def test_01_rlcts_main_process(self):
        """大额监控--建立分组->授权->导入模板->新增报送任务->核对提交->审批通过->上报下载，确认上报->查询，主流程案例"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送授权管理页签
        self.swithToBssq()
        # 6、选择人员授权保存并断言成功
        self.bsglMainFrame()
        self.changeBssqRlctsfxqRymc("征信权限1")
        self.changeBssqRlctsfxqRefresh()
        flag = self.GetTagText(self.TXT_BSSQ_FLAG_DEFXQ)
        if flag != "已授权":
            self.changeBssqRlctsfxqSq()
            self.changeBssqRlctsfxqFrame()
            self.changeBssqRlctsfxqFxk()
            self.changeBssqRlctsfxqSave()
            self.Click(self.ALERT_QRCG1)
            self.SwitchFatherFrame()
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 7、进入审批流程管理页签
        self.changeSplcRlctsfxqYh("征信权限1")
        self.changeSplcRlctsfxqRefresh()
        self.changeSplcRlctsfxqFxk()
        self.changeSplcRlctsfxqPlxg()
        self.QuiteFrame()
        self.changeSplcRlctsfxqframe()
        self.changeSplcRlctsfxqChoiceSplc("大额监控审批")
        self.changeSplcRlctsfxqSave()
        # 8、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 9、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        # 10、切换到品种管理frame
        self.switchBspzFrame()
        # self.swithToBsrw()
        time.sleep(2)
        self.switchBspzFrame()
        self.queryBsrw("2022年08月14日", "大额监控")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("大额监控任务自动化废弃")
        # 11、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 12、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        self.switchBspzFrame()
        # self.swithToBsrw()
        time.sleep(2)
        self.switchBspzFrame()
        self.addBsrw("LCTS01", "20220814", type="day", qssd_index=3)
        self.addBsrwSave()
        # 13、点击主菜单--报送处理，进入大额监控核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsHdPage()
        # 14、输入填报日期查询
        self.inputSjrqForBbDEJK("20220814", "20991231")
        self.clickRefreshButtonForBb()
        # 15、选择报送任务，点击提交
        self.tickAllBoxForBbDEJK()
        self.submitForDEJK()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_BB)
        self.assertIn("提交成功", res1)
        # 16、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsSpPage()
        self.entringHandleForBb(biz_flow_name="大额监控审批")
        # 17、搜索对应的报送任务，全选，审批通过
        self.tickAllBoxForBbDEJKSP()
        self.inputAuditReasonForDEJK("自动化大额监控报表审批通过")
        self.clickAuditAgreeForDEJK()
        res2 = self.GetTagText(self.MSG_PUB_BB)
        self.assertIn("审批通过成功", res2)
        # 18、进入上报页面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsSbPage()
        # 19、输入填报日期查询
        self.inputSjrqForBbDEJKSB("20220814", "20991231")
        self.clickRefreshButtonForBb()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_rlcts_audit_refused(self):
        """大额监控--审批驳回后，核对页面可正常查看报送任务，且驳回意见正确"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送授权管理页签
        self.swithToBssq()
        # 6、选择人员授权保存并断言成功
        self.bsglMainFrame()
        self.changeBssqRlctsfxqRymc("征信权限1")
        self.changeBssqRlctsfxqRefresh()
        flag = self.GetTagText(self.TXT_BSSQ_FLAG_DEFXQ)
        if flag != "已授权":
            self.changeBssqRlctsfxqSq()
            self.changeBssqRlctsfxqFrame()
            self.changeBssqRlctsfxqFxk()
            self.changeBssqRlctsfxqSave()
            self.Click(self.ALERT_QRCG1)
            self.SwitchFatherFrame()
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 7、进入审批流程管理页签
        self.changeSplcRlctsfxqYh("征信权限1")
        self.changeSplcRlctsfxqRefresh()
        self.changeSplcRlctsfxqFxk()
        self.changeSplcRlctsfxqPlxg()
        self.QuiteFrame()
        self.changeSplcRlctsfxqframe()
        self.changeSplcRlctsfxqChoiceSplc("大额监控审批")
        self.changeSplcRlctsfxqSave()
        # 8、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 9、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        # 10、切换到品种管理frame
        self.switchBspzFrame()
        # self.swithToBsrw()
        time.sleep(2)
        self.switchBspzFrame()
        self.queryBsrw("2022年08月14日", "大额监控")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("大额监控任务自动化废弃")
        # 11、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 12、选择大额监控品种进入大额监控管理界面
        self.intoRlctsTab()
        self.switchBspzFrame()
        # self.swithToBsrw()
        time.sleep(2)
        self.switchBspzFrame()
        self.addBsrw("LCTS01", "20220814", type="day", qssd_index=3)
        self.addBsrwSave()
        # 13、点击主菜单--报送处理，进入大额监控核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsHdPage()
        # 14、输入填报日期查询
        self.inputSjrqForBbDEJK("20220814", "20991231")
        self.clickRefreshButtonForBb()
        # 15、选择报送任务，点击提交
        self.tickAllBoxForBbDEJK()
        self.submitForDEJK()
        self.GotoSleep(1)
        res1 = self.GetTagText(self.MSG_PUB_BB)
        self.assertIn("提交成功", res1)
        # 16、进入审批界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsSpPage()
        self.entringHandleForBb(biz_flow_name="大额监控审批")
        # 17、搜索对应的报送任务，全选，审批驳回
        self.tickAllBoxForBbDEJKSP()
        self.inputAuditReasonForDEJK("自动化大额监控报表审批驳回")
        self.clickAuditRefuseForBb()
        res2 = self.GetTagText(self.MSG_PUB_BB)
        self.assertIn("审批驳回成功", res2)
        # 18、点击主菜单--报送处理，进入rlcts核对界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.intoRlctsHdPage()
        # 19、输入填报日期查询
        self.inputSjrqForBbDEJK("20220814", "20991231")
        self.clickRefreshButtonForBb()
        # 断言驳回成功，且驳回意见与审批一致
        res3 = self.GetElementAttrbute(self.DATA_DEJK_RESON_MX, 'value')
        self.assertNotEqual("总计0条", res3)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
