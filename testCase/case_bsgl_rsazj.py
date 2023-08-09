from baseOperation.init_cls import *
from utils.operationXml import *
import sys
from baseOperation.init_self import *
from pageKeyword.keyword_bsgl_common import *
from pageKeyword.keyword_bsgl_rsazj import *
from Common.OtherFunc import *


class BsglRsazjTest(InitCls, BsglMainKeyword, BsglPubBsrwKeyword, BsglPubBsfwKeyword, BsglPubFzglKeyword,
                    BsglPubBssqKeyword, BsglPubSjsqKeyword, BsglPubSplcKeyword, BsglRsazjBscsKeyword, OperationXml):
    def test_01_add_bsrw_success(self):
        """浙江国资委报送任务新增+废弃报送任务成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        # 6、新增报送任务
        self.switchBspzFrame()
        bsnr_no = "ZJJYHZXX"
        bsqj_no = "20220815"
        bsqj_date = "2022年08月15日"
        report_no = bsnr_no + "-" + bsqj_no
        response = self.queryBsrw(bsqj_date, "交易汇总信息")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("浙江国资委任务自动化废弃")
        # 17、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 18、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type="day")
        self.addBsrwSave()
        # 断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.closeXzrw_success()
        # 7、废弃新增的报送任务
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.switchBspzFrame()
        self.queryBsrw(bsqj_date, "交易汇总信息")
        self.abandonBsrw("废弃")
        # 断言废弃成功
        # res = self.GetTagText(self.MSG_ADD_RESULT)
        # self.assertEqual(res, '操作成功!')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_sfbs_bsfw_success(self):
        """浙江国资委报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("按日", "活期账户余额")
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        self.clickOkAlert()
        # 6、查询并点击是否报送按钮(是)
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_change_bsfw_success(self):
        """浙江国资委报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、修改单个报送内容设置
        self.bsglMainFrame()
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 0 8-18 * * ? *", "15", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_add_group_east_success(self):
        """浙江国资委分组管理--新增分组+删除分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签
        self.swithToFzgl()
        # 6、新增分组并断言成功
        self.bsglMainFrame()
        group_name = "浙江国资委自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "浙江国资委权限1", "自动化测试_浙江国资委分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        self.editeGroup(group_name, group_name + "_修改", "自动化测试_浙江国资委分组描述_修改")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 8查询修改后的名称正确
        self.searchGroupName(group_name + "_修改")
        self.refreshGroupPage()
        res = self.GetTagText(self.DATA_FIRST_GROUP.format(1))
        self.assertEqual(res, group_name + "_修改")
        # 删除分组
        self.delGroup(group_name + "_修改")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_bssq_success(self):
        """浙江国资委报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "浙江国资委自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "浙江国资委权限1", "自动化测试_浙江国资委分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("活期账户余额")
        self.refreshBssqPage()
        # 勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.tickSbqx()
        self.tickCxqx()
        self.tickCcqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 进入分组管理
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_change_power_east_success(self):
        """浙江国资委数据授权--修改授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签,新增分组并断言成功
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "浙江国资委自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "浙江国资委权限1", "自动化测试_浙江国资委分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面选择分组
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("活期账户余额")
        self.refreshBssqPage()
        # 7、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 8、进入数据授权页面,选择分组
        self.SwitchFatherFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        self.searchGroupNameSjsq(group_name)
        self.searchBsnrSjsq("活期账户余额")
        self.refreshSjsqPage()
        # 9、点击全部，修改权限为按字段筛选+下拉框并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("币种")
        self.clickZdTwoBssqPage("CNY-人民币")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 10、进入报送管理主界面，选择浙江国资委品种进入浙江国资委管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsazjTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 11、点击数据范围按钮，修改权限为按字段筛选+输入值并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("本方单位名称")
        self.inputZdBssqPage("自动化浙江国资委1")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 12、进入报送管理主界面，选择浙江国资委品种进入浙江国资委管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsazjTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 13、点击数据范围按钮，修改权限为全部并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.clickAllSjsq()
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 14、进入报送管理主界面，选择浙江国资委品种进入浙江国资委管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRsazjTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 15、清除查询条件并断言成功
        self.clearDataBssqPage()
        res = self.GetElementAttrbute(self.INPUT_BSNR_SJSQ, "value")
        self.assertEqual(res, "")
        # 进入分组管理删除分组
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_splc_batch_update_success(self):
        """浙江国资委审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "浙江国资委自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "浙江国资委权限1", "自动化测试_浙江国资委分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("活期账户余额")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入审批流程页面
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshSplcPage()
        # 11、勾选报送内容，批量修改,并断言修改成功
        self.tickBoxAll()
        self.batchUpdateSplc("RSAZJ默认审批流")
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.bsglMainFrame()
        res = self.GetTagText(self.MSG_BATCH_ALERT_SPLC)
        self.assertEqual(res, "保存成功")
        self.closeBatchAlertSplc()
        # 进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_change_bscs_success(self):
        """浙江国资委报送参数修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择浙江国资委品种进入浙江国资委管理界面
        self.intoRsazjTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送参数管理页签
        self.swithToBscs()
        # 6、修改报送参数并保存成功
        self.bsglMainFrame()
        self.changeRsazjBscsFkjylx("交易类型", "付款")
        self.changeRsazjBscsSkjylx("交易类型", "收款")
        self.changeRsazjBscsDesxed("88888888")
        self.changeRsazjBscsDezjIp("192.168.20.157")
        self.changeRsazjBscsDezjPort("1003")
        self.changeRsazjBscsDeProtocol("http")
        self.changeRsazjBscsAppId("12")
        self.changeRsazjBscsSecret("22")
        self.changeRsazjBscsPrivatekey("12")
        self.changeRsazjBscsSmPublickey("22")
        self.changeRsazjBscsSave()
        # 断言修改参数成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
