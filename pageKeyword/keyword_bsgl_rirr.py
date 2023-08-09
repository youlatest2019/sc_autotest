from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRirrBscsKeyword(BsglElementFrame, RirrBscsElement, WebDriver):
    """利率报备R表报送参数"""

    def changeRirrBscsSbspYes(self):
        """利率报备R表修改报送参数-开启上报审批"""
        self.Click(self.RIRR_SBSP_YES)

    def changeRirrBscsSbspNo(self):
        """利率报备R表修改报送参数-关闭上报审批"""
        self.Click(self.RIRR_SBSP_NO)

    def changeRirrBscsYhkjYes(self):
        """利率报备R表修改报送参数-开启用户口径填报说明展示"""
        self.Click(self.RIRR_YHKJ_YES)

    def changeRirrBscsYhkjNo(self):
        """利率报备R表修改报送参数-关闭用户口径填报说明展示"""
        self.Click(self.RIRR_YHKJ_NO)

    def changeRirrBscsSave(self):
        """利率报备R表报送参数-保存"""
        self.Click(self.BUTTON_SAVE_RIRR)