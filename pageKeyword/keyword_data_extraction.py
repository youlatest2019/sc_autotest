from pageElement.page_sjgl_common import *
from baseOperation.WebOperation import *


class DataExtractionKeyword(WebDriver, SjglMainMenueElement, SjglDataExtractionElement):

    def OpenDataExtractPage(self):
        """打开数据抽取页面"""
        self.RefreshPage()
        self.MouseFouce(self.SJGL_MAIN_MENUE)
        self.Click(self.BUTTON_DATA_EXTRACTION)
        self.Click(self.DATA_EXTRACTION_BT)
        self.SwitchFrame(self.DATA_EXTRACTION_FRAME)

    def DataExtractPageCxtj(self, PZMC, TASK_NAME):
        """输入查询条件-报送品种、任务名称"""
        self.Click(self.DATA_EXTRACT_BSPZ.format(PZMC))
        self.Input(TASK_NAME, self.DATA_EXTRACT_TASK_NAME)
        self.Click(self.DATA_EXTRACT_START_DATE)

    def DataExtractPageDate(self, STARTDATE, ENDTDATE):
        """输入查询条件-数据日期"""
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.DATE_FRAME)
        self.Click(self.DATE_CLEAR)
        self.SwitchFatherFrame()
        self.SwitchFrame(self.DATA_EXTRACTION_FRAME)
        self.Input(STARTDATE, self.DATA_EXTRACT_START_DATE)
        self.Click(self.DATA_EXTRACT_END_DATE)
        self.SwitchFatherFrame()
        self.SwitchFrameByElement(self.DATE_FRAME)
        self.Click(self.DATE_CLEAR)
        self.SwitchFatherFrame()
        self.SwitchFrame(self.DATA_EXTRACTION_FRAME)
        self.Input(ENDTDATE, self.DATA_EXTRACT_END_DATE)
        self.Click(self.DATA_EXTRACT_REFRESH)

    def DataExtractPageFxkAll(self):
        """全选复选框"""
        self.Click(self.DATA_EXTRACT_FXK_ALL)

    def DataExtractPageCxqs(self):
        """点击重新取数按钮"""
        self.Click(self.DATA_EXTRACT_DATA_AGAIN)
        self.Click(self.DATA_EXTRACT_ALERT_OK)

    def DataExtractPageClear(self):
        """清空数据按钮"""
        self.Click(self.DATA_EXTRACT_CLEAR_DATA)
        self.Click(self.DATA_EXTRACT_ALERT_OK)

