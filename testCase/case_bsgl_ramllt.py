#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/3 15:02
# @Author   : tangle
# @File     : case_bsgl_ramllt.py

from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from Common.OtherFunc import *
from pageKeyword.keyword_bsgl_ramllt import *


class BsglRamlltTest(InitCls, BsglMainKeyword, OperationXml, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                     BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSjsqKeyword, BsglPubSplcKeyword,
                     BsglPubBssqDeFxqKeyword, BsglPubSplcDeFxqKeyword, BsglRamlltJkzbSzKeyword, BsglRamlltBscsKeyword):

    def test_01_ramllt_jkzbsz_jczbms_succ(self):
        """反洗钱大额-监控指标设置-监测指标描述"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额反洗钱品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入监控指标设置管理页签
        self.swithToJkzbsz()
        self.bsglMainFrame()
        # 监测标准码
        jczbbm = '0501'
        # jczbbm = '0502'
        # jczbbm = '0503'
        # jczbbm = '0504'
        # 6、先将默认的监测指标描述剪切-然后输入新的描述-保存-断言后-再还原将原默认的已剪切的描述粘贴。
        # 将默认的监测指标描述剪切
        self.CutJczbmsRamllt(jczbbm)
        # 输入新的指标描述
        jczbms_new = jczbbm + '新监测指标描述'
        self.InputJczbmsRamllt(jczbms_new, jczbbm)
        # 保存
        self.SaveJkzbSzRamllt()
        #
        self.SwitchFatherFrame()
        self.swithToBscs()
        self.swithToJkzbsz()
        self.bsglMainFrame()
        # 断言
        res = self.GetTagText(self.MSG_JCZBMS.format(jczbbm))
        self.assertEqual(res, jczbms_new)
        # 粘贴还原原来指标描述-保存
        self.PasteJczbmsRamllt(jczbbm)
        self.SaveJkzbSzRamllt()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_ramllt_jkzbsz_csz_succ(self):
        """反洗钱大额-监控指标设置-参数值-是否启用"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额反洗钱品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入监控指标设置管理页签
        self.swithToJkzbsz()
        self.bsglMainFrame()
        # 监测标准码
        jczbbm = '0501'
        # jczbbm = '0502'
        # jczbbm = '0503'
        # jczbbm = '0504'
        # 6、选择上报范围-参数值
        sbfw_csz = '其他'
        self.choiceSbfwCszRamllt(jczbbm, sbfw_csz)
        # # 7、输入累计交易金额（人民币）
        cny_ljje = '50001.00'
        self.inputLjjyjeCnyCszRamllt(jczbbm, cny_ljje)
        # 8、输入单笔交易金额（人民币）
        cny_dbje = '50002.00'
        self.inputDbjyjeCnyCszRamllt(jczbbm, cny_dbje)
        # 9、输入累计交易金额（美元）
        usa_ljje = '10001.00'
        self.inputLjjyjeUsaCszRamllt(jczbbm, usa_ljje)
        # 10、输入单笔交易金额（美元）
        usa_dbje = '10002.00'
        self.inputDbjyjeUsaCszRamllt(jczbbm, usa_dbje)
        # 11、保存
        self.SaveJkzbSzRamllt()
        #
        self.SwitchFatherFrame()
        self.swithToBscs()
        self.swithToJkzbsz()
        self.bsglMainFrame()
        # 12、断言
        self.assertTrue(self.FindElement(self.MSG_SELECT_INPUT_SBFW_CSZ.format(jczbbm, sbfw_csz)))
        self.assertTrue(self.FindElement(self.MSG_INPUT_LJJYJE_CNY_CSZ.format(jczbbm, cny_ljje)))
        self.assertTrue(self.FindElement(self.MSG_INPUT_DBJYJE_CNY_CSZ.format(jczbbm, cny_dbje)))
        self.assertTrue(self.FindElement(self.MSG_INPUT_LJJYJE_USA_CSZ.format(jczbbm, usa_ljje)))
        self.assertTrue(self.FindElement(self.MSG_INPUT_DBJYJE_USA_CSZ.format(jczbbm, usa_dbje)))
        # 还原上报范围的-参数值
        self.choiceSbfwCszRamllt(jczbbm, sbfw_csz)
        self.SaveJkzbSzRamllt()
        # 13、点击启用
        # 默认启用-点击后不启用
        self.changeQyRamllt(jczbbm)
        # 还原为启用
        self.changeQyRamllt(jczbbm)
        # 14、保存
        self.SaveJkzbSzRamllt()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_change_ramllt_bscs_success(self):
        """反洗钱大额报送参数设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额反洗钱品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送参数管理页签
        self.swithToBscs()
        self.bsglMainFrame()
        # 5、修改报送参数设置不正确的编码，点击保存，浏览器弹窗提示-点击确定
        bm_false_1 = 'bgjgbm2022'  # 不足14位编码
        bm_false_2 = 'bgjgbm202201010'  # 超过14位编码
        self.inputBscsRamlltCsz(bm_false_1)
        self.clickBscsRamlltSave()
        self.AlertAccept()
        self.inputBscsRamlltCsz(bm_false_2)
        self.clickBscsRamlltSave()
        self.AlertAccept()
        # 6、修改报送参数正确编码并保存成功
        bm_ture = 'bgjgbm20220101'  # 14位编码
        self.inputBscsRamlltCsz(bm_ture)
        self.clickBscsRamlltSave()
        # 断言
        self.SwitchFatherFrame()
        self.swithToBsfw()
        self.swithToBscs()
        self.bsglMainFrame()
        self.assertTrue(self.FindElement(self.MSG_BGJGBM_CSZ.format(bm_ture)))
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_add_ramllt_bsrw_success(self):
        """反洗钱大额报送任务新增+废弃报送任务成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择大额反洗钱品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        self.bsglMainFrame()
        # 判断报送任务是否存在，存在则废弃
        response = self.queryBsrw("2021年12月31日", "反洗钱大额交易")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("Ramllt任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRamlltTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("AMLLT001", "20211231",qssd_index=3, type="day")
        self.addBsrwSave()
        # 断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.closeXzrw_success()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_sfbs_ramllt_bsfw_success(self):
        """反洗钱大额报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮(否)
        self.bsglMainFrame()
        self.queryBsnr("按日", "反洗钱大额交易")
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

    def test_06_change_ramllt_bsfw_success(self):
        """反洗钱大额报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        self.bsglMainFrame()
        # 6、修改单个报送内容设置
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 0 /2 * * ?", "5", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_add_group_ramllt_success(self):
        """反洗钱大额分组管理--新增分组+删除分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签
        self.swithToFzgl()
        self.bsglMainFrame()
        # 6、新增分组并断言成功
        group_name = "反洗钱大额自动化分组" + get_now_time_to_str()
        group_describe="自动化测试_反洗钱大额分组描述" + get_now_time_to_str()
        self.addGroup(group_name, user_chinese_name, group_describe)
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        group_name_xg = group_name + '_修改'
        group_describe_xg = group_describe + '_修改'
        self.editeGroup(group_name, group_name_xg, group_describe_xg)
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 8查询修改后的名称正确
        self.searchGroupName(group_name_xg)
        self.refreshGroupPage()
        res = self.GetTagText(self.DATA_FIRST_GROUP.format(1))
        self.assertEqual(res,  group_name_xg)
        # 删除分组
        self.delGroup(group_name_xg)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_ramllt_bssq_success(self):
        """反洗钱大额报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "反洗钱大额自动化分组" + get_now_time_to_str()
        group_describe = "自动化测试_反洗钱大额分组描述" + get_now_time_to_str()
        self.addGroup(group_name, user_chinese_name, group_describe)
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("反洗钱大额交易")
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

    def test_09_change_power_ramllt_success(self):
        """反洗钱大额数据授权--修改授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签,新增分组并断言成功
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "反洗钱大额自动化分组" + get_now_time_to_str()
        group_describe = "自动化测试_反洗钱大额分组描述" + get_now_time_to_str()
        self.addGroup(group_name, user_chinese_name, group_describe)
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面选择分组
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("反洗钱大额交易")
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
        self.searchBsnrSjsq("反洗钱大额交易")
        self.refreshSjsqPage()
        # 9、点击全部，修改权限为按按字段筛选+输入值并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("客户号")
        self.inputZdBssqPage("客户号1234")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 10、进入报送管理主界面，选择反洗钱大额品种进入反洗钱大额管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRamlltTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 11、点击数据范围按钮，修改权限为全部并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.clickAllSjsq()
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 12、进入报送管理主界面，选择反洗钱大额品种进入反洗钱大额管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRamlltTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 13、清除查询条件并断言成功
        self.clearDataBssqPage()
        res = self.GetElementAttrbute(self.INPUT_BSNR_SJSQ, "value")
        self.assertEqual(res, "")
        # 进入分组管理删除分组
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        self.delGroup(group_name)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_ramllt_splc_batch_update_success(self):
        """反洗钱大额审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        conf = Config()
        user_chinese_name = conf.get("BaseUrl", "user_name")
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱大额品种进入反洗钱大额管理界面
        self.intoRamlltTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        group_name = "反洗钱大额自动化分组" + get_now_time_to_str()
        group_describe = "自动化测试_反洗钱大额分组描述" + get_now_time_to_str()
        self.addGroup(group_name, user_chinese_name, group_describe)
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq(group_name)
        self.searchBsnr("反洗钱大额交易")
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
        self.batchUpdateSplc("RAMLLT默认审批流")
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
