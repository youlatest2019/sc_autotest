from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRsaferBscsKeyword(BsglElementFrame, RsaferBscsElement, WebDriver):
    """外管局报表报送参数"""

    def changeRsaferBscsSave(self):
        """外管局报表修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RSAFER)

    def changeRsaferBscsJy(self):
        """外管局报表修改报送参数-强制数据校验开关"""
        self.Click(self.BUTTON_JY)

    def changeRsaferBscsDay(self, text):
        """外管局报表修改报送参数-报送提醒天数设置（天）"""
        self.ClearData(self.INPUT_DAY)
        self.Input(text, self.INPUT_DAY)

    def changeRsaferBscsSbsp(self):
        """外管局报表修改报送参数-上报审批"""
        self.Click(self.BUTTON_SBSP)


class BsglRsaferWbzmyhlKeyword(BsglElementFrame, RsaferWbzmyhlszElement, WebDriver):
    """外管局报表外币折美元汇率设置"""

    def changeRsaferWbzmyhlSave(self):
        """外管局报表修改外币折美元汇率设置-保存"""
        self.Click(self.BUTTON_SAVE_WBZMY)

    def ClickRsaferWbzmyhlCxtj(self, wbbz):
        """外管局报表修改外币折美元汇率设置-查询条件"""
        self.Click(self.CLICK_BZ_CHECK)
        self.Click(self.INPUT_BZ_CHECK.format(wbbz))

    def changeRsaferWbzmyhlRfresh(self):
        """外管局报表修改外币折美元汇率设置-刷新"""
        self.Click(self.BUTTON_REFRESH_WBZMY)

    def changeRsaferWbzmyhlAdd(self):
        """外管局报表修改外币折美元汇率设置-新增"""
        self.Click(self.BUTTON_ADD_WBZMY)

    def changeRsaferWbzmyhlBz(self, text):
        """外管局报表修改外币折美元汇率设置-币种"""
        self.Click(self.INPUT_BZ.format(text))

    def changeRsaferWbzmyhlSxrq(self, text):
        """外管局报表修改外币折美元汇率设置-生效日期"""
        self.Input(text, self.INPUT_SXRQ)

    def changeRsaferWbzmyhlRate(self, text):
        """外管局报表修改外币折美元汇率设置-汇率"""
        self.Input(text, self.INPUT_HL_RSAFER)

    def changeRsaferWbzmyhlDelete(self):
        """外管局报表修改外币折美元汇率设置-删除"""
        self.Click(self.BUTTON_DELETE_WBZMY)

    def changeRsaferWbzmyhlDeleteX(self):
        """外管局报表修改外币折美元汇率设置-删除X"""
        self.Click(self.BUTTON_DELETEX_WBZMY)

    def changeRsaferWbzmyhlFxkAll(self):
        """外管局报表修改外币折美元汇率设置-全选复选框"""
        self.Click(self.BUTTON_BOX_ALL_WB)

    def changeRsaferWbzmyhlFxkOne(self):
        """外管局报表修改外币折美元汇率设置-单选复选框"""
        self.Click(self.BUTTON_BOX_ONE_WB)

    def changeRsaferWbzmyhlClose(self):
        """外管局报表修改外币折美元汇率设置-关闭保存成功弹窗"""
        self.Click(self.ALERT_WBZMYHL)
