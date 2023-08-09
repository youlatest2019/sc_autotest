#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/30 17:32
# @Author   : yangshukun
# @File     : keyword_sjgl_common.py

from pageElement.page_sjgl_common import *
from baseOperation.WebOperation import *


class DataSetMain(SjglMainMenueElement, WebDriver):
    """数据集主菜单进入方法"""

    def intoDataSetManagePage(self):
        """进入数据集管理主页面"""
        self.RefreshPage()
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.DATASET_MANAGE_MENUE)
        self.Click(self.DATASET_MANAGE_TAG)

    def intoDataSetQueryPage(self):
        """进入数据集查询主页面"""
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.DATASET_QUERY_MENUE)
        self.Click(self.DATASET_QUERY_TAG)

    def intoDataSetBlPage(self):
        """进入数据集补录主页面"""
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.DATASET_BL_MENUE)
        self.Click(self.DATASET_BL_TAG)

    def intoDataSetSqPage(self):
        """进入数据集授权主页面"""
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.DATASET_SQ_MENUE)
        self.Click(self.DATASET_SQ_TAG)

    def intoDataSetSpPage(self):
        """进入数据集审批主页面"""
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.DATASET_SP_MENUE)
        self.Click(self.DATASET_SP_TAG)
