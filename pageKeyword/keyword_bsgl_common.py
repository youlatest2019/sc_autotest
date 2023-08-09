#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 10:01
# @Author   : yangshukun
# @File     : keyword_bsgl_common.py
from pageElement.page_bsgl import *
from baseOperation.WebOperation import *
from Common.getconf import *


class BsglMainKeyword(BsglElementMain, BsglElementFrame, WebDriver):

    def intoBsglMainMenu(self):
        """进入报送管理主界面"""
        self.RefreshPage()
        self.MouseFouce(self.XTGL)
        self.Click(self.BSGL)
        self.Click(self.BSGL_TAB)

    def switchToBsglBaseFrame(self):
        """切换主框架"""
        self.GotoSleep(0.5)
        self.QuiteFrame()
        self.SwitchFrame(self.MAIN_FRAME)
        self.SwitchFrame(self.TAB_FRAME)

    def switchBspzFrame(self):
        """切换到报送品种页签框架"""
        self.SwitchFrame(self.BSPZ_FRAME)

    def bsglMainFrame(self):
        """报送管理主框架"""
        self.SwitchFrame(self.BSGL_TAB_FRAME)

    def intoReastTab(self):
        """选EAST品种"""
        self.Click(self.SWITCH_BSPZ.format('EAST'))

    def intoRimasTab(self):
        """选利率报备品种"""
        self.Click(self.SWITCH_BSPZ.format('利率报备'))

    def intoRfbsTab(self):
        """选金数品种"""
        self.Click(self.SWITCH_BSPZ.format('金数'))

    def intoRmbtdTab(self):
        """选征信品种"""
        self.Click(self.SWITCH_BSPZ.format('征信'))

    def intoRsazjTab(self):
        """选浙江国资委品种"""
        self.Click(self.SWITCH_BSPZ.format('浙江国资委'))

    def intoRamlrsTab(self):
        """选反洗钱品种"""
        self.Click(self.SWITCH_BSPZ.format('反洗钱'))

    def intoRn1104Tab(self):
        """选1104品种"""
        self.Click(self.SWITCH_BSPZ.format('1104'))

    def intoRpbccTab(self):
        """选人行报表品种"""
        self.Click(self.SWITCH_BSPZ.format('人行报表'))

    def intoRsafeTab(self):
        """选外管局品种"""
        self.Click(self.SWITCH_BSPZ.format('外管局'))

    def intoRsaferTab(self):
        """选外管局报表品种"""
        self.Click(self.SWITCH_BSPZ.format('外管局报表'))

    def intoRptcTab(self):
        """选综合报表品种"""
        self.Click(self.SWITCH_BSPZ.format('综合报表'))

    def intoDptmTab(self):
        """选压力测试品种"""
        self.Click(self.SWITCH_BSPZ.format('压力测试'))

    def intoLqdrmTab(self):
        """选流动性风险分析测试品种"""
        self.Click(self.SWITCH_BSPZ.format('流动性风险分析'))

    def intoRlctsTab(self):
        """选大额监控品种"""
        self.Click(self.SWITCH_BSPZ.format('大额监控'))

    def intoRamlltTab(self):
        """选反洗钱大额品种"""
        self.Click(self.SWITCH_BSPZ.format('反洗钱大额'))

    def swithToBsrw(self):
        """报送任务"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送任务'))

    def swithToBsfw(self):
        """报送范围"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送范围'))

    def swithToXsjdpz(self):
        """小数精度配置"""
        self.Click(self.CHOICE_FUNC_TAB.format('小数精度配置'))

    def swithToBscs(self):
        """报送参数"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送参数'))

    def swithToBssq(self):
        """报送授权"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送授权'))

    def swithToSjsq(self):
        """数据授权"""
        self.Click(self.CHOICE_FUNC_TAB.format('数据授权'))

    def swithToSplc(self):
        """审批流程"""
        self.Click(self.CHOICE_FUNC_TAB.format('审批流程'))

    def swithToKmjzsz(self):
        """科目记账设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('科目记账设置'))

    def swithToMxkmsz(self):
        """明细科目设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('明细科目设置'))

    def swithToZdysjlx(self):
        """自定义数据类型"""
        self.Click(self.CHOICE_FUNC_TAB.format('自定义数据类型'))

    def swithTo(self):
        """编码转换"""
        self.Click(self.CHOICE_FUNC_TAB.format('编码转换'))

    def swithToKytzsz(self):
        """可疑特征设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('可疑特征设置'))

    def swithToJkzbsz(self):
        """监控指标设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('监控指标设置'))

    def swithToSbwdsz(self):
        """上报网点设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('上报网点设置'))

    def swithToKhzlwh(self):
        """客户资料维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('客户资料维护'))

    def swithToSkhmdsz(self):
        """涉恐黑名单设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('涉恐黑名单设置'))

    def swithToBbmb(self):
        """报表模板"""
        self.Click(self.CHOICE_FUNC_TAB.format('报表模板'))

    def swithToBsnrsq(self):
        """报送内容授权"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送内容授权'))

    def swithToHswh(self):
        """函数维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('函数维护'))

    def swithToSjxwh(self):
        """数据项维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('数据项维护'))

    def swithToFzgl(self):
        """分组管理"""
        self.Click(self.CHOICE_FUNC_TAB.format('分组管理'))

    def swithToBsrypz(self):
        """报送人员配置"""
        self.Click(self.CHOICE_FUNC_TAB.format('报送人员配置'))

    def swithToJybmwh(self):
        """交易编码维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('交易编码维护'))

    def swithToZhxzwh(self):
        """账户性质维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('账户性质维护'))

    def swithToTbrwh(self):
        """填报人维护"""
        self.Click(self.CHOICE_FUNC_TAB.format('填报人维护'))

    def swithToZbjjcpz(self):
        """准备金缴存配置"""
        self.Click(self.CHOICE_FUNC_TAB.format('准备金缴存配置'))

    def swithToWbzhmyhl(self):
        """外币折美元汇率设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('外币折美元汇率设置'))

    def swithToCbmbgl(self):
        """财报模板管理"""
        self.Click(self.CHOICE_FUNC_TAB.format('财报模板管理'))

    def swithToZjytsz(self):
        """资金用途设置"""
        self.Click(self.CHOICE_FUNC_TAB.format('资金用途设置'))

    def swithToLsbb(self):
        """历史报表"""
        self.Click(self.CHOICE_FUNC_TAB.format('历史报表'))


class BsglPubBsrwKeyword(BsglElementFrame, PubBsrwElement, WebDriver):
    """报送任务"""

    # 报送任务
    def addBsrw(self, bsnr_name, bsqj, qssd_index=2, type="year", bsqj_month="6月", bsqj_season="第二季度"):
        """新增报送任务,根据type判断，不同的type报送期间不一样"""
        self.Click(self.BUTTON_ADD_BSRW)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.ADD_BSRW_FRAME)
        self.Click(self.ALERT_BSNRMC)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.ADD_BSNR_FRAME)
        self.Click(self.BUTTON_BSNRMC.format(bsnr_name))
        self.QuiteFrame()
        self.SwitchFrameByElement(self.ADD_BSRW_FRAME)
        if type == "year":
            self.ClearData(self.INPUT_ADD_BSQJ_FOR_YEAR)
            self.Input(bsqj, self.INPUT_ADD_BSQJ_FOR_YEAR)
        elif type == "day":
            self.Input(bsqj, self.INPUT_ADD_BSQJ_FOR_DAY)
            self.Click(self.TITLE_ADD_BSRW)
        elif type == 'month':
            self.ClearData(self.INPUT_ADD_BSQJ_FOR_YEAR)
            self.Input(bsqj, self.INPUT_ADD_BSQJ_FOR_YEAR)
            self.Click(self.INPUT_ADD_BSQJ_FOR_MONTH.format(bsqj_month))
        elif type == 'season':
            self.ClearData(self.INPUT_ADD_BSQJ_FOR_YEAR)
            self.Input(bsqj, self.INPUT_ADD_BSQJ_FOR_YEAR)
            self.Click(self.INPUT_ADD_BSQJ_FOR_SEASON.format(bsqj_season))
        self.Click(self.INPUT_RWLX_TQSC)  # 可修改为其他任务类型
        self.Click(self.INPUT_QSSD.format(qssd_index))  # 可修改为其他取数时点,1-指定时间取数，2-立即取数，3-不取数

    def BbpzChoiceMould(self, mb_index=2):
        """报表类品种新增任务选择报表模板，默认选择第一个模板"""
        self.Click(self.INPUT_BBMB_FOR_1104.format(mb_index))

    def addBsrwSave(self):
        """新增报送任务保存按钮"""
        self.Click(self.BUTTON_SAVE_BSRW)

    def closeXzrw_success(self):
        """关闭新增任务成功弹窗"""
        self.Click(self.ALERT_ADD)

    def queryBsrw(self, bsqj, text):
        """查询报送任务"""
        options_list = self.get_select_values(self.SELECT_BSQJ_BSRW)
        if bsqj in options_list:
            self.Click(self.INPUT_BSQJ.format(bsqj))
            self.Input(text, self.INPUT_RWMC)
            self.Click(self.BUTTON_SEARCH)
            mylog.info(options_list)
            return True
        else:
            mylog.info("当前所选的报送期间" + bsqj + "不存在")
            return False

    def createEastJzcj(self):
        """EAST创建集中采集任务"""
        self.Click(self.BUTTON_JZCJ)
        self.QuiteFrame()
        self.SwitchFrame(self.JZCJ_FRAME)
        self.Click(self.BUTTON_SCBSRW)

    def abandonBsrw(self, text):
        """废弃报送任务"""
        self.Click(self.BUTTON_RWFQ)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.RWFQ_FRAME)
        self.Input(text, self.INPUT_RWFQ)
        self.Click(self.ALERT_RWFQ)

    def inputTbjsrq(self):
        """填报结束日期"""
        self.Click(self.BUTTON_TBJSRQ)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.RWFQ_FRAME)
        self.Click(self.BUTTON_TBJSRQ_BC)
        self.Click(self.ALERT_QRCG1)
        self.QuiteFrame()
        self.Click(self.ALERT_QRCG2)


class BsglPubBsfwKeyword(BsglElementFrame, PubBsfwElement, WebDriver):
    """报送范围"""

    def queryBsnr(self, bspl, text):
        """报送范围查询报送内容"""
        self.Click(self.INPUT_BSPL.format(bspl))
        self.Input(text, self.INPUT_BSNR)
        self.Click(self.BUTTON_SEARCH1)

    def whetherBsnr(self):
        """是否报送报送内容"""
        self.Click(self.BUTTON_SFBS)

    def checkAllBsnr(self):
        """复选框全选报送内容"""
        self.Click(self.CHECK_ALL)

    def checkOneBsnr(self):
        """复选框单选报送内容"""
        self.Click(self.CHECK_ONE)

    def changeBsnr(self, qsqj, text, text1, bsjzqx_type, sfhjjr, zdhd):
        """修改报送内容设置"""
        self.Click(self.BUTTON_MODIFY)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.BSFW_CHANGE_FRAME)
        self.Click(self.INPUT_QSQJ.format(qsqj))
        self.ClearData(self.INPUT_QSSD_BSFW)
        self.KeyBordDel(self.INPUT_QSSD_BSFW)
        self.Input(text, self.INPUT_QSSD_BSFW)
        self.ClearData(self.INPUT_BSJZQX)
        self.Input(text1, self.INPUT_BSJZQX)
        self.Click(self.INPUT_BSJZQX_TYPE.format(bsjzqx_type))
        self.Click(self.INPUT_SFHJJR.format(sfhjjr))
        self.Click(self.INPUT_ZDHD.format(zdhd))
        self.Click(self.BUTTON_CHANGE_SAVE)
        self.QuiteFrame()
        self.Click(self.ALERT_MODIFY)

    def clickOkAlert(self):
        """设置成功确认按钮"""
        self.Click(self.BUTTON_OK_ALERT)


class BsglPubFzglKeyword(BsglElementFrame, PubFzglElement, WebDriver):
    """分组管理--公共页面"""

    def searchGroupName(self, group_name):
        # 输入分组名称
        self.Input(group_name, self.INPUT_GROUP_NAME)

    def searchUser(self, user_name):
        # 输入成员姓名
        self.Input(user_name, self.INPUT_GROUP_USER)

    def refreshGroupPage(self):
        # 刷新按钮
        self.Click(self.BUTTON_GROUP_REFRESH)

    def addGroup(self, add_group_name, user, add_group_ms):
        # 新增分组,保存，并关闭弹窗
        conf = Config()
        login_user = conf.get("BaseUrl", "user_name")
        self.Click(self.BUTTON_GROUP_ADD)
        self.Input(add_group_name, self.INPUT_ADD_FZMC)
        self.Click(self.BUTTON_CLICK_CYLB)
        self.Input(login_user, self.INPUT_ADD_CYLB)
        self.Click(self.BOX_CYLB)
        self.Input(add_group_ms, self.INPUT_ADD_FZMS)
        self.Click(self.BUTTON_GROUP_SAVE)

    def addUserForAdminGroup(self):
        # 管理员分组中新增用户，判断该用户是否已经在管理员分组中，如果存在则直接保存，不存在则添加后保存
        conf = Config()
        login_user = conf.get("BaseUrl", "user_name")
        all_user = self.GetTagText(self.DATA_GROUP_USER_LIST)
        if login_user not in all_user:
            self.Click(self.BUTTON_GROUP_EDITE_OR_DEL.format("管理员", 1))
            self.Click(self.BUTTON_CLICK_CYLB)
            self.Input(login_user, self.INPUT_ADD_CYLB)
            self.Click(self.BOX_CYLB)
            self.Click(self.BUTTON_GROUP_SAVE)
            self.Click(self.ALERT_GROUP_SAVE_CLOSE)

    def closeGroupSaveAlert(self):
        self.Click(self.ALERT_GROUP_SAVE_CLOSE)

    def editeGroup(self, group_name, new_name, new_ms):
        # 编辑分组
        self.Click(self.BUTTON_GROUP_EDITE_OR_DEL.format(group_name, 1))  # group_name定位某一行数据，1代表编辑，2代表删除
        self.ClearData(self.INPUT_EDITE_GROUP_BY_NAME.format(group_name))
        self.Input(new_name, self.INPUT_EDITE_GROUP_BY_NAME.format(group_name))
        self.ClearData(self.INPUT_EDITE_GROUP_BY_MS.format(group_name))
        self.Input(new_ms, self.INPUT_EDITE_GROUP_BY_MS.format(group_name))
        self.Click(self.BUTTON_GROUP_SAVE)

    def delGroup(self, group_name):
        # 删除分组
        self.Click(self.BUTTON_GROUP_EDITE_OR_DEL.format(group_name, 2))  # group_name定位某一行数据，1代表编辑，2代表删除
        self.Click(self.BUTTON_GROUP_DEL_CONFIRM)


class BsglPubBssqKeyword(BsglElementFrame, PubBssqElement, WebDriver):
    """报送授权"""

    def searchGroupNameBssq(self, group_name):
        """选择分组"""
        self.Click(self.CLICK_GROUP_NAME_BSSQ)
        self.Input(group_name, self.INPUT_GROUP_NAME_BSSQ)
        self.Click(self.CLICK_GROUP_NAME_ONE_BSSQ)

    def searchBsnr(self, bsnr):
        """报送内容输入框"""
        self.Input(bsnr, self.INPUT_BSNR_BSSQ)

    def refreshBssqPage(self):
        """报送内容页面刷新按钮"""
        self.Click(self.BUTTON_REFRESH_BSSQ)

    def tickHdqx(self):
        """报送授权勾选核对权限"""
        self.Click(self.BUTTON_HDQX)

    def tickSbqx(self):
        """报送授权勾选上报权限"""
        self.Click(self.BUTTON_SBQX)

    def tickCxqx(self):
        """报送授权勾选查询权限"""
        self.Click(self.BUTTON_CXQX)

    def tickCcqx(self):
        """报送授权勾选重抽权限"""
        self.Click(self.BUTTON_CCQX)

    def saveBssq(self):
        """报送授权保存授权"""
        self.Click(self.BUTTON_SAVE_BSSQ)


class BsglPubSjsqKeyword(BsglElementFrame, PubSjsqElement, PubBssqElement, WebDriver):
    """数据授权"""

    def bssqMainFrame(self):
        """数据授权frame"""
        self.SwitchFrameByElement(self.SJSQ_FRAME)

    def searchGroupNameSjsq(self, group_name):
        """选择分组"""
        self.Click(self.CLICK_GROUP_NAME_BSSQ)
        self.Input(group_name, self.INPUT_GROUP_NAME_BSSQ)
        self.Click(self.CLICK_GROUP_NAME_ONE_BSSQ)

    def searchBsnrSjsq(self, bsnr):
        """报送内容输入框"""
        self.Input(bsnr, self.INPUT_BSNR_SJSQ)

    def refreshSjsqPage(self):
        """数据授权页面刷新按钮"""
        self.Click(self.BUTTON_REFRESH_SJSQ)

    def clearDataBssqPage(self):
        """数据授权页面清除条件按钮"""
        self.Click(self.BUTTON_CLEAR)

    def clickAllBssqPage(self):
        """数据授权页面全部按钮"""
        self.Click(self.BUTTON_ALL)
        self.QuiteFrame()

    def checkZdBssqPage(self):
        """数据授权页面按字段筛选按钮"""
        self.Click(self.BUTTON_AZDSX)

    def clickZdOneBssqPage(self, text):
        """数据授权页面按字段筛选-第一个下拉框"""
        self.Click(self.INPUT_AZDSX.format(text))

    def clickZdTwoBssqPage(self, text):
        """数据授权页面按字段筛选-第二个下拉框"""
        self.Click(self.CLICK_AZDSX_XLK)
        self.Click(self.INPUT_AZDSX_CLICK.format(text))

    def inputZdBssqPage(self, text):
        """数据授权页面按字段筛选-第二个输入框"""
        self.Input(text, self.INPUT_AZDSX_INPUT)

    def clickSjbsBssqPage(self):
        """数据授权页面按数据标识筛选"""
        self.Click(self.BUTTON_ASJBSSX)

    def inputSjbsBssqPage(self, text):
        """数据授权页面按数据标识筛选-输入框"""
        self.Input(text, self.INPUT_ASJBSSX)

    def saveSjsqPage(self):
        """数据授权页面保存按钮"""
        self.Click(self.BUTTON_SAVE_SJSQ)

    def alertSucBssqPage(self):
        """数据授权页面保存成功确认按钮"""
        self.Click(self.ALERT_QR_SJSQ)

    def alertBssqPage(self):
        """数据授权页面关闭数据范围弹窗"""
        self.SwitchFatherFrame()
        self.Click(self.ALERT_CLOSE_SJSQ)

    def clickAllSjsq(self):
        """选择全部权限"""
        self.Click(self.INPUT_ALL_SJSQ)


class BsglPubSplcKeyword(BsglElementFrame, PubSplcElement, WebDriver):
    """审批流程--公共页面"""

    def searchGroupNameSplc(self, group_name):
        """选择分组"""
        self.Click(self.CLICK_GROUP_NAME_SPLC)
        self.Input(group_name, self.INPUT_GROUP_NAME_SPLC)
        self.Click(self.CLICK_GROUP_NAME_ONE_SPLC)

    def refreshSplcPage(self):
        """报送内容页面刷新按钮"""
        self.Click(self.BUTTON_REFRESH_SPLC)

    def batchUpdateSplc(self, bizflow_name):
        """点击批量修改按钮"""
        self.Click(self.BUTTON_BATCH_UPDATE)
        self.QuiteFrame()
        self.SwitchFrame(self.PUB_SPLC_BATCH_UPDATE_FRAME)
        self.Click(self.INPUT_BIZCODE_SPLC.format(bizflow_name))
        self.Click(self.BUTTON_BATCH_SAVE_SPLC)

    def closeBatchAlertSplc(self):
        """关闭批量修改保存弹窗"""
        self.Click(self.BUTTON_BATCH_ALERT_CLOSE_SPLC)

    def tickBoxAll(self):
        """复选框全选"""
        self.Click(self.BOX_ALL_SPLC)


class BsglPubBbmbKeyword(BsglElementMain, BsglElementFrame, WebDriver, PubBbmbElement):
    """报表模板界面关键字"""

    def importBbmb(self, file_path):
        """导入报表模板"""
        self.Click(self.BUTTON_IMPORT_MB)
        self.QuiteFrame()
        self.SwitchFrame(self.BBMB_IMPORT_CHOICE_FRAME)
        self.Click(self.BUTTON_IMPORT_CHOICE_ITEM_CONFIRM)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.RN1104_UPLOAD_ALTER_FRAME)
        self.Click(self.BUTTON_UPLOAD)
        self.UploadFile(file_path)
        self.GotoSleep(2)
        self.Click(self.BUTTON_UPLOAD_FILE)
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.RN1104_MSG_ALTER_FRAME)

    def exportBbmb(self):
        """导出模板"""
        self.Click(self.BUTTON_EXPORT)

    def inputBsnrbh(self, text):
        """输入报送内容编号"""
        self.Input(text, self.INPUT_BSNRBH)

    def inputBsnrmc(self, text):
        """输入报送内容名称"""
        self.Input(text, self.INPUT_BSNRMC)

    def choiceGroup(self, group_name):
        """选择报送分组"""
        self.Click(self.CHOOSE_GROUP_NAME.format(group_name))

    def choiceReportFlag(self, flag_index):
        """选择是否报送"""
        self.Click(self.INPUT_REPORT_FLAG.format(flag_index))

    def clickCheckBox(self, box_index):
        """复选框单选数据"""
        self.Click(self.BOX_BBMB.format(box_index))

    def checkAllBox(self, box_index):
        """复选框全选数据"""
        self.Click(self.BOX_BBMB.format(box_index))

    def refreshBbmbPage(self):
        """点击刷新按钮"""
        self.Click(self.BUTTON_BBMB_REFRESH)

    def closeDrts(self):
        """关闭导入提示弹窗"""
        self.Click(self.CLOSE_DRTS)

    def closeMbdrtc(self):
        """关闭模板导入弹窗"""
        self.Click(self.CLOSE_MBDRTC)


class BsglPubBsnrsqKeyword(BsglElementMain, BsglElementFrame, WebDriver, PubBsnrsqElement):
    """报表类--报送内容授权界面关键字"""

    def searchGroupNameBsnrsq(self, group_name):
        """选择分组"""
        self.Click(self.CLICK_GROUP_NAME_BSNRSQ)
        self.Input(group_name, self.INPUT_GROUP_NAME_BSNRSQ)
        self.Click(self.CLICK_GROUP_NAME_ONE_BSNRSQ)

    def searchBsnrBsnrsq(self, bsnr):
        """报送内容输入框"""
        self.Input(bsnr, self.INPUT_BSNR_BSNRSQ)

    def refreshBsnrsqPage(self):
        """报送内容页面刷新按钮"""
        self.Click(self.BUTTON_REFRESH_BSNRSQ)

    def choiceBoxAllBsnrsq(self):
        """报送内容授权页面，复选框全选"""
        self.Click(self.BOX_ALL_BSNRSQ)

    def choiceBoxByNameBsnrsq(self, bsnr_name):
        """根据报送内容名称，选择单个复选框"""
        self.Click(self.BOX_ANY_BY_NAME_BSNRSQ.format(bsnr_name))

    def clickEditAllBsnrsq(self):
        """点击编辑全部按钮"""
        self.Click(self.BUTTON_EDIT_ALL_BSNRSQ)

    def clickTraceAllBsnrsq(self):
        """点击追溯全部按钮"""
        self.Click(self.BUTTON_TRACE_ALL_BSNRSQ)

    def clickCancelAllBsnrsq(self):
        """点击取消全部权限按钮"""
        self.Click(self.BUTTON_CANCEL_ALL_BSNRSQ)

    def clickRefreshBsnrsq(self):
        """报送内容授权--点击刷新按钮"""
        self.Click(self.BUTTON_REFRESH_BSNRSQ)


class ZdysjlxPubSplcKeyword(BsglElementFrame, PubZdysjlxElement, WebDriver):
    """自定义数据类型--公共页面"""

    def ZdysjlxFrame(self):
        self.SwitchFrame(self.BSGL_TAB_FRAME)

    def addSjlxButton(self):
        """数据类型-新增按钮"""
        self.Click(self.BUTTON_SJLX_ADD)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJLX_ADD_FRAME)

    def addSjlxBh(self, text):
        """数据类型-新增-编号"""
        self.Input(text, self.INPUT_SJLX_ADD_BH)

    def addSjlxName(self, text):
        """数据类型-新增-名称"""
        self.Input(text, self.INPUT_SJLX_ADD_NAME)

    def addSjlxSm(self, text):
        """数据类型-新增-说明"""
        self.Input(text, self.INPUT_SJLX_ADD_SM)

    def addSjlxSave(self):
        """数据类型-新增-保存按钮"""
        self.Click(self.BUTTON_SJLX_ADD_SAVE)

    def choiceSjlxClick(self, bh):
        """选择一条数据类型编号-点击"""
        self.Click(self.CLICK_SJLX_BH.format(bh))

    def editSjlxButton(self):
        """数据类型--编辑按钮"""
        self.Click(self.BUTTON_SJLX_EDIT)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJLX_EIDT_FRAME)

    def editSjlxName(self, text):
        """数据类型-编辑-名称"""
        self.ClearData(self.INPUT_SJLX_EDIT_NAME)
        self.Input(text, self.INPUT_SJLX_EDIT_NAME)

    def editSjlxSm(self, text):
        """数据类型-编辑-说明"""
        self.ClearData(self.INPUT_SJLX_EDIT_SM)
        self.Input(text, self.INPUT_SJLX_EDIT_SM)

    def editSjlxSave(self):
        """数据类型-编辑-保存按钮"""
        self.Click(self.BUTTON_SJLX_EDIT_SAVE)

    def delSjlxButton(self):
        """数据类型-删除按钮"""
        self.Click(self.BUTTON_SJLX_DEL)
        self.AlertAccept()

    def delSjlxSuccessClose(self):
        """数据类型-删除-删除成功--弹窗关闭"""
        self.Click(self.DEL_SJLX_SUCCESS_CLOSE)

    def delSjlxFail(self):
        """数据类型-删除失败-确定"""
        self.Click(self.DEL_SJLX_FAIL)

    def addSjlxMxButton(self):
        """数据类型明细-新增按钮"""
        self.Click(self.BUTTON_SJLXMX_ADD)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJLXMX_ADD_FRAME)

    def addSjlxMxName(self, text):
        """数据类型明细-新增-名称"""
        self.Input(text, self.INPUT_SJLXMX_ADD_NAME)

    def addSjlxMxCsz(self, text):
        """数据类型明细-新增-参数值"""
        self.Input(text, self.INPUT_SJLXMX_ADD_CSZ)

    def addSjlxMxSave(self):
        """数据类型明细-新增-保存按钮"""
        self.Click(self.BUTTON_SJLXMX_ADD_SAVE)

    def SelectSjlxMxAll(self):
        """勾选数据类型明细复选框"""
        self.Click(self.SELECT_SJLXMX_ALL)

    def SelectSjlxMxFrist(self):
        """勾选数据类型明细第一条"""
        self.Click(self.SELECT_SJLXMX_FRIST)

    def editSjlxMxButton(self):
        """数据类型明细-编辑按钮"""
        self.Click(self.BUTTON_SJLXMX_EDIT)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJLXMX_EIDT_FRAME)

    def editSjlxMxName(self, text):
        """数据类型明细-编辑-名称"""
        self.ClearData(self.INPUT_SJLXMX_EDIT_NAME)
        self.Input(text, self.INPUT_SJLXMX_EDIT_NAME)

    def editSjlxMxCsz(self, text):
        """数据类型明细-编辑-参数值"""
        self.ClearData(self.INPUT_SJLXMX_EDIT_CSZ)
        self.Input(text, self.INPUT_SJLXMX_EDIT_CSZ)

    def editSjlxMxSave(self):
        """数据类型明细-编辑-保存按钮"""
        self.Click(self.BUTTON_SJLXMX_EDIT_SAVE)

    def delSjlxMxButton(self):
        """数据类型明细-删除按钮"""
        self.Click(self.BUTTON_SJLXMX_DEL)
        self.AlertAccept()

    def delSjlxMxSuccessClose(self):
        """数据类型明细-删除-删除成功弹窗关闭"""
        self.Click(self.DEL_SJLXMX_SUCCESS_CLOSE)


class BsglPubHswhKeyword(BsglElementMain, BsglElementFrame, WebDriver, PubHswhElement):

    def searchHslbHswhMainPage(self, hslb_name):
        """函数类别搜索"""
        self.Click(self.SELECT_HSLB_HSWH.format(hslb_name))

    def searchStatusHswhMainPage(self, index):
        """函数维护--状态搜索"""
        self.Click(self.SELECT_STATUS_HSWH.format(index))

    def refreshHswhMainPage(self):
        """函数维护--刷新按钮"""
        self.Click(self.BUTTON_REFRESH_HSWH)

    def addHswhMainPage(self):
        """函数维护--新增按钮"""
        self.Click(self.BUTTON_ADD_HSWH)

    def switchToDetailFrame(self):
        """切换到函数详情frame框架"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.PUB_HSWH_DETAIL_FRAME)

    def inputHsmcHswhDetailPage(self, hsmc_name):
        """函数详情页面--函数名称输入框"""
        self.Input(hsmc_name, self.INPUT_FUNC_NAME)

    def inputHslbHswhDetailPage(self, hslb_name):
        """函数详情页面--函数类别输入框"""
        self.Click(self.SELECT_DETAIL_HSLB_HSWH.format(hslb_name))

    def inputHsmsHswhDetailPage(self, hsms):
        """函数详情页面--函数描述输入框"""
        self.Input(hsms, self.INPUT_FUNC_DESCRIBE)

    def inputResTypeHswhDetailPage(self, res_type):
        """函数详情页面--函数返回值输入框"""
        self.Click(self.SELECT_DETAIL_RESTYPE_HSWH.format(res_type))

    def inputSqlHswhDetailPage(self, sql_text):
        """函数详情页面--函数sql语句输入框"""
        self.Input(sql_text, self.INPUT_DETAIL_SQL_HSWH)

    def clickAnalParamHswhDetailPage(self):
        """函数详情页面--解析参数按钮"""
        self.Click(self.BUTTON_DETAIL_PARAM_HSWH)

    def clickTestHswhDetailPage(self):
        """函数详情页面--点击测试并且弹窗再次测试"""
        self.Click(self.BUTTON_DETAIL_CHECK_HSWH)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.PUB_HSWH_DETAIL_CHECK_FRAME)
        self.Click(self.BUTTON_DETAIL_CHECK_CHECK_HSWH)

    def closeAlertTestHswhDetailPage(self):
        """函数维护详情页面--测试页面--关闭测试弹窗提示信息按钮"""
        self.Click(self.BUTTON_CLOSE_ALERT_CHECK_CHECK_HSWH)

    def closeTestHswhDetailPage(self):
        """函数维护详情页面--测试页面--关闭按钮"""
        self.QuiteFrame()
        self.Click(self.BUTTON_CLOSE_CHECK_HSWH)

    def makeParamsInfoHswhDetailPage(self, params_name, params_type, params_value):
        """函数维护详情页面--输入参数名称、参数类型、参数值"""
        self.Input(params_name, self.INPUT_DETAIL_PARAM_NAME_HSWH)
        self.Click(self.INPUT_DETAIL_PARAM_TYPE_HSWH.format(params_type))
        self.Input(params_value, self.INPUT_DETAIL_PARAM_VALUE_HSWH)

    def clickForbidHswhDetailPage(self):
        """函数详情页面--点击禁用按钮"""
        self.Click(self.BUTTON_DETAIL_FORBID_HSWH)

    def clickSaveHswhDetailPage(self):
        """函数详情页面--点击保存按钮"""
        self.Click(self.BUTTON_DETAIL_SAVE_HSWH)

    def closeHswhAlert(self):
        """函数详情，保存弹窗关闭"""
        self.Click(self.BUTTON_DETAIL_ALERT_CLOSE_HSWH)

    def closeHswhDetailMainPage(self):
        """函数详情，关闭详情页面主窗口"""
        self.QuiteFrame()
        self.Click(self.BUTTON_DETAIL_MAIN_CLOSE_HSWH)


class BsglPubSjxwhKeyword(BsglElementMain, BsglElementFrame, WebDriver, PubSjxwhElement):

    def clickSjxwhAddButton(self):
        """数据项维护--点击新增按钮"""
        self.Click(self.BUTTON_ADD_SJXWH)

    def inputSjxwhInfo(self, sjx_name, sjx_ms, table_group, table_name):
        """数据项维护--新增--数据项名称输入"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJXWH_ADD_MAIN_FRAME)
        self.Input(sjx_name, self.INPUT_DETAIL_NAME_SJXWH)
        self.Input(sjx_ms, self.INPUT_DETAIL_DESCRIBE_SJXWH)
        self.Click(self.SELECT_DETAIL_GROUP_SJXWH.format(table_group))
        self.Click(self.SELECT_DETAIL_TABLE_SJXWH.format(table_name))

    def choiceSjxwhFuncDataAndInster(self, params_value):
        """数据项维护--新增页面--添加函数--选择第一个函数，输入参数值，并插入"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJXWH_ADD_MAIN_FRAME)
        self.Click(self.BUTTON_DETAIL_ADD_FUNC_SJXWH)
        self.SwitchFrame(self.SJXWH_DETAIL_FRAME)
        self.SwitchFrame(self.SJXWH_ADD_FUNC_FRAME)
        self.Click(self.DATA_FUNC_FORM_FIRST_SJXWH)
        self.SwitchFatherFrame()
        self.SwitchFrame(self.SJXWH_ADD_FUNC_PARAMS_FRAME)
        self.Input(params_value, self.INPUT_FUNC_FORM_PARAMS_VALUE_SJXWH)
        self.Click(self.BUTTON_INSTER_FUNC_SJXWH)

    def choiceSjxwhItemsDataAndInster(self, sjx_name):
        """数据项维护--新增页面--添加数据项--根据数据项名称选择数据项，并插入"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJXWH_ADD_MAIN_FRAME)
        self.Click(self.BUTTON_DETAIL_ADD_ITEMS_SJXWH)
        self.SwitchFrame(self.SJXWH_DETAIL_FRAME)
        self.Click(self.DATA_ITEMS_FORM_SJXWH.format(sjx_name))
        self.Click(self.BUTTON_INSTER_ITEMS_SJXWH)

    def clickSjxwhSaveButton(self):
        """数据项维护--新增页面--点击保存按钮"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.SJXWH_ADD_MAIN_FRAME)
        self.Click(self.BUTTON_FUNC_FORM_SAVE_SJXWH)


class BsglPubBssqDeFxqKeyword(PubBssqElement_rlcts_ramlrs, BsglElementFrame, WebDriver):
    """大额监控、反洗钱报送授权"""

    def changeBssqRlctsfxqSave(self):
        """大额监控、反洗钱报送授权-保存按钮"""
        self.Click(self.BUTTON_SAVE_DEFXQ)

    def changeBssqRlctsfxqRymc(self, text):
        """大额监控、反洗钱报送授权-人员名称"""
        self.Input(text, self.INPUT_RYMC_DEFXQ)

    def changeBssqRlctsfxqRefresh(self):
        """大额监控、反洗钱报送授权-刷新按钮"""
        self.Click(self.BUTTON_REFRESH_BSSQ_DEFXQ)

    def changeBssqRlctsfxqSq(self):
        """大额监控、反洗钱报送授权-授权"""
        self.Click(self.BUTTON_SQ_DEFXQ)

    def changeBssqRlctsfxqFxk(self):
        """大额监控、反洗钱报送授权-勾选复选框"""
        self.Click(self.BUTTON_BOX_DEFXQ)

    def changeBssqRlctsfxqFrame(self):
        """大额监控、反洗钱报送授权-切换frame"""
        self.SwitchFrame(self.BSSQ_QXX_FRAME)


class BsglPubSplcDeFxqKeyword(PubSplcElement_rlcts_ramlrs, BsglElementFrame, WebDriver):
    """大额监控、反洗钱审批流程"""

    def changeSplcRlctsfxqSave(self):
        """大额监控、反洗钱审批流程-保存按钮"""
        self.Click(self.BUTTON_SAVE_SPLC_DEFXQ)

    def changeSplcRlctsfxqYh(self, text):
        """大额监控、反洗钱审批流程-用户"""
        self.Click(self.INPUT_USER_SPLC.format(text))

    def changeSplcRlctsfxqRefresh(self):
        """大额监控、反洗钱审批流程-刷新按钮"""
        self.Click(self.BUTTON_REFRESH_SPLC_DEFXQ)

    def changeSplcRlctsfxqFxk(self):
        """大额监控、反洗钱审批流程-复选框"""
        self.Click(self.BUTTON_BOX_FXK_DEFXQ)

    def changeSplcRlctsfxqPlxg(self):
        """大额监控、反洗钱审批流程-批量修改"""
        self.Click(self.BUTTON_PLXG_DEFXQ)

    def changeSplcRlctsfxqChoiceSplc(self, text):
        """大额监控、反洗钱审批流程-审批流程"""
        self.Click(self.INPUT_SPLC_DEFXQ.format(text))

    def changeSplcRlctsfxqframe(self):
        """大额监控、反洗钱审批流程-审批流程"""
        self.SwitchFrame(self.SPLC_QXX_FRAME)


class XsjdpzPubSplcKeyword(BsglElementFrame, PubXsjdpzElement, WebDriver):
    """小数精度配置--公共页面"""

    def clickTyxswspz(self):
        """小数精度配置--点击通用小数位数配置"""
        self.Click(self.BUTTON_TYXSWSPZ)

    def changeTyxswspzframe(self):
        """切换通用小数位数配置页面frame"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.XSJDPZ_TYXSWSPZ_FRAME)

    def inputTyxswspzSzJs(self, text):
        """通用小数位数配置-输入数值-通用计算小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_SZ_TYJSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_SZ_TYJSXSWS)

    def inputTyxswspzSzXs(self, text):
        """通用小数位数配置-输入数值-通用显示小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_SZ_TYXSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_SZ_TYXSXSWS)

    def inputTyxswspzBfbJs(self, text):
        """通用小数位数配置-输入百分比-通用计算小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_BFB_TYJSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_BFB_TYJSXSWS)

    def inputTyxswspzBfbXs(self, text):
        """通用小数位数配置-输入百分比-通用显示小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_BFB_TYXSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_BFB_TYXSXSWS)

    def inputTyxswspzJeJs(self, text):
        """通用小数位数配置-输入金额-通用计算小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_je_TYJSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_je_TYJSXSWS)

    def inputTyxswspzJeXs(self, text):
        """通用小数位数配置-输入金额-通用显示小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_je_TYXSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_je_TYXSXSWS)

    def inputTyxswspzLlJs(self, text):
        """通用小数位数配置-输入利率-通用计算小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_ll_TYJSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_ll_TYJSXSWS)

    def inputTyxswspzLlXs(self, text):
        """通用小数位数配置-输入利率-通用显示小数位数"""
        self.ClearData(self.INPUT_TYXSWSPZ_ll_TYXSXSWS)
        self.Input(text, self.INPUT_TYXSWSPZ_ll_TYXSXSWS)

    def saveTyxswspz(self):
        """通用小数位数配置-点击保存"""
        self.Click(self.BUTTON_TYXSWSPZ_SAVE)

    def closeTyxswspzSaveSuccess(self):
        """通用小数位数配置-关闭保存成功弹窗"""
        self.Click(self.CLOSE_TYXSWSPZ_SAVE_SUCCESS)

    def closeTyxswspz(self):
        """通用小数位数配置-关闭通用小数位数配置页面"""
        self.Click(self.CLOSE_TYXSWSPZ)

    def refeshXsjdpzPage(self):
        """小数精度配置页面--刷新"""
        self.Click(self.BUTTON_XSJDPZ_REFRESH)

    def inputXsjdpzBsnrmc(self, text):
        """小数精度配置--输入报送内容名称"""
        self.ClearData(self.INPUT_XSJDPZ_BSNRMC)
        self.Input(text, self.INPUT_XSJDPZ_BSNRMC)

    def clickXsjdpzEdit(self):
        """小数精度配置--编辑按钮"""
        self.Click(self.BUTTON_XSJDPZ_EDIT)
        self.GotoSleep(2)

    def refeshXsjdplpzPage(self):
        """小数精度配置--编辑-小数精度批量配置页面-刷新"""
        self.Click(self.BUTTON_XSJDPLPZ_REFESH)
        self.GotoSleep(2)

    def alterXsjdplpz(self, text):
        """小数精度批量配置页面-修改小数位数按钮"""
        self.Click(self.BUTTON_XSJDPLPZ_ALTER.format(text))

    def okXsjdplpzAlterNull(self):
        """小数精度批量配置-未勾选单元格-点击小数位数-提示弹窗-确认按钮"""
        self.Click(self.XSJDPLPZ_ALTER_NULL_OK)

    def changeXsjdplpzDygframe(self):
        """小数精度批量配置-单元格frame"""
        self.SwitchFrame(self.XSJDPZ_EDIT_DYG_FRAME)

    def chooseXsjdplpzDyg(self, ri, ci):
        """小数精度批量配置-勾选单元格"""
        self.Click(self.CHOOSE_XSJDPLPZ_DYG.format(ri, ci))

    def changeAlterDygxswsframe(self):
        """切换修改小数位数frame"""
        self.SwitchFrameByElement(self.XSJDPZ_EDIT_ALTER_FRAME)

    def chooseXsjdplpzAlterSjlx(self, sjlx):
        """小数精度批量配置-修改小数位数-选择数据类型"""
        self.Click(self.CHOOSE_XSJDPLPZ_ALTER_SJXLX.format(sjlx))

    def inputXsjdplpzAlterJsxsws(self, text):
        """小数精度批量配置-修改小数位数-计算小数位数"""
        self.ClearData(self.INPUT_XSJDPLPZ_ALTER_JSXSWS)
        self.Input(text, self.INPUT_XSJDPLPZ_ALTER_JSXSWS)

    def inputXsjdplpzAlterXsxsws(self, text):
        """小数精度批量配置-修改小数位数-显示小数位数"""
        self.ClearData(self.INPUT_XSJDPLPZ_ALTER_XSXSWS)
        self.Input(text, self.INPUT_XSJDPLPZ_ALTER_XSXSWS)

    def clickXsjdplpzAlterSave(self):
        """小数精度批量配置-修改小数位数-保存按钮"""
        self.Click(self.BUTTON_XSJDPLPZ_ALTER_SAVE)
        self.GotoSleep(2.5)


class PubLsbbKeyword(BsglElementFrame, PubLsbbElement, WebDriver):
    """历史报表--公共页面"""

    def changeLsbbBspl(self, text):
        """历史报表-查询条件-报送频率"""
        self.Click(self.QUERY_BSPL_LSBB)
        self.Click(self.INPUT_BSPL_LSBB.format(text))

    def changeLsbbBsrq(self, text):
        """历史报表-查询条件-报送日期"""
        self.Input(text, self.QUERY_BSRQ_LSBB)

    def changeLsbbRefresh(self):
        """历史报表-刷新按钮"""
        self.Click(self.BUTTON_REFRESH_LSBB)

    def changeLsbbImport(self, file_path):
        """历史报表-导入按钮"""
        self.Click(self.BUTTON_IMPORT_LSBB)
        self.GotoSleep(3)
        self.UploadFile(file_path)
        self.GotoSleep(2)
