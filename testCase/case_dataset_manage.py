#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/9/1 14:51
# @Author   : yangshukun
# @File     : case_dataset_manage.py


from pageKeyword.keyword_dataset_manage import *
from baseOperation.init_cls import *
import sys
from pageKeyword.keyword_sjgl_common import *
from Common.OtherFunc import *


class DataSetManageTest(InitCls, DataSetMain, DataSetMainPageKeyword, DataSetGroupPageKeyword, DataSetConfigBaseInfoKeyword):
    group_name = "自动化测试分组" + get_now_time_to_str()
    dataset_name = "自动化数据集" + get_now_time_to_str()
    export_name = "自动化导出名称" + get_now_time_to_str()
    desc_info = "自动化描述信息" + get_now_time_to_str()

    def test_01_add_group_succ(self):
        """数据集管理--新增数据集分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入数据集管理页面
        self.intoDataSetManagePage()
        self.changeToMainFrameForDataSet()
        # 3、点击新建分组按钮
        self.pressAddGroupButton()
        # 4、新增分组
        self.addGroupMainprocess("", self.group_name, "1")
        # 5、查看新增分组，断言新增成功
        self.SwitchFatherFrame()
        self.choiceDataSetGroup(self.group_name)
        self.pressRefreshButton()
        self.assertTrue(self.FindElement(self.DATA_TABLE_LIST_GROUP_NAME_DATASET.format(self.group_name)))
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_add_dataset_baseinfo_succ(self):
        """数据集管理--新增数据集基础信息成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入数据集管理页面
        self.RefreshPage()
        self.intoDataSetManagePage()
        self.changeToMainFrameForDataSet()
        # 3、点击新增数据集按钮
        self.pressAddDataSetButton()
        # 4、新增数据集基本信息，保存
        self.addDataSetBaseInfoMergeKwd(self.dataset_name, "", self.export_name, self.desc_info)
        # 5、查看新增数据集，断言新增成功
        self.sendDataSetName(self.dataset_name)
        self.pressRefreshButton()
        self.assertTrue(self.FindElement(self.DATA_TABLE_LIST_GROUP_NAME_DATASET.format(self.dataset_name)))
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

