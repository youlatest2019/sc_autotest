#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/11 17:34
# @Author   : tangle
# @File     : case_1104_xxhzbdb.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bscl_common import *
from data.data_class.common_data import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_baobiao_common import *
import sys
from Common.OtherFunc import *


class Rn1104XxhzbdbTest(InitCls, BsclMainKeyword, PubKeywordForBb, BsglPubBsrwKeyword, BsglMainKeyword):


    def test_01_1104_xxhzbdb(self):
        """1104--线下汇总表对比页面"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择1104品种进入1104管理界面
        self.intoRn1104Tab()
        # 4、切换到品种管理frame
        bsnr_name = "G0102-201-第Ⅱ部分：贷款质量五级分类情况简表"
        bsqj = "2022年06月"
        bbbh = "G0102"
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        response = self.queryBsrw(bsqj, bbbh)
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("1104任务自动化废弃")
        # 5、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 6、选择1104品种进入1104管理界面
        self.intoRn1104Tab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bbbh, "2022", qssd_index=3, type="month")
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 7、点击主菜单--报送处理，进入1104线下汇总表对比界面
        self.RefreshPage()
        self.clickBsclMainMenue()
        self.into1104XxhzbdbPage()
        # 8、未导入数据--点击对比-给出提示信息
        self.clickXxhzbdbCompare()
        # 断言提示信息--点击确定
        res = self.GetTagText(self.MAS_COMPARE_NULL_TS)
        self.assertEqual(res, '请先导入文件再进行对比。')
        self.closeCompareTs()
        # 9、导入数据一条数据
        self.importData(self.FILE_PATH)
        self.GotoSleep(2.5)
        # 10、删除按钮
        self.deleteData()
        # 断言删除提示信息
        res = self.GetTagText(self.MAS_CLEAN_TS)
        self.assertEqual(res, '是否删除当前文件。')
        # 否--回到列表页
        self.clickNo()
        # 再点击删除按钮--是
        self.deleteData()
        self.clickSure()
        # 断言页面无数据
        res = self.GetTagText(self.MAS_CLEAN_DATE)
        self.assertEqual(res, '共有 0 条数据')
        # 11、导入数据--选择报送内容名称
        self.importData(self.FILE_PATH)
        self.GotoSleep(2.5)
        self.clickBsnrmc()
        self.choiceBsnrmc(bbbh)
        # 12、点击对比，进入对比页面
        self.clickXxhzbdbCompare()
        self.intoDbFrame()
        # 13、选择对比小数位数
        dbxsws = '两位小数'
        # dbxsws = '实际小数位数'
        self.choiceDbxsws(dbxsws)
        # 14、对比日期
        data = '2022-06-30'
        self.inputDbData(data)
        # 15、选择取值方式
        qzfs = '最后一次报送数据'
        # qzfs = '首次报送数据'
        self.choiceQzfs(qzfs)
        # 16、刷新对比页面
        self.refreshDbPage()
        # 17、点击导出按钮
        self.downloadDb()
        # 18、关闭对比页面
        self.SwitchFatherFrame()
        self.closeDbPage()
        # 19、清空按钮
        self.cleanData()
        # 断言情空提示信息
        res = self.GetTagText(self.MAS_CLEAN_TS)
        self.assertEqual(res, '是否清空所有文件。')
        # 否--回到列表页
        self.clickNo()
        # 再点击清空按钮--是
        self.cleanData()
        self.clickSure()
        # 断言页面无数据
        res = self.GetTagText(self.MAS_CLEAN_DATE)
        self.assertEqual(res, '共有 0 条数据')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
