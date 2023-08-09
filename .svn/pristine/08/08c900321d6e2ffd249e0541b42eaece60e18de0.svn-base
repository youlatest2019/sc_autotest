#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 9:42
# @Author   : yangshukun
# @File     : page_bsgl.py
from Common.common_map import *


class RmbtdDataModifyElementMain(object):
    """征信数据更正页面元素"""
    INPUT_GROUP = "//*[@name='dataChangeGroup']/option[@value='{}']".__add__(
        XPATH)  # 分组 1-企业基本信息 2-企业财务报表信息 3-企业授信协议信息 4-企业借贷交易信息 5-企业担保交易信息 6-抵质押物信息
    BUSINESS_NAME = "//*[@id='queryArea']/table/tbody/tr/td[6]/input".__add__(XPATH)  # 企业名称/债务人名称输入框
    BUTTON_MODIFY = "//*[@id='listTable']/tbody/tr/td[7]/a[2]".__add__(XPATH)  # 更正按钮
    INPUT_BUSINESS_NAME = "//*[@name='DM_MBTD_BD_EBB_BASE_CAM.ENTNAME']".__add__(XPATH)  # 基础段-企业名称输入框
    BUSINESS_INFO_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@RMBTD_DataChangeAction.sf%3Fcn%3DMBTD210')]".__add__(
        XPATH)  # 企业基本信息记录frame
    BUTTON_SUBMIT = "//*[@class='button28 button submitBtn']".__add__(XPATH)  # 提交按钮
    BUTTON_CLOSE = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/a".__add__(XPATH)

    FXK_ALL_MBTDGZ = "//*[@id='fixedTitle']//input[@name='_all']".__add__(XPATH)  # 勾选全部复选框
    BUTTON_DELETE_MBTDGZ = "unifyDel".__add__(ID)  # 整笔删除按钮
    BUTTON_OK_DELETE = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 确认删除弹窗-是
    INPUT_DEBTOR_NAME = "//*[@name='DM_MBTD_BD_WARRANT_BASE_CAM.NAME']".__add__(XPATH)  # 基础段-债务人名称输入框
    QYDB_INFO_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMM-Web@RMBTD_DataChangeAction.sf%3Fcn%3DMBTD250')]".__add__(
        XPATH)  # 企业担保账户信息记录frame
    BUTTON_DELETE_INFO_ZX = "//*[@class='groupTitle']/span[text()='{}']/../span[@class='btn icon_del editBtn']".__add__(
        XPATH)  # 删除信息段按钮   {}：在保责任信息段  基本信息段
    AD_ALERT_DELETE_FRAME = "//iframe[contains(@id,'LAYOUT_WIN_/SmartPage/RMBTD-Web@deletePartRange.do%3FreportContentNo%3DMBTD253')]".__add__(
        XPATH)  # 按段删除弹窗frame
    DELETE_MODE_CHOICE = "//*[@id='deleteType']/option[@value='1']".__add__(XPATH)  # 删除方式选择 1-按天删除  2-按范围删除
    SJ_DATE_ZXSJGZ = "//*[@class='xm-label single-row']".__add__(XPATH)  # 报送数据日期
    SJ_DATE_ZXSHGZ_ALL = "//*[@class='xm-iconfont xm-icon-quanxuan']".__add__(XPATH)  # 勾选全部按钮
    BUTTON_OK_ZX = "//*[@class='button28 button']".__add__(XPATH)  # 确认按钮
    ALERT_DELETE_OK = "//*[@class='aui_buttons']/button[1]".__add__(XPATH)  # 是否删除数据  1-是   2-否
    ALERT_TIPS_OK = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 确认按钮

