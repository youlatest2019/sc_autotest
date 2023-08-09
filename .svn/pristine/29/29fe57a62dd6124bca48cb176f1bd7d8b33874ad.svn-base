#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/4 10:01
# @Author   : yangshukun
# @File     : keyword_bsgl.py
from pageElement.page_bsgl import *
from baseOperation.WebOperation import *
from data.data_class.common_data import *
from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from Common.OtherFunc import *


class BsglRptcBscsKeyword(BsglElementFrame, RPTCBscsElement, WebDriver):
    """综合报表报送参数"""

    def changeRptcBscsSbsp(self):
        """综合报表修改报送参数-上报审批"""
        self.Click(self.BUTTON_SBSP)

    def changeRptcBscsSave(self):
        """综合报表修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RPTC)