from baseOperation.init_cls import *
from pageKeyword.keyword_data_extraction import *
from Common.OtherFunc import *
from pageKeyword.keyword_bscl_common import *
from pageKeyword.keyword_mingxi_common import *
from pageKeyword.keyword_bsgl_common import *


# class DataExtractionTest(InitCls, DataExtractionKeyword, BsclMainKeyword, PubKeywordHdPageForMx, BsglPubFzglKeyword,
#                          BsglMainKeyword, BsglPubBsrwKeyword):

    # def test_01_data_extraction(self):
    #     """数据抽取情况-筛选报送品种、报送任务进行重新取数"""
    #     mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
    #     # 1、进入报送管理主界面
    #     self.intoBsglMainMenu()
    #     self.switchToBsglBaseFrame()
    #     # 2、进入反洗钱大额管理界面
    #     self.intoReastTab()
    #     # 3、切换到品种管理frame
    #     self.switchBspzFrame()
    #     # 4、进入分组管理页签
    #     self.swithToFzgl()
    #     self.bsglMainFrame()
    #     # 5、将当前登录用户添加到管理员分组，如果存在则不添加
    #     self.addUserForAdminGroup()
    #     # 6、进入报送任务页面，查看报送任务是否存在，存在则废弃报送任务
    #     self.intoBsglMainMenu()
    #     self.switchToBsglBaseFrame()
    #     # 7、选择征信品种进入征信管理界面
    #     self.intoRmbtdTab()
    #     # 8、切换到品种管理frame
    #     self.switchBspzFrame()
    #     self.swithToBsrw()
    #     self.switchBspzFrame()
    #     bsnr_no = "MBTD210"
    #     bsqj_no = "20211231"
    #     bsqj_date = "2021年12月31日"
    #     response = self.queryBsrw(bsqj_date, "企业基本信息记录")
    #     if response:
    #         res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
    #         if res == "共有 0 个报送任务，0 个已过期":
    #             self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type='day')
    #             self.addBsrwSave()
    #     # # 17、新增报送任务
    #     # self.intoBsglMainMenu()
    #     # self.switchToBsglBaseFrame()
    #     # # 18、选择征信品种进入征信管理界面
    #     # self.intoRmbtdTab()
    #     # self.switchBspzFrame()
    #     # self.swithToBsrw()
    #     # self.switchBspzFrame()
    #     # self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type='day')
    #     # self.addBsrwSave()
    #     # 1、打开数据抽取页面
    #     self.OpenDataExtractPage()
    #     # 2、输入查询条件并刷新
    #     self.DataExtractPageCxtj("征信", "企业基本信息记录")
    #     self.DataExtractPageDate("2022-03-31", "2022-03-31")
    #     # 3、勾选全选复选框
    #     self.DataExtractPageFxkAll()
    #     # 4、点击重新取数按钮
    #     self.DataExtractPageCxqs()
    #     self.GotoSleep(3)
    #     # 5、断言重抽成功
    #     res = self.GetTagText(self.DATA_EXTRACT_ALERT_INFO)
    #     self.assertEqual(res, '所有任务调用重新计算成功！')
    #     # 关闭
    #     mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
    #
    # def test_02_data_clear(self):
    #     """数据抽取情况-筛选报送品种、报送任务清空数据"""
    #     mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
    #     # 1、打开数据抽取页面
    #     self.OpenDataExtractPage()
    #     # 2、输入查询条件并刷新
    #     self.DataExtractPageCxtj("征信", "企业间关联关系信息记录")
    #     self.DataExtractPageDate("2021-12-31", "2021-12-31")
    #     # 3、勾选全选复选框
    #     self.DataExtractPageFxkAll()
    #     # 4、点击清空数据按钮
    #     self.DataExtractPageClear()
    #     self.GotoSleep(1)
    #     # 5、点击确认按钮，关闭弹窗
    #     self.Click(self.ALERT_OK_BUTTON)
    #     # 6、进入对应品种核对页面
    #     self.RefreshPage()
    #     self.clickBsclMainMenue()
    #     self.intoRmbtdHdPage()
    #     self.choiceHdReportDateForMx("2021年12月31日")
    #     self.inputHdReportNameForMx("企业间关联关系信息记录")
    #     self.refreshHdDataForMx()
    #     # 5、断言清空数据成功
    #     res = self.GetElementAttrbute(self.DATA_NUMBER, "value")
    #     self.assertEqual(res, '0')
    #     # 关闭
    #     mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
