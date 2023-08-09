#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/10/31 17:08
# @Author   : tangle
# @File     : page_dataset_sq.py

from Common.common_map import *


class DataSetSqFrame():
    """数据集授权页面frame类"""
    FRAME_SQ_PAGE = "ifrSupplement010504"  # 数据集授权--主页面frame
    FRAME_USERQUERY_PAGE = "//iframe[starts-with(@id,'layui-layer-iframe')]".__add__(
        XPATH)  # 数据集授权--人员权限查询页面frame


class DataSetSqMainPage():
    """数据集授权页面元素"""
    BUTTON_USERXM = "userXmSelect".__add__(ID)  # 数据集授权--人员姓名下拉框
    INPUT_USERXM = "//*[@id='userXmSelect']/xm-select/div[3]/div/div/div[1]/input".__add__(
        XPATH)  # 数据集授权--人员姓名下拉框-输入人员姓名
    SELECT_USERXM = "//*[@class='xm-option   hide-icon']/div[text()='{}']".__add__(
        XPATH)  # 数据集授权--根据输入人员姓名选择，人员姓名使用{}占位符，可在案例中传参
    SELECT_SJJFZ_ALL_SQ = "//span[text()='{}']/../div/i".__add__(XPATH)  # 数据集授权--权限项--勾选数据集选框，使用{}占位符，可在案例中传参
    BUTTON_SAVE_SQ = "saveGrant".__add__(ID)  # 数据集授权--保存按钮
    BUTTON_REFRESH_SQ = "refresh".__add__(ID)  # 数据集授权--刷新按钮
    BUTTON_USERQUERY = "userQuery".__add__(ID)  # 数据集授权--人员权限查询按钮
    REFRESH_USERQUERY = "//*[@class='fa fa-refresh ']".__add__(XPATH)  # 数据集授权--人员权限查询页面刷新
    CLOSE_USERQUERY = "//*[@class='layui-layer-ico layui-layer-close layui-layer-close1']".__add__(
        XPATH)  # 数据集授权--关闭人员权限查询

    MSG_SELECT_SUCC = "//div[@class='layui-unselect layui-form-checkbox layui-form-checked']/../span[text()='{}']".__add__(
        XPATH)  # 断言勾选成功，使用{}占位符，可在案例中传参
    MSG_USERQUERY = "//span[text()='{}']".__add__(
        XPATH)  # 人员权限查询页面-断言授权后的数据集信息是否存在，使用{}占位符，可在案例中传参

    BUTTON_ROLE = "roleXmSelect".__add__(ID)  # 数据集授权--角色下拉框
    INPUT_ROLE = "//*[@id='roleXmSelect']/xm-select/div[3]/div/div/div[1]/input".__add__(XPATH)  # 数据集授权--角色下拉框-输入角色
    SELECT_ROLE = "//*[@class='xm-option   hide-icon']/div[text()='{}']".__add__(
        XPATH)  # 数据集授权--根据输入角色选择，角色使用{}占位符，可在案例中传参
