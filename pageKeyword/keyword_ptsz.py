#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 10:01
# @Author   : yangshukun
# @File     : keyword_bsgl_common.py
from pageElement.page_bsgl import *
from pageElement.page_ptsz import *
from baseOperation.WebOperation import *
from Common.getconf import *


class PTSZMainKeyword(PTSZElementMain, PtszCwgsElementFrame, PtszJtgsElementFrame, WebDriver):

    def intoPtszMainMenu(self):
        """进入平台设置主界面"""
        self.RefreshPage()
        self.MouseFouce(self.XTGL)
        self.Click(self.PTSZ)
        self.Click(self.PTSZ_TAB)

    def switchToPTSZBaseFrame(self):
        """切换主框架"""
        self.GotoSleep(0.5)
        self.QuiteFrame()
        self.SwitchFrame(self.MAIN_FRAME)
        self.SwitchFrame(self.TAB_FRAME)

    def intoBsjgxxTab(self):
        """选报送机构信息"""
        self.Click(self.SWITCH_PTSZ.format('报送机构信息'))

    def switchGSYQFrame(self):
        """切换到财务/集团公司页签框架"""
        self.SwitchFrame(self.GSYQ_FRAME)

    def intoGzrszTab(self):
        """选工作日设置"""
        self.Click(self.SWITCH_PTSZ.format('工作日设置'))

    def intoBmcshTab(self):
        """选编码初始化"""
        self.Click(self.SWITCH_PTSZ.format('编码初始化'))

    def swithToCwgs(self):
        """财务公司"""
        self.Click(self.CHOICE_FUNC_TAB.format('财务公司'))
        self.SwitchFrame(self.FRAME)

    def swithToJtgs(self):
        """集团公司"""
        self.Click(self.CHOICE_FUNC_TAB.format('集团公司'))

    def swithToYwbz(self):
        """业务币种"""
        self.Click(self.CHOICE_FUNC_TAB.format('业务币种'))

    def swithToXydj(self):
        """信用等级"""
        self.Click(self.CHOICE_FUNC_TAB.format('信用等级'))


class CWGSMainKeyword(PTSZElementMain, PtszCwgsElementFrame, PtszJtgsElementFrame, WebDriver):
    def tbCWGS(self):
        """同步财务公司"""
        self.Click(self.TB)

    def sxCWGS(self):
        """刷新财务公司"""
        self.Click(self.SX)

    def SaveCWGS(self):
        """保存财务公司"""
        self.Click(self.BC)

    ##财务公司
    def addCwgs_ggxx(self, sjkzr_name, sjkzr_no, cwgsgdxx_zjhm):
        """新增财务公司-公共信息"""
        self.ClearData(self.CWGSQC)  # 清除财务公司全称
        self.Input('财务公司全称', self.CWGSQC)  # 财务公司全称
        self.ClearData(self.TYSHXYDM)  # 清除统一社会信用代码
        self.Input('91510100MA61RTKK6Q', self.TYSHXYDM)  # 统一社会信用代码
        self.ClearData(self.JGBM)  # 清除机构编码
        self.Input('JGBM0123456789', self.JGBM)  # 机构编码
        self.ClearData(self.QQFRSBBM)  # 清除全球法人识别编码
        self.Input('123456', self.QQFRSBBM)  # 全球法人识别编码
        self.ClearData(self.JRXKZH)  # 清除金融许可证号
        self.Input('234234234', self.JRXKZH)  # 金融许可证号
        self.ClearData(self.JRJGDM)  # 清除金融机构代码
        self.Input('111111', self.JRJGDM)  # 金融机构代码
        self.ClearData(self.JGH_NB)  # 清除机构号（内部）
        self.Input('00101', self.JGH_NB)  # 机构号（内部）
        self.ClearData(self.KHBM_NB)  # 清除客户编码（内部）
        self.Input('321654', self.KHBM_NB)  # 客户编码（内部）
        self.ClearData(self.CYRYS)  # 清除从业人员数
        self.Input('1000', self.CYRYS)  # 从业人员数
        # self.ClearData(self.JJCF)  # 清除经济成分
        self.Click(self.JJCF)  # 经济成分
        # self.ClearData(self.QYGM)  # 清除企业规模
        self.Click(self.QYGM)  # 企业规模
        self.ClearData(self.ZFHH)  # 清除支付行号
        self.Input('123123', self.ZFHH)  # 支付行号
        # self.ClearData(self.JYZT)  # 清除经营状态
        self.Click(self.JYZT)  # 经营状态
        # self.ClearData(self.CKZBJJCFS)  # 清除存款准备金缴存方式
        self.Click(self.CKZBJJCFS)  # 存款准备金缴存方式
        # self.ClearData(self.SFSS)  # 清除是否上市
        self.Click(self.SFSS)  # 是否上市
        """新增财务公司-注册信息"""
        # self.ClearData(self.CLRQ)  # 清除成立日期
        self.Click(self.CLRQ)  # 点击成立日期
        self.Input('2020-12-03', self.CLRQ)  # 输入成立日期
        # self.ClearData(self.ZCDQ_S_ZXS)  # 清除注册地区——直辖市/省
        self.Click(self.ZCDQ_S_ZXS)  # 注册地区——直辖市/省
        # self.ClearData(self.ZCDQ_S_Q)  # 清除注册地区——市/区
        self.Click(self.ZCDQ_S_Q)  # 注册地区——市/区
        self.ClearData(self.ZCZB)  # 清除注册资本
        self.Input('100000', self.ZCZB)  # 注册资本
        self.ClearData(self.YZBM)  # 清除邮政编码
        self.Input('565656', self.YZBM)  # 邮政编码
        self.ClearData(self.ZCDZ)  # 清除注册地址
        self.Input('注册地址', self.ZCDZ)  # 注册地址
        """新增财务公司-法定代表人"""
        self.ClearData(self.FDDBR_XM)  # 清除姓名
        self.Input('法定代表人', self.FDDBR_XM)  # 姓名
        # self.ClearData(self.FDDBR_ZJLB)  # 清除证件类别
        self.Click(self.FDDBR_ZJLB)  # 证件类别
        self.ClearData(self.FDDBR_ZJHM)  # 清除证件号码
        self.Input('123456', self.FDDBR_ZJHM)  # 证件号码
        """新增财务公司-主要负责人（EAST报送）"""
        self.ClearData(self.ZYFZR_XM)  # 清除姓名
        self.Input('姓名', self.ZYFZR_XM)  # 姓名
        # self.ClearData(self.ZYFZR_ZJLB)  # 清除证件类别
        self.Click(self.ZYFZR_ZJLB)  # 证件类别
        self.ClearData(self.ZYFZR_ZJHM)  # 清除证件号码
        self.Input('123456', self.ZYFZR_ZJHM)  # 证件号码
        self.ClearData(self.ZYFZR_ZW)  # 清除职务
        self.Input('职务', self.ZYFZR_ZW)  # 职务
        self.ClearData(self.ZYFZR_LXDH)  # 清除联系电话
        self.Input('1789789789', self.ZYFZR_LXDH)  # 联系电话
        """新增财务公司-对外联系人"""
        self.ClearData(self.DWLXR_LXR)  # 清除联系人
        self.Input('联系人', self.DWLXR_LXR)  # 联系人
        self.ClearData(self.DWLXR_LXDH)  # 清除联系电话
        self.Input('1789789789', self.DWLXR_LXDH)  # 联系电话
        """新增财务公司-实际控制人"""
        self.Click(self.SJKZR_XZ)  # 实际控制人-新增
        self.SwitchFrame(self.SJKZR_FRAME)
        self.ClearData(self.SJKZR_MC)  # 清除名称
        self.Input(sjkzr_name, self.SJKZR_MC)  # 名称
        # self.ClearData(self.SJKZR_ZJLX)  # 清除证件类型
        self.Click(self.SJKZR_ZJLX)  # 证件类型
        self.ClearData(self.SJKZR_ZJHM)  # 清除证件号码
        self.Input(sjkzr_no, self.SJKZR_ZJHM)  # 证件号码
        self.Click(self.SJKZR_BC)  # 保存
        self.SwitchFatherFrame()
        # self.Click(self.QD_FRAME)
        self.Click(self.SJKZR_QD)  # 确定
        """新增财务公司-财务公司股东信息"""
        self.Click(self.CWGSGDXX_XZ)  # 财务公司股东信息-新增
        self.SwitchFrame(self.CWGGGDXX_FRAME)
        self.ClearData(self.CWGSGDXX_GDBH)  # 清除股东编号
        self.Input('001', self.CWGSGDXX_GDBH)  # 股东编号
        self.ClearData(self.CWGSGDXX_GDMC)  # 清除股东名称
        self.Input('股东名称', self.CWGSGDXX_GDMC)  # 股东名称
        self.ClearData(self.CWGSGDXX_QQFRSBBM)  # 清除全球法人识别编码
        self.Input('123123', self.CWGSGDXX_QQFRSBBM)  # 全球法人识别编码
        # self.ClearData(self.CWGSGDXX_SSHY)  # 清除所属行业
        self.Click(self.CWGSGDXX_SSHY)  # 所属行业
        # self.ClearData(self.CWGSGDXX_GDZT)  # 清除股东状态
        self.Click(self.CWGSGDXX_GDZT)  # 股东状态
        # self.ClearData(self.CWGSGDXX_ZJLB)  # 清除证件类别
        self.Click(self.CWGSGDXX_ZJLB)  # 证件类别
        self.ClearData(self.CWGSGDXX_ZJHM)  # 清除证件号码
        self.Input(cwgsgdxx_zjhm, self.CWGSGDXX_ZJHM)  # 证件号码
        self.ClearData(self.CWGSGDXX_GDDZ)  # 清除股东地址
        self.Input('股东地址', self.CWGSGDXX_GDDZ)  # 股东地址
        self.ClearData(self.CWGSGDXX_ZCFZL)  # 清除资产负债率
        self.Input('20', self.CWGSGDXX_ZCFZL)  # 资产负债率
        self.ClearData(self.CWGSGDXX_JLR)  # 清除净利润
        self.Input('2000000', self.CWGSGDXX_JLR)  # 净利润
        self.ClearData(self.CWGSGDXX_RGRQ)  # 清除入股日期
        self.Click(self.CWGSGDXX_RGRQ)  # 点击入股日期
        self.Input('2021-03-01', self.CWGSGDXX_RGRQ)  # 输入入股日期
        self.ClearData(self.CWGSGDXX_CZE)  # 清除出资额
        self.Input('20000', self.CWGSGDXX_CZE)  # 出资额
        self.ClearData(self.CWGSGDXX_CGBL)  # 清除持股比例
        self.Input('30', self.CWGSGDXX_CGBL)  # 持股比例
        # self.ClearData(self.TZQTJRJGBZ)  # 清除投资其他金融机构标志
        self.Click(self.TZQTJRJGBZ)  # 投资其他金融机构标志
        self.Click(self.CWGSGDXX_BC)  # 保存
        self.SwitchFatherFrame()
        self.Click(self.SJKZR_QD)  # 确定


class JTGSMainKeyword(PTSZElementMain, PtszCwgsElementFrame, PtszJtgsElementFrame, WebDriver):
    def sxJTGS(self):
        """刷新集团公司"""
        self.Click(self.SX)

    def SaveCWGS(self):
        """保存集团公司"""
        self.Click(self.BC)

    ##集团公司
    def addJtgs_ggxx(self):
        """新增集团公司"""
        self.SwitchFrame(self.FRAME)
        self.ClearData(self.JGQC)  # 清除机构全称
        self.Input('机构全称', self.JGQC)  # 机构全称
        self.ClearData(self.JGJC)  # 清除机构简称
        self.Input('机构简称', self.JGJC)  # 机构简称
        self.ClearData(self.JGBM)  # 清除机构编码
        self.Input('123456', self.JGBM)  # 机构编码
        self.ClearData(self.JTGS_TYSHXYDM)  # 清除统一社会信用代码
        self.Input('123456789410231526', self.JTGS_TYSHXYDM)  # *统一社会信用代码
