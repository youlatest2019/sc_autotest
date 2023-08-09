#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/12/7 14:00
# @Author   : tangle
# @File     : keyword_sqgl_common.py

from pageElement.page_sqgl import *
from baseOperation.WebOperation import *


class SqglMainKeyword(SqglElementMain, SqglElementFrame, WebDriver):

    def intoSqglMainMenu(self):
        """进入授权管理主界面"""
        self.RefreshPage()
        self.MouseFouce(self.XTGL)
        self.Click(self.SQGL)
        self.Click(self.SQGL_TAB)

    def switchToSqglBaseFrame(self):
        """切换主框架"""
        self.GotoSleep(0.5)
        self.QuiteFrame()
        self.SwitchFrame(self.SQGL_MAIN_FRAME)
        self.SwitchFrame(self.SQGL_TAB_FRAME)

    def switchSqglFrame(self):
        """切换到授权管理页签框架"""
        self.SwitchFrame(self.SQ_PAGE_FRAME)

    def intoYwglSqTab(self):
        """选业务模型授权"""
        self.Click(self.SWITCH_SQ.format('业务模型授权'))

    def intoBsglSqTab(self):
        """选报送管理授权"""
        self.Click(self.SWITCH_SQ.format('报送管理授权'))

    def intoGzlglTab(self):
        """选工作流管理"""
        self.Click(self.SWITCH_SQ.format('工作流管理'))

    def intoGzlqxTab(self):
        """选工作流权限"""
        self.Click(self.SWITCH_SQ.format('工作流权限'))


class YwglSqKeyword(YwmxSqElement, WebDriver):
    """业务模型授权"""

    def chioceYwglSqJs(self, js):
        """选择角色"""
        self.Click(self.CHOOSE_YWMXSQ_JS.format(js))

    def clickYwglSqRefresh(self):
        """刷新按钮"""
        self.Click(self.BUTTON_YWMXSQ_REFRESH)

    def chioceYwglSqAllQxx(self, text):
        """全选业务列表-权限项复选框"""
        self.Click(self.CHOOSE_ALL_QXX.format(text))

    def clickYwglSqSave(self):
        """保存按钮"""
        self.Click(self.BUTTON_YWMXSQ_SAVE)


class BsglSqKeyword(BsglSqElement, WebDriver):
    """报送管理授权"""

    def chioceBsglSqJs(self, js):
        """选择角色"""
        self.Click(self.CHOOSE_BSGLSQ_JS.format(js))

    def clickBsglSqRefresh(self):
        """刷新按钮"""
        self.Click(self.BUTTON_BSGLSQ_REFRESH)

    def chioceBsglSqAllpz(self):
        """全选品种列表-复选框"""
        self.Click(self.CHOOSE_ALL_PZLB)

    def clickBsglSqSave(self):
        """保存按钮"""
        self.Click(self.BUTTON_BSGLSQ_SAVE)


class GzlglKeyword(GzlglElement, WebDriver):
    """工作流管理授权"""

    def chioceGzlglMkmc(self, mkmc):
        """选择模块名称"""
        self.Click(self.CHOOSE_GZLGL_MKMC.format(mkmc))

    def inputGzlglMkbh(self, mkbh):
        """输入模块编号"""
        self.Input(mkbh, self.INPUT_GZLGL_MKBH)

    def inputGzlglMbmc(self, mbmc):
        """输入模板名称"""
        self.Input(mbmc, self.INPUT_GZLGL_MBMC)

    def chioceGzlglFl(self, fl):
        """选择分类"""
        self.Click(self.CHOOSE_GZLGL_FL.format(fl))

    def chioceGzlglSydw(self, sydw):
        """选择适用单位"""
        self.Click(self.CHOOSE_GZLGL_SYDW.format(sydw))

    def clickGzlglAdd(self):
        """新增按钮"""
        self.Click(self.BUTTON_GZLGL_XZ)

    def clickGzlglCx(self):
        """查询按钮"""
        self.Click(self.BUTTON_GZLGL_CX)

    def clickGzlglJh(self):
        """激活按钮"""
        self.Click(self.BUTTON_GZLGL_JH)
        self.AlertAccept()

    def clickGzlglDel(self):
        """删除按钮"""
        self.Click(self.BUTTON_GZLGL_DEL)

    def clickBsglSqDc(self):
        """导出按钮"""
        self.Click(self.BUTTON_GZLGL_EXPORT)

    def clickGzlgCk(self):
        """查看按钮"""
        self.Click(self.BUTTON_GZLGL_VIEW)

    def clickGzlglBj(self):
        """编辑按钮"""
        self.Click(self.BUTTON_GZLGL_MODIFY)

    def chioceGzlglOne(self, mkbh, version):
        """定位勾选的工作流单选框-第一个传入模块编号（如：RPTC.001），第二个传入版本号（如：1）"""
        self.Click(self.CHOOSE_GZLGL_ONE.format(mkbh, version))


class GzlqxKeyword(SqglElementMain, GzlqxElement, WebDriver):
    """工作流权限"""

    def chioceGzlqxMkmc(self, mkmc):
        """选择模块名称"""
        self.Click(self.CHOOSE_GZLQX_MKMC.format(mkmc))

    def inputGzlqxMkbh(self, mkbh):
        """输入模块编号"""
        self.Input(mkbh, self.INPUT_GZLQX_MKBH)

    def inputGzlqxMbmc(self, mbmc):
        """输入模板名称"""
        self.Input(mbmc, self.INPUT_GZLQX_MBMC)

    def clickGzlqxCx(self):
        """查询按钮"""
        self.Click(self.BUTTON_GZLQX_CX)

    def clickGzlqxCz(self):
        """重置按钮"""
        self.Click(self.BUTTON_GZLQX_CZ)

    def clickGzlqxPldc(self):
        """批量导出按钮"""
        self.Click(self.BUTTON_GZLQX_PLSQ)

    def clickGzlqxDc(self):
        """导出按钮"""
        self.Click(self.BUTTON_GZLQX_DC)

    def clickJhmblbCk(self):
        """激活模板列表-查看按钮"""
        self.Click(self.BUTTON_JHMBLB_CK)

    def clickJhmblbBj(self):
        """激活模板列表-编辑按钮"""
        self.Click(self.BUTTON_JHMBLB_BJ)

    def switchToBjQxmxFrame(self):
        """切换到编辑-权限明细页面frame"""
        self.QuiteFrame()
        self.SwitchFrameByElement(self.PUB_GZLQX_DETAIL_FRAME)

    def clickQxmxAdd(self):
        """权限明细页面-新增按钮"""
        self.Click(self.BUTTON_QXMX_ADD)

    def clickQxmxSave(self):
        """权限明细页面-保存按钮"""
        self.Click(self.BUTTON_QXMX_SAVE)

    def clickQxmxDel(self):
        """权限明细页面-删除按钮"""
        self.Click(self.BUTTON_QXMX_DEL)
