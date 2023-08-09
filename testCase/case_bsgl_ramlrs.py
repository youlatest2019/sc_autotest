from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_rmbtd import *
from pageKeyword.keyword_bsgl_common import *
from Common.OtherFunc import *
from pageKeyword.keyword_bsgl_ramlrs import *


class BsglRmbtdTest(InitCls, BsglMainKeyword, OperationXml, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                    BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSjsqKeyword, BsglPubSplcKeyword,
                    BsglRamlrsSbwdszKeyword, BsglRamlrsBscsKeyword, BsglPubBssqDeFxqKeyword, BsglPubSplcDeFxqKeyword,
                    BsglRamlrsKytzszKeyword, BsglRamlrsKhzlwhKeyword, BsglRamlrsSkhmdszKeyword,
                    BsglRamlrsJkzbszKeyword):

    def test_01_add_bsrw_success(self):
        """反洗钱报送任务新增+废弃报送任务成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        self.bsglMainFrame()
        # 判断报送任务是否存在，存在则废弃
        self.queryBsrw("2020年07月18日", "可疑报告")
        res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
        if res != "共有 0 个报送任务，0 个已过期":
            self.abandonBsrw("反洗钱任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRamlrsTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw("SUS010", "20200718", type="day")
        self.addBsrwSave()
        # 断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.closeXzrw_success()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_ramlrs_bsfw_success(self):
        """反洗钱报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("非固定频率", "可疑报告")
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
        """反洗钱报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、修改单个报送内容设置
        self.bsglMainFrame()
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 0 /2 * * ?", "5", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_change_bscs_success(self):
        """反洗钱报送参数设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送参数管理页签
        self.swithToBscs()
        # 6、修改报送参数设置并保存成功
        self.bsglMainFrame()
        self.changeBscsRamlrsGsbm("测试部门1")
        self.changeBscsRamlrsBgjgbm("bgjgbm20210644")
        self.changeBscsRamlrsSjblj("C:/TEST/RAMLRS//TEST/RAMLRS")
        self.changeBscsRamlrsZjdq("15")
        self.changeBscsRamlrsSave()
        # 断言保存成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功!')
        # 关闭弹窗
        self.changeBscsRamlrsSaveOk()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_change_bssq_success(self):
        """反洗钱报送授权+取消授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送授权管理页签
        self.swithToBssq()
        # 6、选择人员授权保存并断言成功
        self.bsglMainFrame()
        conf = Config()
        login_user = conf.get("BaseUrl", "user_name")
        self.changeBssqRlctsfxqRymc(login_user)
        self.changeBssqRlctsfxqRefresh()
        self.changeBssqRlctsfxqSq()
        self.changeBssqRlctsfxqFrame()
        self.changeBssqRlctsfxqFxk()
        self.changeBssqRlctsfxqSave()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '授权成功！')
        self.Click(self.ALERT_QRCG1)
        # 6、选择人员取消授权保存并断言成功
        self.changeBssqRlctsfxqFxk()
        self.changeBssqRlctsfxqSave()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '授权成功！')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_change_splc_success(self):
        """反洗钱审批流程成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送授权管理页签
        self.swithToBssq()
        # 6、选择人员授权保存并断言成功
        self.bsglMainFrame()
        conf = Config()
        login_user = conf.get("BaseUrl", "user_name")
        self.changeBssqRlctsfxqRymc(login_user)
        self.changeBssqRlctsfxqRefresh()
        res = self.GetTagText(self.SQBZ_TEXT)
        if res != "已授权":
            self.changeBssqRlctsfxqSq()
            self.changeBssqRlctsfxqFrame()
            self.changeBssqRlctsfxqFxk()
            self.changeBssqRlctsfxqSave()
            self.Click(self.ALERT_QRCG1)
            self.SwitchFatherFrame()
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 5、进入审批流程管理页签
        self.changeSplcRlctsfxqYh(login_user)
        self.changeSplcRlctsfxqRefresh()
        self.changeSplcRlctsfxqFxk()
        self.changeSplcRlctsfxqPlxg()
        self.QuiteFrame()
        self.changeSplcRlctsfxqframe()
        self.changeSplcRlctsfxqChoiceSplc("反洗钱审批")
        self.changeSplcRlctsfxqSave()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        self.Click(self.ALERT_QRCG1)
        self.SwitchFatherFrame()
        # 5、进入报送授权管理页签
        self.swithToBssq()
        # 6、选择人员授权保存并断言成功
        self.bsglMainFrame()
        self.changeBssqRlctsfxqRymc(login_user)
        self.changeBssqRlctsfxqRefresh()
        self.changeBssqRlctsfxqSq()
        self.changeBssqRlctsfxqFrame()
        self.changeBssqRlctsfxqFxk()
        self.changeBssqRlctsfxqSave()
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_change_kytzsz_success(self):
        """反洗钱新增+删除可疑特征设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入可疑特征设置页签
        self.swithToKytzsz()
        # 6、新增可疑特征设置
        self.bsglMainFrame()
        self.changeKytzszRamlrsAdd()
        self.changeKytzszRamlrsDm("1213")
        self.changeKytzszRamlrsSm("12345")
        self.changeKytzszRamlrsSzlx()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        self.changeKytzszRamlrsJcbzm()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        self.changeKytzszRamlrsJszb("1213")
        self.changeKytzszRamlrsSave()
        # 7.删除可疑特征设置
        self.changeKytzszRamlrsDelete("1213")
        # 断言删除成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '删除成功!')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_change_sbwdsz_success(self):
        """反洗钱新增+删除上报网点设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入上报网点设置页签
        self.swithToSbwdsz()
        # 6、新增上报网点设置
        self.bsglMainFrame()
        self.changeSbwdszRamlrsAdd()
        self.changeSbwdszRamlrsAddWddm("111333")
        self.changeSbwdszRamlrsAddWdmc("zlm111333")
        self.changeSbwdszRamlrsAddHylb("财务公司")
        self.changeSbwdszRamlrsSave()
        self.Click(self.ALERT_QRCG1)
        # 7.删除上报网点设置
        self.changeSbwdszRamlrsFxkOne("111333")
        self.changeSbwdszRamlrsDelete()
        # 断言删除成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '删除成功!')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_09_change_khzlwh_success(self):
        """反洗钱客户资料维护成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入客户资料维护页签
        self.swithToKhzlwh()
        # 6、修改客户资料维护信息
        self.bsglMainFrame()
        self.changeKhzlwhRamlrsKhbh("12345")
        self.changeKhzlwhRamlrsRefresh()
        res = self.GetTagText(self.TEXT_ZJ_KHZL)
        if res != "总计0条":
            self.changeKhzlwhRamlrsXq("12345")
            self.QuiteFrame()
            self.SwitchFrame(self.KHZLWH_KHXQ_FRAME)
            self.changeKhzlwhRamlrsFrzmwjyxq("20250329")
            self.changeKhzlwhRamlrsGdzmwjyxq("2025-03-29")
            self.changeKhzlwhRamlrsSave()
        # 没有这个客户信息
        else:
            print("查询结果为0，请重新输入")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_change_skhmdsz_success(self):
        """反洗钱新增+删除涉恐黑名单设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入涉恐黑名单设置页签
        self.swithToSkhmdsz()
        # 6、新增涉恐黑名单设置并将新增数据删除
        self.bsglMainFrame()
        self.changeSkhmdszRamlrsAdd()
        self.changeSkhmdszRamlrsAddSkzzhrymc("1213")
        self.changeSkhmdszRamlrsAddZjhm("1213")
        self.changeSkhmdszRamlrsAddBz("自动化测试")
        self.changeSkhmdszRamlrsSave()
        self.Click(self.ALERT_QRCG1)
        self.changeSkhmdszRamlrsSkzzhrymc("1213")
        self.changeSkhmdszRamlrsZjhm("1213")
        self.changeSkhmdszRamlrsRefresh()
        self.changeSkhmdszRamlrsFxkOne("1213")
        self.changeSkhmdszRamlrsDelete()
        # 断言删除成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '删除成功')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_11_change_jkzbsz_success(self):
        """反洗钱编辑监控指标设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择反洗钱品种进入反洗钱管理界面
        self.intoRamlrsTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入监控指标设置页签
        self.swithToJkzbsz()
        # 6、查询监控指标设置并修改该数据
        self.bsglMainFrame()
        self.changeJkzbszRamlrsJczb("人民币对公大额")
        self.changeJkzbszRamlrsRefresh()
        self.changeJkzbszRamlrsSbfw("人民币对公大额")
        self.changeJkzbszRamlrsLjjyje("1800000")
        self.changeJkzbszRamlrsDbjyje("600000")
        self.changeJkzbszRamlrsSave()
        # 断言编辑成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.Click(self.ALERT_QRCG1)
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
