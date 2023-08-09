#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 17:42
# @Author   : yangshukun
# @File     : page_kqdb.py

from Common.common_map import *


class Rn1104kqdbMainPage(object):
    BUTTON_BSNRMC1 = "//*[@id='bsnrbhSel']//div[@class='xm-label single-row']".__add__(XPATH)  # 点击报送内容名称
    SELECT_BSNRMC1 = "//*[@class='xm-option   hide-icon' and @value='G0100']".__add__(XPATH)  # 选择报送内容名称
    BUTTON_BSQJ1 = "//*[@id='reportRange']//div[@class='xm-label single-row']".__add__(XPATH)  # 点击报送期间
    # SELECT_BSQJ1 = "//*[@class='xm-iconfont xm-icon-quanxuan']".__add__(XPATH)  # 全选报送期间
    SELECT_BSQJ1 = "//*[@class='layui-form-item']/div[2]//div[@class='scroll-body']/div[1]/i".__add__(XPATH)  # 选择第一个
    BUTTON_QZFS = "//*[@class='layui-edge']".__add__(XPATH)  # 点击取值方式
    SELECT_QZFS_BQZHYICBS = "//*[@class='layui-anim layui-anim-upbit']/dd[@lay-value='0']".__add__(
        XPATH)  # 选择取值方式-本期最后一次报送
    SELECT_QZFS_BQSCBS = "//*[@class='layui-anim layui-anim-upbit']/dd[@lay-value='1']".__add__(XPATH)  # 选择取值方式-本期首次报送
    BUTTON_REFRESH_RN1104_KQDB = "//*[@class='fa fa-refresh']".__add__(XPATH)  # 1104跨期对比页面--刷新按钮
    BUTTON_EXPORT_RN1104_KQDB = "//*[@class='fa fa-sign-out']".__add__(XPATH)  # 1104跨期对比页面--导出按钮


class RPBCCkqdbMainPage(object):
    BUTTON_BSNRMC2 = "//*[@id='bsnrbhSel']//div[@class='xm-label single-row']".__add__(XPATH)  # 点击报送内容名称
    SELECT_BSNRMC2 = "//*[@class='xm-option   hide-icon' and @value='A1333']".__add__(XPATH)  # 选择报送内容名称
    BUTTON_BSQJ2 = "//*[@id='reportRange']//div[@class='xm-label single-row']".__add__(XPATH)  # 点击报送期间
    SELECT_BSQJ2 = "//*[@class='xm-iconfont xm-icon-quanxuan']".__add__(XPATH)  # 全选报送期间
    BUTTON_QZFS = "//*[@class='layui-edge']".__add__(XPATH)  # 点击取值方式
    SELECT_QZFS_BQZHYICBS = "//*[@class='layui-anim layui-anim-upbit']/dd[@lay-value='0']".__add__(
        XPATH)  # 选择取值方式-本期最后一次报送
    SELECT_QZFS_BQSCBS = "//*[@class='layui-anim layui-anim-upbit']/dd[@lay-value='1']".__add__(XPATH)  # 选择取值方式-本期首次报送
    BUTTON_REFRESH_RPBCC_KQDB = "//*[@class='fa fa-refresh']".__add__(XPATH)  # 1104跨期对比页面--刷新按钮
    BUTTON_EXPORT_RPBCC_KQDB = "//*[@class='fa fa-sign-out']".__add__(XPATH)  # 1104跨期对比页面--导出按钮


class RFBSkqdbMainPage(object):
    INPUT_PUB_SJRQ = "rfbsMultiContrastForm.sjrq".__add__(NAME)  # 金数跨期对比数据日期
    BUTTON_QZFS = "//*[@id='rfbsMultiContrastForm.flag']".__add__(XPATH)  # 点击取值方式
    SELECT_QZFS_BQZHYICBS = "//*[@id='rfbsMultiContrastForm.flag']/option[@value='1']".__add__(XPATH)  # 选择取值方式-本期最后一次报送
    SELECT_QZFS_BQSCBS = "//*[@id='rfbsMultiContrastForm.flag']/option[@value='0']".__add__(XPATH)  # 选择取值方式-本期首次报送
    BUTTON_REFRESH_RFBS_KQDB = "//*[@class='button31 button']".__add__(XPATH)  # 金数跨期对比页面--刷新按钮
    BUTTON_EXPORT_RFBS_KQDB = "//*[@class='button28 button']".__add__(XPATH)  # 金数跨期对比页面--导出按钮
    BUTTNO_DWCKYE = "//*[@class='currentBtnLeft']/span[text()='单位存款余额']".__add__(XPATH)  # 单位存款余额
    BUTTNO_DWCKFSE = "//*[@class='noBtnRight']/span[text()='单位存款发生额']".__add__(XPATH)  # 单位存款发生额
    BUTTNO_JDSJHCXXE = "//*[@class='noBtn']/span[text()='极端数据核查信息']".__add__(XPATH)  # 极端数据核查信息
    BUTTNO_CLFTY = "//*[@class='noBtn']/span[text()='存量非同业单位存款信息大集中数据核对']".__add__(XPATH)  # 存量非同业单位存款信息大集中数据核对
