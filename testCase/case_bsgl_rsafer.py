from baseOperation.init_cls import *
from utils.operationXml import *
import sys
from baseOperation.init_self import *
from pageKeyword.keyword_bsgl_common import *
from Common.OtherFunc import *
from pageKeyword.keyword_bsgl_rsafer import *
from data.data_class.common_data import *


class BsglRimasTest(InitCls, BsglMainKeyword, BsglPubBsrwKeyword, BsglPubBsfwKeyword, BsglPubFzglKeyword,
                    BsglPubBssqKeyword, BsglPubSjsqKeyword, BsglPubSplcKeyword, BsglRsaferBscsKeyword, OperationXml,
                    BsglPubHswhKeyword, BsglPubSjxwhKeyword, BsglBsplData, BsglRsaferWbzmyhlKeyword,BsglPubBsnrsqKeyword,
                    ZdysjlxPubSplcKeyword,BsglPubBbmbKeyword,PubBbmbElement):

    def test_01_rsafer_import_module_success(self):
        """外管局报表模板导入成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择外管局品种进入外管局管理界面
        self.switchToBsglBaseFrame()
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导入模板
        self.switchBspzFrame()
        self.importBbmb(self.RSAFER_P02_PATH)
        self.GotoSleep(1)
        # 断言导入成功
        res = self.GetTagText(self.MSG_IMPORT_RESULT)
        self.assertEqual(res, '成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_rsafer_export_module_success(self):
        """外管局报表模板导出成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.switchToBsglBaseFrame()
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报表模板管理页签
        self.swithToBbmb()
        # 6、导出模板
        self.switchBspzFrame()
        self.inputBsnrbh("P02")
        self.refreshBbmbPage()
        self.clickCheckBox(1)
        self.exportBbmb()
        self.GotoSleep(1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_add_bsrw_success(self):
        """外管局报表废弃报送任务+报送任务新增成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        self.bsglMainFrame()
        # 判断报送任务是否存在，存在则废弃
        self.queryBsrw("2021年03月29日", "P02-大额结售汇交易统计表")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("Rsafer任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRsaferTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("P02", "20210329", type="day")
        self.BbpzChoiceMould()
        self.addBsrwSave()
        # 断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.closeXzrw_success()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_sfbs_bsfw_success(self):
        """外管局报表报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("按日", "P02-大额结售汇交易统计表")
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

    def test_05_change_bsfw_success(self):
        """外管局报表报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、修改单个报送内容设置
        self.bsglMainFrame()
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 0 /1 * * ?", "1", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_add_group_east_success(self):
        """外管局报表分组管理--新增分组+删除分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签
        self.swithToFzgl()
        # 6、新增分组并断言成功
        self.bsglMainFrame()
        group_name = "外管局报表自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "利率报备权限1", "自动化测试_外管局报表分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        self.editeGroup(group_name, group_name + "_修改", "自动化测试_外管局报表分组描述_修改")
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

    def test_07_bssq_success(self):
        """外管局报表报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "外管局报表自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "利率报备权限1", "自动化测试_外管局报表分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
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

    def test_08_splc_batch_update_success(self):
        """外管局报表审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "外管局报表自动化分组" + get_now_time_to_str()
        self.addGroup(group_name, "利率报备权限1", "自动化测试_外管局报表分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
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
        self.batchUpdateSplc("外管局报表审批")
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

    def test_09_bscs_update_success(self):
        """外管局报表报送参数修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、修改报送参数并保存成功
        self.swithToBscs()
        self.bsglMainFrame()
        self.changeRsaferBscsJy()
        self.changeRsaferBscsDay("2")
        self.changeRsaferBscsSbsp()
        self.changeRsaferBscsSave()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_rsafer_hswh_add_function_success(self):
        """外管局报表函数维护--新增函数成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择1104品种进入1104管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入函数维护页面，点击新增进入新增页面
        self.swithToHswh()
        self.bsglMainFrame()
        self.addHswhMainPage()
        self.switchToDetailFrame()
        # 6、输入函数基础信息
        hsmc = "rsafer自动化测试函数" + get_now_time_to_str()
        self.inputHsmcHswhDetailPage(hsmc)
        self.inputHslbHswhDetailPage(self.HSLB_DKYE)
        self.inputHsmsHswhDetailPage("rsafer自动化测试-函数描述")
        self.inputResTypeHswhDetailPage(self.RES_ZS)
        self.inputSqlHswhDetailPage("select @1 from dual")
        # 7、点击解析参数，并输入参数名称、类型、参数值
        self.clickAnalParamHswhDetailPage()
        self.makeParamsInfoHswhDetailPage("rsafer自动化测试参数", self.PARAMS_TEXT, "1")
        # 8、点击测试,并断言测试sql成功,退出测试界面
        self.clickTestHswhDetailPage()
        res = self.GetTagText(self.MSG_DETAIL_HSWH)
        self.assertEqual(res, "SQL预执行成功，语法正确！")
        self.closeAlertTestHswhDetailPage()
        self.closeTestHswhDetailPage()
        # 9、切换到详情frame，点击保存，并断言保存成功
        self.switchToDetailFrame()
        self.clickSaveHswhDetailPage()
        res1 = self.GetTagText(self.MSG_DETAIL_HSWH)
        self.assertEqual(res1, "保存成功")
        self.closeHswhAlert()
        self.closeHswhDetailMainPage()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_11_rsafer_sjxwh_add_data_success(self):
        """外管局报表数据项维护维护--新增数据项成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择1104品种进入1104管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入数据项维护页面，点击新增按钮
        self.swithToSjxwh()
        self.switchBspzFrame()
        self.clickSjxwhAddButton()
        # 6、输入数据项基本信息
        sjx_name = "rsafer自动化数据项名称" + get_now_time_to_str()
        self.inputSjxwhInfo(sjx_name, "rsafer自动化数据项描述", self.GROUP_JSH_MONTH, "S01-即期结售汇统计月报表—结汇")
        # 7、添加函数并插入
        self.choiceSjxwhFuncDataAndInster("9")
        # 8、添加数据项并插入
        self.choiceSjxwhItemsDataAndInster("S03.其他_外资机构")
        # 9、保存
        self.clickSjxwhSaveButton()
        res2 = self.GetTagText(self.MSG_FUNC_FORM_SJXWH)
        self.assertEqual(res2, "保存成功！")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_12_rsafer_set_zdysjlx_success(self):
        """设置rsafer-自定义数据类型"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入rsafer管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入自定义数据类型页签
        self.swithToZdysjlx()
        self.ZdysjlxFrame()
        # 新增数据类型-编辑数据类型-新增数据类型明细-编辑数据类型明细-删除数据类型失败（该自定义类型已被引用，不可删除！）--删除数据类型明细后（删除成功！）--删除数据类型成功（删除成功！）
        # 6、数据类型-新增按钮
        self.addSjlxButton()
        # 7、数据类型-新增-编号
        bh = "zdy" + get_now_time_to_str()
        self.addSjlxBh(bh)
        # 8、数据类型-新增-名称
        base_name = "rsafer自定义" + get_now_time_to_str()
        add_name = base_name + "-新增"
        edit_name = base_name + "-编辑"
        self.addSjlxName(add_name)
        # 9、数据类型-新增-说明
        self.addSjlxSm(add_name + "说明")
        # 10、数据类型-新增-保存按钮
        self.addSjlxSave()
        # 11、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 12、数据类型-选择点击数据行
        self.choiceSjlxClick(bh)
        # 13、数据类型-编辑按钮
        self.editSjlxButton()
        # 14、数据类型-编辑-名称
        self.editSjlxName(edit_name)
        # 15、数据类型-编辑-说明
        self.editSjlxSm(edit_name + "说明")
        # 16、数据类型-编辑-保存按钮
        self.editSjlxSave()
        # 17、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 18、数据类型-选择点击数据行
        self.choiceSjlxClick(bh)
        # 19、数据类型明细-新增按钮
        self.addSjlxMxButton()
        # 20、数据类型明细-新增-名称
        self.addSjlxMxName("数据类型明细-新增名称")
        # 21、数据类型明细-新增-参数值
        self.addSjlxMxCsz("数据类型明细-新增参数值")
        # 22、数据类型明细-新增-保存按钮
        self.addSjlxMxSave()
        # 23、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 24、数据类型明细-勾选第一行
        self.SelectSjlxMxFrist()
        # 25、数据类型明细-编辑按钮
        self.editSjlxMxButton()
        # 26、数据类型-编辑-名称
        self.editSjlxMxName("数据类型明细-编辑名称")
        # 27、数据类型-编辑-说明
        self.editSjlxMxCsz("数据类型明细-编辑参数值")
        # 28、数据类型-编辑-保存按钮
        self.editSjlxMxSave()
        # 29、切换frame
        self.QuiteFrame()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.ZdysjlxFrame()
        # 30、数据类型-删除按钮
        self.delSjlxButton()
        # 31、断言 -数据类型-删除按钮-删除失败-该自定义类型已被引用，不可删除！
        res = self.GetTagText(self.MSG_SJLX_RESULT_SUCCESS)
        self.assertEqual(res, '该自定义类型已被引用，不可删除！')
        # 32、数据类型--删除失败--确定
        self.delSjlxFail()
        # 33、数据类型明细复选框全选
        self.SelectSjlxMxAll()
        # 34、数据类型明细-删除按钮
        self.delSjlxMxButton()
        # 35、断言 -数据类型明细-删除按钮-删除成功
        res = self.GetTagText(self.MSG_SJLXMX_RESULT_SUCCESS)
        self.assertEqual(res, '删除成功！')
        # 36、关闭删除成功弹窗
        self.delSjlxMxSuccessClose()
        # 37、数据类型-删除按钮
        self.delSjlxButton()
        # 38、断言 -数据类型-删除按钮-删除成功
        res = self.GetTagText(self.MSG_SJLX_RESULT_SUCCESS)
        self.assertEqual(res, '删除成功！')
        # 39、关闭删除成功弹窗
        self.delSjlxSuccessClose()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_13_Wbzmyhl_update_success(self):
        """外管局报表外币折美元汇率修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、新增外币折美元汇率并断言成功
        self.swithToWbzhmyhl()
        self.bsglMainFrame()
        self.changeRsaferWbzmyhlAdd()
        self.changeRsaferWbzmyhlBz("人民币")
        self.changeRsaferWbzmyhlSxrq("2030-03-29")
        self.changeRsaferWbzmyhlRate("1.23")
        self.changeRsaferWbzmyhlSave()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功")
        self.changeRsaferWbzmyhlClose()
        # 6、删除新增的外币折美元汇率并断言成功
        self.ClickRsaferWbzmyhlCxtj("人民币")
        self.changeRsaferWbzmyhlRfresh()
        self.changeRsaferWbzmyhlFxkAll()
        self.changeRsaferWbzmyhlDelete()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "删除成功")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_14_rsafer_bsnrsq_edit_all_success(self):
        """外管局报表报送内容授权--编辑全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rsafer分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rsafer授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("P02-大额结售汇交易统计表")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("P02-大额结售汇交易统计表")
        # 12、点击编辑全部，进行授权
        self.clickEditAllBsnrsq()
        self.AlertAccept()
        # 13、断言编辑全部授权后，检查编辑权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("P02-大额结售汇交易统计表", 1)).split("(")[1].split(")")[0]
        self.assertGreater(int(res), 0)
        # 14、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 15、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_15_rsafer_bsnrsq_trace_all_success(self):
        """外管局报表报送内容授权--追溯全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择人行报表外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rsafer分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rsafer授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("P02-大额结售汇交易统计表")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("P02-大额结售汇交易统计表")
        # 12、点击追溯全部，进行授权
        self.clickTraceAllBsnrsq()
        self.AlertAccept()
        # 13、断言追溯全部授权后，检查追溯权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("P02-大额结售汇交易统计表", 2)).split("(")[1].split(")")[0]
        self.assertGreater(int(res), 0)
        # 14、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 15、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_16_rsafer_bsnrsq_cancel_all_success(self):
        """外管局报表报送内容授权--取消全部成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择外管局报表品种进入外管局报表管理界面
        self.intoRsaferTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "rsafer分组" + get_now_time_to_str()
        self.addGroup(group_name, "人行报表权限2", "自动化测试_rsafer授权分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("P02-大额结售汇交易统计表")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入报送内容授权页面
        self.SwitchFatherFrame()
        self.swithToBsnrsq()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc(group_name)
        self.refreshBsnrsqPage()
        # 11、输入报送内容，点击刷新
        self.searchBsnrBsnrsq("P02-大额结售汇交易统计表")
        self.clickRefreshBsnrsq()
        self.choiceBoxByNameBsnrsq("P02-大额结售汇交易统计表")
        # 12、点击追溯全部，进行授权
        self.clickTraceAllBsnrsq()
        self.AlertAccept()
        # 13、断言追溯全部授权后，检查追溯权限项不为0
        res = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("P02-大额结售汇交易统计表", 2)).split("(")[1].split(")")[0]
        self.assertGreater(int(res), 0)
        # 14、取消全部授权，断言取消后权限项为0
        self.choiceBoxByNameBsnrsq("P02-大额结售汇交易统计表")
        self.clickCancelAllBsnrsq()
        self.AlertAccept()
        res1 = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("P02-大额结售汇交易统计表", 2)).split("(")[1].split(")")[0]
        self.assertEqual(int(res1), 0)
        res2 = self.GetTagText(self.BUTTON_EDIT_COUNT_BSNRSQ.format("P02-大额结售汇交易统计表", 1)).split("(")[1].split(")")[0]
        self.assertEqual(int(res2), 0)
        # 15、进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 16、删除分组
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
