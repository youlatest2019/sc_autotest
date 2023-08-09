from Common.common_map import *


class FxgkMainMenueElement(object):
    """风险管控主菜单"""
    FXGK_MENUE = "//span[text()='风险管控']".__add__(XPATH)  # 主菜单--风险管控
    FXQZB_TAB = "//a[@menuid='BIRMFXQ010201']".__add__(XPATH)  # 可疑交易甄别
    FXQZB_TAG = "//li[@menuid='BIRMFXQ010201']/a".__add__(XPATH)  # 可疑交易甄别标题菜单
    FXQSP_TAB = "//a[@menuid='BIRMFXQ010203']".__add__(XPATH)  # 可疑交易审批
    FXQSP_TAG = "//li[@menuid='BIRMFXQ010203']/a".__add__(XPATH)  # 可疑交易审批标题菜单
    FXQBS_TAB = "//a[@menuid='BIRMFXQ010202']".__add__(XPATH)  # 可疑交易报送
    FXQBS_TAG = "//li[@menuid='BIRMFXQ010202']/a".__add__(XPATH)  # 可疑交易报送标题菜单
    FXQCX_TAB = "//a[@menuid='BIRMFXQ010204']".__add__(XPATH)  # 可疑交易查询
    FXQCX_TAG = "//li[@menuid='BIRMFXQ010204']/a".__add__(XPATH)  # 可疑交易查询标题菜单
    FXQZB_FRAME = "ifrBIRMFXQ010201"  # 可疑交易甄别FRAME
    FXQSP_FRAME = "ifrBIRMFXQ010203"  # 可疑交易审批FRAME
    FXQBS_FRAME = "ifrBIRMFXQ010202"  # 可疑交易上报FRAME


class PubFxqBspzElement(object):
    """反洗钱品种公共组件"""
    # 可疑交易甄别页面
    BUTTON_ADD_FXQ = "KYJYZB_list.add".__add__(ID)  # 反洗钱甄别-新增按钮
    ADD_FRAME_FXQ = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_KYJY_Detail.sf%3Fm%3Da_iframe"  # 新增页面FRAME
    GET_CUST_NUMBER = "KYJYZB_list.cliNo".__add__(ID)  # 获取客户编号
    BUTTON_SAVE_FXQ = "KYJY_detail_affix1.save".__add__(ID)  # 保存按钮
    INPUT_QUERY_DFHM_FXQ = "KYJYZB_form.douOpAcntName".__add__(ID)  # 查询条件-对方户名
    BUTTON_REFRESH_FXQ = "KYJYZB_form.refresh".__add__(ID)  # 刷新按钮
    # GET_CUST_NAME = "//*[@CLASS='rowCss2']/td/a[@id='KYJYZB_list.douClientName']".__add__(XPATH)  # 获取客户名称
    FXK_ALL_FXQ = "//*[@id='div_title']//span[@class='checkbox_bg']".__add__(XPATH)  # 全选复选框
    BUTTON_SUBMIT_FXQ = "KYJYZB_list.submit".__add__(ID)  # 提交审批按钮
    BUTTON_QRKY_FXQ = "KYJYZB_list.key_sure".__add__(ID)  # 确认可疑按钮
    BUTTON_PCKY_FXQ = "KYJYZB_list.key_unsure".__add__(ID)  # 排除可疑按钮
    BUTTON_DELETE_FXQ = "KYJYZB_list.del".__add__(ID)  # 删除按钮
    BUTTON_EXPORT_FXQ = "KYJYZB_list.exp".__add__(ID)  # 导出按钮
    QRKY_FRAME_FXQ = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLS_KYJYZB_keySure.sf%3Fm%3Dv')]".__add__(
        XPATH)  # 确认可疑frame
    INPUT_QRKY_FXQ = "KYJYZB_keySure.aff_explain".__add__(ID)  # 确认可疑原因输入框
    BUTTON_QRKY_SAVE_FXQ = "KYJYZB_keySure.save".__add__(ID)  # 确认可疑原因保存按钮
    INPUT_QRKY_FXQ_CONTENT = "确认可疑"
    BUTTON_CLOSE_QRKY = "//*[@CLASS='layoutContentHeader_right']".__add__(XPATH)  # 确认可疑弹窗关闭按钮
    AUI_CLOSE = "//*[@CLASS='aui_close']".__add__(XPATH)  # 弹窗关闭按钮
    AUI_CONTENT = "//*[@CLASS='aui_content']".__add__(XPATH)  # 弹窗提示信息
    # 可疑甄别审批页面
    BUTTON_INTO_FXQ = "//*[@id='bf_common_todo_statistic_list.taskName' and @value='{}']/../../..//a[@id='bf_common_todo_statistic_list.entering_handle']/font".__add__(
        XPATH)  # 可疑甄别审批   反洗钱审批
    KYZBSP = "可疑甄别审批"
    FXQSP = "反洗钱审批"
    INPUT_CUST_NUMBER_KYJYSP = "KYJYZB_audit_form.cliNo".__add__(ID)  # 查询条件--客户编号
    INPUT_CUST_NAME_KYZBSP = "KYJYZB_audit_form.douClientName".__add__(ID)  # 查询条件--客户名称
    BUTTON_REFRESH_KYZBSP = "KYJYZB_audit_form.refresh".__add__(ID)  # 审批页面刷新按钮
    FXK_KYZBSP = "//*[@id='fixed_title']//span[@class='checkbox_bg']".__add__(XPATH)  # 复选框
    INPUT_SPYJ_KYZBSP = "KYJYZB_audit_remark.apr_reason".__add__(ID)  # 可疑甄别审批-审批意见
    BUTTON_AGREE_KYZBSP = "KYJYZB_audit_remark._um_agree".__add__(ID)  # 可疑甄别审批-同意按钮
    BUTTON_REJECT_KYZBSP = "KYJYZB_audit_remark._um_agree".__add__(ID)  # 可疑甄别审批-驳回按钮
    # 可疑甄别报送页面
    INPUT_CUST_NUMBER_KYJYBS = "KYJYZB_audit_form.cliNo".__add__(ID)  # 查询条件--客户编号
    INPUT_CUST_NAME_KYJYBS = "susDataManager_form.cliName".__add__(ID)  # 查询条件--客户名称
    BUTTON_REFRESH_KYJYBS = "susDataManager_list.refresh".__add__(ID)  # 刷新按钮
    FXK_KYJYBS = "//*[@id='fixed_title']//span[@class='checkbox_bg']".__add__(XPATH)  # 复选框
    BUTTON_SUBMIT_KYJYBS = "susDataManager_list.submit".__add__(ID)  # 提交按钮
    ADD_KYBW_FRAME = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_report_add.sf%3Fm%3Da_iframe"  # 新增可疑报文frame
    SBWD_KYJYBS = "report_add_info.organName".__add__(ID)  # 上报网点
    CHOICE_SBWD_KYJYBS_FRAME = "LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_choice_organNo.sf%3Fm%3Dv_iframe"  # 选择上报网点frame
    CHOICE_SBWD_KYJYBS = "//*[@id='choice_organNo_list']//tr[1]/td[1]/a[@id='choice_organNo_list.organNo']".__add__(
        XPATH)  # 单击选择上报网点
    KYJYTZ_KYJYBS = "report_add_info.msgDoubtCharacter".__add__(ID)  # 可疑交易特征
    CHOICE_KYJYTZ_KYJYBS_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_choice_doubtCharacter.sf%3Fm%3Dv%')]".__add__(
        XPATH)  # 选择可疑交易特征frame
    CHOICE_KYJYTZ_KYJYBS = "//*[@id='fixed_title']/thead//span[@class='checkbox_bg']".__add__(XPATH)  # 选择可疑交易特征复选框
    BUTTON_KYJYTZ_KYJYBS = "choice_doubtCharacter_list.save".__add__(ID)  # 选择可疑交易特征--确认按钮
    YSSZLXDM_KYJYBS = "report_add_info.msgCriminousType".__add__(ID)  # 疑似涉罪类型代码
    CHOICE_YSSZLXDM_KYJYBS_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RAMLRS-Web@RAMLRS_choice_msgCriminousType.sf%3Fm%3Dv%26msgCriminous%3D%26maxMsgCriminousType%')]".__add__(
        XPATH)  # 选择疑似涉罪类型代码frame
    CHOICE_YSSZLXDM_KYJYBS = "//*[@id='fixed_title']//span[@class='checkbox_bg']".__add__(XPATH)  # 选择疑似涉罪类型代码-复选框
    BUTTON_YSSZLXDM_KYJYBS = "choice_msgCriminousType_list.save".__add__(ID)  # 选择疑似涉罪类型代码-确认
    INPUT_JJCD_KYJYBS = "//*[@id='report_add_info.msgUrgencyDegree']/option[text()='非特别紧急']".__add__(
        XPATH)  # 紧急程度  1-非特别紧急  2-特别紧急
    INPUT_BSFX_KYJYBS = "//*[@id='report_add_info.msgReportDirection']/option[text()='报告中国反洗钱监测分析中心']".__add__(
        XPATH)  # 报送方向  1-报告中国反洗钱监测分析中心  2-报告中国反洗钱监测分析中心和当地公安机关 ......
    INPUT_OTHER_BSFX_KYJYBS = "report_add_info.msgReportDirectionOthers".__add__(ID)  # 其他报送方向说明
    INPUT_KYJYBGCFD_KYJYBS = "//*[@id='report_add_info.msgTriggerPoint']/option[text()='模型筛选']".__add__(
        XPATH)  # 可疑交易报告触发点  1-模型筛选 2-执法部门指令（公安、纪检、安全等部门的境内冻结、协查等） 3-社会舆情 ......
    INPUT_OTHER_KYJYBGCFD_KYJYBS = "report_add_info.msgTriggerPointOthers".__add__(ID)  # 其他可疑交易报告触发点说明
    INPUT_ZJJYKHXW_KYJYBS = "report_add_info.msgReportSTCB".__add__(ID)  # 资金交易及客户行为情况
    INPUT_YDFX_KYJYBS = "report_add_info.msgReportAosp".__add__(ID)  # 疑点分析
    BUTTON_SUBMIT_XZKYBW = "report_add_info.submit".__add__(ID)  # 新增可疑报文-提交按钮

