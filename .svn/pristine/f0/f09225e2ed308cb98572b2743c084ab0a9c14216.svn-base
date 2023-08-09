from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRsazjBscsKeyword(BsglElementFrame, RsazjBscsElement, WebDriver):
    """浙江国资委报送参数"""

    def changeRsazjBscsSave(self):
        """浙江国资委修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RSAZJ)

    def changeRsazjBscsFkjylx(self, text, text1):
        """浙江国资委修改报送参数-付款交易类型"""
        self.Click(self.BUTTON_FKJYLX)
        self.Click(self.INPUT_FKJYLX.format(text))
        self.Click(self.INPUT_FKJYLX.format(text))
        self.Click(self.INPUT_FKJYLX.format(text1))
        self.Click(self.BUTTON_FKJYLX)

    def changeRsazjBscsSkjylx(self, text, text1):
        """浙江国资委修改报送参数-收款交易类型"""
        self.Click(self.BUTTON_SKJYLX)
        self.Click(self.INPUT_SKJYLX.format(text))
        self.Click(self.INPUT_SKJYLX.format(text))
        self.Click(self.INPUT_SKJYLX.format(text1))
        self.Click(self.BUTTON_SKJYLX)

    def changeRsazjBscsDesxed(self, text):
        """浙江国资委修改报送参数-大额筛选额度"""
        self.ClearData(self.INPUT_DESXED)
        self.Input(text, self.INPUT_DESXED)

    def changeRsazjBscsDezjIp(self, text):
        """浙江国资委修改报送参数-大额资金监测系统服务端IP"""
        self.ClearData(self.INPUT_DE_IP)
        self.Input(text, self.INPUT_DE_IP)

    def changeRsazjBscsDezjPort(self, text):
        """浙江国资委修改报送参数-大额资金监测系统服务端端口号"""
        self.ClearData(self.INPUT_DE_PORT)
        self.Input(text, self.INPUT_DE_PORT)

    def changeRsazjBscsDeProtocol(self, text):
        """浙江国资委修改报送参数-大额资金监测系统服务端协议类型"""
        self.ClearData(self.INPUT_DE_PROTOCOL)
        self.Input(text, self.INPUT_DE_PROTOCOL)

    def changeRsazjBscsAppId(self, text):
        """浙江国资委修改报送参数-AppId"""
        self.ClearData(self.INPUT_APPID)
        self.Input(text, self.INPUT_APPID)

    def changeRsazjBscsSecret(self, text):
        """浙江国资委修改报送参数-SECRET"""
        self.ClearData(self.INPUT_SECRET)
        self.Input(text, self.INPUT_SECRET)

    def changeRsazjBscsPrivatekey(self, text):
        """浙江国资委修改报送参数-privatekey"""
        self.ClearData(self.INPUT_PRIVATEKEY)
        self.Input(text, self.INPUT_PRIVATEKEY)

    def changeRsazjBscsSmPublickey(self, text):
        """浙江国资委修改报送参数-sm-publickey"""
        self.ClearData(self.INPUT_SMPUBLICKEY)
        self.Input(text, self.INPUT_SMPUBLICKEY)
