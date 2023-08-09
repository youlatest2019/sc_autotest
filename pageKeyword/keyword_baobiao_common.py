#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/25 11:28
# @Author   : yangshukun
# @File     : keyword_baobiao_common.py
import time

from pageElement.page_bscl_common import *
from baseOperation.WebOperation import *


class PubKeywordForBb(WebDriver, PubBbBspzElement):

    def inputSjrqForBbDEJK(self, start_date, end_date):
        """大额监控--通填报日期日期输入框（包括核对）--核对"""
        self.Click(self.INPUT_PUB_START_DATE_DEJK)
        self.ClearData(self.INPUT_PUB_START_DATE_DEJK)
        self.Input(start_date, self.INPUT_PUB_START_DATE_DEJK)
        self.Click(self.INPUT_PUB_END_DATE_DEJK)
        self.ClearData(self.INPUT_PUB_END_DATE_DEJK)
        self.Input(end_date, self.INPUT_PUB_END_DATE_DEJK)

    def inputSjrqForBbDEJKSB(self, start_date, end_date):
        """大额监控--通填报日期日期输入框（包括核对）--上报"""
        self.Click(self.INPUT_PUB_START_DATE_DEJK_SB)
        self.ClearData(self.INPUT_PUB_START_DATE_DEJK_SB)
        self.Input(start_date, self.INPUT_PUB_START_DATE_DEJK_SB)
        self.Click(self.INPUT_PUB_END_DATE_DEJK_SB)
        self.ClearData(self.INPUT_PUB_END_DATE_DEJK_SB)
        self.Input(end_date, self.INPUT_PUB_END_DATE_DEJK_SB)

    def clickRefreshButtonForBb(self):
        """报表类品种--通用刷新按钮（包括核对、审批、上报、查询）"""
        self.Click(self.BUTTON_PUB_REFRESH_BB)

    def choiceGroupForBb(self, group_name):
        """报表类品种--通用报表分组下拉选择（包括核对、审批、上报、查询）"""
        self.Click(self.SELECT_PUB_GROUP_BB.format(group_name))

    def inputReportNameForBb(self, rp_name):
        """报表类品种--通用任务名称输入（包括核对、审批、上报、查询）"""
        self.Input(rp_name, self.INPUT_PUB_REPORT_NAME_BB)

    def inputReportNoForBb(self, rp_no):
        """报表类品种--通用报表编号输入（包括核对、审批、上报、查询）"""
        self.Input(rp_no, self.INPUT_PUB_REPORT_NO_BB)

    def choiceReportDateForBb(self, rp_date):
        """报表类品种--通用报送期间选择（包括核对、审批、上报、查询）"""
        self.Click(self.SELECT_PUB_REPORT_DATA_BB.format(rp_date))

    def openForBb(self):
        """报表类品种--通用打开功能（包括核对、审批、上报、查询）"""
        self.Click(self.BUTTON_PUB_OPEN_BB)

    def exportBatchForBb(self):
        """报表类品种--通用批量导出（包括核对、审批、上报、查询）"""
        self.Click(self.BUTTON_PUB_EXPORT_BATCH_BB)

    def submitForBb(self):
        """报表类品种--通用提交按钮（包括核对、审批、上报、查询）"""
        self.Click(self.BUTTON_PUB_SUBMIT_BB)

    def submitForDEJK(self):
        """报表类品种--通用提交按钮大额监控（包括核对、审批、上报、查询）"""
        self.Click(self.BUTTON_PUB_SUBMIT_DEJK)

    def entringHandleForBb(self, biz_flow_name):
        """报表类品种--通用审批页面进入办理（包括核对、审批）"""
        self.Click(self.BUTTON_PUB_ENTERING_HANDLE_BB.format(biz_flow_name))

    def tickAllBoxForBb(self):
        """报表类品种--通用任务列表全选复选框（包括核对、审批，上报，不含查询）"""
        self.Click(self.BOX_PUB_CHOOSE_ALL)

    def tickAllBoxForBbDEJK(self):
        """报表类品种--通用任务列表全选复选框（包括核对、审批，上报，不含查询）-核对"""
        self.Click(self.BOX_PUB_CHOOSE_ALL_DEJK)

    def tickAllBoxForBbDEJKSP(self):
        """报表类品种--通用任务列表全选复选框（包括核对、审批，上报，不含查询）-审批"""
        self.Click(self.BOX_PUB_CHOOSE_ALL_DEJK_SP)

    def tickAllBoxCxPageForBb(self):
        """报表类品种--通用任务列表全选复选框（包括核对、审批，上报，不含查询）"""
        self.Click(self.BOX_PUB_CHOOSE_ALL_CX_BB)

    def inputAuditReasonForBb(self, audit_reson):
        """报表类品种--通用审批页面输入审批意见（审批）"""
        self.Click(self.INPUT_PUB_AUDIT_RESON_BB)
        self.Input(audit_reson, self.INPUT_PUB_AUDIT_RESON_BB)

    def inputAuditReasonForDEJK(self, audit_reson):
        """报表类品种--通用审批页面输入审批意见（审批）--大额监控"""
        self.Click(self.INPUT_PUB_AUDIT_RESON_DEJK)
        self.Input(audit_reson, self.INPUT_PUB_AUDIT_RESON_DEJK)

    def clickAuditAgreeForBb(self):
        """报表类品种--通用审批页面-同意按钮（审批）"""
        self.Click(self.BUTTON_PUB_AGREE_BB)

    def clickAuditAgreeForDEJK(self):
        """报表类品种--通用审批页面-同意按钮（审批）"""
        self.Click(self.BUTTON_PUB_SP_AUDIT_AGREE_DEJK)

    def clickAuditRefuseForBb(self):
        """报表类品种--通用审批页面-驳回按钮（审批）"""
        self.Click(self.BUTTON_PUB_REFUSE_BB)

    def clickAlertConfirmButtonForBb(self):
        """报表类品种--通用弹窗确认按钮（提交、审批同意、驳回）"""
        self.Click(self.ALERT_PUB_BB)

    def clickDownloadButtonForBb(self):
        """报表类品种--通用打包下载按钮（上报）"""
        self.Click(self.BUTTON_PUB_DBXZ_BB)

    def clickQrcgButtonForBb(self):
        """报表类品种--通用确认成功按钮（上报）"""
        self.Click(self.BUTTON_PUB_QRCG_BB)

    def clickBbxqButtonForBb(self):
        """报表类品种--通用报表详情按钮（所有页面通用）"""
        self.Click(self.BUTTON_PUB_BBXQ_BB)

    def clickBsjdButtonForBb(self):
        """报表类品种--通用报送进度按钮（所有页面通用）"""
        self.Click(self.BUTTON_PUB_BSJD_BB)

    def clickGoBackButtonForBb(self):
        """报表类品种--通用报表详情--退回按钮（所有页面通用）"""
        self.Click(self.BUTTON_LJJY)
        time.sleep(3)
        self.Click(self.BUTTON_PUB_GOBACK_BB)

    def changeToGoBackFrameForBb(self):
        """报表类品种--通用报表详情--切换到退回窗口frame（所有页面通用）"""
        self.SwitchFrameByElement(self.FRAME_PUB_GOBACK_BB)

    def tickAllGoBackAlertForBb(self):
        """报表类品种--通用报表详情--退回窗口--复选框全选（所有页面通用）"""
        self.Click(self.BOX_PUB_GOBACK_ALL_BB)

    def clickGoBackButtonAlertForBb(self):
        """报表类品种--通用报表详情--退回窗口--批量退回按钮（所有页面通用）"""
        self.Click(self.BUTTON_PUB_GOBACK_ALERT_BB)

    def changeToGoBackAlertReasonFrameForBb(self):
        """报表类品种--通用报表详情--退回窗口--批量退回按钮--切换到退回原因frame（所有页面通用）"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.FRAME_PUB_GOBACK_RESON_ALERT_BB)

    def inputGoBackReasonForBb(self, back_reason):
        """报表类品种--通用报表详情--退回窗口--输入退回原因（所有页面通用）"""
        self.Click(self.INPUT_PUB_GOBACK_RESON_BB)
        self.Input(back_reason, self.INPUT_PUB_GOBACK_RESON_BB)

    def clickGoBackReasonConfirmButtonForBb(self):
        """报表类品种--通用报表详情--退回窗口--输入退回原因--确认按钮（所有页面通用）"""
        self.Click(self.BUTTON_PUB_GOBACK_ALERT_CONFIRM_BB)

    def clickGoBackReasonCancelButtonForBb(self):
        """报表类品种--通用报表详情--退回窗口--输入退回原因--取消按钮（所有页面通用）"""
        self.Click(self.BUTTON_PUB_GOBACK_ALERT_CANCEL_BB)

    def goBackSuccForBb(self, back_reason):
        """报表类--完整的退回成功组合关键字"""
        self.SwitchFrameByElement(self.FRAME_PUB_GOBACK_BB)
        self.Click(self.BOX_PUB_GOBACK_ALL_BB)
        self.Click(self.BUTTON_PUB_GOBACK_ALERT_BB)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.FRAME_PUB_GOBACK_RESON_ALERT_BB)
        self.Click(self.INPUT_PUB_GOBACK_RESON_BB)
        self.Input(back_reason, self.INPUT_PUB_GOBACK_RESON_BB)
        self.Click(self.BUTTON_PUB_GOBACK_ALERT_CONFIRM_BB)

    def clickXxhzbdbCompare(self):
        """报表类--线下汇总表对比-对比按钮"""
        self.Click(self.BUTTON_COMPARE)

    def closeCompareTs(self):
        """线下汇总表对比页面-对比按钮--点击确定关闭提示页面"""
        self.Click(self.BUTTON_COMPARE_TS_SURE)

    def importData(self, file_dir):
        """线下汇总表对比页面--导入数据"""
        self.Click(self.BUTTON_IMPORT)
        self.GotoSleep(1)
        self.UploadFile(file_dir)

    def cleanData(self):
        """线下汇总表对比页面--清空按钮"""
        self.Click(self.BUTTON_CLEAN)

    def clickSure(self):
        """线下汇总表对比页面--清空按钮提示页面--点击是"""
        self.Click(self.BUTTON_TS_SURE)

    def clickNo(self):
        """线下汇总表对比页面--清空按钮提示页面--点击否"""
        self.Click(self.BUTTON_TS_NO)

    def deleteData(self):
        """线下汇总表对比页面--删除按钮"""
        self.Click(self.BUTTON_DELETE)

    def clickBsnrmc(self):
        """点击报送内容名称下拉列表"""
        self.Click(self.BUTTON_SELECT_BSNRMC)

    def choiceBsnrmc(self, bbbh):
        """选择报送内容名称(传报送内容编号)"""
        self.Click(self.SELECT_BSNRMC.format(bbbh))

    def intoDbFrame(self):
        """进入页面frame"""
        self.SwitchFrameByElement(self.IMPORT_FRAME)

    def choiceDbxsws(self, dbxsws):
        """选择对比小数位数"""
        self.Click(self.BUTTON_SELECT_DBLWXS)
        self.Click(self.SELECT_DBLWXS.format(dbxsws))

    def inputDbData(self, data):
        """输入对比日期"""
        self.Input(data, self.INPUT_DBDATA)
        self.Click(self.INPUT_DBDATA)

    def choiceQzfs(self, qzfs):
        """选择取值方式"""
        self.Click(self.BUTTON_SELECT_QZFS)
        self.Click(self.SELECT_QZFS.format(qzfs))

    def refreshDbPage(self):
        """刷新对比页面"""
        self.Click(self.BUTTON_DB_REFRESH)

    def downloadDb(self):
        """对比页面-点击导出"""
        self.Click(self.BUTTON_DB_DOWNLOAD)

    def closeDbPage(self):
        """关闭对比页面"""
        self.Click(self.CLOSE_DB_PAGE)

    def inputSbSjrqForBb(self, SB_MAIN_FRAME):
        """报表类品种--上报页面--通用数据日期输入框"""
        self.Click(self.INPUT_PUB_SB_START_DATE_BB)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJ_DATE_FRAME)
        self.Click(self.CLEAR_SJ_DATE)
        self.QuiteFrame()
        self.SwitchFrame(SB_MAIN_FRAME)
        self.Click(self.INPUT_PUB_SB_END_DATE_BB)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJ_DATE_FRAME)
        self.Click(self.CLEAR_SJ_DATE)
        self.QuiteFrame()
        self.SwitchFrame(SB_MAIN_FRAME)

    def inputCxSjrqForBb(self, CX_MAIN_FRAME):
        """报表类品种--查询页面--通用数据日期输入框"""
        self.Click(self.INPUT_PUB_SB_START_DATE_BB)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJ_DATE_FRAME)
        self.Click(self.CLEAR_SJ_DATE)
        self.QuiteFrame()
        self.SwitchFrame(CX_MAIN_FRAME)
        self.Click(self.INPUT_PUB_SB_END_DATE_BB)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJ_DATE_FRAME)
        self.Click(self.CLEAR_SJ_DATE)
        self.QuiteFrame()
        self.SwitchFrame(CX_MAIN_FRAME)
