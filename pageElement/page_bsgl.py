#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 9:42
# @Author   : yangshukun
# @File     : page_bsgl.py
from Common.common_map import *


class BsglElementMain(object):
    """主页面功能按钮及tab页切换"""
    XTGL = "//span[text()='系统管理']".__add__(XPATH)  # 主菜单--系统管理
    BSGL = "//a[@menuid='Setings010102']".__add__(XPATH)  # 报送管理菜单按钮
    BSGL_TAB = "//li[@menuid='Setings010102']".__add__(XPATH)  # 报送管理标题菜单
    SWITCH_BSPZ = "//li[contains(@url,'{}')]".__add__(XPATH)  # 切换报送品种的表达式，以占位符{}对品种进行站位，可以在关键字中传递品种名称
    CHOICE_FUNC_TAB = "//a[text()='{}']".__add__(XPATH)  # 不同品种下管理页签切换的表达式，使用占位符{}，可通过传参确定页签


class BsglElementFrame(object):
    """报送管理菜单相关frame"""
    MAIN_FRAME = "ifrSetings010102"  # 报送管理页面主框架frameID
    TAB_FRAME = "frame"  # 报送管理--功能按钮及数据主框架frameID
    BSPZ_FRAME = "ifrmcontent"  # 各报送品种页签功能框架frameID
    ADD_BSRW_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@createOrUpdateReport.do')]".__add__(
        XPATH)  # 新增报送任务框架frameID
    ADD_BSNR_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@Pub_queryBsnr.sf')]".__add__(
        XPATH)  # 新增--选择报送内容框架frameID
    JZCJ_FRAME = "LAYOUT_WIN_/SmartPage/REAST-Web-ROOT/page/centralizedCollection.html_iframe"  # 集中采集框架frameID
    # RN1104_UPLOAD_ALTER_FRAME = "LAYOUT_WIN_/RPTS/upload.jsp_iframe"  # 报表模板导入弹窗frameID
    RN1104_UPLOAD_ALTER_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/RPTS/upload.jsp')]".__add__(
        XPATH)  # 报表模板导入弹窗frameID
    BBMB_IMPORT_CHOICE_FRAME = "LAYOUT_WIN_/RPTS/page/reportDispose/importSelection.jsp_iframe"  # 报表导入，导入选项弹窗frameID
    RN1104_MSG_ALTER_FRAME = "//iframe[@id='LAYOUT_WIN_/RPTS/errorMsg.jsp_iframe']".__add__(
        XPATH)  # 报表模板导入弹窗，导入结果frameID
    RN1104_BSRYPZ_BATCH_UPDATE_FRAME = "LAYOUT_WIN_/SmartPage/RN1104-Web@RN1104_Oper_Param.sf%3Fm%3De_iframe"  # 1104报送人员配置批量编辑frameID
    BSGL_TAB_FRAME = "ifrmcontent"  # 报送品种管理框架ID
    RWFQ_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_missionLocked')]".__add__(
        XPATH)  # 任务废弃原因框架frameXPATH
    BSFW_CHANGE_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@RMM_BSFWEditPage')]".__add__(
        XPATH)  # EAST报送范围修改框架frameXPATH
    SJSQ_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@Pub_RptGrant_DataRange')]".__add__(
        XPATH)  # 数据授权frame
    PUB_SPLC_BATCH_UPDATE_FRAME = "LAYOUT_WIN_/SmartPage/RMM-Web@PubBatchBizFlow.sf%3F_iframe"  # 审批流程--批量修改，公共frameID
    PUB_HSWH_DETAIL_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_Set_funcDetail')]".__add__(
        XPATH)  # 函数维护页面，新增/编辑frame表达式
    PUB_HSWH_DETAIL_CHECK_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_Set_CheckFunc')]".__add__(
        XPATH)  # 函数维护页面，新增/编辑测试弹窗frame表达式
    SJLX_ADD_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_CustomDataAdd')]".__add__(
        XPATH)  # 自定义数据类型--数据类型--新增页面frame
    SJLX_EIDT_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_CustomDataEdit')]".__add__(
        XPATH)  # 自定义数据类型--数据类型--编辑页面
    SJLXMX_ADD_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_CustomDataDetailAdd')]".__add__(
        XPATH)  # 自定义数据类型--数据类型明细--新增页面）
    SJLXMX_EIDT_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_CustomDataDetailEdit')]".__add__(
        XPATH)  # 自定义数据类型--数据类型明细--编辑页面
    SJXWH_ADD_MAIN_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_Set_DataItemDetail')]".__add__(
        XPATH)  # 数据项维护页面，新增页面主frame
    SJXWH_DETAIL_FRAME = "dataItemDetail_ifm"  # 数据项维护页面，新增页面主frame--详情主frameID
    SJXWH_ADD_FUNC_FRAME = "basic_func_iframe"  # 数据项维护页面，新增页面主frame--详情主frameID--添加函数页面frameID
    SJXWH_ADD_FUNC_PARAMS_FRAME = "dataItemDetail_func_ifm"  # 数据项维护页面，新增页面主frame--详情主frameID--添加函数页面frameID
    BSSQ_QXX_FRAME = "DOM_auth_rpt_adm_frame2"  # 大额监控、反洗钱报送授权frame
    SPLC_QXX_FRAME = "LAYOUT_WIN_/SmartPage/RMM-Web@PubBatchBizFlow.sf%3F_iframe"  # 大额监控、反洗钱审批流程frame
    XZYSSZLX_FRAME = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_choice_msgCriminousType.sf%3Fm%3Dv%26msgCriminous%3D_iframe"  # 选择疑似涉罪类型
    XZJCBZMLX_FRAME = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_choice_msgMonitorType.sf%3Fm%3Dv%26msgMonitors%3D%26msgMonitorIndexs%3D_iframe"  # 选择监测标准码类型
    KHZLWH_YXQ_CJ = "//*[@id='_my97DP']/iframe".__add__(XPATH)  # 客户资料维护日期插件frame
    KHZLWH_KHXQ_FRAME = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_client_info.sf%3Fm%3Da%26cliNo%3D12345%26dataSourceFlag%3DTRUE_iframe"  # 客户资料维护
    XSJDPZ_TYXSWSPZ_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@RMM_Report_Currency_Conf')]".__add__(
        XPATH)  # 小数精度配置--通用小数位数配置frame
    XSJDPZ_EDIT_DYG_FRAME = "rptsIframe"  # 小数精度配置--编辑-小数精度批量配置页面--下方单元格frame
    XSJDPZ_EDIT_ALTER_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@RMM_Report_Item_Decimal_conf')]".__add__(
        XPATH)  # 小数精度配置--编辑-小数精度批量配置-修改小数位数-单元格小数位数配置frame


class PubBbmbElement(object):
    """1104报表模板页面"""
    CHOOSE_GROUP_NAME = "//select[@id='dom_ReportTemplateSettingForm.dgroup_s']/option[text()='{}']".__add__(
        XPATH)  # 报送分组选择，分组名称使用{}占位符，可在案例中传参
    INPUT_BSNRBH = "dom_ReportTemplateSettingForm.bsnrbh".__add__(ID)  # 报送内容编号输入框
    INPUT_BSNRMC = "dom_ReportTemplateSettingForm.bsnrmc".__add__(ID)  # 报送内容名称输入框
    INPUT_REPORT_FLAG = "//select[@id='dom_ReportTemplateSettingForm.availableFlag']/option[{}]".__add__(
        XPATH)  # 是否报送下拉框，传参2为“是”，3为“否”
    BUTTON_BBMB_REFRESH = "//input[@id='dom_ReportTemplateSettingForm.refresh']".__add__(XPATH)  # 报表模板页面刷新按钮
    BUTTON_IMPORT_MB = "dom_ReportTemplateList.export".__add__(ID)  # 导入模板按钮
    BUTTON_IMPORT_CHOICE_ITEM_CONFIRM = "//input[@class='buttonNew3 button']".__add__(XPATH)  # 报表导入，导入项选择弹窗-确认按钮
    BUTTON_UPLOAD = "//span[@class='fileInput']".__add__(XPATH)  # 导入弹窗上传按钮
    BUTTON_UPLOAD_FILE = "upload".__add__(ID)  # 模板导入弹窗中，文件导入按钮
    MSG_IMPORT_RESULT = "//table[@id='msgTable']/tbody/tr/td[2]".__add__(XPATH)  # 导入结果提示信息
    G0100_PATH = "D:\\DcabAtuoTest\\data\\1104模板\\月报\\G0100-211.xls"
    G0700_PATH = "D:\\DcabAtuoTest\\data\\1104模板\\半年报\\G0700-211.xls"
    G2300_PATH = "D:\\DcabAtuoTest\\data\\1104模板\\半年报\\G2300-091.xls"
    G0102_PATH = "D:\\DcabAtuoTest\\data\\1104模板\\月报\\G0102-201.xls"
    RPBCC_A1302_PATH = "D:\\DcabAtuoTest\\data\\人行报表模板\\季报第1批\\A1302-监管类指标季报表1（人民币）.xls"
    RPTC_T115_PATH = "D:\\DcabAtuoTest\\data\\综合报表模版\\江铃个性化报表\\综合报表表样\\半年报\\绿色融资统计表_T115.xls"
    RPTC_FXCJGZB01_PATH = "D:\\DcabAtuoTest\\data\\综合报表模版\\江铃个性化报表\\综合报表表样\\季报\\非现场监管关键指标.xls"
    RSAFER_P02_PATH = "D:\\DcabAtuoTest\\data\\外管局报表模板\\日报\\P02：大额结售汇交易统计表.xls"  # 外管局报表-P02
    BUTTON_EXPORT = "dom_ReportTemplateList.import".__add__(ID)  # 导出模板按钮
    BOX_BBMB = "//*[@id='dom_ReportTemplateList']/tbody/tr[1]/td[{}]/span/span".__add__(
        XPATH)  # 复选框选择，传参1为第一条，2为第二条，last()为最后一条
    DPTM_7DAY_JC_XPATH = "D:\\DcabAtuoTest\\data\\压力测试模板\\流动性缺口压力测试-7天生存期-基础场景.xls"  # 流动性缺口压力测试-7天生存期-基础场景
    DPTM_7DAY_TY_XPATH = "D:\\DcabAtuoTest\\data\\压力测试模板\\流动性缺口压力测试-7天生存期-通用场景.xls"  # 流动性缺口压力测试-7天生存期-通用场景
    LQDRM_G22_XPATH = "D:\\DcabAtuoTest\\data\\压力测试模板\\流动性缺口压力测试-7天生存期-通用场景.xls"  # G22流动性比例监测表
    CLOSE_DRTS = "//*[@id='LAYOUT_WIN_/RPTS/errorMsg.jsp']/div[3]".__add__(
        XPATH)  # 关闭导入提示弹窗
    CLOSE_MBDRTC = "//*[@id='LAYOUT_WIN_/RPTS/upload.jsp']/div[3]".__add__(
        XPATH)  # 关闭模板导入弹窗


class PubBsrwElement(object):
    """EAST报送任务页签相关元素"""
    SELECT_BSQJ_BSRW = "//*[@id='reportJobManagement_from.bsqj']".__add__(XPATH)  # 报送期间所有下拉值
    INPUT_BSQJ = "//*[@id='reportJobManagement_from.bsqj']/option[text()='{}']".__add__(XPATH)  # 查询条件--报送期间
    INPUT_RWMC = "//*[@id='reportJobManagement_from.reportName']".__add__(XPATH)  # 查询条件--任务名称
    BUTTON_SEARCH = "reportJobManagement_from.refresh".__add__(ID)  # 刷新按钮
    BUTTON_ADD_BSRW = "//*[@id='reportJobManagement_list.add']".__add__(XPATH)  # 新增报送任务按钮
    TITLE_ADD_BSRW = "//th[@class='DefaultTitleBar-title']".__add__(XPATH)  # 新增报送任务页面标题
    ALERT_BSNRMC = "//*[@id='bsnrmc']".__add__(XPATH)  # 新增--点击报送内容名称选择框
    BUTTON_BSNRMC = "//*[@id='queryBsnrList.bsnrbh' and text()='{}']".__add__(XPATH)  # 选择报送内容编号
    INPUT_ADD_BSQJ_FOR_YEAR = "//input[@id='reportRangeYearSel']".__add__(XPATH)  # 选择报送期间--年
    INPUT_ADD_BSQJ_FOR_MONTH = "//*[@id='reportRangeYearSel_4']/option[text()='{}']".__add__(XPATH)  # 选择报送期间--月
    INPUT_ADD_BSQJ_FOR_SEASON = "//*[@id='reportRangeYearSel_5']/option[text()='{}']".__add__(XPATH)  # 选择报送期间--季度
    INPUT_ADD_BSQJ_FOR_DAY = "//span[@id='reportRangeDay']/input".__add__(XPATH)  # 外管局选择报送期间
    INPUT_RWLX_BB = "//td[text()='任务类型']/../td[2]/input[1]".__add__(XPATH)  # 选择任务类型为补报
    INPUT_RWLX_TQSC = "//td[text()='任务类型']/../td[2]/input[2]".__add__(XPATH)  # 选择任务类型为提前生成任务
    INPUT_QSSD = "//input[@name='params.getDataTimeType' and @value='{}']".__add__(
        XPATH)  # 选择取数时点,传参1-指定时间取数，2-立即取数，3-不取数
    BUTTON_SAVE_BSRW = "//*[@class='button2 button']".__add__(XPATH)  # 新增--保存按钮
    ALERT_ADD = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 关闭新增任务成功弹窗按钮
    BUTTON_JZCJ = "//*[@id='ccBtn']".__add__(XPATH)  # 集中采集按钮
    BUTTON_SCBSRW = "//*[@id='confirm']".__add__(XPATH)  # 点击生成集中采集报送任务
    ALERT_JZCJ = "//*[@class='layui-layer-btn0']".__add__(XPATH)  # 确认按钮
    BUTTON_RWFQ = "reportJobManagement_list.lockedText".__add__(ID)  # 任务废弃按钮
    INPUT_RWFQ = "missionLocked_from.lockedReason".__add__(ID)  # 任务废弃原因输入框
    ALERT_RWFQ = "missionLocked_from.reset".__add__(ID)  # 确定废弃该任务
    ALERT_QRCG1 = "aui_close".__add__(CLASS)  # 关闭废弃/填报结束日期成功弹窗
    ALERT_QRCG2 = "layoutContentHeader_right".__add__(CLASS)  # 关闭废弃任务/填报结束日期弹窗
    BUTTON_TBJSRQ = "//*[@id='reportJobManagement_list.changeEndTime']".__add__(XPATH)  # 填报结束日期
    BUTTON_TBJSRQ_BC = "//*[@id='missionChangeEndTime.save']".__add__(XPATH)  # 保存填报结束日期
    MSG_ADD_RESULT = "//*[@class='aui_content']".__add__(XPATH)  # 新增成功提示信息
    MSG_JZCJ_RESULT = "//*[@class='layui-layer-content']".__add__(XPATH)  # 集中采集生成报送任务后断言
    INPUT_BBMB_FOR_1104 = "//select[@id='version']/option[{}]".__add__(XPATH)  # 报表类新增任务选择模板，{}占位符，输入int型，2代表第一个
    COUNG_QUERY_RESULT_BSRW = "//td[@id='reportJobManagement_list.to']//td[1]/span[1]".__add__(XPATH)  # 报送任务--查询结果统计信息


class PubBsfwElement(object):
    """EAST报送范围页签相关元素"""
    INPUT_BSPL = "//*[@id='bsfwSettingForm.bspl']/option[text()='{}']".__add__(XPATH)  # 查询条件--报送频率
    INPUT_BSNR = "//*[@id='bsfwSettingForm.bsnr']".__add__(XPATH)  # 查询条件--报送内容
    BUTTON_SEARCH1 = "//input[@id='bsfwSettingForm.refresh']".__add__(XPATH)  # 刷新按钮
    BUTTON_SFBS = "//*[@id='bsfwSettingList']/tbody/tr[1]/td[6]/span/label".__add__(XPATH)  # 是否报送按钮
    CHECK_ALL = "//*[@id='fixed_title']/thead/tr/th[1]/span/span".__add__(XPATH)  # 全选复选框
    CHECK_ONE = '//*[@id="bsfwSettingList"]/tbody/tr[1]/td[1]/span[1]/span'.__add__(XPATH)  # 单选复选框
    BUTTON_MODIFY = "//input[@id='bsfwSettingList.btnEdit']".__add__(XPATH)  # 修改按钮
    INPUT_QSQJ = "//select[@id='bsfwBatchSettingForm.dataPeriod']/option[text()='{}']".__add__(XPATH)  # 取数期间-本期 上期
    INPUT_QSSD_BSFW = "//input[@id='bsfwBatchSettingForm.cronExp']".__add__(XPATH)  # 输入取数时点
    INPUT_BSJZQX = "//input[@id='bsfwBatchSettingForm.deadLineNum']".__add__(XPATH)  # 输入报送截止期限
    INPUT_BSJZQX_TYPE = "//*[@id='bsfwBatchSettingForm.deadLineUnit']/option[text()='{}']".__add__(
        XPATH)  # 报送截止期限类型  天  小时  分
    INPUT_SFHJJR = "//select[@id='bsfwBatchSettingForm.isHolidayIncluded']/option[text()='{}']".__add__(
        XPATH)  # 是否含节假日 是 否
    INPUT_ZDHD = "//select[@id='bsfwBatchSettingForm.autoCheck']/option[text()='{}']".__add__(XPATH)  # 自动核对  是  否
    BUTTON_CHANGE_SAVE = "//input[@id='bsfwBatchSettingForm.save']".__add__(XPATH)  # 保存按钮
    ALERT_MODIFY = "//*[@class='layoutContentHeader_right']".__add__(XPATH)  # 关闭弹窗
    MSG_SFBS_RESULT = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div".__add__(
        XPATH)  # 断言是否报送
    MSG_CHANGE_RESULT = "//*[@id='bsfwSettingList']/tbody/tr[1]/td[9]/span[1]/text()".__add__(XPATH)  # 断言修改配置成功
    BUTTON_OK_ALERT = '//*[@class="aui_state_highlight"]'.__add__(XPATH)  # 保存成功弹窗确认按钮


class Rn1104ElementBsrypzElement(object):
    """1104报送人员配置"""
    INPUT_BSPL_BSRYPZ = "//select[@id='report_Oper_Param_Form.bspl']/option[text()='{}']".__add__(
        XPATH)  # 报送频率，频率名称使用{}站位，案例编写根据需要传参
    INPUT_BBBH = "//*[@id='report_Oper_Param_Form.reportNo']".__add__(XPATH)  # 报表编号输入框
    INPUT_BBMC = "//*[@id='report_Oper_Param_Form.reportName']".__add__(XPATH)  # 报表名称输入框
    INPUT_BBFZ = "//select[@id='report_Oper_Param_Form.reportGroup']/option[text()='{}']".__add__(
        XPATH)  # 报表分组下拉选择，使用{}占位，案例根据需要传参
    BUTTON_REFRESH = "//*[@id='report_Oper_Param_Form.refresh']".__add__(XPATH)  # 刷新按钮
    BOX_ALL = "//*[@id='fixed_title']/thead/tr/th[1]/span/span".__add__(XPATH)  # 全选复选框
    BOX_ALONE = "//*[@id='report_Oper_Param_List']/tbody/tr[1]/td[1]/span/span"  # 复选框单选
    BUTTON_EDIT_MANY = "//*[@id='report_Oper_Param_List.el']".__add__(XPATH)  # 批量编辑按钮
    INPUT_RYLX = "//select[@id='oper_param_form.operTye']/option[text()='{}']".__add__(
        XPATH)  # 批量编辑弹窗，人员类型下拉选项，{}占位，案例传参
    INPUT_NAME = "//*[@id='oper_param_form.operName']".__add__(XPATH)  # 批量编辑弹窗，人员姓名输入框
    BUTTON_CONFIRM = "//*[@id='oper_param_form.save']".__add__(XPATH)  # 批量编辑弹窗，确认按钮
    BUTTON_SAVE = "//*[@id='report_Oper_Param_List.save']".__add__(XPATH)  # 保存按钮
    INPUT_TBR = "//*[@id='report_Oper_Param_List.preparer']".__add__(XPATH)  # 填表人输入框
    INPUT_FHR = "//*[@id='report_Oper_Param_List.reviewer']".__add__(XPATH)  # 复核人输入框
    INPUT_FZR = "//*[@id='report_Oper_Param_List.chargePerson']".__add__(XPATH)  # 负责人输入框
    DATA_BBBH = "//table[@id='report_Oper_Param_List']/tbody/tr[1]/td[2]/span[1]".__add__(XPATH)  # 第一行数据的第一个值
    MSG_SAVE_SUCC = "//div[@class='aui_content']".__add__(XPATH)  # 保存成功提示信息


class RsafeZhxzwhElement(object):
    """外管局--账户性质维护"""
    BUTTON_ADD = "U01_28_list.newRow".__add__(ID)  # 新增按钮
    INPUT_ZHXZBH = "//table[@id='mainTable']/tbody/tr[last()]/td[2]/input".__add__(XPATH)  # 账户性质编号输入框
    INPUT_ZHXZMC = "//table[@id='mainTable']/tbody/tr[last()]/td[3]/input".__add__(XPATH)  # 账户性质名称输入框
    BUTTON_SAVE = "U01_28_list.save".__add__(ID)  # 保存按钮
    BUTTON_DEL = "U01_28_list.deleteData".__add__(ID)  # 删除按钮
    BOX_DEL_DATA = "//table[@id='mainTable']/tbody//input[@value='{}'][1]/../../td[1]/img".__add__(
        XPATH)  # 根据编号定位数据，编号值为占位符{}


class EastBscsElement(object):
    """EAST报送参数页签相关元素"""
    INPUT_LEAD_PERSON = "//span[text()='牵头部门负责人']/../../td[2]/span[1]/input".__add__(XPATH)  # 牵头部门负责人
    INPUT_DEPARTMENT_PERSON = "//span[text()='部门负责人联系方式']/../../td[2]/span[1]/input".__add__(XPATH)  # 部门负责人联系方式
    INPUT_PREPARER = "//span[text()='填表人']/../../td[2]/span[1]/input".__add__(XPATH)  # 填表人
    INPUT_PREPARER_NUMBER = "//span[text()='填表人手机号']/../../td[2]/span[1]/input".__add__(XPATH)  # 填表人手机号
    INPUT_MONTH_COUNT = "//select[@id='mcaltype_select']/option[text()='30天']".__add__(XPATH)  # 月份计算方式  30天  自然月
    INPUT_REMOVE_NUMBER = "//span[text()='内部分户账需排除的账号']/../../td[2]/span[1]/input".__add__(XPATH)  # 内部分户账需排除的账号
    INPUT_REMOVE_SUBJECT = "//span[text()='内部分户账需排除的科目']/../../td[2]/span[1]/input".__add__(XPATH)  # 内部分户账需排除的科目
    BUTTON_SBSP = "//*[@id='reast_Param_Settings_list']/tbody/tr[8]/td[2]/span[1]/input[2]".__add__(
        XPATH)  # 上报审批  是：input[2]   否：input[3]
    BUTTON_EXPORT = '//*[@id="reast_Param_Settings_list"]/tbody/tr[9]/td[2]/span[1]/input[3]'.__add__(
        XPATH)  # 导出控制开关 是：input[2]  否：input[3]
    INPUT_ORGANIZATION_CODE = "//span[text()='机构代码']/../../td[2]/span[1]/input".__add__(XPATH)  # 机构代码
    BUTTON_SAVE_CSSZ = "//input[@id='reast_Param_Settings_list.save']".__add__(XPATH)  # 保存参数设置


class EastBmzhElement(object):
    """EAST编码转换页签相关元素"""
    INPUT_BMLX = "//select[@id='pub_report_code_change_form.codeType']/option[text()='金融机构类型']".__add__(
        XPATH)  # 标准编码类型 1、金融机构类型  2、被投资机构类型
    INPUT_BM_NAME = "pub_report_code_change_form.codeName".__add__(ID)  # 标准编码名称
    INPUT_IFBSBM = "//select[@id='pub_report_code_change_form.isCodeEmpty']/option[2]".__add__(
        XPATH)  # 报送编码是否为空 1、是：option[2]  2、否：option[3]
    INPUT_MODIFY = "//select[@id='pub_report_code_change_form.isChanged']/option[2]".__add__(
        XPATH)  # 是否修改 1、是：option[2]  2、否：option[3]
    BUTTON_REFRESH = "//input[@id='pub_report_code_change_form.refresh']".__add__(XPATH)  # 刷新按钮
    INPUT_MODIFY_BSBM = "/html/body/center/form/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/div/div[2]/table/tbody/tr[1]/td[3]/span[1]/input".__add__(
        XPATH)  # 修改报送编码


class JsZbjpzElement(object):
    """金数准备金配置页签相关元素"""
    INPUT_CKZL = "//*[@id='depositSettingForm.paramname']".__add__(XPATH)  # 查询条件--存款种类输入框
    CHOICE_JCFS = "//*[@id='depositSettingForm.reservesType']/option[text()='{}']".__add__(XPATH)  # 查询条件--缴存方式下拉
    BUTTON_REFRESH = "depositSettingForm.refresh".__add__(ID)  # 刷新按钮
    SET_ZBJJC = "//span[text()='{}']/../../td/span/select/option[text()='{}']".__add__(
        XPATH)  # 准备金缴存方式列表--存款种类,缴存方式下拉使用{}站位，案例编写根据需要传参
    SET_ZBJJC_NULL = "//span[text()='{}']/../../td/span/select/option[1]".__add__(
        XPATH)  # 准备金缴存方式列表--存款种类使用{}站位，缴存方式为空
    MSG_JCFS_RESULT = "//*[@class='aui_content']".__add__(XPATH)  # 准备金缴存方式列表--选择缴存方式后断言 --保存成功
    SUCCESS_CLOSE = "//a[@class='aui_close']".__add__(XPATH)  # 关闭弹窗


class JsBscsElement(object):
    """金数报送参数页签相关元素"""
    SET_QYPJHL = "//select[@id='rfbsParamSettingsform.AVG_EXCHANGE_RATE']/option[text()='{}']".__add__(
        XPATH)  # 启用平均汇率，是/否--下拉列表使用{}占位
    SET_SBSP_YES = "//input[@id='reportBizFlagY']".__add__(XPATH)  # 上报审批--是
    SET_SBSP_NO = "//input[@id='reportBizFlagN']".__add__(XPATH)  # 上报审批--否
    BUTTON_SAVE = "//input[@id='rfbsParamSettingsform.save']".__add__(XPATH)  # 保存
    MSG_SAVE_RESULT = "//*[@class='aui_content']".__add__(XPATH)  # 准备金缴存方式列表--选择缴存方式后断言 --保存成功
    SUCCESS_CLOSE = "//a[@class='aui_close']".__add__(XPATH)  # 关闭弹窗


class EastKmjzElement(object):
    """EAST科目记账设置页签相关元素"""
    INPUT_BSKJ = "//*[@id='REAST_KMJZ_form.bskj']/option[text()='{}']".__add__(
        XPATH)  # 查询条件-报送口径 203-对公活期存款分户账、205-对公定期存款分户账、211-内部分户账
    INPUT_KMH = "//*[@id='REAST_KMJZ_form.kmh']".__add__(XPATH)  # 查询条件-科目号
    BUTTON_REFRESH_KMJZ = "//*[@id='REAST_KMJZ_form.refresh']".__add__(XPATH)  # 刷新按钮
    BUTTON_ADD_KMJZ = "//*[@id='REAST_KMJZ_list.add']".__add__(XPATH)  # 新增按钮
    INPUT_ADD_KMH = "//table[@id='REAST_KMJZ_list']/tbody/tr[last()]//input[@id='REAST_KMJZ_list.SUBJECT_NO']".__add__(
        XPATH)  # 输入科目号
    INPUT_ADD_BZ = "//table[@id='REAST_KMJZ_list']/tbody/tr[last()]//select[@id='REAST_KMJZ_list.BZ']/option[text()='{}']".__add__(
        XPATH)  # 选择币种 人民币
    INPUT_ADD_BSKJ = "//table[@id='REAST_KMJZ_list']/tbody/tr[last()]//select[@id='REAST_KMJZ_list.GSBW']/option[text()='{}']".__add__(
        XPATH)  # 选择报送口径
    INPUT_ADD_KMM = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.SUBJECT_NAME"]'.__add__(
        XPATH)  # 输入科目名
    INPUT_ADD_KHBH = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.CLTNO"]'.__add__(
        XPATH)  # 输入客户编号
    INPUT_ADD_KHRQ = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.KHRQ"]'.__add__(
        XPATH)  # 选择开户日期
    INPUT_ADD_XHRQ = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.XHRQ"]'.__add__(
        XPATH)  # 选择销户日期
    INPUT_ADD_RATE = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.RATE_VALUE"]'.__add__(
        XPATH)  # 输入利率
    INPUT_ADD_ZHZT = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//select[@id="REAST_KMJZ_list.ZHZT"]/option[text()="{}"]'.__add__(
        XPATH)  # 选择账户状态  正常、冻结、销户、其他
    INPUT_ADD_BZJZHBZ = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//select[@id="REAST_KMJZ_list.BZJZHBZ"]/option[text()="{}"]'.__add__(
        XPATH)  # 选择保证金账户标志(203)  是、否
    INPUT_ADD_CKQX = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.CKQX"]'.__add__(
        XPATH)  # 输入存款期限
    INPUT_ADD_DGDQCKZHLX = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.DGDQCKZHLX"]'.__add__(
        XPATH)  # 输入对公定期存款账户类型(205)
    INPUT_ADD_DQR = '//table[@id="REAST_KMJZ_list"]/tbody/tr[last()]//input[@id="REAST_KMJZ_list.DQR"]'.__add__(
        XPATH)  # 输入到期日(205)
    CHECK_ALL_KMJZ = "//*[@id='fixed_title']/thead/tr/th[1]/span/span".__add__(XPATH)  # 复选框全选
    CHECK_ONE_KMJZ = "//*[@id='REAST_KMJZ_list']/tbody/tr[1]/td[1]/span[1]/span".__add__(XPATH)  # 复选框单选
    BUTTON_DELETE_KMJZ = '//*[@id="REAST_KMJZ_list.del"]'.__add__(XPATH)  # 删除按钮
    BUTTON_DELETE_KMJZ_X = '//*[@id="tableCopy_REAST_KMJZ_list"]/td[1]/input[1]'.__add__(XPATH)  # 删除X按钮
    BUTTON_SAVE_KMJZ = '//*[@id="REAST_KMJZ_list.save"]'.__add__(XPATH)  # 保存按钮
    ALERT_ADD_SUC = '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/a'.__add__(
        XPATH)  # 保存成功弹窗关闭按钮
    MSG_DELETE_SUCC = '//*[@id="REAST_KMJZ_list.tipsText"]'.__add__(XPATH)  # 断言删除成功


class EastMxkmElement(object):
    """EAST明细科目设置页签相关元素"""
    BUTTON_SAVA_MXKM = '//*[@id="settingForm"]/table/tbody/tr[1]/td[2]/input'.__add__(XPATH)  # 保存按钮
    INPUT_GET_MODE = "//form[@id='settingForm']/table/tbody//span[text()='{}']/../..//select[@name='GETTYPE']/option[text()='{}']".__add__(
        XPATH)  # 获取方式
    INPUT_VALUE_MXKM = "//form[@id='settingForm']/table/tbody//span[text()='{}']/../..//input[@name='KB']".__add__(
        XPATH)  # 参数值
    INPUT_KM_NAME = "//form[@id='settingForm']/table/tbody//span[text()='{}']/../..//input[@name='KB_NAME']".__add__(
        XPATH)  # 科目名称
    MSG_MXKM_SAVE = '//*[@class="layui-layer-content"]'.__add__(XPATH)  # 断言保存成功


class PubFzglElement(object):
    """分组管理，公共页面元素"""
    INPUT_GROUP_NAME = "groupName".__add__(ID)  # 分组名称输入框
    INPUT_GROUP_USER = "groupUserName".__add__(ID)  # 分组成员姓名
    BUTTON_GROUP_REFRESH = "//*[@class='button31 button']".__add__(XPATH)  # 分组管理刷新按钮
    BUTTON_GROUP_ADD = "//*[@class='button26 button']".__add__(XPATH)  # 分组管理新增按钮
    INPUT_ADD_FZMC = "//*[@id='listTable']/tbody/tr[1]/td[1]/input".__add__(XPATH)  # 新增分组时，输入分组名称（新增时，默认在第一条数据）
    DATA_FIRST_GROUP = "//*[@id='listTable']/tbody/tr[1]/td[{}]/span".__add__(
        XPATH)  # 第一条数据的标签（传参，1为分组名称，2为成员列表，3为分组描述）
    BUTTON_CLICK_CYLB = "//*[@class='xm-icon']".__add__(XPATH)  # 新增分组时，点击选择成员列表（新增时，默认在第一条数据）
    BUTTON_CLEAN_CYLB = "//*[@class='xm-iconfont xm-icon-qingkong']".__add__(XPATH)  # 成员列表清空按钮
    INPUT_ADD_CYLB = "//*[@class='xm-input xm-search-input']".__add__(XPATH)  # 成员列表输入查询人员
    BOX_CYLB = "//*[@class='xm-iconfont xm-icon-quanxuan']".__add__(XPATH)  # 成员列表全选
    INPUT_ADD_FZMS = "//*[@id='listTable']/tbody/tr[1]/td[3]/textarea".__add__(XPATH)  # 分组描述
    BUTTON_GROUP_SAVE = "//*[@class='button30 button']".__add__(XPATH)  # 分组管理-保存按钮
    ALERT_GROUP_SAVE_CLOSE = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 分组管理-保存-弹窗关闭
    MSG_GROUP_SAVE = "//td[@class='aui_main']/div".__add__(XPATH)  # 保存弹窗提示信息
    INPUT_EDITE_GROUP_BY_NAME = "//span[text()='{}']/../input".__add__(XPATH)  # 编辑状态下，根据分组名称定位到数据行的名称编辑框
    INPUT_EDITE_GROUP_BY_MS = "//span[text()='{}']/../../td[3]/textarea".__add__(XPATH)  # 编辑状态下，根据分组名称定位到数据行的描述编辑框
    BUTTON_GROUP_EDITE_OR_DEL = "//span[text()='{}']/../../td[4]/a[{}]".__add__(
        XPATH)  # 根据分组名称定位到数据行的操作列（分别输入分组名称和序号，序号1代表编辑，2代表删除）
    BUTTON_GROUP_DEL_CONFIRM = "aui_state_highlight".__add__(CLASS)  # 删除弹窗--确认按钮
    DATA_GROUP_USER_LIST = "//table[@id='listTable']/tbody/tr[1]/td[2]/span".__add__(XPATH)  # 管理员分组中所有成员列表


class PubBssqElement(object):
    """报送授权，公共页面"""
    CLICK_GROUP_NAME_BSSQ = "search_input_input".__add__(CLASS)  # 查询条件-分组名称
    INPUT_GROUP_NAME_BSSQ = "//*[@class='search_input_input_table']//input".__add__(XPATH)  # 查询条件-输入分组名称
    CLICK_GROUP_NAME_ONE_BSSQ = "//*[@class='search_input_table']/tbody/tr[1]".__add__(XPATH)  # 查询条件-选择查询出的第一个分组名称
    INPUT_BSNR_BSSQ = "//*[@id='reportUserAuthorizationForm.bsnrmc']".__add__(XPATH)  # 查询条件-报送内容
    BUTTON_REFRESH_BSSQ = "reportUserAuthorizationForm.refresh".__add__(ID)  # 刷新按钮
    BUTTON_HDQX = "//*[@id='fixed_title']/thead/tr/th[2]/span/span".__add__(XPATH)  # 核对权限
    BUTTON_SBQX = '//*[@id="fixed_title"]/thead/tr/th[3]/span/span'.__add__(XPATH)  # 上报权限
    BUTTON_CXQX = '//*[@id="fixed_title"]/thead/tr/th[4]/span/span'.__add__(XPATH)  # 查询权限
    BUTTON_CCQX = '//*[@id="fixed_title"]/thead/tr/th[5]/span/span'.__add__(XPATH)  # 重抽权限
    BUTTON_SAVE_BSSQ = "//input[@id='reportUserAuthorizationList.save']".__add__(XPATH)  # 保存按钮
    MSG_SAVE_BSSQ = "//div[@class='aui_content']".__add__(XPATH)  # 保存弹窗提示信息
    ALERT_SAVE_BSSQ_CLOSE = "aui_close".__add__(CLASS)  # 关闭保存成功弹窗


class PubSjsqElement(object):
    """数据授权，公共页面"""
    INPUT_BSNR_SJSQ = "//input[@id='rptContentGrant_form.bscontent']".__add__(XPATH)  # 查询条件-报送内容
    BUTTON_REFRESH_SJSQ = "//input[@id='rptContentGrant_form.refresh']".__add__(XPATH)  # 刷新按钮
    BUTTON_CLEAR = "//input[@id='rptContentGrant_form.clearInput']".__add__(XPATH)  # 清除条件按钮
    BUTTON_ALL = '//*[@id="rptContentGrant_list.dataRange"]'.__add__(XPATH)  # 全部按钮
    INPUT_ALL_SJSQ = "//input[@id='pubRptGrantDataRangeForm.dataRangeType_all']/../span".__add__(XPATH)  # 选择全部权限
    BUTTON_AZDSX = "//input[@id='pubRptGrantDataRangeForm.dataRangeType_column']/../span".__add__(XPATH)  # 按字段筛选
    INPUT_AZDSX = "//*[@name='pubRptGrantDataRangeForm.column']/option[text()='{}']".__add__(XPATH)  # 按字段筛选-选择下拉框字段
    CLICK_AZDSX_XLK = '//*[@class="MultiDropIMG"]'.__add__(XPATH)  # 按字段筛选-点击第二个下拉框
    INPUT_AZDSX_CLICK = '//*[@id="nstc.sf.multiDropDivEle"]/div/span[text()="{}"]/../span[1]'.__add__(
        XPATH)  # 按字段筛选-第二个为下拉框
    INPUT_AZDSX_INPUT = '//*[@name="pubRptGrantDataRangeForm.columnValue"]'.__add__(XPATH)  # 按字段筛选-第二个为输入框
    BUTTON_ASJBSSX = "//*[@value='按数据标识筛选']/../../span/span[@class='radioStyle']".__add__(XPATH)  # 按数据标识筛选
    INPUT_ASJBSSX = "//input[@id='pubRptGrantDataRangeForm.dataFlag']".__add__(XPATH)  # 按数据标识筛选-输入值
    BUTTON_SAVE_SJSQ = "//input[@id='pubRptGrantDataRangeForm.save']".__add__(XPATH)  # 保存按钮
    ALERT_QR_SJSQ = '//*[@class="aui_state_highlight"]'.__add__(XPATH)  # 保存成功确认按钮
    ALERT_CLOSE_SJSQ = "//*[@class='layoutContentHeader_right']".__add__(XPATH)  # 关闭数据范围弹窗


class PubSplcElement(object):
    """公共页面-审批流程"""
    CLICK_GROUP_NAME_SPLC = "search_input_input".__add__(CLASS)  # 查询条件-分组名称
    INPUT_GROUP_NAME_SPLC = "//*[@class='search_input_input_table']//input".__add__(XPATH)  # 查询条件-输入分组名称
    CLICK_GROUP_NAME_ONE_SPLC = "//*[@class='search_input_table']/tbody/tr[1]".__add__(XPATH)  # 查询条件-选择查询出的第一个分组名称
    BOX_ALL_SPLC = "//*[@id='fixed_title']/thead/tr/th[1]/span/span".__add__(XPATH)  # 审批流程，复选框全选
    BOX_BY_BSNRMC = "//span[text()='{}']/../../td[1]/span[1]".__add__(XPATH)  # 根据传入的报送内容名称，定位单个复选框
    BUTTON_BATCH_UPDATE = "reportBizFlow_List.batchModify".__add__(ID)  # 批量修改按钮
    INPUT_BIZCODE_SPLC = "//*[@id='reportBizFlow_List.bizCode']/option[text()='{}']".__add__(
        XPATH)  # 审批流程名称，通过传参选择，每个品种名称不一样
    BUTTON_BATCH_SAVE_SPLC = "batchBizFlowForm.save".__add__(ID)  # 审批流程批量修改弹窗保存按钮
    BUTTON_MAIN_SAVE_SPLC = "reportBizFlow_List.save".__add__(ID)  # 审批流程主页面保存按钮
    BUTTON_REFRESH_SPLC = "reportBizFlow_Form.refresh".__add__(ID)  # 审批流程页面--刷新按钮
    BUTTON_BATCH_ALERT_CLOSE_SPLC = "aui_close".__add__(CLASS)  # 审批流程--批量修改弹窗--关闭
    MSG_BATCH_ALERT_SPLC = "//div[@class='aui_content']".__add__(XPATH)  # 审批流程-批量修改保存--弹窗提示信息


class PubBsnrsqElement(object):
    """报表类--报送内容授权公共页面"""
    CLICK_GROUP_NAME_BSNRSQ = "search_input_input".__add__(CLASS)  # 查询条件-分组名称
    INPUT_GROUP_NAME_BSNRSQ = "//*[@class='search_input_input_table']//input".__add__(XPATH)  # 查询条件-输入分组名称
    CLICK_GROUP_NAME_ONE_BSNRSQ = "//*[@class='search_input_table']/tbody/tr[1]".__add__(XPATH)  # 查询条件-选择查询出的第一个分组名称
    INPUT_BSNR_BSNRSQ = "//*[@id='reportDataGrantForm.reportName']".__add__(XPATH)  # 查询条件-报送内容
    BUTTON_REFRESH_BSNRSQ = "reportDataGrantForm.refresh".__add__(ID)  # 报送内容授权页面--刷新按钮
    BOX_ALL_BSNRSQ = "//input[@id='reportDataGrantList.chk_box']/../span".__add__(XPATH)  # 报送内容授权复选框全选
    BOX_ANY_BY_NAME_BSNRSQ = "//span[text()='{}']/../../td[1]".__add__(XPATH)  # 根据报送内容名称定位到复选框，报送内容名称作为参数
    BUTTON_EDIT_ALL_BSNRSQ = "reportDataGrantList.editAll".__add__(ID)  # 编辑全部按钮
    BUTTON_TRACE_ALL_BSNRSQ = "reportDataGrantList.traceAll".__add__(ID)  # 追溯全部按钮
    BUTTON_CANCEL_ALL_BSNRSQ = "reportDataGrantList.cancelAll".__add__(ID)  # 取消操作权限按钮
    BUTTON_EDIT_COUNT_BSNRSQ = "//span[text()='{}']/../../td[4]/a[{}]".__add__(
        XPATH)  # 操作列，编辑/追溯按钮，根据报送内容名称作为参数定位，并且传入索引值，1为编辑，2为追溯


class RimasBscsElement(object):
    """利率报备-报送参数"""
    BUTTON_SAVE_RIMAS = 'rimas_param_Settings_list.save'.__add__(ID)  # 保存按钮
    INPUT_BSJRFS = "//*[@id='prpMode_select']/option[text()='{}']".__add__(XPATH)  # 报送接入方式
    INPUT_QTBM = "//*[@value='{}']/../../../td[2]/span/input[@id='rimas_param_Settings_list.value_']".__add__(
        XPATH)  # 输入牵头部门/牵头部门联系人/牵头部门联系电话/用户名/人行直连服务地址/密码/发起参与者应用系统标识/接收参与者编码/接收参与者应用系统标识/RIMAS_LINK服务地址/
    INPUT_SBSP_RIMAS = "//*[@value='上报审批']/../../../td[2]/span/input[2]".__add__(XPATH)  # 上报审批 是：input[2]   否：input[3]


class RPTCBscsElement(object):
    """综合报表报送参数页签相关元素"""
    BUTTON_SBSP = "//*[@class='content_body']/td[2]/input[2]".__add__(
        XPATH)  # 上报审批  是：input[1]   否：input[2]
    BUTTON_SAVE_RPTC = "//*[@class='button button0111']".__add__(XPATH)  # 保存


class RsazjBscsElement(object):
    """浙江国资委-报送参数"""
    BUTTON_SAVE_RSAZJ = "rsazj_ParamSettings_form.save".__add__(ID)  # 保存按钮
    INPUT_FKJYLX = "//*[@id='rsazj_ParamSettings_form_TRADETYPE.TreeId']//a[text()='{}']/../span[starts-with(@data-id,'SmartPage_DropTree.rsazj_ParamSettings_form_TRADETYPE_checbox')]".__add__(
        XPATH)  # 选择付款交易类型  交易类型/付款/内部转账/外部转账/上收
    INPUT_SKJYLX = "//*[@id='rsazj_ParamSettings_form_INTRADETYPE.TreeId']//a[text()='交易类型']/../span[starts-with(@data-id,'SmartPage_DropTree.rsazj_ParamSettings_form_INTRADETYPE_checbox')]".__add__(
        XPATH)  # 选择收款交易类型  交易类型/收款/内部转账/外部转账/上收
    INPUT_DESXED = "rsazj_ParamSettings_form.AMOUNTLIMIT".__add__(ID)  # 输入大额筛选额度
    INPUT_DE_IP = "rsazj_ParamSettings_form.SERVER_IP".__add__(ID)  # 输入大额资金监测系统服务端IP
    INPUT_DE_PORT = "rsazj_ParamSettings_form.SERVER_PORT".__add__(ID)  # 输入大额资金监测系统服务端端口号
    INPUT_DE_PROTOCOL = "rsazj_ParamSettings_form.SERVER_PROTOCOL".__add__(ID)  # 输入大额资金监测系统服务端协议类型
    INPUT_APPID = "rsazj_ParamSettings_form.SERVER_APPID".__add__(ID)  # 输入AppId
    INPUT_SECRET = "rsazj_ParamSettings_form.SERVER_SECRET".__add__(ID)  # 输入SECRET
    INPUT_PRIVATEKEY = "rsazj_ParamSettings_form.SERVER_PRIVATEKEY".__add__(ID)  # 输入PRIVATEKEY
    INPUT_SMPUBLICKEY = "rsazj_ParamSettings_form.SERVER_SMPUBLICKEY".__add__(ID)  # 输入SMPUBLICKEY
    BUTTON_FKJYLX = "//*[@id='rsazj_ParamSettings_form_TRADETYPE']/div[1]".__add__(XPATH)  # 付款交易类型按钮
    BUTTON_SKJYLX = "//*[@id='rsazj_ParamSettings_form_INTRADETYPE']/div[1]".__add__(XPATH)  # 收款交易类型按钮


class ZXBmzhElement(object):
    """征信编码转换页签相关元素"""
    INPUT_BMLX = "//select[@id='pub_report_code_change_form.codeType']/option[text()='行政区划']".__add__(
        XPATH)  # 标准编码类型：行政区划
    INPUT_BM_NAME = "pub_report_code_change_form.codeName".__add__(ID)  # 标准编码名称
    INPUT_IFBSBM = "//select[@id='pub_report_code_change_form.isCodeEmpty']/option[2]".__add__(
        XPATH)  # 报送编码是否为空 1、是：option[2]  2、否：option[3]
    INPUT_MODIFY = "//select[@id='pub_report_code_change_form.isChanged']/option[2]".__add__(
        XPATH)  # 是否修改 1、是：option[2]  2、否：option[3]
    BUTTON_REFRESH = "//input[@id='pub_report_code_change_form.refresh']".__add__(XPATH)  # 刷新按钮
    INPUT_MODIFY_BSBM = "//input[@id='pub_report_code_change_list.reportCode']".__add__(
        XPATH)  # 修改报送编码


class PubHswhElement(object):
    """报表类通用--函数维护"""
    SELECT_HSLB_HSWH = "//select[@id='functionqry_form.funcType']/option[text()='{}']".__add__(
        XPATH)  # 函数维护--函数类别下拉列表，参数为函数类别名称
    SELECT_STATUS_HSWH = "//select[@id='functionqry_form.valid']/option[@value='{}']".__add__(
        XPATH)  # 函数维护--状态下拉列表，参数1为生效，-1为失效
    BUTTON_REFRESH_HSWH = "functionqry_list.refresh".__add__(ID)  # 函数维护--刷新按钮
    BUTTON_ADD_HSWH = "functionqry_list.add".__add__(ID)  # 函数维护--新增按钮
    BUTTON_MODIFY_HSWH = "//span[text()='{}']/../../td[last()-1]".__add__(XPATH)  # 函数维护--数据操作列查看/修改，根据函数名称定位
    INPUT_FUNC_NAME = "functionDetail_form.funcName".__add__(ID)  # 函数维护-新增/修改--函数名称输入框
    INPUT_FUNC_DESCRIBE = "functionDetail_form.memo".__add__(ID)  # 函数维护-新增/修改--描述输入框
    SELECT_DETAIL_HSLB_HSWH = "//select[@id='functionDetail_form.funcType']/option[text()='{}']".__add__(
        XPATH)  # 函数维护--新增/编辑--函数类别下拉列表，传入类别名称
    SELECT_DETAIL_RESTYPE_HSWH = "//select[@id='functionDetail_form.resType']/option[text()='{}']".__add__(
        XPATH)  # 函数维护--新增/编辑--返回值类型下拉列表，传入返回值类型名称
    INPUT_DETAIL_SQL_HSWH = "//textarea[@id='functionDetail_form.funcSql']".__add__(XPATH)  # 函数维护--新增/编辑--查询语句输入框
    SELECT_DETAIL_REMARK_HSWH = "//textarea[@id='functionDetail_form.remarkMsg']".__add__(XPATH)  # 函数维护--新增/编辑--备注输入框
    BUTTON_DETAIL_PARAM_HSWH = "//input[@id='functionDetail_form.analyParam']".__add__(XPATH)  # 函数维护--新增/编辑--解析参数按钮
    BUTTON_DETAIL_CHECK_HSWH = "//input[@id='functionDetail_list.check']".__add__(XPATH)  # 函数维护--新增/编辑--测试按钮
    BUTTON_DETAIL_CHECK_CHECK_HSWH = "//input[@id='checkFunc_list.check']".__add__(XPATH)  # 函数维护--新增/编辑--测试--测试按钮
    BUTTON_CLOSE_CHECK_HSWH = "//div[starts-with(@id,'LAYOUT_WIN_/SmartPage/DOM-Web@DOM_Set_CheckFunc')]/div[@class='layoutContentHeader_right']".__add__(
        XPATH)  # 函数维护--新增/编辑--测试--关闭按钮
    INPUT_DETAIL_PARAM_NAME_HSWH = "//table[@id='functionDetail_list']//tbody/tr[2]//input[@id='functionDetail_list.paraName']".__add__(
        XPATH)  # 函数维护--测试--参数列表输入参数名称(仅适用一个参数的情况）
    INPUT_DETAIL_PARAM_TYPE_HSWH = "//table[@id='functionDetail_list']//tbody/tr[2]//select[@id='functionDetail_list.paraType']/option[text()='{}']".__add__(
        XPATH)  # 函数维护--测试--参数列表输入参数类型(仅适用一个参数的情况）
    INPUT_DETAIL_PARAM_VALUE_HSWH = "//table[@id='functionDetail_list']//tbody/tr[2]//input[@id='functionDetail_list.defaultValue']".__add__(
        XPATH)  # 函数维护--测试--参数列表输入参数默认值(仅适用一个参数的情况）
    BUTTON_CLOSE_ALERT_CHECK_CHECK_HSWH = "//a[@class='aui_close']".__add__(XPATH)  # 函数维护-测试-测试-消息弹窗关闭按钮
    BUTTON_DETAIL_FORBID_HSWH = "//input[@id='functionDetail_list.close']".__add__(XPATH)  # 函数维护--新增/编辑--禁用按钮
    BUTTON_DETAIL_SAVE_HSWH = "//input[@id='functionDetail_list.save']".__add__(XPATH)  # 函数维护--新增/编辑--保存按钮
    MSG_DETAIL_HSWH = "//div[@class='aui_content']".__add__(XPATH)  # 函数详情页面，保存提示信息
    BUTTON_DETAIL_ALERT_CLOSE_HSWH = "//a[@class='aui_close']".__add__(XPATH)  # 函数添加保存弹窗关闭
    BUTTON_DETAIL_MAIN_CLOSE_HSWH = "//div[@class='layoutContentHeader_right']".__add__(XPATH)  # 函数详情主页面，右上角关闭按钮


class RsaferBscsElement(object):
    """外管局报表-报送参数"""
    BUTTON_SAVE_RSAFER = '//*[@class="button button0111"]'.__add__(XPATH)  # 保存按钮
    BUTTON_JY = '//*[@class="mainTab"]/tbody//tr/td/span[text()="强制数据校验开关"]/../../td[2]/input[1]'.__add__(
        XPATH)  # 输入 强制数据校验开关   开启：input[1]   关闭：input[2]
    BUTTON_SBSP = '//*[@class="mainTab"]/tbody//tr/td/span[text()="上报审批"]/../../td[2]/input[2]'.__add__(
        XPATH)  # 输入上报审批  是：input[1]   否：input[2]
    INPUT_DAY = "remindDayVal".__add__(ID)  # 输入报送提醒天数设置（天)
    MSG_SAVE_RSAFER = "layui-layer-setwin".__add__(ID)  # 保存成功弹窗


class RsaferWbzmyhlszElement(object):
    """外管局报表-外币折美元汇率设置"""
    CLICK_BZ_CHECK = '//*[@id="rsafer_exchangeRate_form.currencyCode"]'.__add__(XPATH)  # 点击查询条件框
    INPUT_BZ_CHECK = "//*[@id='rsafer_exchangeRate_form.currencyCode']/option[text()='{}']".__add__(
        XPATH)  # 选择币种：人民币、日元等
    BUTTON_REFRESH_WBZMY = '//*[@id="rsafer_exchangeRate_form.refresh"]'.__add__(XPATH)  # 刷新按钮
    BUTTON_ADD_WBZMY = '//*[@id="rsafer_exchangeRate_list.add"]'.__add__(XPATH)  # 新增按钮
    INPUT_BZ = '//table[@id="rsafer_exchangeRate_list"]/tbody/tr[last()]//select[@id="rsafer_exchangeRate_list.currency"]/option[text()="{}"]'.__add__(
        XPATH)  # 输入币种
    INPUT_SXRQ = '//table[@id="rsafer_exchangeRate_list"]/tbody/tr[last()]//input[@id="rsafer_exchangeRate_list.effectiveDate"]'.__add__(
        XPATH)  # 输入生效日期
    INPUT_HL_RSAFER = '//table[@id="rsafer_exchangeRate_list"]/tbody/tr[last()]//input[@id="rsafer_exchangeRate_list.rateValue"]'.__add__(
        XPATH)  # 输入汇率
    BUTTON_SAVE_WBZMY = '//*[@id="rsafer_exchangeRate_list.save"]'.__add__(XPATH)  # 保存按钮
    BUTTON_DELETE_WBZMY = '//*[@id="rsafer_exchangeRate_list.del"]'.__add__(XPATH)  # 删除按钮
    BUTTON_DELETEX_WBZMY = '//*[@id="tableCopy_rsafer_exchangeRate_list"]/td[1]/input[1]'.__add__(XPATH)  # 删除x按钮
    BUTTON_BOX_ALL_WB = '//*[@id="fixed_title"]/thead/tr/th[1]/span/span'.__add__(XPATH)  # 复选框全选
    BUTTON_BOX_ONE_WB = '//*[@id="rsafer_exchangeRate_list"]/tbody/tr[1]/td[1]/span[1]/span'.__add__(XPATH)  # 复选框单选
    ALERT_WBZMYHL = "aui_close".__add__(CLASS)  # 关闭成功弹窗


class PubZdysjlxElement(object):
    """公共页面-自定义数据类型"""
    BUTTON_SJLX_ADD = "//*[@id ='DOM_CustomDataList.add']".__add__(XPATH)  # 数据类型-新增按钮
    INPUT_SJLX_ADD_BH = "//*[@id = 'DOM_CustomDataAdd.key']".__add__(XPATH)  # 数据类型-新增页面-编号
    INPUT_SJLX_ADD_NAME = "//*[@id='DOM_CustomDataAdd.value']".__add__(XPATH)  # 数据类型-新增页面-名称
    INPUT_SJLX_ADD_SM = "//*[@id='DOM_CustomDataAdd.memo']".__add__(XPATH)  # 数据类型-新增页面-说明
    BUTTON_SJLX_ADD_SAVE = "//*[@id = 'DOM_CustomDataAdd.save']".__add__(XPATH)  # 数据类型-新增页面-保存

    CLICK_SJLX_BH = "//*[@id='DOM_CustomDataList']/tbody/tr/td/span[text()='{}']".__add__(XPATH)  # 数据类型-选择数据行-编号用{}站位

    BUTTON_SJLX_EDIT = "//*[@id='DOM_CustomDataList.edit']".__add__(XPATH)  # 数据类型-选择数据行-点击编辑按钮
    INPUT_SJLX_EDIT_NAME = "//*[@id='DOM_CustomDataEdit.value']".__add__(XPATH)  # 数据类型-选择数据行-编辑-名称
    INPUT_SJLX_EDIT_SM = "//*[@id='DOM_CustomDataEdit.memo']".__add__(XPATH)  # 数据类型-选择数据行-编辑-说明
    BUTTON_SJLX_EDIT_SAVE = "//*[@id = 'DOM_CustomDataEdit.save']".__add__(XPATH)  # 数据类型-选择数据行-编辑-保存

    BUTTON_SJLX_DEL = "//*[@id='DOM_CustomDataList.del']".__add__(XPATH)  # 数据类型-选择数据行-点击删除按钮
    MSG_SJLX_RESULT_FAIL = "//*[@class='aui_content']".__add__(XPATH)  # 数据类型-选择数据行-点击删除--"该自定义类型已被引用，不可删除！"
    DEL_SJLX_FAIL = "//button[@class='aui_state_highlight']".__add__(XPATH)  # 数据类型-选择数据行-删除失败提示确定按钮

    MSG_SJLX_RESULT_SUCCESS = "//div[@class='aui_content']".__add__(XPATH)  # 数据类型-选择数据行--"删除成功！"
    DEL_SJLX_SUCCESS_CLOSE = "//a[@class='aui_close']".__add__(XPATH)  # 数据类型-关闭删除成功提示弹窗

    BUTTON_SJLXMX_ADD = "//*[@id ='DOM_CustomDataDetailList.add']".__add__(XPATH)  # 选择数据行-数据类型明细-新增按钮
    INPUT_SJLXMX_ADD_NAME = "//*[@id = 'DOM_CustomDataDetailAdd.name_']".__add__(XPATH)  # 选择数据行-数据类型明细-新增-名称
    INPUT_SJLXMX_ADD_CSZ = "//*[@id='DOM_CustomDataDetailAdd.value_']".__add__(XPATH)  # 选择数据行-数据类型明细-新增-参数值
    BUTTON_SJLXMX_ADD_SAVE = "//*[@id='DOM_CustomDataDetailAdd.save']".__add__(XPATH)  # 选择数据行-数据类型明细-新增-保存

    SELECT_SJLXMX_ALL = "//*[@id='fixed_title']/thead/tr/th[1]/span/span".__add__(XPATH)  # 勾选数据类型明细复选框全选
    SELECT_SJLXMX_FRIST = "//*[@id='DOM_CustomDataDetailList']/tbody/tr[1]/td[1]/span[1]/span".__add__(
        XPATH)  # 勾选数据类型明细第一条

    BUTTON_SJLXMX_EDIT = "//*[@id='DOM_CustomDataDetailList.el_3']".__add__(XPATH)  # 数据类型明细-编辑按钮
    INPUT_SJLXMX_EDIT_NAME = "//*[@id='DOM_CustomDataDetailEdit.name_']".__add__(XPATH)  # 数据类型明细-编辑-名称
    INPUT_SJLXMX_EDIT_CSZ = "//*[@id='DOM_CustomDataDetailEdit.value_']".__add__(XPATH)  # 数据类型明细-编辑-参数值
    BUTTON_SJLXMX_EDIT_SAVE = "//*[@id='DOM_CustomDataDetailEdit.save']".__add__(XPATH)  # 数据类型明细-编辑-保存

    BUTTON_SJLXMX_DEL = "//*[@id='DOM_CustomDataDetailList.del']".__add__(XPATH)  # 数据类型明细-删除按钮
    MSG_SJLXMX_RESULT_SUCCESS = "//*[@class='aui_content']".__add__(XPATH)  # 数据类型明细--"删除成功！"
    DEL_SJLXMX_SUCCESS_CLOSE = "//a[@class='aui_close']".__add__(XPATH)  # 数据类型明细--关闭删除成功提示弹窗


class PubSjxwhElement(object):
    """报表类公共页面--数据项维护"""
    BUTTON_ADD_SJXWH = "dataItemsQry_list.add".__add__(ID)  # 数据项维护--新增按钮
    INPUT_DETAIL_NAME_SJXWH = "dataItemDetail_form.itemName".__add__(ID)  # 数据项维护--新增页面--数据项名称输入框
    INPUT_DETAIL_DESCRIBE_SJXWH = "dataItemDetail_form.memo".__add__(ID)  # 数据项维护--新增页面--数据项描述输入框
    SELECT_DETAIL_GROUP_SJXWH = "//select[@id='dataItemDetail_form.itemSubModel']/option[text()='{}']".__add__(
        XPATH)  # 数据项维护--新增页面--所属分类-报表分组下拉
    SELECT_DETAIL_TABLE_SJXWH = "//select[@id='dataItemDetail_form.itemDetailModel']/option[text()='{}']".__add__(
        XPATH)  # 数据项维护--新增页面--所属分类-报表分组下拉
    BUTTON_DETAIL_ADD_FUNC_SJXWH = "dataItemDetail_form.addFunc".__add__(ID)  # 数据项维护--新增页面--添加函数按钮
    BUTTON_DETAIL_ADD_ITEMS_SJXWH = "dataItemDetail_form.addItems".__add__(ID)  # 数据项维护--新增页面--添加数据项按钮
    INPUT_FUNC_FORM_NAME_SJXWH = "dataItemDetail_funcForm.func".__add__(ID)  # 数据项维护--新增页面--添加函数--函数名称查询框
    BUTTON_FUNC_FORM_REFRESH_SJXWH = "dataItemDetail_funcForm.func".__add__(ID)  # 数据项维护--新增页面--添加函数--刷新按钮
    DATA_FUNC_FORM_SJXWH = "//span[text()='{}']".__add__(XPATH)  # 数据项维护--新增页面--添加函数--函数列表--定位到数据行（传参-根据函数名称精准定位）
    DATA_FUNC_FORM_FIRST_SJXWH = "//table[@id='dataItemDetail_func']/tbody/tr[1]".__add__(
        XPATH)  # 数据项维护--新增页面--添加函数--函数列表--第一个函数
    INPUT_FUNC_FORM_PARAMS_VALUE_SJXWH = "dataItemDetail_funcParam.pv_text".__add__(
        ID)  # 数据项维护--新增页面--添加函数--函数列表--函数参数值输入框
    BUTTON_INSTER_FUNC_SJXWH = "dataItemDetail_funcParam.InsertFormula".__add__(ID)  # 数据项维护--新增页面--添加函数--插入公式按钮
    BUTTON_INSTER_ITEMS_SJXWH = "dataItemDetail_items.InsertFormula".__add__(ID)  # 数据项维护--新增页面--添加数据项--插入公式按钮
    DATA_ITEMS_FORM_SJXWH = "//span[text()='{}']".__add__(XPATH)  # 添加数据项，根据参数值（数据项名称）选择数据项
    BUTTON_FUNC_FORM_SAVE_SJXWH = "dataItemDetail_form.save".__add__(ID)  # 数据项维护--新增页面--保存按钮
    MSG_FUNC_FORM_SJXWH = "//div[@class='aui_content']".__add__(XPATH)  # 数据项维护--新增页面--弹窗提示信息


class RpbccBscsElement(object):
    """人行报表--报送参数"""
    INPUT_JGLDM_RH = 'organize'.__add__(ID)  # 输入机构类代码
    INPUT_DQDM_RH = 'area'.__add__(ID)  # 输入地区代码
    INPUT_FILE_RH = "//*[@class='mainTab']//span[text()='下载文件设置']/../../td[2]/input[1]".__add__(
        XPATH)  # 选择下载文件设置  excel：input[1]   ij：input[2]
    INPUT_SBSP_RH = "//*[@class='mainTab']//span[text()='上报审批']/../../td[2]/input[2]".__add__(
        XPATH)  # 选择上报审批  是：input[1] 否：input[2]
    BUTTON_SAVE_RH = "//*[@class='button button0111']".__add__(XPATH)  # 保存按钮


class RsafeBscsElement(object):
    """外管局--报送参数"""
    INPUT_YHFZJGDM_WGJ = "//*[@name='bankCode']".__add__(XPATH)  # 输入银行分支机构代码
    INPUT_YHFZJGMC_WGJ = "//*[@name='bankName']".__add__(XPATH)  # 输入银行分支机构名称
    INPUT_WBZHKMH_WGJ = "//*[@name='kmh']".__add__(XPATH)  # 输入外币账户科目号
    INPUT_HLZSGZ_WGJ = "//*[@class='FormUnitTable table']//td[text()='汇率折算规则']/../td[2]/input[1]".__add__(
        XPATH)  # 选择汇率折算规则  通过人民币中间价折算：input[1]   外币直接折算：input[2]
    INPUT_WGJSBHM = "//*[@name='declareNo']".__add__(XPATH)  # 输入外管局申报号码
    BUTTON_SAVE_WGJ = "//*[@class='button12 button']".__add__(XPATH)  # 保存按钮


class RsafeJybmwhElement(object):
    """外管局--交易编码维护"""
    BUTTON_ADD_WGJ = "//*[@id='U01_28_list.newRow']".__add__(XPATH)  # 新增按钮
    INPUT_JYBM_WGJ = "//*[@name='transactCode_1']".__add__(XPATH)  # 输入交易编码
    INPUT_JYMC_WGJ = "//*[@name='transactName_1']".__add__(XPATH)  # 输入交易名称
    BUTTON_SAVE_JYBMWH = "//*[@id='U01_28_list.save']".__add__(XPATH)  # 保存按钮
    BUTTON_CLOSE_WGJ = "//*[@name='selectElement_1']".__add__(XPATH)  # 关闭x按钮
    BUTTON_DELETE_JYBMWH = "U01_28_list.deleteData".__add__(ID)  # 删除按钮
    CHECK_BOX_ALL_WGJ = "//*[@onclick='clickThCheckBox(this)']".__add__(XPATH)  # 全选复选框
    CHECK_BOX_ONE_WGJ = "//*[@id='mainTable']//input[@name='transactCode' and @value='{}']/../../td[1]/img".__add__(
        XPATH)  # 单选复选框


class RmbtdCbmbglElement(object):
    """征信--财报模板管理"""
    BUTTON_REFRESH_CB = "//*[@class='button31 button']".__add__(XPATH)  # 刷新按钮
    BUTTON_SYKHMB = "div[class^='layui-table-cell laytable-cell']>label".__add__(CSS)  # 使用客户模板
    QZGX_TEXT_NO = "//*[contains(@class,'layui-table-cell laytable-cell')]/input[@value='{}']/../span".__add__(
        XPATH)  # 取值关系--未使用客户模板
    QZGX_TEXT_YES = "//*[contains(@class,'layui-table-cell laytable-cell')]/input[@value='{}']/../a".__add__(
        XPATH)  # 取值关系--使用客户模板
    BUTTON_SYKHMB_OK = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 使用客户模板--确认按钮
    INPUT_SJX_NAME = "//*[@name='dataItemName']".__add__(XPATH)  # 输入数据项名称
    RMBTD_CB_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web-ROOT/page/reportSendManage/reportTempManage/detailConfig')]".__add__(
        XPATH)  # 征信财报frame
    INPUT_QZDYGZB = "//*[contains(@class,'layui-table-cell laytable-cell')]/input[@value='{}']/../../../td[3]//input".__add__(
        XPATH)  # 输入取值单元格坐标
    BUTTON_SAVE_CB = "//*[@class='button2 button submitBtn']".__add__(XPATH)  # 保存按钮


class RAMLRSBscsElement(object):
    """反洗钱--报送参数"""
    BUTTON_SAVE_RAMLRS = "//*[@id='param_Settings_list.save']".__add__(XPATH)  # 保存按钮
    INPUT_GSBM_RAMLRS = "//*[@id='param_Settings_list.paramValue_1']/option[text()='{}']".__add__(XPATH)  # 可疑交易默认归属部门
    INPUT_BGJGBM_RAMLRS = "//*[@id='param_Settings_list']/tbody//span[text()='报告机构编码']/../../td[2]/span[1]/input".__add__(
        XPATH)  # 报告机构编码
    INPUT_SJBLJ_RAMLRS = "//*[@id='param_Settings_list']/tbody//span[text()='数据包文件保存路径']/../../td[2]/span[1]/input".__add__(
        XPATH)  # 数据包文件保存路径
    INPUT_ZJDQTXTS_RAMLRS = "//*[@id='param_Settings_list']/tbody//span[text()='证件到期提醒天数']/../../td[2]/span[1]/input".__add__(
        XPATH).__add__(XPATH)  # 证件到期提醒天数
    BUTTON_CLOSE_RAMLRS = "//*[@class='aui_close']".__add__(XPATH)  # 保存成功关闭按钮


class RLCTSBscsElement(object):
    """大额监控--报送参数"""
    INPUT_JEDW_DE = "//*[@id='reporting_parameters_form.amount_unit']/option[text()='{}']".__add__(XPATH)  # 金额单位
    INPUT_JESXED_DE = "reporting_parameters_form.amount".__add__(ID)  # 金额筛选额度
    INPUT_DEZJBM_DE = "reporting_parameters_form.lcts_code".__add__(ID)  # 大额资金编码
    INPUT_DEZJSJBBBH_DE = "reporting_parameters_form.big_data_page_code".__add__(ID)  # 大额资金数据包版本号
    INPUT_DRZFZJE_DE = "reporting_parameters_form.total_data_page_code".__add__(ID)  # 当日支付总金额编码
    INPUT_DRZFZJESJBBBH_DE = "reporting_parameters_form.data_page_type".__add__(ID)  # 当日支付总金额数据包版本号
    INPUT_DEWJSCDZ_DE = "reporting_parameters_form.uploadUrl".__add__(ID)  # 大额文件上传地址
    INPUT_DYJKYHM_DE = "reporting_parameters_form.uploadUser".__add__(ID)  # 调用接口用户名
    INPUT_DYJKMM_DE = "reporting_parameters_form.uploadPassword".__add__(ID)  # 调用接口密码
    BUTTON_ZDWJGXTZRY_DE = "reporting_parameters_form.notifyNameStr".__add__(ID)  # 制度文件更新通知人员
    INPUT_ZDWJGXTZRY_DE = "//*[@class='xm-input xm-search-input']".__add__(XPATH)  # 输入通知人员
    BUTTON_CHOICE_ALL = "//*[@class='toolbar-tag']/span[text()='全选']".__add__(XPATH)  # 全选通知人员
    INPUT_ZDWJXZDZ_DE = "reporting_parameters_form.downFilesGetUrl".__add__(ID)  # 制度文件下载地址
    INPUT_ZDWJQDCXDZ_DE = "reporting_parameters_form.downFilesListUrl".__add__(ID)  # 制度文件清单查询地址
    INPUT_RZWJCXDZ_DE = "reporting_parameters_form.synPushDtUrl".__add__(ID)  # 日志文件查询地址
    BUTTON_SAVE_BSCS_DE = "reporting_parameters_form.save".__add__(ID)  # 保存按钮
    BUTTON_XL_DE = "//*[@class='xm-icon']".__add__(XPATH)  # 选择通知人员


class RLCTSZjytszElement(object):
    """大额监控--资金用途设置"""
    BUTTON_ADD_DEJK = "proceeds_use_list.add".__add__(ID)  # 新增
    BUTTON_SAVE_DEJK = "proceeds_use_list.save".__add__(ID)  # 保存
    BUTTON_DELETE_DEJK = "proceeds_use_list.del".__add__(ID)  # 删除
    INPUT_ZJYTBM_DE = '//table[@id="proceeds_use_list"]/tbody/tr[last()]//input[@id="proceeds_use_list.user_code"]'.__add__(
        XPATH)  # 输入资金用途编码
    INPUT_ZJYTBMHY_DE = "//table[@id='proceeds_use_list']/tbody/tr[last()]//input[@id='proceeds_use_list.user_explain']".__add__(
        XPATH)  # 输入资金用途编码含义
    BUTTON_BOX_ONE = "//table[@id='proceeds_use_list']/tbody//input[@value='{}']/../../../td/span/span".__add__(
        XPATH)  # 单选复选框


class PubBssqElement_rlcts_ramlrs(object):
    """大额监控、反洗钱公共页面--报送授权"""
    BUTTON_REFRESH_BSSQ_DEFXQ = "dom_auth_report_from.refresh".__add__(ID)  # 刷新按钮
    INPUT_RYMC_DEFXQ = "dom_auth_report_from.userName".__add__(ID)  # 输入人员名称
    BUTTON_SQ_DEFXQ = "//*[@id='dom_auth_report_list']/tbody/tr[1]//a[@id='dom_auth_report_list.authorize']".__add__(
        XPATH)  # 点击授权按钮
    BUTTON_BOX_DEFXQ = "//*[@id='multiTree_tree_1']/div[1]//span[@class='checkbox_bg']".__add__(XPATH)  # 勾选复选框
    BUTTON_SAVE_DEFXQ = "DOM_auth_rpt_admSRight_form.save".__add__(ID)  # 保存按钮
    TXT_BSSQ_FLAG_DEFXQ = "//span[text()='征信权限1']/../../td[3]/span".__add__(XPATH)  # 报送授权列表中的授权标志文本值
    SQBZ_TEXT = "//*[@id='dom_auth_report_list']//tbody/tr[1]/td[3]/span".__add__(
        XPATH)  # 授权标志


class PubSplcElement_rlcts_ramlrs(object):
    """大额监控、反洗钱公共页面--审批流程"""
    INPUT_USER_SPLC = "//*[@id='reportBizFlow_Form.uno']/option[text()='{}']".__add__(XPATH)  # 选择用户
    BUTTON_BOX_FXK_DEFXQ = "//*[@id='fixed_title']/thead//span[@class='checkbox_bg']".__add__(XPATH)  # 选择复选框
    BUTTON_PLXG_DEFXQ = "reportBizFlow_List.batchModify".__add__(ID)  # 批量修改
    INPUT_SPLC_DEFXQ = "//*[@id='reportBizFlow_List.bizCode']/option[text()='{}']".__add__(XPATH)  # 选择审批流程
    BUTTON_SAVE_SPLC_DEFXQ = "batchBizFlowForm.save".__add__(ID)  # 保存按钮
    BUTTON_REFRESH_SPLC_DEFXQ = "reportBizFlow_Form.refresh".__add__(ID)  # 刷新按钮


class RAMLRSKytzszElement(object):
    """反洗钱--可疑特征设置"""
    BUTTON_ADD_RAMLRS_KY = "KYTZSettings_list.add".__add__(ID)  # 新增按钮
    BUTTON_DETELE_RAMLRS_KY = "KYTZSettings_list.del".__add__(ID)  # 删除按钮
    BUTTON_SAVE_RAMLRS_KY = "KYTZSettings_list.save".__add__(ID)  # 保存按钮
    INPUT_KYJYTZDM_KY = "//*[@id='KYTZSettings_list']/tbody/tr[last()]//input[@id='KYTZSettings_list.feaCode']".__add__(
        XPATH)  # 可疑交易特征代码
    INPUT_KYJYTZSM_KY = "//*[@id='KYTZSettings_list']/tbody/tr[last()]//input[@id='KYTZSettings_list.feaDesc']".__add__(
        XPATH)  # 可疑交易特征说明
    INPUT_SZLXDM_KY = "//*[@id='KYTZSettings_list']/tbody/tr[last()]//input[@id='KYTZSettings_list.crimeCode']".__add__(
        XPATH)  # 涉罪类型代码
    INPUT_JCBZM_KY = "//*[@id='KYTZSettings_list']/tbody/tr[last()]//input[@id='KYTZSettings_list.monitorCode']".__add__(
        XPATH)  # 监测标准码
    INPUT_JSZB_KY = "//*[@id='KYTZSettings_list']/tbody/tr[last()]//input[@id='KYTZSettings_list.normCode']".__add__(
        XPATH)  # 技术指标
    BUTTON_FXK_ALL_KY = "//*[@id='fixed_title']//span[@class='checkbox_bg']".__add__(XPATH)  # 涉罪类型代码、监测标准码复选框all
    BUTTON_FXK_ONE_SZ = "//*[@id='choice_msgCriminousType_list']/tbody//span[text()='{}']/../..//span[@class='checkbox_bg']".__add__(
        XPATH)  # 涉罪类型代码复选框ONE
    BUTTON_OK_SZ = "choice_msgCriminousType_list.save".__add__(ID)  # 涉罪类型代码-确定按钮
    BUTTON_FXK_ONE_JC = "//*[@id='choice_msgMonitorType_list']/tbody//span[text()='{}']/../..//span[@class='checkbox_bg']".__add__(
        XPATH)  # 监测标准码复选框ONE
    BUTTON_OK_JC = "choice_msgMonitorType_list.save".__add__(ID)  # 监测标准码-确定按钮
    BUTTON_FXK_ALL_KYJYTZ = "//*[@id='KYTZSettings_list']/tbody//span/input[@value='{}']/../../..//span[contains(@class,'checkbox_bg')]".__add__(
        XPATH)  # 可疑交易特征复选框ONE


class RAMLRSJkzbszElement(object):
    """反洗钱--监控指标设置"""
    BUTTON_REFRESH_JK = "monitor_Index_qry.refresh".__add__(ID)  # 刷新按钮
    QUERY_JCZB_JK = "//*[@id='monitor_Index_qry.paramType']/option[text()='{}']".__add__(XPATH)  # 查询条件-监测指标
    QUERY_CSMC_JK = "monitor_Index_qry.paramName".__add__(ID)  # 查询条件-参数名称
    BUTTON_SAVE_JK = "monitor_Index_list.save".__add__(ID)  # 保存按钮
    BUTTON_SBFW_CSZ_JK = "//*[@id='monitor_Index_list']/tbody//span[text()='{}']/../..//div[@class='DroTreeIMG']".__add__(
        XPATH)  # 上报范围-选择参数值
    FXK_SBFW_JYLX_NO_JK = "//*[@id='SmartPage_DropTree.monitor_Index_list_pullValue_tree_1']/div/nobr/span[@class='checkbox_bg_f']".__add__(
        XPATH)  # 上报范围-取消勾选交易类型复选框
    FXK_SBFW_JYLX_YES_JK = "//*[@id='SmartPage_DropTree.monitor_Index_list_pullValue_tree_1']/div/nobr/span[@class='checkbox_bg']".__add__(
        XPATH)  # 上报范围-勾选交易类型复选框
    LJJYJE_CSZ_JK = "//*[@class='rowCss1']//span[text()='累计交易金额']/../..//input[@id='monitor_Index_list.paramValue']".__add__(
        XPATH)  # 累计交易金额-参数值
    DBJYJE_CSZ_JK = "//*[@class='rowCss2']//span[text()='单笔交易金额']/../..//input[@id='monitor_Index_list.paramValue']".__add__(
        XPATH)  # 单笔交易金额-参数值
    BUTTON_OK_JK = "//*[@class='aui_state_highlight']".__add__(XPATH)  # 不能输入小于0的弹窗确认按钮


class RAMLRSSbwdszElement(object):
    """反洗钱--上报网点设置"""
    QUERY_WDDM_SBWD = "organ_settings_form.organNo".__add__(ID)  # 查询条件-网点代码
    QUERY_WDMC_SBWD = "organ_settings_form.organName".__add__(ID)  # 查询条件-网点名称
    BUTTON_REFRESH_SBWD = "organ_settings_list.refresh".__add__(ID)  # 刷新按钮
    BUTTON_ADD_SBWD = "organ_settings_list.add".__add__(ID)  # 新增按钮
    BUTTON_SAVE_SBWD = "organ_settings_list.save".__add__(ID)  # 保存按钮
    BUTTON_DELETE_SBWD = "organ_settings_list.del".__add__(ID)  # 删除按钮
    INPUT_WDDM_SBWD = "//*[@id='organ_settings_list']/tbody/tr[last()]//input[@id='organ_settings_list.organNo']".__add__(
        XPATH)  # 输入网点代码
    INPUT_WDMC_SBWD = "//*[@id='organ_settings_list']/tbody/tr[last()]//input[@id='organ_settings_list.organName']".__add__(
        XPATH)  # 输入网点名称
    INPUT_HYLB_SBWD = "//*[@id='organ_settings_list']/tbody/tr[last()]//select[@id='organ_settings_list.organCalling']/option[text()='{}']".__add__(
        XPATH)  # 选择行业类别
    FXK_ONE_SBWD = "//*[@id='organ_settings_list']/tbody//input[@value='{}']/../../../td[1]//span/span".__add__(
        XPATH)  # 单个复选框


class RN1104BscsElement(object):
    """1104报送参数页签相关元素"""
    SET_QZSJJJKG_YES = "//input[@id='valideSwitchOpen']".__add__(XPATH)  # 强制数据校验开关--是
    SET_QZSJJJKG_NO = "//input[@id='valideSwitchClose']".__add__(XPATH)  # 强制数据校验开关--否
    SET_BJQS_YES = "//input[@id='reapprovalSwitchOpen']".__add__(XPATH)  # 表间取数数据变化时重新审批开关	--是
    SET_BJQS_NO = "//input[@id='reapprovalSwitchClose']".__add__(XPATH)  # 表间取数数据变化时重新审批开关	--否
    SET_SBSP_YES = "//input[@id='reportBizFlagY']".__add__(XPATH)  # 上报审批--是
    SET_SBSP_NO = "//input[@id='reportBizFlagN']".__add__(XPATH)  # 上报审批--否
    BUTTON_SAVE_1104 = "//*[@class='button button0111']".__add__(XPATH).__add__(XPATH)  # 保存


class RAMLRSKhzlwhElement(object):
    """反洗钱--客户资料维护"""
    QUERY_KHBH_KHZL = "client_manage_form.cliNo".__add__(ID)  # 客户编号
    QUERY_KHMC_KHZL = "client_manage_form.cliName".__add__(ID)  # 客户名称
    BUTTON_REFRESH_KHZL = "client_manage_list.refresh".__add__(ID)  # 刷新按钮
    BUTTON_XQ_KHZL = "//*[@id='client_manage_list']//span[text()='12345']/../../td[3]/a".__add__(XPATH)  # 详情按钮
    INPUT_NAME_KHZL = "client_info_form.cliName".__add__(ID)  # 客户详情-名称
    INPUT_ZJLX_KHZL = "client_info_form.cliCertificateTypeName".__add__(ID)  # 客户详情-证件类型
    INPUT_XZZJLX_KHZL = "//*[@id='div_gridtable']//tbody//a[text()='{}']".__add__(XPATH)  # 客户详情-证件类型-选择证件类型
    INPUT_ZMWJHM_KHZL = "client_info_form.cliCertificateNo".__add__(ID)  # 客户详情-证明文件号码
    INPUT_FR_ZMWJYXQ_KHZL = "client_info_form.cliJurCertificateEndDate".__add__(ID)  # 客户详情-法人证明文件有效期
    INPUT_GDSJR_ZMWJYXQ_KHZL = "client_info_form.cliPriCertificateEndDate".__add__(ID)  # 客户详情-股东或实际控制人信息-证明文件有效期
    BUTTON_SAVE_KHZL = "client_info_form.save".__add__(ID)  # 客户详情-保存按钮
    TEXT_ZJ_KHZL = "//*[@class='DefaultTopToolBar']/tbody//td[1]/span".__add__(XPATH)  # 总计条数信息
    BUTTON_CLEAR_KHZL = "dpClearInput".__add__(ID)  # 日期插件中的清空按钮


class PubXsjdpzElement(object):
    """报表类公共页面--小数精度配置"""
    INPUT_XSJDPZ_BSNRMC = "decimalConfigForm.bsnrmc".__add__(ID)  # 小数精度配置--报送内容名称
    BUTTON_XSJDPZ_REFRESH = "decimalConfigForm.refresh".__add__(ID)  # 小数精度配置--刷新按钮

    BUTTON_TYXSWSPZ = "decimalConfigList.decimalSet".__add__(ID)  # 小数精度配置--通用小数位数配置按钮
    INPUT_TYXSWSPZ_SZ_TYJSXSWS = "currencyDecimalSetForm.comCalcDigitsNum".__add__(ID)  # 小数精度配置--通用小数位数配置-数值-通用计算小数位数
    INPUT_TYXSWSPZ_SZ_TYXSXSWS = "currencyDecimalSetForm.comShowDigitsNum".__add__(ID)  # 小数精度配置--通用小数位数配置-数值-通用显示小数位数
    INPUT_TYXSWSPZ_BFB_TYJSXSWS = "currencyDecimalSetForm.comCalcDigitsPercent".__add__(
        ID)  # 小数精度配置--通用小数位数配置-百分比-通用计算小数位数
    INPUT_TYXSWSPZ_BFB_TYXSXSWS = "currencyDecimalSetForm.comShowDigitsPercent".__add__(
        ID)  # 小数精度配置--通用小数位数配置-百分比-通用显示小数位数
    INPUT_TYXSWSPZ_je_TYJSXSWS = "currencyDecimalSetForm.comCalcDigitsMoney".__add__(ID)  # 小数精度配置--通用小数位数配置-金额-通用计算小数位数
    INPUT_TYXSWSPZ_je_TYXSXSWS = "currencyDecimalSetForm.comShowDigitsMoney".__add__(ID)  # 小数精度配置--通用小数位数配置-金额-通用显示小数位数
    INPUT_TYXSWSPZ_ll_TYJSXSWS = "currencyDecimalSetForm.comCalcDigitsRate".__add__(ID)  # 小数精度配置--通用小数位数配置-利率-通用计算小数位数
    INPUT_TYXSWSPZ_ll_TYXSXSWS = "currencyDecimalSetForm.comShowDigitsRate".__add__(ID)  # 小数精度配置--通用小数位数配置-利率-通用显示小数位数

    BUTTON_TYXSWSPZ_SAVE = "currencyDecimalSetForm.save".__add__(ID)  # 小数精度配置--通用小数位数配置-保存
    MSG_TYXSWSPZ_SAVE_SUCCESS = "//*[@class='aui_content']".__add__(XPATH)  # 通用小数位数配置-保存信息-"保存成功"
    CLOSE_TYXSWSPZ_SAVE_SUCCESS = "//a[@class='aui_close']".__add__(XPATH)  # 通用小数位数配置--关闭保存成功提示弹窗
    CLOSE_TYXSWSPZ = "//*[@class='layoutContentHeader_right']".__add__(XPATH)  # 关闭通用小数位数配置页面
    MSG_TYXSWSPZ_SJLBXS = "//*[@id='imgTitle']".__add__(XPATH)  # 数据列表表头显示通用小数位数信息

    BUTTON_XSJDPZ_EDIT = "decimalConfigList.oper".__add__(ID)  # 小数精度配置-编辑
    BUTTON_XSJDPLPZ_REFESH = "refreshButton".__add__(ID)  # 小数精度配置-编辑-小数精度批量配置-刷新
    BUTTON_XSJDPLPZ_ALTER = "//*[@id='updateButton' and @value='{}']".__add__(XPATH)  # 小数精度配置-编辑-小数精度批量配置-修改小数位数
    MSG_XSJDPLPZ_ALTER_NULL = "//*[@class='aui_content']".__add__(
        XPATH)  # 小数精度批量配置-未勾选单元格-点击修改小数位数-"请选择需要修改的数据项。"弹窗信息
    XSJDPLPZ_ALTER_NULL_OK = "//button[@class=' aui_state_highlight']".__add__(
        XPATH)  # 小数精度批量配置-未勾选单元格-点击修改小数位数-弹窗信息点击确认

    CHOOSE_XSJDPLPZ_DYG = "//div[@ri='{}' and @ci='{}']".__add__(XPATH)  # 小数精度批量配置-选择单元格{}占位-
    CHOOSE_XSJDPLPZ_ALTER_SJXLX = "//select[@id='itemDecimalForm.itemType']/option[text()='{}']".__add__(
        XPATH)  # 小数精度批量配置-修改小数位数-选择数据类型-用{}站位
    INPUT_XSJDPLPZ_ALTER_JSXSWS = "//input[@id='itemDecimalForm.calcDigits']".__add__(XPATH)  # 小数精度批量配置-修改小数位数-计算小数位数
    INPUT_XSJDPLPZ_ALTER_XSXSWS = "//input[@id='itemDecimalForm.showDigits']".__add__(XPATH)  # 小数精度批量配置-修改小数位数-显示小数位数
    BUTTON_XSJDPLPZ_ALTER_SAVE = "//input[@id='itemDecimalForm.save']".__add__(XPATH)  # 小数精度批量配置-修改小数位数-保存按钮
    MSG_XSJDPLPZ_DYG = "//div[@ri='{}' and @ci='{}']/div[@class='ss-vcell']".__add__(XPATH)  # 小数精度批量配置-单元格内信息


class RSAFEtbrwhElement(object):
    """外管局--填报人维护"""
    RSAFEtbrwhXZ = "U01_28_list.newRow".__add__(ID)  # 新增
    RSAFEtbrwhSC = "U01_28_list.deleteData".__add__(ID)  # 删除
    RSAFEtbrwhBC = "U01_28_list.save".__add__(ID)  # 保存
    RSAFEtbrwh_ALL = '//*[@id="mainTable"]/tbody/tr[1]/th[1]/img'.__add__(XPATH)  # 全选
    RSAFEtbrwh_ONE = '//*[@id="mainTable"]/tbody/tr[2]/td[1]/img'.__add__(XPATH)  # 单选
    INPUT_TBRZH = '//*[@id="contactsCode_1"]'.__add__(XPATH)  # 填报人账号（登录用户编号）
    INPUT_TBRMC = '//*[@id="contactsName_1"]'.__add__(XPATH)  # 填报人名称（登录用户名称）
    INPUT_TBRDH = '//*[@id="contactsPhone_1"]'.__add__(XPATH)  # 填报人电话


class RAMLRSSkhmdszElement(object):
    """反洗钱涉恐黑名单设置"""
    QUERY_SKZZHRYMC_HMD = "terro_Black_form.terroName".__add__(ID)  # 查询条件-涉恐组织或人员名称
    QUERY_ZJHM_HMD = "terro_Black_form.idNum".__add__(ID)  # 查询条件-证件号码
    BUTTON_REFRESH_HMD = "terro_Black_form.refresh".__add__(ID)  # 刷新按钮
    BUTTON_ADD_HMD = "terro_Black_list.add".__add__(ID)  # 新增按钮
    INPUT_SKZZHRYMC_HMD = "//*[@id='terro_Black_list']/tbody/tr[last()]//input[@id='terro_Black_list.terroName']".__add__(
        XPATH)  # 新增-涉恐组织或人员名称
    INPUT_ZJHM_HMD = "//*[@id='terro_Black_list']/tbody/tr[last()]//input[@id='terro_Black_list.idNum']".__add__(
        XPATH)  # 新增-证件号码
    INPUT_BZ_HMD = "//*[@id='terro_Black_list']/tbody/tr[last()]//input[@id='terro_Black_list.memo']".__add__(
        XPATH)  # 新增-备注
    BUTTON_SAVE_HMD = "terro_Black_list.save".__add__(ID)  # 保存按钮
    FXK_ONE_HMD = "//*[@id='terro_Black_list.terroName' and @value = '{}']/../../..//span[@class = 'checkbox_bg']".__add__(
        XPATH)  # 勾选单条数据复选框
    BUTTON_DELETE_HMD = "terro_Black_list.del".__add__(ID)  # 删除按钮


class RRMBTDBscsElement(object):
    """征信报送参数页签相关元素"""
    INPUT_ZXBSFS = "//*[@id='prpMode_select']/option[text()='手动报送']".__add__(XPATH)
    # 征信报送方式  1、征信中心直连报送  2、手动报送   3、金电接口报送3.4  4、金电接口报送3.5
    # 手动报送
    INPUT_CCFKWJDML = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='存储反馈文件的目录']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 存储反馈文件的目录
    INPUT_WJBDBCGLJ = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='文件本地保存根路径']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 文件本地保存根路径
    INPUT_SFTPIP = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='sftp服务器ip']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # sftp服务器ip
    INPUT_SFTPDK = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='sftp服务器端口']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # sftp服务器端口
    INPUT_SFTPYHM = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='sftp用户名']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # sftp用户名
    INPUT_SFTPMM = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='sftp密码']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # sftp密码
    INPUT_FSML = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='发送目录']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 发送目录
    INPUT_SJTGJGQDM = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='数据提供机构区段码']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 数据提供机构区段码
    INPUT_URL = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='人行预处理程序URL']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 人行预处理程序URL
    INPUT_ZXZXDM = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='征信中心代码']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 征信中心代码
    INPUT_YWGLJGDM = "//input[@id='RMBTD_DM_MBTD_RPPCD_list.keyName' and @value='业务管理机构代码']/../../..//input[@id='RMBTD_DM_MBTD_RPPCD_list.value']".__add__(
        XPATH)  # 业务管理机构代码
    SET_ZXSBSP_YES = "//input[@id='reportBizFlagY']".__add__(XPATH)  # 上报审批--是
    SET_ZXSBSP_NO = "//input[@id='reportBizFlagN']".__add__(XPATH)  # 上报审批--否
    SET_RGQR_YES = "//input[@id='confirmButtonFlagY']".__add__(XPATH)  # 人工确认成功--是
    SET_RGQR_NO = "//input[@id='confirmButtonFlagN']".__add__(XPATH)  # 人工确认成功--否
    BUTTON_SAVE_ZX = "//*[@class='button12 button']".__add__(XPATH).__add__(XPATH)  # 保存
    MSG_ADD_RESULT_zx = "//*[@class='aui_content']".__add__(XPATH)  # 新增成功提示信息
    SUCCESS_CLOSE_zx = "//a[@class='aui_close']".__add__(XPATH)  # 关闭弹窗
    MSG_SB_ZX = "//*[@id='pub_report_page_list.total']".__add__(XPATH)
    MSG_CX_ZX = "pub_result_page_list.total".__add__(ID)


class PubLsbbElement(object):
    """报表类历史报表页签相关元素"""
    QUERY_BSPL_LSBB = "//*[@class='search_input_input']".__add__(XPATH)  # 查询条件-报送频率
    INPUT_BSPL_LSBB = "//*[@class='search_input_table']//td[text()='{}']".__add__(XPATH)  # 查询条件-选择频率
    QUERY_BSRQ_LSBB = "//*[@class='layui-input']".__add__(XPATH)  # 查询条件-报送日期
    BUTTON_REFRESH_LSBB = "//*[@class='button31 button']".__add__(XPATH)  # 刷新按钮
    BUTTON_IMPORT_LSBB = "importButton".__add__(ID)  # 导入按钮
    G0800_PATH = "D:\\DcabAtuoTest\\data\\历史报表\\G0800-231-银行业金融机构引进外商投资情况表.xls"
    A1411_PATH = "D:\\DcabAtuoTest\\data\\历史报表\\A1411金融机构资产负债项目表.xls"
    PHJR01_PATH = "D:\\DcabAtuoTest\\data\\历史报表\\PHJR01-普惠金融工作月报表.xls"
    ALERT_OK_LSBB = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 弹窗确认关闭按钮


class RAMLLTBscsElement(object):
    """反洗钱大额报送参数相关元素"""
    INPUT_BGJGBM_CSZ = "//span[text()='报告机构编码']/../../td/span/input[@name='repOrganNo']".__add__(
        XPATH)  # 报告机构编码-参数值
    BUTTON_SAVE = "//input[@class='button button0111']".__add__(XPATH)  # 保存
    MSG_BGJGBM_CSZ = "//span[text()='报告机构编码']/../../td/span/input[@value='{}']".__add__(
        XPATH)  # 断言：报告机构编码-参数值


class RAMLLTJkzbSzElement(object):
    """反洗钱大额监控指标设置页面相关元素"""
    INPUT_JCZBMS = "//div[text()='{}']/../..//div[text()='上报范围']/../..//textarea[@name='monitorMemo']".__add__(
        XPATH)  # 各监测标准码的-监测指标描述,  使用占位符{}，可传参监测标准码：0501，0502，0503，0504
    MSG_JCZBMS = "//div[text()='{}']/../..//div[text()='上报范围']/../..//textarea[@name='monitorMemo']".__add__(
        XPATH)  # 断言-监测指标描述, 可传参监测标准码：0501，0502，0503，0504

    BUTTON_SBFW_CSZ = "//div[text()='{}']/../..//div[text()='上报范围']/../../td/div/div/xm-select/i".__add__(
        XPATH)  # 各监测标准码的--上报范围-参数值--下拉列表，监测标准码使用占位符{}，可传参：0501，0502，0503，0504
    INPUT_SBFW_CSZ = "//div[text()='{}']/../..//div[text()='上报范围']/../../td/div/div/xm-select/div/div/div/input".__add__(
        XPATH)  # 各监测标准码的--上报范围-参数值--下拉列表输入查询，监测标准码使用占位符{}
    SELECT_INPUT_SBFW_CSZ = "//div[text()='{}']/../..//div[text()='上报范围']/../..//div[text()='{}']/../i[@class='xm-option-icon xm-iconfont xm-icon-duox']".__add__(
        XPATH)  # 各监测标准码的--上报范围-参数值--下拉列表输入并勾选，监测标准码使用第一个占位符{}；第二个{}传输入的参数值
    MSG_SELECT_INPUT_SBFW_CSZ = "//div[text()='{}']/../..//div[text()='上报范围']/../..//span[text()='{}']".__add__(
        XPATH)  # 断言--各监测标准码的--上报范围-参数值,监测标准码使用第一个占位符{}；第二个{}参数值

    DEL_SBFW_CSZ = "//div[text()='{}']/../..//div[text()='上报范围']/../..//span[text()='{}']/../i".__add__(
        XPATH)  # 各监测标准码的--上报范围-参数值--删除添加的参数值，监测标准码使用第一个占位符{}；第二个{}传删除的参数值

    INPUT_LJJYJE_CNY_CSZ = "//div[text()='{}']/../..//div[text()='累计交易金额（人民币）']/../../td/div/input[@class='layui-input currency']".__add__(
        XPATH)  # 各监测标准码的--累计交易金额（人民币）-参数值，监测标准码使用占位符{}
    MSG_INPUT_LJJYJE_CNY_CSZ = "//div[text()='{}']/../..//div[text()='累计交易金额（人民币）']/../..//input[@value='{}']".__add__(
        XPATH)  # 断言--各监测标准码的--累计交易金额（人民币）-参数值,监测标准码使用第一个占位符{}；第二个{}参数值

    INPUT_DBJYJE_CNY_CSZ = "//div[text()='{}']/../..//div[text()='单笔交易金额（人民币）']/../../td/div/input[@class='layui-input currency']".__add__(
        XPATH)  # 各监测标准码的--单笔交易金额（人民币）--参数值，监测标准码使用占位符{}
    MSG_INPUT_DBJYJE_CNY_CSZ = "//div[text()='{}']/../../td/div[text()='单笔交易金额（人民币）']/../..//input[@value='{}']".__add__(
        XPATH)  # 断言--各监测标准码的--单笔交易金额（人民币）-参数值,监测标准码使用第一个占位符{}；第二个{}参数值

    INPUT_LJJYJE_USA_CSZ = "//div[text()='{}']/../../td/div[text()='累计交易金额（美元）']/../../td/div/input[@class='layui-input currency']".__add__(
        XPATH)  # 各监测标准码的--累计交易金额（美元）-参数值，监测标准码使用占位符{}
    MSG_INPUT_LJJYJE_USA_CSZ = "//div[text()='{}']/../../td/div[text()='累计交易金额（美元）']/../..//input[@value='{}']".__add__(
        XPATH)  # 断言--各监测标准码的--累计交易金额（美元）-参数值,监测标准码使用第一个占位符{}；第二个{}参数值

    INPUT_DBJYJE_USA_CSZ = "//div[text()='{}']/../../td/div[text()='单笔交易金额（美元）']/../../td/div/input[@class='layui-input currency']".__add__(
        XPATH)  # 各监测标准码的--单笔交易金额（美元）-参数值，监测标准码使用占位符{}，可传参：0501，0502，0503，0504
    MSG_INPUT_DBJYJE_USA_CSZ = "//div[text()='{}']/../../td/div[text()='单笔交易金额（美元）']/../..//input[@value='{}']".__add__(
        XPATH)  # 断言--各监测标准码的--单笔交易金额（美元）-参数值,监测标准码使用第一个占位符{}；第二个{}参数值

    BUTTON_CZ_QY = "//div[text()='{}']/../../td/div[text()='上报范围']/../../td/div/div/i".__add__(
        XPATH)  # 各监测标准码的--操作-启用按钮

    BUTTON_SAVEMONITOR = "saveMonitor".__add__(ID)  # 保存按钮


class RirrBscsElement(object):
    """利率报备R表--报送参数"""
    RIRR_SBSP_YES = "//input[@id='reportBizFlagY']".__add__(XPATH)  # 上报审批--是
    RIRR_SBSP_NO = "//input[@id='reportBizFlagN']".__add__(XPATH)  # 上报审批--否
    RIRR_YHKJ_YES = "//input[@id='fillExplainCustFlagY']".__add__(XPATH)  # 用户口径填报说明是否展示--是
    RIRR_YHKJ_NO = "//input[@id='fillExplainCustFlagN']".__add__(XPATH)  # 用户口径填报说明是否展示--否
    BUTTON_SAVE_RIRR = "//*[@class='button button0111']".__add__(XPATH)  # 保存按钮
