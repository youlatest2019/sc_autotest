from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRpbccBscsKeyword(BsglElementFrame, RpbccBscsElement, WebDriver):
    """人行报表报送参数"""

    def changeRpbccBscsSave(self):
        """人行报表修改报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RH)

    def changeRpbccBscsJgldm(self, text):
        """人行报表修改报送参数-机构类代码"""
        self.ClearData(self.INPUT_JGLDM_RH)
        self.Input(text, self.INPUT_JGLDM_RH)

    def changeRpbccBscsDqdm(self, text):
        """人行报表修改报送参数-地区代码"""
        self.ClearData(self.INPUT_DQDM_RH)
        self.Input(text, self.INPUT_DQDM_RH)

    def changeRpbccBscsFile(self):
        """人行报表修改报送参数-下载文件设置"""
        self.Click(self.INPUT_FILE_RH)

    def changeRpbccBscsSbsp(self):
        """人行报表修改报送参数-上报审批"""
        self.Click(self.INPUT_SBSP_RH)
