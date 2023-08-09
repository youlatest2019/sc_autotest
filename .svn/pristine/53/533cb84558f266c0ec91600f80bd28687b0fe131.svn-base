from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_common import *
from pageElement.page_bsgl import *
import sys
from pageKeyword.keyword_fxgk_ramlrs import *
from Common.OracleControl import *
from Config.BaseEnv import *


class RamlrsMainProcessTest(InitCls, BsglMainKeyword, BsglPubBssqDeFxqKeyword, BsglPubSplcDeFxqKeyword, PubBsrwElement,
                            RamlrsMainKeyword):
    def test_01_rmbtd_main_process(self):
        """征信--建立分组->授权->新增报送任务->报送任务新增一条数据-->核对提交->审批通过->上报下载，确认成功->查询，主流程案例"""
        sql = "UPDATE dcab_pub_setting SET PARAM_VALUE = 1 where BSPZBH = 'RAMLRS'"
        ora = OracleControl(oracle_157_dm)
        ora.exc_sql(sql)
        ora.commit()
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        # self.intoBsglMainMenu()
        # self.switchToBsglBaseFrame()
        # # 3、选择征信品种进入征信管理界面
        # self.intoRamlrsTab()
        # # 4、切换到品种管理frame
        # self.switchBspzFrame()
        # # 5、进入报送授权管理页签
        # self.swithToBssq()
        # # 6、选择人员授权保存并断言成功
        # self.bsglMainFrame()
        # conf = Config()
        # login_user = conf.get("BaseUrl", "user_name")
        # self.changeBssqRlctsfxqRymc(login_user)
        # self.changeBssqRlctsfxqRefresh()
        # res = self.GetTagText(self.SQBZ_TEXT)
        # if res != "已授权":
        #     self.changeBssqRlctsfxqSq()
        #     self.changeBssqRlctsfxqFrame()
        #     self.changeBssqRlctsfxqFxk()
        #     self.changeBssqRlctsfxqSave()
        #     self.Click(self.ALERT_QRCG1)
        #     self.SwitchFatherFrame()
        # self.SwitchFatherFrame()
        # self.swithToSplc()
        # self.bsglMainFrame()
        # # 7、进入审批流程管理页签
        # self.changeSplcRlctsfxqYh(login_user)
        # self.changeSplcRlctsfxqRefresh()
        # self.changeSplcRlctsfxqFxk()
        # self.changeSplcRlctsfxqPlxg()
        # self.QuiteFrame()
        # self.changeSplcRlctsfxqframe()
        # self.changeSplcRlctsfxqChoiceSplc("反洗钱审批")
        # self.changeSplcRlctsfxqSave()
        # self.switchToBsglBaseFrame()
        # self.switchBspzFrame()
        # self.bsglMainFrame()
        # self.Click(self.ALERT_QRCG1)
        # 8、点击主菜单--风险管控，进入可疑交易甄别界面
        self.RefreshPage()
        self.clickFxgkMainMenue()
        self.intoRamlrsZbPage()
        # 9、点击新增按钮，新增数据
        self.AddButtonRamlrs()
        self.AddRamlrsData()
        # 10、将数据确认可疑，并提交审批
        self.QueryRamlrsData()
        CUST_NUMBER = self.GetElementAttrbute(self.GET_CUST_NUMBER, "value")
        self.SubmitRamlrsHdData()
        res1 = self.GetTagText(self.AUI_CONTENT)
        self.assertIn("提交成功!", res1)
        # self.AUI_CLOSE()
        # 11、进入可疑交易审批页面,审批通过
        self.RefreshPage()
        self.clickFxgkMainMenue()
        self.intoRamlrsSpPage()
        self.QueryRamlrsSpDataPage(CUST_NUMBER)
        self.InputRamlrsSpyj("审批通过")
        self.RamlrsSpAgree()
        res2 = self.GetTagText(self.AUI_CONTENT)
        self.assertIn("审批通过成功!", res2)
        # self.AUI_CLOSE()
        # 12、进入可疑交易报送页面,提交审批
        self.RefreshPage()
        self.clickFxgkMainMenue()
        self.intoRamlrsBsPage()

