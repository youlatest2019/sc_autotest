#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/30 17:08
# @Author   : yangshukun
# @File     : page_dataset_management.py

from Common.common_map import *


class DataSetManageFrame():
    """数据集管理页面frame类"""
    FRAME_MAIN_PAGE = "ifrSupplement010501"  # 数据集管理--主页面frame


class DataSetManageMainPage():
    """数据集管理主页面元素"""
    BUTTON_GROUP_FOR_DATASET = "groupId".__add__(ID)  # 数据集管理--主页面--数据集分组下拉框
    SELECT_GROUP_NAME_OF_DATASET = "//div[text()='{}']/../i[last()]".__add__(XPATH)  # 数据集管理--主页面--根据输入名称选择数据集分组
    INPUT_DATASET_NAME_QUERY = "datasetName".__add__(ID)  # 数据集管理--主页面--数据集名称查询输入框
    BUTTON_RESET_FOR_DATASET = "//button[@id='saveDatasetBase']".__add__(XPATH)  # 数据集管理--主页面--重置按钮
    BUTTON_REFRESH_DATASET_MAIN_PAGE = "refresh".__add__(ID)  # 数据集管理--主页面--刷新按钮
    BUTTON_ADD_GROUP_FOR_DATASET = "//button[@lay-filter='addGroup']".__add__(XPATH)  # 数据集管理--主页面--新建分组
    BUTTON_ADD_DATASET_FOR_DATASET = "//button[@lay-filter='addDataSet']".__add__(XPATH)  # 数据集管理--主页面--新建数据集
    BUTTON_EDIT_GROUP_FOR_DATASET = "//a[@lay-event='editGroup']".__add__(XPATH)  # 数据集管理--主页面--编辑分组
    BUTTON_DEL_GROUP_FOR_DATASET = "//a[@lay-event='deleteGroup']".__add__(XPATH)  # 数据集管理--主页面--删除分组
    BUTTON_EDIT_DATASET_FOR_DATASET = "//a[@lay-event='editDataSetDetail']".__add__(XPATH)  # 数据集管理--主页面--编辑数据集
    BUTTON_DEL_DATASET_FOR_DATASET = "//a[@lay-event='deleteDataSet']".__add__(XPATH)  # 数据集管理--主页面--删除数据集
    DATA_TABLE_LIST_GROUP_NAME_DATASET = "//td[@data-field='datasetName' and @title='{}']".__add__(XPATH)  # 数据集管理--主页面--数据列表，分组名称


class DataSetGroupPage():
    """数据集分组新增，编辑页面元素"""
    FRAME_GROUP_PAGE = "//iframe[starts-with(@id,'layui-layer-iframe')]".__add__(XPATH)  # 数据集管理--主页面--分组管理页面frame
    BUTTON_UP_GROUP_DATASET = "pgroup".__add__(ID)  # 数据集管理--主页面--分组管理--上级分组选择按钮
    SELECT_UP_GROUP_DATASET = "//div[@class='xm-option-content' and text()='{}']/../i[last()]".__add__(XPATH)  # 数据集管理--主页面--分组管理--上级分组下拉数据列表根据分组名称选择
    INPUT_GROUP_NAME_DATASET = "//input[@name='groupName']".__add__(XPATH)  # 数据集管理--主页面--分组管理--分组名称输入
    INPUT_GROUP_SORT_DATASET = "//input[@name='groupSort']".__add__(XPATH)  # 数据集管理--主页面--分组管理--分组排序输入
    BUTTON_GROUP_SAVE_DATASET = "//button[@lay-filter='saveGroupDetail']".__add__(XPATH)  # 数据集管理--主页面--分组管理--分组保存


class DataSetConfigBaseInfoPage():
    """数据集配置--基本信息页面"""
    FRAME_BASE_INFO_PAGE = "//iframe[starts-with(@id,'layui-layer-iframe')]".__add__(XPATH)  # 数据集管理--主页面--数据集配置基本信息frame
    INPUT_DATASET_NAME_DATASET = "datasetName".__add__(NAME)  # 数据集管理--数据集配置--基本信息--数据集名称输入框
    BUTTON_GET_DATASET_CODE_DATASET = "getNewDatasetCode".__add__(ID)  # 数据集管理--数据集配置--基本信息--获取编码按钮
    BUTTON_SELGROUP_DATASET = "selGroupId".__add__(ID)  # 数据集管理--数据集配置--基本信息--所属分组按钮
    SELECT_SEL_GROUP_DATASET = "//div[@class='xm-option-content' and text()='{}']/../i[last()]".__add__(XPATH)  # 数据集管理--数据集配置--基本信息--所属分组下拉数据选择
    INPUT_EXPORT_NAME_DATASET = "exportFileName".__add__(NAME)  # 数据集管理--数据集配置--基本信息--导出文件名称输入框
    INPUT_DESCRIBE_DATASET = "//textarea[@name='comm']".__add__(XPATH)  # 数据集管理--数据集配置--基本信息--描述信息输入框
    BUTTON_SAVE_BASE_INFO_DATASET = "//button[@onclick='saveDatasetBase();']".__add__(XPATH)  # 数据集管理--数据集配置--基本信息--保存按钮
    DATA_SETGROUP_FIRST_DATASET = "//div[@id='selGroupId']/xm-select/div[last()]/div/div[last()]/div[1]/i[last()]".__add__(XPATH)  # 数据集管理--数据集配置--基本信息--所属分组第一个数据
    BUTTON_CLOSE_FOR_BASE_INFO_DATASET = "//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']".__add__(XPATH)  # 数据集管理--数据集配置--基本信息--右上角关闭
    TAB_BASE_INFO = "//li[@lay-id='baseConfig']"  # 数据集配置--基本信息TAB页签


class DataSetConfigCheckRulePage():
    """数据集配置--查询规则配置页面"""
    FRAME_CHECK_RULE_MAIN_PAGE = "//iframe[starts-with(@id,'layui-layer-iframe')]".__add__(XPATH)  # 数据集管理--主页面--数据集配置--查询规则frame
    TAB_CHECK_RULE = "//li[@lay-id='dataConfig']"  # 数据集配置--查询规则TAB页签
    SELECT_DATA_SOURCE = "//select[@name='dataSource']/../div[1]/dl/dd[@lay-value='{}']".__add__(XPATH)  # 数据集配置--查询规则--数据源选择
    INPUT_SQL = "querySqlTextarea".__add__(ID)  # 数据集配置--查询规则--SQL语句输入
    BUTTON_PARAMCONFIG = "//button[@onclick='paramConfig();']".__add__(XPATH)  # 数据集配置--查询规则--参数配置按钮
    BUTTON_TEST_SQL = "//button[@onclick='testSql();']".__add__(XPATH)  # 数据集配置--查询规则--测试按钮
    BUTTON_ADD_CHECK_FILED = "//button[@onclick='addParam(this);']".__add__(XPATH)  # 数据集配置--查询规则--新增查询条件
    BUTTON_REFRESH_QUERY_RULE = "//button[@id='queryRuleRefreshBtn']".__add__(XPATH)  # 数据集配置--查询规则--刷新按钮
    BUTTON_SAVE_QUERY_RULE = "//button[@onclick='saveQueryRule();']".__add__(XPATH)  # 数据集配置--查询规则--保存按钮
    FRAME_PARAM_CONFIG_PAGE = "//iframe[starts-with(@id,'layui-layer-iframe')]".__add__(XPATH)  # 数据集管理--主页面--数据集配置--查询规则--参数配置弹窗frame
    SELECT_PARAM_CONFIG_CODE = "//input[@name='paramCode']/../../dl/dd[@lay-value='{}']"  # 数据集配置--查询规则--参数配置--参数编码选择（传参数名称）
    SELECT_PARAM_CONFIG_TYPE = "//select[@name='inputType']/../div/dl/dd[@lay-value='{}']"
    # 数据集配置--查询规则--参数配置--参数类型选择（传英文名，映射关系：input--文本，currency--金额，number--数值，date--日期，datetime--时间戳，select--单码值，xmSelect--多码值，textArea--多行文本）
    INPUT_PARAM_CONFIG_NAME = "//input[@name='paramName']".__add__(XPATH)  # 数据集配置--查询规则--参数配置--参数名称输入框
    INPUT_PARAM_CONFIG_DEFAULT_VALUE = "//textarea[@name='defaultValue']".__add__(XPATH)  # 数据集配置--查询规则--参数配置--参数默认值输入框
    BUTTON_DEL_PARAM_CONFIG = "deltParamConfig".__add__(ID)  # 数据集配置--查询规则--参数配置--删除按钮
    BUTTON_SAVE_PARAM_CONFIG = "saveParamConfig".__add__(ID)  # 数据集配置--查询规则--参数配置--保存按钮
    BUTTON_CLOSE_WINDOW = "//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']".__add__(XPATH)  # 数据集配置--查询规则--参数配置--右上角关闭弹窗按钮
