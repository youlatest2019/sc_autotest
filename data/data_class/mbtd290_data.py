#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/8 18:07
# @Author   : yangshukun
# @File     : mbtd290_data.py

from Common.common_map import *


class MBTD290DATA(object):
    INFRECTYPE = ""  # 信息记录类型
    INFRECTYPE_XPATH = "".__add__(XPATH)  # 信息记录类型元素表达式
    ACCTTYPE = ""  # 账户类型
    ACCTTYPE_XPATH = "//select[@name='DM_MBTD_GRJD_JCD.ACCTTYPE']/option[3]".__add__(XPATH)  # 账户类型元素表达式
    ACCTCODE = "auto_test"  # 账户标识码
    ACCTCODE_XPATH = "//input[@name='DM_MBTD_GRJD_JCD.ACCTCODE']".__add__(XPATH)  # 账户标识码元素表达式
    RPTDATE = "20220331"  # 信息报告日期
    RPTDATE_XPATH = "//input[@name='DM_MBTD_GRJD_JCD.RPTDATE']".__add__(XPATH)  # 信息报告日期元素表达式
    RPTDATECODE = ""  # 报告时点说明代码
    RPTDATECODE_XPATH = "//select[@name='DM_MBTD_GRJD_JCD.RPTDATECODE']/option[2]".__add__(XPATH)  # 报告时点说明代码元素表达式
    NAME = "test_script"  # 借款人姓名
    NAME_XPATH = "//input[@name='DM_MBTD_GRJD_JCD.NAME']".__add__(XPATH)  # 借款人姓名元素表达式
    IDTYPE = ""  # 借款人证件类型
    IDTYPE_XPATH = "//select[@name='DM_MBTD_GRJD_JCD.IDTYPE']/option[2]".__add__(XPATH)  # 借款人证件类型元素表达式
    IDNUM = "5221231"  # 借款人证件号码
    IDNUM_XPATH = "//input[@name='DM_MBTD_GRJD_JCD.IDNUM']".__add__(XPATH)  # 借款人证件号码元素表达式
    MNGMTORGCODE = "auto_jgdm001"  # 业务管理机构代码
    MNGMTORGCODE_XPATH = "//input[@name='DM_MBTD_GRJD_JCD.MNGMTORGCODE']".__add__(XPATH)  # 业务管理机构代码元素表达式
