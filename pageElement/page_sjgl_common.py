#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/30 17:10
# @Author   : yangshukun
# @File     : page_sjgl_common.py
from Common.common_map import *


class SjglMainMenueElement():
    """数据管理菜单"""
    SJGL_MAIN_MENUE = "//span[text()='数据管理']".__add__(XPATH)  # 数据管理菜单
    DATASET_MANAGE_MENUE = "//a[@menuid='Supplement010501']".__add__(XPATH)  # 数据集管理菜单
    DATASET_MANAGE_TAG = "//li[@menuid='Supplement010501']".__add__(XPATH)  # 数据集管理标题栏页签
    DATASET_QUERY_MENUE = "//a[@menuid='Supplement010502']".__add__(XPATH)  # 数据查询菜单
    DATASET_QUERY_TAG = "//li[@menuid='Supplement010502']".__add__(XPATH)  # 数据查询标题栏页签
    DATASET_BL_MENUE = "//a[@menuid='Supplement010503']".__add__(XPATH)  # 数据补录菜单
    DATASET_BL_TAG = "//li[@menuid='Supplement010503']".__add__(XPATH)  # 数据补录标题栏页签
    DATASET_SQ_MENUE = "//a[@menuid='Supplement010504']".__add__(XPATH)  # 数据授权菜单
    DATASET_SQ_TAG = "//li[@menuid='Supplement010504']".__add__(XPATH)  # 数据授权标题栏页签
    DATASET_SP_MENUE = "//a[@menuid='Supplement010505']".__add__(XPATH)  # 数据审批菜单
    DATASET_SP_TAG = "//li[@menuid='Supplement010505']".__add__(XPATH)  # 数据审批标题栏页签
    BUTTON_DATA_EXTRACTION = "//h5[text()='报送数据']/..//li[2]/a[text()='数据抽取情况']".__add__(XPATH)  # 数据抽取情况
    DATA_EXTRACTION_BT = "//li[@class='tagFocus']/a".__add__(XPATH)  # 数据抽取情况标题栏
    DATA_EXTRACTION_FRAME = "ifrSupplement010202"  # 数据抽取情况页面frame


class SjglDataExtractionElement():
    """数据抽取情况"""
    DATA_EXTRACT_BSPZ = "//*[@class='bspzbh']/option[text()='{}']".__add__(XPATH)  # 查询条件-报送品种  传品种中文名称
    DATA_EXTRACT_TASK_NAME = "//*[@name='reportName']".__add__(XPATH)  # 查询条件-任务名称
    DATA_EXTRACT_TASK_CODE = "//*[@name='reportNo']".__add__(XPATH)  # 查询条件-任务号
    DATE_FRAME = "//*[@id='_my97DP']/iframe".__add__(XPATH)  # 数据日期弹窗frame
    DATA_EXTRACT_START_DATE = "//*[@name='startDate']".__add__(XPATH)  # 查询条件-数据日期-开始
    DATE_CLEAR = "//*[@id='dpClearInput']".__add__(XPATH)  # 查询条件-数据日期-清空按钮
    DATA_EXTRACT_END_DATE = "//*[@name='endDate']".__add__(XPATH)  # 查询条件--数据日期-结束
    DATA_EXTRACT_FXK_ALL = "//*[@id='btSelectItemVal0']".__add__(XPATH)  # 全选复选框
    DATA_EXTRACT_REFRESH = "//*[@id='refreshBtn']".__add__(XPATH)  # 刷新按钮
    DATA_EXTRACT_CLEAR_DATA = "//*[@class='button25 button']".__add__(XPATH)  # 清空数据按钮
    DATA_EXTRACT_DATA_AGAIN = "//*[@class='button30 button']".__add__(XPATH)  # 重新取数按钮
    DATA_EXTRACT_ALERT_INFO = "//*[@class='aui_content']".__add__(XPATH)  # 弹窗信息
    DATA_EXTRACT_ALERT_OK = "//*[@class='aui_buttons']/button[text()='是']".__add__(XPATH)  # 是否确认抽取   是
    DATA_NUMBER = "//*[@id='pub_check_page_list.contentCount']".__add__(XPATH)  # 数据条数
    ALERT_OK_BUTTON = "//*[@class=' aui_state_highlight']".__add__(XPATH)  # 确认按钮
    DATA_EXTRACT_MC_CS = "//*[@class='treegrid-402841LCTS01-20230105 treegrid-parent-1000']/td[2]".__add__(
        XPATH)  # 检查查询结果
