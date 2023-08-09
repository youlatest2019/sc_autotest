#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/12/7 14:00
# @Author   : tangle
# @File     : page_sqgl.py

from Common.common_map import *


class SqglElementMain(object):
    """主页面功能按钮及tab页切换"""
    XTGL = "//span[text()='系统管理']".__add__(XPATH)  # 主菜单--系统管理
    SQGL = "//a[@menuid='Setings010103']".__add__(XPATH)  # 授权管理菜单按钮
    SQGL_TAB = "//li[@menuid='Setings010103']".__add__(XPATH)  # 授权管理标题菜单
    SWITCH_SQ = "//li[contains(@url,'{}')]".__add__(XPATH)  # 切换授权管理菜单的表达式，以占位符{}对品种进行站位，可以在关键字中传递
    PUB_GZLQX_DETAIL_FRAME = "//iframe[starts-with(@id,'LAYOUT_WIN_/SmartPage/BIZFLOW@bf_common_right_detail')]".__add__(
        XPATH)  # 工作流权限页面，编辑-权限明细frame表达式


class SqglElementFrame(object):
    """授权管理菜单相关frame"""
    SQGL_MAIN_FRAME = "ifrSetings010103"  # 授权管理页面主框架frameID
    SQGL_TAB_FRAME = "frame"  # 授权管理--功能按钮及数据主框架frameID
    SQ_PAGE_FRAME = "ifrmcontent"  # 各授权页签功能框架frameID


class YwmxSqElement(object):
    """业务模型授权页面"""
    CHOOSE_YWMXSQ_JS = "//option[text()='{}']".__add__(XPATH)  # 角色选择，使用{}占位符，可在案例中传参
    BUTTON_YWMXSQ_REFRESH = "refresh".__add__(ID)  # 刷新按钮
    CHOOSE_ALL_QXX = "//div[text()='权限项']/../../..//i[@class='layui-icon layui-icon-ok']".__add__(
        XPATH)  # 权限项-全选复选框
    BUTTON_YWMXSQ_SAVE = "//span[@onclick='doSave()']".__add__(
        XPATH)  # 保存按钮


class BsglSqElement(object):
    """报送管理授权页面相关元素"""
    CHOOSE_BSGLSQ_JS = "//option[text()='{}']".__add__(XPATH)  # 角色选择，使用{}占位符，可在案例中传参
    BUTTON_BSGLSQ_REFRESH = "reportManageGrant_form.refresh".__add__(ID)  # 刷新按钮
    CHOOSE_ALL_PZLB = "//table[@id='fixed_title']//span[@onclick='click_checkbox(this)']".__add__(XPATH)  # 品种列表-全选复选框
    BUTTON_BSGLSQ_SAVE = "reportManageGrant_list.save".__add__(ID)  # 保存按钮


class GzlglElement(object):
    """工作流管理页面相关元素"""
    CHOOSE_GZLGL_MKMC = "//*[@id='bf_version_ctrl_qry.app_code']/option[text()='{}']".__add__(
        XPATH)  # 模块名称选择，使用{}占位符，可在案例中传参
    INPUT_GZLGL_MKBH = "bf_version_ctrl_qry.fw_key".__add__(ID)  # 输入模块编码
    INPUT_GZLGL_MBMC = "bf_version_ctrl_qry.fw_name".__add__(ID)  # 输入模板名称
    CHOOSE_GZLGL_FL = "//*[@id='bf_version_ctrl_qry.ft_pid']/option[text()='{}']".__add__(
        XPATH)  # 分类选择，使用{}占位符，可在案例中传参
    CHOOSE_GZLGL_SYDW = "//*[@id='bf_version_ctrl_qry.cltNo']/option[text()='{}']".__add__(
        XPATH)  # 适用单位选择，使用{}占位符，可在案例中传参
    BUTTON_GZLGL_XZ = "bf_version_ctrl_qry.newFlow".__add__(ID)  # 新增按钮
    BUTTON_GZLGL_CX = "bf_version_ctrl_qry.refresh".__add__(ID)  # 查询按钮
    BUTTON_GZLGL_JH = "bf_version_ctrl_qry.active".__add__(ID)  # 激活按钮
    BUTTON_GZLGL_DEL = "bf_version_ctrl_qry.bf_del".__add__(ID)  # 删除按钮
    BUTTON_GZLGL_EXPORT = "bf_version_ctrl_list.export_sql".__add__(ID)  # 导出按钮
    BUTTON_GZLGL_VIEW = "bf_version_ctrl_list.view".__add__(ID)  # 查看按钮
    BUTTON_GZLGL_MODIFY = "bf_version_ctrl_list.modify".__add__(ID)  # 编辑按钮
    CHOOSE_GZLGL_ONE = "//*[@value='{}']/../../..//*[@id='bf_version_ctrl_list.fw_version' and @value='{}']/../../..//span[@class = 'checkbox_bg']".__add__(
        XPATH)  # 定位勾选的工作流单选框， 两个传参{}占位，第一个传入模块编号（如：RPTC.001），第二个传入版本号（如：1）。

class GzlqxElement(object):
    """工作流权限页面相关元素"""
    CHOOSE_GZLQX_MKMC = "//*[@id='bf_common_right_qry.app_code']/option[text()='{}']".__add__(
        XPATH)  # 模块名称选择，使用{}占位符，可在案例中传参
    INPUT_GZLQX_MKBH = "bf_common_right_qry.flow_key".__add__(ID)  # 输入模块编码
    INPUT_GZLQX_MBMC = "bf_common_right_qry.flow_name".__add__(ID)  # 输入模板名称
    BUTTON_GZLQX_CX = "bf_common_right_qry.refresh".__add__(ID)  # 查询按钮
    BUTTON_GZLQX_CZ = "bf_common_right_qry.refresh".__add__(ID)  # 重置按钮
    BUTTON_GZLQX_PLSQ = "bf_common_right_list.el".__add__(ID)  # 批量授权按钮
    BUTTON_GZLQX_DC = "bf_common_right_list.export_de".__add__(ID)  # 导出按钮
    BUTTON_JHMBLB_CK = "bf_common_right_list.btn_refresh".__add__(ID)  # 查看按钮
    BUTTON_JHMBLB_BJ = "bf_common_right_list.btn_edit".__add__(ID)  # 编辑按钮
    BUTTON_QXMX_ADD = "bf_common_right_detail_list.add".__add__(ID)  # 编辑页面权限明细-新增按钮
    BUTTON_QXMX_SAVE = "bf_common_right_detail_list.save".__add__(ID)  # 编辑页面权限明细-保存按钮
    BUTTON_QXMX_DEL = "//*[@class='button4 button']".__add__(XPATH)  # 编辑页面权限明细-删除按钮







