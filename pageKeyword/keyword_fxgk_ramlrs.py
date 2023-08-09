from pageElement.page_fxgk_common import *
from baseOperation.WebOperation import *
from data.data_class.ramlrs_data import *


class RamlrsMainKeyword(WebDriver, FxgkMainMenueElement, PubFxqBspzElement, RamlrsData):

    def clickFxgkMainMenue(self):
        """进入风险管控主菜单"""
        self.Click(self.FXGK_MENUE)

    def intoRamlrsZbPage(self):
        """进入反洗钱甄别界面"""
        self.Click(self.FXQZB_TAB)
        self.Click(self.FXQZB_TAG)
        self.SwitchFrame(self.FXQZB_FRAME)

    def intoRamlrsSpPage(self):
        """进入可疑交易审批界面"""
        self.Click(self.FXQSP_TAB)
        self.Click(self.FXQSP_TAG)
        self.SwitchFrame(self.FXQSP_FRAME)
        self.Click(self.BUTTON_INTO_FXQ.format(self.KYZBSP))

    def intoRamlrsBsPage(self):
        """进入可疑交易报送界面"""
        self.Click(self.FXQBS_TAB)
        self.Click(self.FXQBS_TAG)
        self.SwitchFrame(self.FXQBS_FRAME)

    def AddButtonRamlrs(self):
        """反洗钱甄别界面-新增按钮"""
        self.Click(self.BUTTON_ADD_FXQ)
        self.QuiteFrame()
        self.SwitchFrame(self.ADD_FRAME_FXQ)

    def AddRamlrsData(self):
        """反洗钱甄别界面-新增数据"""
        self.Click(self.BUTTON_CUST_INFO_FXQ)
        self.QuiteFrame()
        self.SwitchFrame(self.CUST_FARME_FXQ)
        self.DoubleClick(self.DOUBLE_CLICK_CUST_FXQ)
        self.QuiteFrame()
        self.SwitchFrame(self.ADD_FRAME_FXQ)
        self.Input(self.JYLSH, self.INPUT_TRANSACTION_NUMBER_FXQ)
        self.Click(self.INPUT_SF_FLAG_FXQ.format(self.SFBZ))
        self.Input(self.JY_DATE, self.INPUT_BUS_DATE_FXQ)
        self.Click(self.INPUT_BUS_TYPE_FXQ.format(self.JY_TYPE))
        self.Click(self.INPUT_BZ_FXQ.format(self.BZ))
        self.Input(self.JY_MONEY, self.INPUT_BUS_AMOUNT_FXQ)
        self.Input(self.NOTES, self.INPUT_REMARKS_FXQ)
        self.Input(self.BFZH, self.INPUT_OUR_ACCOUNT_NUMBER_FXQ)
        self.Input(self.BFKHHM, self.INPUT_NAME_OF_OUR_BANK_FXQ)
        self.Input(self.DFZH, self.INPUT_OTHER_ACCOUNT_NUMBER_FXQ)
        self.Input(self.DFHM, self.INPUT_OTHER_ACCOUNT_NAME_FXQ)
        self.Input(self.DFKHHM, self.INPUT_NAME_OF_OTHER_BANK_FXQ)
        self.Click(self.INPUT_JCZB_FXQ.format(self.JCZB))
        self.Click(self.INPUT_ZBJL_FXQ.format(self.ZBJL))
        self.Input(self.REASON_SM, self.INPUT_REASON_FXQ)
        self.Click(self.BUTTON_SAVE_FXQ)
        self.QuiteFrame()
        self.SwitchFrame(self.FXQZB_FRAME)

    def QueryRamlrsData(self):
        """查询对方户名、确认可疑"""
        self.Input(self.DFHM, self.INPUT_QUERY_DFHM_FXQ)
        self.Click(self.BUTTON_REFRESH_FXQ)
        self.Click(self.FXK_ALL_FXQ)
        self.Click(self.BUTTON_QRKY_FXQ)
        self.QuiteFrame()
        self.SwitchFrameByElement(self.QRKY_FRAME_FXQ)
        self.Input(self.INPUT_QRKY_FXQ_CONTENT, self.INPUT_QRKY_FXQ)
        self.Click(self.BUTTON_QRKY_SAVE_FXQ)
        self.Click(self.AUI_CLOSE)
        self.SwitchFatherFrame()
        self.Click(self.BUTTON_CLOSE_QRKY)
        self.QuiteFrame()
        self.SwitchFrame(self.FXQZB_FRAME)
        self.Click(self.BUTTON_REFRESH_FXQ)
        self.Click(self.FXK_ALL_FXQ)

    def SubmitRamlrsHdData(self):
        """提交审批"""
        self.Click(self.BUTTON_SUBMIT_FXQ)

    def QueryRamlrsSpDataPage(self, INPUT_CUST_NUMBER):
        """可疑交易审批界面-查询数据"""
        self.Input(INPUT_CUST_NUMBER, self.INPUT_CUST_NUMBER_KYJYSP)
        self.Click(self.BUTTON_REFRESH_KYZBSP)
        self.Click(self.FXK_KYZBSP)

    def InputRamlrsSpyj(self, SPYJ):
        """可疑交易审批界面-输入审批意见"""
        self.Input(SPYJ, self.INPUT_SPYJ_KYZBSP)

    def RamlrsSpAgree(self):
        """可疑交易审批界面-同意"""
        self.Click(self.BUTTON_AGREE_KYZBSP)

    def QueryRamlrsBsDataPage(self, INPUT_CUST_NUMBER):
        """可疑交易报送界面-查询数据并点击提交"""
        self.Input(INPUT_CUST_NUMBER, self.INPUT_CUST_NUMBER_KYJYBS)
        self.Click(self.BUTTON_REFRESH_KYJYBS)
        self.Click(self.FXK_KYJYBS)
        self.Click(self.BUTTON_SUBMIT_KYJYBS)
        self.SwitchFrame(self.ADD_KYBW_FRAME)

    def AddRamlrsBsDataPage(self, INPUT_CUST_NUMBER):
        """新增可疑交易报文并点击提交"""
        self.Input(INPUT_CUST_NUMBER, self.INPUT_CUST_NUMBER_KYJYBS)
