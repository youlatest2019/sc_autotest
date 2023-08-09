#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/8 18:07
# @Author   : yangshukun
# @File     : mbtd290_data.py

from Common.common_map import *


class MBTD210DATA(object):
    INFRECTYPE = ""  # 信息记录类型
    BUSINESS_NAME_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.ENTNAME']".__add__(XPATH)  # 企业名称元素表达式
    IDENTITY_TYPE_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.ENTCERTTYPE']/option[@value='30']".__add__(
        XPATH)  # 企业身份标识类型元素表达式（填写数字） 10-中征码（原贷款卡编码） 20-统一社会信用代码   30-组织机构代码
    IDENTITY_NUMBER_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.ENTCERTNUM']".__add__(XPATH)  # 企业身份标识号码元素表达式
    IDENTITY_NUMBER = "123456789"
    INFORMATION_SOURCE_CODE_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.INFSURCCODE']".__add__(XPATH)  # 信息来源编码
    INFORMATION_SOURCE_CODE = "999888"
    REPORT_DATE_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.RPTDATE']".__add__(XPATH)  # 信息报告日期
    REPORT_DATE = "20220331"
    REPORT_TIME_CODE = "//*[@name='DM_MBTD_BD_EBB_BASE.RPTDATECODE']/option[@value='10']".__add__(
        XPATH)  # 报告时点说明代码（填写数字） 10-新增客户资料/首次上报  20-更新客户资料
    CUSTOMER_DATA_CODE = "111222"
    CUSTOMER_DATA_CODE_XPATH = "//*[@name='DM_MBTD_BD_EBB_BASE.CIMOC']".__add__(XPATH)  # 客户资料维护机构代码
    CUSTOMER_DATA_TYPE = "//*[@name='DM_MBTD_BD_EBB_BASE.CUSTOMERTYPE']/option[@value='1']".__add__(
        XPATH)  # 客户资料类型 1-基本存款账户客户资料  2-授信业务客户资料   X-未知
    ORGANIZATION_TYPE = "//*[@name='DM_MBTD_BD_EBB_BASE.ORGTYPE']/option[@value='1']".__add__(
        XPATH)  # 组织机构类型 1-企业   11-公司  13-非公司制企业法人  15-企业分支机构  17-个人独资企业、合伙企业  19-其他企业  ...
    STATUS = "//*[@name='DM_MBTD_BD_EBB_BASE.ETPSTS']/option[@value='1']".__add__(XPATH)  # 存续状态 1-正常  2-注销  9-其他  X-未知


class MBTD250DATA(object):
    # 基础段
    INFRECTYPE = ""  # 信息记录类型
    ACCOUNT_TYPE = "//*[@name='DM_MBTD_BD_WARRANT_BASE.ACCTTYPE']/option[@value='G1']".__add__(
        XPATH)  # 账户类型  G1-融资担保账户  G2-非融资担保账户  G3-支付担保账户
    ACCOUNT_CODE_TYPE = "//*[@name='DM_MBTD_BD_WARRANT_BASE.ACCTCODE']".__add__(XPATH)  # 账户标识码
    ACCOUNT_CODE = "123456"
    REPORT_DATE250_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASE.RPTDATE']".__add__(XPATH)  # 信息报告日期
    REPORT_DATE250 = "20220331"
    REPORT_TIME_CODE250 = "//*[@name='DM_MBTD_BD_WARRANT_BASE.RPTDATECODE']/option[@value='10']".__add__(
        XPATH)  # 报告时点说明代码  10-新开户/首次上报  20-账户关闭  30-在保责任变化  40-五级分类调整  50-其他信息变化（包括相关还款责任人、抵（质）押合同等信息发生变化）
    DEBTOR_NAME = "//*[@name='DM_MBTD_BD_WARRANT_BASE.NAME']".__add__(XPATH)  # 债务人名称
    DEBTOR_TYPE = "//*[@name='DM_MBTD_BD_WARRANT_BASE.IDTYPE']/option[@value = '10']".__add__(
        XPATH)  # 债务人身份标识类型  10-中征码（原贷款卡编码）  20-统一社会信用代码  30-组织机构代码
    DEBTOR_CODE_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASE.IDNUM']".__add__(XPATH)  # 债务人身份标识号码
    DEBTOR_CODE = "666888"
    ORGAN_CODE_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASE.MNGMTORGCODE']".__add__(XPATH)  # 业务管理机构代码
    ORGAN_CODE = "12345"
    # 基本信息段
    DBYW_MAJOR = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.BUSILINES']/option[@value='1']".__add__(
        XPATH)  # 担保业务大类 1-融资担保 2-非融资担保  3-再担保  4-保证保险  5-信用证  6-承兑汇票  7-银行保函
    DBYW_BREAK = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.BUSIDTILLINES']/option[@value='01']".__add__(
        XPATH)  # 担保业务种类细分 01-贷款担保 02-票据承兑担保 03-贸易融资担保 04-项目融资担保 05-信用证担保 06-其他融资担保 10-债券发行担保
    ACC_OPEN_DATE_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.OPENDATE']".__add__(XPATH)  # 开户日期
    ACC_OPEN_DATE = "20190329"
    GUARANTEE_AMOUNT_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.GUARAMT']".__add__(XPATH)  # 担保金额
    GUARANTEE_AMOUNT = "50000"
    BZ = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.CY']/option[@value='CNY']".__add__(XPATH)  # 币种
    DUEDATE_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.DUEDATE']".__add__(XPATH)  # 到期日期
    DUEDATE = "20230329"
    FDB_METHOD = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.GUARMODE']/option[@value='2']".__add__(
        XPATH)  # 反担保方式 0-信用/免担保 1-保证 2-质押 3-抵押 4-组合
    OTHERS_HK_METHOD = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.OTHREPYGUARWAY']/option[@value='0']".__add__(
        XPATH)  # 其他还款保证方式 0-无 1-保证金 2-第三方付款承诺 9-其他
    BOND_PERCENT_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.SECDEP']".__add__(XPATH)  # 保证金百分比
    BOND_PERCENT = "20"
    DBHT_TEXT_NUMBER_XPATH = "//*[@name='DM_MBTD_BD_WARRANT_BASEINFO.CTRCTTXTCODE']".__add__(XPATH)  # 担保合同文本编号
    DBHT_TEXT_NUMBER = "9801"

