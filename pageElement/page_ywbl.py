#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/6/15 11:41
# @Author   : yangshukun
# @File     : page_ywbl.py

from Common.common_map import *
import os


class YwblElementMain(object):
    """一级页面的功能及按钮"""
    SJGL = "//span[text()='数据管理']".__add__(XPATH)  # 数据管理菜单
    YWSJCX = "//a[@menuid='Supplement010101']".__add__(XPATH)  # 主框架
    YWBL = "//li[text()='业务数据补录']".__add__(XPATH)  # 业务补录界面
    BUTTON_TJQB = "//*[@id='submitAllBtn']".__add__(XPATH)  # 提交全部按钮
    ALTER_TJQB_HL = "//div[text()='是否提交全部数据?']/../div[3]/a[1]".__add__(XPATH)  # 汇率模型，提交全部后确认按钮
    BUTTON_DR = "//*[@id='mainTab']/tbody/tr[4]/td[2]/span[3]/input".__add__(XPATH)  # 导入按钮
    BUTTON_JYQB = "//*[@id='mainTab']/tbody/tr[4]/td[2]/span[7]".__add__(XPATH)  # 校验全部按钮
    MSG_CHECK_END = "//div[@class='layui-layer-content']".__add__(XPATH)  # 校验结束提示信息
    BUTTON_EXPORT = "//*[@id='export']".__add__(XPATH)  # 导出按钮
    BUTTON_DELETE = "//*[@id='dataDelBtn']".__add__(XPATH)  # 删除按钮
    CHECKBOX_ALL = "//*[@id='listTabHead']/thead/tr/th[1]/input".__add__(XPATH)  # 复选框全选
    CHECKBOX_FIRST_ONE = "//*[@id='listTabBody']/tbody/tr[1]/td[1]".__add__(XPATH)  # 复选框选择第一个数据
    BUTTON_ADD = "//*[@id='dataAddBtn']".__add__(XPATH)  # 新增按钮
    BUTTON_REFRESH = "javascript:pageRefresh()"  # 刷新按钮
    EXPORT_EXCEL = "//span[text()='导出EXCEL格式']".__add__(XPATH)  # 选择导出EXCEL
    EXPORT_CSV = "//span[text()='导出CSV格式']".__add__(XPATH)  # 选择导出CSV
    CHECKBOX_BY_DATA = "//span[text()='auto_test_01']/../../td[1]".__add__(XPATH)  # 通过第一列数据名称进行复选框勾选


class YwblElementAdd(object):
    """业务补录二级页面功能及按钮"""
    INPUT_TJRQ = "//*[@id='dataDate']".__add__(XPATH)  # 提交日期输入框
    BUTTON_TJQR = "/html/body/div[2]/div[2]/input".__add__(XPATH)  # 提交日期确认按钮
    BUTTON_UPLOAD = "//*[@class='fileInput']".__add__(XPATH)  # 导入弹窗上传文件按钮
    BUTTON_IMPORT = "//*[@id='upload']".__add__(XPATH)  # 导入弹窗导入按钮
    VALUE_TOTAL = "//font[@id='total']".__add__(XPATH)  # 导入弹窗数据总数
    BUTTON_DRQR = "//*[@id='confirmBtn']".__add__(XPATH)  # 导入弹窗确认按钮
    ALERT_DDRW = "//*[@id='LAYOUT_WIN_/SmartPage/DOM-Web-ROOT/page/monitor.html']/div[3]".__add__(
        XPATH)  # 提交后调度进度弹窗关闭按钮
    ALERT_CONFIRM = "//a[text()='是']".__add__(XPATH)  # 删除确认
    BUTTON_ADD_SAVE = "//form[@id='formArea']//ul/li[last()]".__add__(XPATH)  # 新增页面保存按钮
    ALERT_ADD_SAVE = "//div[@class='layui-layer layui-layer-dialog layui-layer-border layui-layer-msg layui-layer-hui']/div[1]".__add__(
        XPATH)  # 新增页面保存提示信息
    BUTTON_QRQBTJ = "//a[text()='是']".__add__(XPATH)  # 确认全部提交


class YwblElementFrame(object):
    """业务补录各界面的frame框架表达式，ID，索引或者定位元素"""
    FRAME_01 = "ifrSupplement010101"  # 业务补录主框架frameID
    FRAME_02 = "frame"  # 业务补录页面数据功能页面frameID
    # FRAME_02 =  "//iframe[@src='DOM-Web@dataSupplement.do']".__add__(XPATH)
    FRAME_DATE = "LAYOUT_WIN_/SmartPage/DOM-Web-ROOT/page/supDataSubmit.html_iframe"  # 提交弹窗frame定位ID
    FRAME_DR_INDEX = 2  # 导入界面frame，定位的索引号
    FRAME_ADD = "//iframe[contains(@src,'moduleId=JCXX_YGXX')]".__add__(XPATH)  # 新增页面的frame定位元素表达式
    FRAME_ADD_COMMANY = "//iframe[contains(@src,'moduleId=QUERY_KHXX')]".__add__(XPATH)  # 新增员工信息选择所属单位时弹出页面frame的定位表达式


class YwblElementDataPath(object):
    """业务补录不同模型选项及文件路径"""

    # -----------财务信息-----------
    YWLX_CWXX = "//*[@id='ywlx']/option[text()='财务信息']".__add__(XPATH)  # 财务信息
    YWMX_KJKM = "//*[@id='moduleId']/option[text()='会计科目']".__add__(XPATH)  # 会计科目
    FILE_PATH_KJKM = "1-财务信息\\1-会计科目.xlsx"  # 会计科目导入文件路径
    YWMX_FZHSX = "//*[@id='moduleId']/option[text()='辅助核算项']".__add__(XPATH)  # 辅助核算项
    FILE_PATH_FZHSX = "1-财务信息\\2-辅助核算项.xlsx"  # 辅助核算项导入文件路径
    YWMX_FTPDJBDMX = "//*[@id='moduleId']/option[text()='FTP定价变动明细信息']".__add__(XPATH)  # FTP定价变动明细信息
    FILE_PATH_FTPDJBDMX = "1-财务信息\\3-FTP定价变动明细信息.xlsx"  # FTP定价变动明细信息导入文件路径

    # -----------基础信息-----------
    YWLX_JCXX = "//*[@id='ywlx']/option[text()='基础信息']".__add__(XPATH)  # 基础信息
    YWMX_YGXX = "//*[@id='moduleId']/option[text()='员工信息']".__add__(XPATH)  # 业务模型下拉选择
    FILE_PATH_YGXX = "2-基本信息\\3-员工信息.xlsx"  # 员工信息导入文件路径
    YWMX_HL = "//*[@id='moduleId']/option[text()='汇率']".__add__(XPATH)  # 汇率
    FILE_PATH_HL = "2-基本信息\\6-汇率.xlsx"  # 汇率导入文件路径
    YWMX_JZLL = "//*[@id='moduleId']/option[text()='基准利率']".__add__(XPATH)  # 基准利率
    FILE_PATH_JZLL = "2-基本信息\\7-基准利率.xlsx"  # 基准利率导入文件路径
    YWMX_QYKH = "//*[@id='moduleId']/option[text()='企业客户']".__add__(XPATH)  # 企业客户
    FILE_PATH_QYKH = "2-基本信息\\1-企业客户.xlsx"  # 企业客户导入文件路径
    YWMX_JRJG = "//*[@id='moduleId']/option[text()='金融机构']".__add__(XPATH)  # 金融机构
    FILE_PATH_JRJG = "2-基本信息\\2-金融机构.xlsx"  # 金融机构导入文件路径
    YWMX_NBZH = "//*[@id='moduleId']/option[text()='内部账户']".__add__(XPATH)  # 内部账户
    FILE_PATH_NBZH = "2-基本信息\\4-内部账户.xlsx"  # 内部账户导入文件路径
    YWMX_YHZH = "//*[@id='moduleId']/option[text()='银行账户']".__add__(XPATH)  # 银行账户
    FILE_PATH_YHZH = "2-基本信息\\5-银行账户.xlsx"  # 银行账户导入文件路径
    YWMX_DBRXXZZJG = "//*[@id='moduleId']/option[text()='担保人信息（组织机构）']".__add__(XPATH)  # 担保人信息（组织机构）
    FILE_PATH_DBRXXZZJG = "2-基本信息\\9-担保人信息（组织机构）.xlsx"  # 担保人信息（组织机构）导入文件路径
    YWMX_DBRXXZRR = "//*[@id='moduleId']/option[text()='担保人信息（自然人）']".__add__(XPATH)  # 担保人信息（自然人）
    FILE_PATH_DBRXXZRR = "2-基本信息\\10-担保人信息（自然人）.xlsx"  # 担保人信息（自然人）导入文件路径
    YWMX_GRKH = "//*[@id='moduleId']/option[text()='个人客户']".__add__(XPATH)  # 个人客户
    FILE_PATH_GRKH = "2-基本信息\\8-个人客户.xlsx"  # 个人客户导入文件路径
    YWMX_JTZHXX = "//*[@id='moduleId']/option[text()='集团账户']".__add__(XPATH)  # 集团账户
    FILE_PATH_JTZHXX = "2-基本信息\\11-集团账户.xlsx"  # 集团账户导入文件路径

    # -----------存款业务-----------
    YWLX_CKYW = "//*[@id='ywlx']/option[text()='存款业务']".__add__(XPATH)  # 存款业务
    YWMX_HQCK = "//*[@id='moduleId']/option[text()='活期存款']".__add__(XPATH)  # 活期存款
    FILE_PATH_HQCK = "3-存款业务\\1-活期存款.xlsx"  # 活期存款导入文件路径
    YWMX_DQCK = "//*[@id='moduleId']/option[text()='定期存款']".__add__(XPATH)  # 定期存款
    FILE_PATH_DQCK = "3-存款业务\\3-定期存款.xlsx"  # 定期存款导入文件路径
    YWMX_TZCK = "//*[@id='moduleId']/option[text()='通知存款']".__add__(XPATH)  # 通知存款
    FILE_PATH_TZCK = "3-存款业务\\4-通知存款.xlsx"  # 通知存款导入文件路径
    YWMX_XYCK = "//*[@id='moduleId']/option[text()='协议存款']".__add__(XPATH)  # 协议存款
    FILE_PATH_XYCK = "3-存款业务\\5-协议存款.xlsx"  # 协议存款导入文件路径
    YWMX_BZJCK = "//*[@id='moduleId']/option[text()='保证金存款']".__add__(XPATH)  # 保证金存款
    FILE_PATH_BZJCK = "3-存款业务\\6-保证金存款.xlsx"  # 保证金存款导入文件路径
    YWMX_CKZBJ = "//*[@id='moduleId']/option[text()='存款准备金']".__add__(XPATH)  # 存款准备金
    FILE_PATH_CKZBJ = "3-存款业务\\7-存款准备金.xlsx"  # 存款准备金导入文件路径
    YWMX_WTCK = "//*[@id='moduleId']/option[text()='委托存款']".__add__(XPATH)  # 委托存款
    FILE_PATH_WTCK = "3-存款业务\\8-委托存款.xlsx"  # 委托存款导入文件路径

    # -----------贷款业务-----------
    YWLX_DKYW = "//*[@id='ywlx']/option[text()='贷款业务']".__add__(XPATH)  # 贷款业务
    YWMX_LDZJDK = "//*[@id='moduleId']/option[text()='流动资金贷款']".__add__(XPATH)  # 流动资金贷款
    FILE_PATH_LDZJDK = "4-贷款业务\\1-流动资金贷款.xlsx"  # 流动资金贷款导入文件路径
    YWMX_XMDK = "//*[@id='moduleId']/option[text()='项目贷款']".__add__(XPATH)  # 项目贷款
    FILE_PATH_XMDK = "4-贷款业务\\2-项目贷款.xlsx"  # 项目贷款导入文件路径
    YWMX_ZRRXFXD = "//*[@id='moduleId']/option[text()='自然人消费信贷']".__add__(XPATH)  # 自然人消费信贷
    FILE_PATH_ZRRXFXD = "4-贷款业务\\19-自然人消费信贷.xlsx"  # 自然人消费信贷导入文件路径
    YWMX_FRZHTZ = "//*[@id='moduleId']/option[text()='法人账户透支']".__add__(XPATH)  # 法人账户透支
    FILE_PATH_FRZHTZ = "4-贷款业务\\4-法人账户透支.xlsx"  # 法人账户透支导入文件路径
    YWMX_GDZCDK = "//*[@id='moduleId']/option[text()='固定资产贷款']".__add__(XPATH)  # 固定资产贷款
    FILE_PATH_GDZCDK = "4-贷款业务\\5-固定资产贷款.xlsx"  # 固定资产贷款导入文件路径
    YWMX_BGDK = "//*[@id='moduleId']/option[text()='并购贷款']".__add__(XPATH)  # 并购贷款
    FILE_PATH_BGDK = "4-贷款业务\\6-并购贷款.xlsx"  # 并购贷款导入文件路径
    YWMX_DW_RZZL = "//*[@id='moduleId']/option[text()='单位融资租赁']".__add__(XPATH)  # 单位融资租赁
    FILE_PATH_DW_RZZL = "4-贷款业务\\7-单位融资租赁.xlsx"  # 单位融资租赁导入文件路径
    YWMX_BL = "//*[@id='moduleId']/option[text()='保理']".__add__(XPATH)  # 保理
    FILE_PATH_BL = "4-贷款业务\\8-保理.xlsx"  # 保理导入文件路径
    YWMX_MFXD = "//*[@id='moduleId']/option[text()='买方信贷']".__add__(XPATH)  # 买方信贷
    FILE_PATH_MFXD = "4-贷款业务\\9-买方信贷.xlsx"  # 买方信贷导入文件路径
    YWMX_BH = "//*[@id='moduleId']/option[text()='保函']".__add__(XPATH)  # 保函
    FILE_PATH_BH = "4-贷款业务\\11-保函.xlsx"  # 保函导入文件路径
    YWMX_DBHT = "//*[@id='moduleId']/option[text()='担保合同']".__add__(XPATH)  # 担保合同
    FILE_PATH_DBHT = "4-贷款业务\\12-担保合同.xlsx"  # 担保合同导入文件路径
    YWMX_SX_DW = "//*[@id='moduleId']/option[text()='授信（单位）']".__add__(XPATH)  # 授信（单位）
    FILE_PATH_SX_DW = "4-贷款业务\\13-授信（单位）.xlsx"  # 授信（单位）导入文件路径
    YWMX_XYPJ_DW = "//*[@id='moduleId']/option[text()='信用评级（单位）']".__add__(XPATH)  # 信用评级（单位）
    FILE_PATH_XYPJ_DW = "4-贷款业务\\14-信用评级（单位）.xlsx"  # 信用评级（单位）导入文件路径
    YWMX_FRXFXD = "//*[@id='moduleId']/option[text()='法人消费信贷']".__add__(XPATH)  # 法人消费信贷
    FILE_PATH_FRXFXD = "4-贷款业务\\18-法人消费信贷.xlsx"  # 法人消费信贷导入文件路径
    YWMX_RZDB = "//*[@id='moduleId']/option[text()='融资担保']".__add__(XPATH)  # 融资担保
    FILE_PATH_RZDB = "4-贷款业务\\21-融资担保.xlsx"  # 融资担保导入文件路径
    YWMX_RZZL_ZRR = "//*[@id='moduleId']/option[text()='自然人融资租赁']".__add__(XPATH)  # 自然人融资租赁
    FILE_PATH_RZZL_ZRR = "4-贷款业务\\15-自然人融资租赁.xlsx"  # 自然人融资租赁导入文件路径
    YWMX_CYDWCPDRZZL_FR = "//*[@id='moduleId']/option[text()='成员单位产品的融资租赁（法人）']".__add__(XPATH)  # 成员单位产品的融资租赁（法人）
    FILE_PATH_CYDWCPDRZZL_FR = "4-贷款业务\\16-成员单位产品的融资租赁（法人）.xlsx"  # 成员单位产品的融资租赁（法人）导入文件路径
    YWMX_MYRZ = "//*[@id='moduleId']/option[text()='贸易融资']".__add__(XPATH)  # 贸易融资
    FILE_PATH_MYRZ = "4-贷款业务\\17-贸易融资.xlsx"  # 贸易融资导入文件路径
    YWMX_SX_ZRR = "//*[@id='moduleId']/option[text()='授信（自然人）']".__add__(XPATH)  # 授信（自然人）
    FILE_PATH_SX_ZRR = "4-贷款业务\\22-授信（自然人）.xlsx"  # 授信（自然人）导入文件路径
    YWMX_XYPJ_ZRR = "//*[@id='moduleId']/option[text()='信用评级（自然人）']".__add__(XPATH)  # 信用评级（自然人）
    FILE_PATH_XYPJ_ZRR = "4-贷款业务\\23-信用评级（自然人）.xlsx"  # 信用评级（自然人）导入文件路径
    YWMX_CYDWCPDRZZL_ZRR = "//*[@id='moduleId']/option[text()='成员单位产品的融资租赁（自然人）']".__add__(XPATH)  # 成员单位产品的融资租赁（自然人）
    FILE_PATH_CYDWCPDRZZL_ZRR = "4-贷款业务\\24-成员单位产品的融资租赁（自然人）.xlsx"  # 成员单位产品的融资租赁（自然人）导入文件路径

    # -----------同业业务-----------
    YWLX_TYYW = "//*[@id='ywlx']/option[text()='同业业务']".__add__(XPATH)  # 同业业务
    YWMX_TYCR = "//*[@id='moduleId']/option[text()='同业拆入']".__add__(XPATH)  # 同业拆入
    FILE_PATH_TYCR = "5-同业业务\\4-同业拆入.xlsx"  # 同业拆入导入文件路径
    YWMX_TYCC = "//*[@id='moduleId']/option[text()='同业拆出']".__add__(XPATH)  # 同业拆出
    FILE_PATH_TYCC = "5-同业业务\\8-同业拆出.xlsx"  # 同业拆出导入文件路径
    YWMX_TYCF = "//*[@id='moduleId']/option[text()='同业存放']".__add__(XPATH)  # 同业存放
    FILE_PATH_TYCF = "5-同业业务\\3-同业存放.xlsx"  # 同业存放导入文件路径
    YWMX_CFTY = "//*[@id='moduleId']/option[text()='存放同业']".__add__(XPATH)  # 存放同业
    FILE_PATH_CFTY = "5-同业业务\\9-存放同业.xlsx"  # 存放同业导入文件路径
    YWMX_TYSXHD = "//*[@id='moduleId']/option[text()='同业授信（获得）']".__add__(XPATH)  # 同业授信（获得）
    FILE_PATH_TYSXHD = "5-同业业务\\5-同业授信（获得）.xlsx"  # 同业授信（获得）导入文件路径
    YWMX_TYSXSY = "//*[@id='moduleId']/option[text()='同业授信（授予）']".__add__(XPATH)  # 同业授信（授予）
    FILE_PATH_TYSXSY = "5-同业业务\\6-同业授信（授予）.xlsx"  # 同业授信（授予）导入文件路径
    YWMX_TYKHXYPJ = "//*[@id='moduleId']/option[text()='同业客户信用评级']".__add__(XPATH)  # 同业客户信用评级
    FILE_PATH_TYKHXYPJ = "5-同业业务\\7-同业客户信用评级.xlsx"  # 同业客户信用评级导入文件路径
    YWMX_TYJR = "//*[@id='moduleId']/option[text()='同业借入']".__add__(XPATH)  # 同业借入
    FILE_PATH_TYJR = "5-同业业务\\1-同业借入.xlsx"  # 同业借入导入文件路径
    YWMX_TYJC = "//*[@id='moduleId']/option[text()='同业借出']".__add__(XPATH)  # 同业借出
    FILE_PATH_TYJC = "5-同业业务\\2-同业借出.xlsx"  # 同业借出导入文件路径

    # -----------投资业务-----------
    YWLX_TZYW = "//*[@id='ywlx']/option[text()='投资业务']".__add__(XPATH)  # 投资业务
    YWMX_ZQTZ = "//*[@id='moduleId']/option[text()='债券投资']".__add__(XPATH)  # 债券投资
    FILE_PATH_ZQTZ = "6-投资业务\\1-债券投资.xlsx"  # 债券投资导入文件路径
    YWMX_ZQHG = "//*[@id='moduleId']/option[text()='债券回购']".__add__(XPATH)  # 债券回购
    FILE_PATH_ZQHG = "6-投资业务\\2-债券回购.xlsx"  # 债券回购导入文件路径
    YWMX_QYTZ = "//*[@id='moduleId']/option[text()='权益投资']".__add__(XPATH)  # 权益投资
    FILE_PATH_QYTZ = "6-投资业务\\3-权益投资.xlsx"  # 权益投资导入文件路径
    YWMX_GMJJTZ = "//*[@id='moduleId']/option[text()='公募基金']".__add__(XPATH)  # 公募基金
    FILE_PATH_GMJJTZ = "6-投资业务\\4-公募基金.xlsx"  # 公募基金导入文件路径
    YWMX_SMJJTZ = "//*[@id='moduleId']/option[text()='私募基金']".__add__(XPATH)  # 私募基金
    FILE_PATH_SMJJTZ = "6-投资业务\\5-私募基金.xlsx"  # 私募基金导入文件路径
    YWMX_ZGCP = "//*[@id='moduleId']/option[text()='资管产品']".__add__(XPATH)  # 资管产品
    FILE_PATH_ZGCP = "6-投资业务\\6-资管产品.xlsx"  # 资管产品导入文件路径
    YWMX_JGXCK = "//*[@id='moduleId']/option[text()='结构性存款']".__add__(XPATH)  # 结构性存款
    FILE_PATH_JGXCK = "6-投资业务\\7-结构性存款.xlsx"  # 结构性存款导入文件路径
    YWMX_BBLC = "//*[@id='moduleId']/option[text()='保本理财']".__add__(XPATH)  # 保本理财
    FILE_PATH_BBLC = "6-投资业务\\8-保本理财.xlsx"  # 保本理财导入文件路径
    YWMX_TYCDTZ = "//*[@id='moduleId']/option[text()='同业存单投资']".__add__(XPATH)  # 同业存单投资
    FILE_PATH_TYCDTZ = "6-投资业务\\9-同业存单投资.xlsx"  # 同业存单投资导入文件路径

    # -----------融资业务-----------
    YWLX_RZYW = "//*[@id='ywlx']/option[text()='融资业务']".__add__(XPATH)  # 融资业务
    YWMX_ZQFX = "//*[@id='moduleId']/option[text()='债券发行']".__add__(XPATH)  # 债券发行
    FILE_PATH_ZQFX = "7-融资业务\\1-债券发行.xlsx"  # 债券发行导入文件路径
    YWMX_XDZCZR = "//*[@id='moduleId']/option[text()='信贷资产转让']".__add__(XPATH)  # 信贷资产转让
    FILE_PATH_XDZCZR = "7-融资业务\\2-信贷资产转让.xlsx"  # 信贷资产转让导入文件路径
    YWMX_TYCDRZ = "//*[@id='moduleId']/option[text()='同业存单融资']".__add__(XPATH)  # 同业存单融资
    FILE_PATH_TYCDRZ = "7-融资业务\\3-同业存单融资.xlsx"  # 同业存单融资导入文件路径

    # -----------外汇业务-----------
    YWLX_WHYW = "//*[@id='ywlx']/option[text()='外汇业务']".__add__(XPATH)  # 外汇业务
    YWMX_WH = "//*[@id='moduleId']/option[text()='外汇']".__add__(XPATH)  # 外汇
    FILE_PATH_WH = "8-外汇业务\\1-外汇.xlsx"  # 外汇导入文件路径
    YWMX_JSH = "//*[@id='moduleId']/option[text()='结售汇']".__add__(XPATH)  # 结售汇
    FILE_PATH_JSH = "8-外汇业务\\2-结售汇.xlsx"  # 结售汇导入文件路径

    # -----------委托代理业务-----------
    YWLX_WTDLYW = "//*[@id='ywlx']/option[text()='委托代理业务']".__add__(XPATH)  # 委托代理业务
    YWMX_WTDK = "//*[@id='moduleId']/option[text()='委托贷款']".__add__(XPATH)  # 委托贷款
    FILE_PATH_WTDK = "9-委托代理业务\\1-委托贷款.xlsx"  # 委托贷款导入文件路径
    YWMX_DLDX = "//*[@id='moduleId']/option[text()='代理代销']".__add__(XPATH)  # 代理代销
    FILE_PATH_DLDX = "9-委托代理业务\\2-代理代销.xlsx"  # 代理代销导入文件路径
    YWMX_WTTZ = "//*[@id='moduleId']/option[text()='委托投资']".__add__(XPATH)  # 委托投资
    FILE_PATH_WTTZ = "9-委托代理业务\\3-委托投资.xlsx"  # 委托投资导入文件路径

    # -----------票据业务-----------
    YWLX_PJYW = "//*[@id='ywlx']/option[text()='票据业务']".__add__(XPATH)  # 票据业务
    YWMX_PJJBXX = "//*[@id='moduleId']/option[text()='票据基本信息']".__add__(XPATH)  # 票据基本信息
    FILE_PATH_PJJBXX = "10-票据业务\\1-票据基本信息.xlsx"  # 票据基本信息导入文件路径
    YWMX_TX = "//*[@id='moduleId']/option[text()='贴现']".__add__(XPATH)  # 贴现
    FILE_PATH_TX = "10-票据业务\\2-贴现.xlsx"  # 贴现导入文件路径
    YWMX_ZHUANTX = "//*[@id='moduleId']/option[text()='转贴现']".__add__(XPATH)  # 转贴现
    FILE_PATH_ZHUANTX = "10-票据业务\\3-转贴现.xlsx"  # 转贴现导入文件路径
    YWMX_ZAITX = "//*[@id='moduleId']/option[text()='再贴现']".__add__(XPATH)  # 再贴现
    FILE_PATH_ZAITX = "10-票据业务\\4-再贴现.xlsx"  # 再贴现导入文件路径
    YWMX_PJCD = "//*[@id='moduleId']/option[text()='票据承兑']".__add__(XPATH)  # 票据承兑
    FILE_PATH_PJCD = "10-票据业务\\5-票据承兑.xlsx"  # 票据承兑导入文件路径
