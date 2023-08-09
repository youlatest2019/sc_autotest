#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 10:01
# @Author   : yangshukun
# @File     : keyword_bsgl.py
from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRmbtdBmzhKeyword(BsglElementFrame, ZXBmzhElement, WebDriver):
    """征信编码转换"""

    def bsglMainFrame(self):
        """征信报送管理主框架"""
        self.SwitchFrame(self.BSGL_TAB_FRAME)

    def changeRmbtdBmzh(self, text, bm_code):
        """征信编码转换修改报送编码"""
        self.Click(self.INPUT_BMLX)
        self.Input(text, self.INPUT_BM_NAME)
        self.Click(self.BUTTON_REFRESH)
        self.ClearData(self.INPUT_MODIFY_BSBM)
        self.Input(bm_code, self.INPUT_MODIFY_BSBM)
        self.Click(self.INPUT_BM_NAME)


class BsglRmbtdCbmbglKeyword(BsglElementFrame, RmbtdCbmbglElement, WebDriver):
    """征信财报模板管理"""

    def changeCbRmbtdRefresh(self):
        """征信财报模板管理-刷新"""
        self.Click(self.BUTTON_REFRESH_CB)

    def changeCbRmbtdSykhmb(self):
        """征信财报模板管理-使用客户模板"""
        self.Click(self.BUTTON_SYKHMB)

    def changeCbRmbtdQzgxY(self, text):
        """征信财报模板管理-取值关系-使用客户模板"""
        self.Click(self.QZGX_TEXT_YES.format(text))

    def changeCbRmbtdSykhmbOK(self):
        """征信财报模板管理-确认按钮"""
        self.Click(self.BUTTON_SYKHMB_OK)

    def changeCbRmbtdSjxmc(self, text):
        """征信财报模板管理-数据项名称"""
        self.ClearData(self.INPUT_SJX_NAME)
        self.Input(text, self.INPUT_SJX_NAME)

    def changeCbRmbtdFrame(self):
        """征信财务报表frame"""
        self.SwitchFrameByElement(self.RMBTD_CB_FRAME)

    def changeCbRmbtdQzdygzb(self, text1):
        """征信财报模板管理-清除取值单元格坐标"""
        self.ClearData(self.INPUT_QZDYGZB.format(text1))

    def changeCbRmbtdQzdygzbok(self, text, text1):
        """征信财报模板管理-输入取值单元格坐标"""
        self.Input(text, self.INPUT_QZDYGZB.format(text1))

    def changeCbRmbtdSave(self):
        """征信财报模板管理-保存按钮"""
        self.Click(self.BUTTON_SAVE_CB)


class BscsRmbtdKeyword(BsglElementFrame,RRMBTDBscsElement, WebDriver):
    """征信报送参数界面关键字"""

    def RmbtdBscsFrame(self):
        self.SwitchFrame(self.BSGL_TAB_FRAME)

    def setRmbtdBsfs(self, zxbsfs):
        """征信报送方式--手动报送"""
        self.Click(self.INPUT_ZXBSFS)

    def setRmbtdCcfkwjdml(self, ccfkwjdml):
        """存储反馈文件的目录"""
        self.ClearData(self.INPUT_CCFKWJDML)
        self.Input(ccfkwjdml, self.INPUT_CCFKWJDML)

    def setRmbtdWjbdbcgml(self, wjbdbcgml):
        """文件本地保存根路径"""
        self.ClearData(self.INPUT_WJBDBCGLJ)
        self.Input(wjbdbcgml, self.INPUT_WJBDBCGLJ)

    def setRmbtdsftpip(self, ftpip):
        """sftp服务器ip"""
        self.ClearData(self.INPUT_SFTPIP)
        self.Input(ftpip, self.INPUT_SFTPIP)

    def setRmbtdsftpdk(self, ftpdk):
        """sftp服务器端口"""
        self.ClearData(self.INPUT_SFTPDK)
        self.Input(ftpdk, self.INPUT_SFTPDK)

    def setRmbtdsftpyhm(self, ftpyhm):
        """sftp用户名"""
        self.ClearData(self.INPUT_SFTPYHM)
        self.Input(ftpyhm, self.INPUT_SFTPYHM)

    def setRmbtdsftpmm(self, ftpmm):
        """sftp密码"""
        self.ClearData(self.INPUT_SFTPMM)
        self.Input(ftpmm, self.INPUT_SFTPMM)

    def setRmbtdfsml(self, fsml):
        """发送目录"""
        self.ClearData(self.INPUT_FSML)
        self.Input(fsml, self.INPUT_FSML)

    def setRmbtdsjtgjgqdm(self, sjtgjgqdm):
        """数据提供机构区段码"""
        self.ClearData(self.INPUT_SJTGJGQDM)
        self.Input(sjtgjgqdm, self.INPUT_SJTGJGQDM)

    def setRmbtdrhyclcxURL(self, rhyclcxURL):
        """人行预处理程序URL"""
        self.ClearData(self.INPUT_URL)
        self.Input(rhyclcxURL, self.INPUT_URL)

    def setRmbtdzxdm(self, zxdm):
        """征信中心代码"""
        self.ClearData(self.INPUT_ZXZXDM)
        self.Input(zxdm, self.INPUT_ZXZXDM)

    def setRmbtdywgljgdm(self, ywgljgdm):
        """业务管理机构代码"""
        self.ClearData(self.INPUT_YWGLJGDM)
        self.Input(ywgljgdm, self.INPUT_YWGLJGDM)

    def setRmbtdSbspYes(self):
        """设置上报审批--是"""
        self.Click(self.SET_ZXSBSP_YES)

    def setRmbtdSbspNo(self):
        """设置上报审批--否"""
        self.Click(self.SET_ZXSBSP_NO)

    def setRmbtdrgqrcgYes(self):
        """人工确认成功--是"""
        self.Click(self.SET_RGQR_YES)

    def setRmbtdrgqrcgNo(self):
        """人工确认成功--否"""
        self.Click(self.SET_RGQR_NO)

    def save(self):
        """保存设置"""
        self.Click(self.BUTTON_SAVE_ZX)

    def successZXClose(self):
        """关闭保存成功弹窗"""
        self.Click(self.SUCCESS_CLOSE_zx)  # 关闭成功弹窗
