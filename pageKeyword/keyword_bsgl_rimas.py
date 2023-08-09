from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRimasBscsKeyword(BsglElementFrame, RimasBscsElement, WebDriver):
    """利率报备报送参数"""

    def changeRimasBscsSave(self):
        """利率报备修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RIMAS)

    def changeRimasBscsBsjrfs(self, text):
        """利率报备修改报送参数-报送接入方式"""
        self.Click(self.INPUT_BSJRFS.format(text))

    def changeRimasBscsQtbm(self, qtbm, text):
        """利率报备修改报送参数-牵头部门"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(qtbm, self.INPUT_QTBM.format(text))

    def changeRimasBscsQtbmlxr(self, qtbmlxr, text):
        """利率报备修改报送参数-牵头部门联系人"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(qtbmlxr, self.INPUT_QTBM.format(text))

    def changeRimasBscsQtbmlxdh(self, qtbmlxdh, text):
        """利率报备修改报送参数-牵头部门联系电话"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(qtbmlxdh, self.INPUT_QTBM.format(text))

    def changeRimasBscsYhm(self, yhm, text):
        """利率报备修改报送参数-用户名"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(yhm, self.INPUT_QTBM.format(text))

    def changeRimasBscsRhzl(self, rhzl, text):
        """利率报备修改报送参数-人行直连服务地址"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(rhzl, self.INPUT_QTBM.format(text))

    def changeRimasBscsPassw(self, password, text):
        """利率报备修改报送参数-密码"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(password, self.INPUT_QTBM.format(text))

    def changeRimasBscsFqcyz(self, fcyz, text):
        """利率报备修改报送参数-发起参与者应用系统标识"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(fcyz, self.INPUT_QTBM.format(text))

    def changeRimasBscsJscyz(self, jcyz, text):
        """利率报备修改报送参数-接收参与者编码"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(jcyz, self.INPUT_QTBM.format(text))

    def changeRimasBscsJscyzbs(self, jcyzbs, text):
        """利率报备修改报送参数-接收参与者应用系统标识"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(jcyzbs, self.INPUT_QTBM.format(text))

    def changeRimasBscsLink(self, link, text):
        """利率报备修改报送参数-RIMAS_LINK服务地址"""
        self.ClearData(self.INPUT_QTBM.format(text))
        self.Input(link, self.INPUT_QTBM.format(text))

    def changeRimasBscsSbsp(self):
        """利率报备修改报送参数-上报审批"""
        self.Click(self.INPUT_SBSP_RIMAS)
