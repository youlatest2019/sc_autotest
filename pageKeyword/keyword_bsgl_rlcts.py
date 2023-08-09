from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRlctsBscsKeyword(RLCTSBscsElement, WebDriver):
    """大额监控报送参数"""

    def changeBscsRlctsSave(self):
        """大额监控报送参数-保存按钮"""
        self.Click(self.BUTTON_SAVE_BSCS_DE)

    def changeBscsRlctsJedw(self, text):
        """大额监控报送参数-金额单位"""
        self.Click(self.INPUT_JEDW_DE.format(text))

    def changeBscsRlctsJesxed(self, text):
        """大额监控报送参数-金额筛选额度"""
        self.ClearData(self.INPUT_JESXED_DE)
        self.Input(text, self.INPUT_JESXED_DE)

    def changeBscsRlctsDezjbm(self, text):
        """大额监控报送参数-大额资金编码"""
        self.ClearData(self.INPUT_DEZJBM_DE)
        self.Input(text, self.INPUT_DEZJBM_DE)

    def changeBscsRlctsDezjsjbbbh(self, text):
        """大额监控报送参数-大额资金数据包版本号"""
        self.ClearData(self.INPUT_DEZJSJBBBH_DE)
        self.Input(text, self.INPUT_DEZJSJBBBH_DE)

    def changeBscsRlctsDrzfzjebm(self, text):
        """大额监控报送参数-当日支付总金额编码"""
        self.ClearData(self.INPUT_DRZFZJE_DE)
        self.Input(text, self.INPUT_DRZFZJE_DE)

    def changeBscsRlctsDrzfzjesjbbbh(self, text):
        """大额监控报送参数-当日支付总金额数据包版本号"""
        self.ClearData(self.INPUT_DRZFZJESJBBBH_DE)
        self.Input(text, self.INPUT_DRZFZJESJBBBH_DE)

    def changeBscsRlctsDewjscdz(self, text):
        """大额监控报送参数-大额文件上传地址"""
        self.ClearData(self.INPUT_DEWJSCDZ_DE)
        self.Input(text, self.INPUT_DEWJSCDZ_DE)

    def changeBscsRlctsDyjkyhm(self, text):
        """大额监控报送参数-调用接口用户名"""
        self.ClearData(self.INPUT_DYJKYHM_DE)
        self.Input(text, self.INPUT_DYJKYHM_DE)

    def changeBscsRlctsDyjkmm(self, text):
        """大额监控报送参数-调用接口密码"""
        self.ClearData(self.INPUT_DYJKMM_DE)
        self.Input(text, self.INPUT_DYJKMM_DE)

    def changeBscsRlctsTzry(self, text):
        """大额监控报送参数-制度文件更新通知人员"""
        self.Click(self.BUTTON_ZDWJGXTZRY_DE)
        self.Click(self.BUTTON_XL_DE)
        self.Input(text, self.INPUT_ZDWJGXTZRY_DE)
        self.Click(self.BUTTON_CHOICE_ALL)

    def changeBscsRlctsZdwjxzdz(self, text):
        """大额监控报送参数-制度文件下载地址"""
        self.ClearData(self.INPUT_ZDWJXZDZ_DE)
        self.Input(text, self.INPUT_ZDWJXZDZ_DE)

    def changeBscsRlctsZdwjqdcxdz(self, text):
        """大额监控报送参数-制度文件清单查询地址"""
        self.ClearData(self.INPUT_ZDWJQDCXDZ_DE)
        self.Input(text, self.INPUT_ZDWJQDCXDZ_DE)

    def changeBscsRlctsRzwjcxdz(self, text):
        """大额监控报送参数-日志文件查询地址"""
        self.ClearData(self.INPUT_RZWJCXDZ_DE)
        self.Input(text, self.INPUT_RZWJCXDZ_DE)


class BsglRlctsZjytszKeyword(RLCTSZjytszElement, WebDriver):
    """大额监控资金用途设置"""

    def changeZjytszRlctsSave(self):
        """大额监控资金用途设置-保存按钮"""
        self.Click(self.BUTTON_SAVE_DEJK)

    def changeZjytszRlctsAdd(self):
        """大额监控资金用途设置-新增按钮"""
        self.Click(self.BUTTON_ADD_DEJK)

    def changeZjytszRlctsDelete(self):
        """大额监控资金用途设置-删除按钮"""
        self.Click(self.BUTTON_DELETE_DEJK)

    def changeZjytszRlctsZjytbm(self, text):
        """大额监控资金用途设置-资金用途编码"""
        self.Input(text, self.INPUT_ZJYTBM_DE)

    def changeZjytszRlctsZjytbmhy(self, text):
        """大额监控资金用途设置-资金用途编码含义"""
        self.Input(text, self.INPUT_ZJYTBMHY_DE)

    def changeZjytszRlctsFxk(self, text):
        """大额监控资金用途设置-单选复选框"""
        self.Click(self.BUTTON_BOX_ONE.format(text))
