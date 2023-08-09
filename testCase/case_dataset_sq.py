#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/1 10:10
# @Author   : tangle
# @File     : case_dataset_sq.py


from pageKeyword.keyword_dataset_manage import *
from pageKeyword.keyword_dataset_sq import *
from baseOperation.init_cls import *
import sys
from pageKeyword.keyword_sjgl_common import *
from Common.OtherFunc import *


class DataSetManageTest(InitCls, DataSetMain, DataSetMainPageKeyword, DataSetGroupPageKeyword,
                        DataSetConfigBaseInfoKeyword, DataSetSqPageKeyword):
    group_name = "自动化测试分组" + get_now_time_to_str()
    dataset_name = "自动化数据集" + get_now_time_to_str()
    export_name = "自动化导出名称" + get_now_time_to_str()
    desc_info = "自动化描述信息" + get_now_time_to_str()

    def test_01_sq_dataset_succ(self):
        """数据集管理--新增数据集授权成功"""
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
        # 6、点击新增数据集按钮
        self.pressAddDataSetButton()
        # 7、新增数据集基本信息，保存
        self.addDataSetBaseInfoMergeKwd(self.dataset_name, self.group_name, self.export_name, self.desc_info)
        # 8、查看新增分组，断言新增成功
        self.sendDataSetName(self.dataset_name)
        self.pressRefreshButton()
        self.assertTrue(self.FindElement(self.DATA_TABLE_LIST_GROUP_NAME_DATASET.format(self.dataset_name)))
        # 9、刷新页面，切换frame进入数据集授权页面
        self.RefreshPage()
        self.intoDataSetSqPage()
        self.changeToMainFrameForDataSq()
        # 10、数据集授权-点击人员名称下拉框输入并选择
        user_name = 'EAST权限1'
        self.choiceDataSqUserXm(user_name)
        # 11、数据集授权--权限项--勾选数据集选框
        self.choiceDataSqSjjFz(self.dataset_name)
        # 12、点击保存按钮
        self.saveDataSetSq()
        # 13、点击刷新按钮
        self.refreshDataSetSq()
        # 14、断言勾选授权成功
        self.assertTrue(self.FindElement(self.MSG_SELECT_SUCC.format(self.dataset_name)))
        # 15、点击人员权限查询按钮
        self.clickUserQuery()
        # 16、断言人员权限查询页面--人员授权数据集成功
        self.changeToFrameForUserQuery()
        self.refreshUserQuery()
        self.assertTrue(self.FindElement(self.MSG_USERQUERY.format(self.dataset_name)))
        # 17、关闭人员权限查询页面
        self.QuiteFrame()
        self.changeToMainFrameForDataSq()
        self.closeUserQuery()
        # 18、数据集授权-点击角色下拉框输入并选择
        role_name = 'EAST角色'
        self.choiceDataSqRole(role_name)
        # 19、数据集授权--权限项--勾选数据集选框
        self.choiceDataSqSjjFz(self.dataset_name)
        # 20、点击保存按钮
        self.saveDataSetSq()
        # 21、点击刷新按钮
        self.refreshDataSetSq()
        # 22、断言勾选授权成功
        self.assertTrue(self.FindElement(self.MSG_SELECT_SUCC.format(self.dataset_name)))
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
