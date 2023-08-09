from pageElement.page_bsgl import *
from baseOperation.WebOperation import *


class BsglRamlrsBscsKeyword(RAMLRSBscsElement, WebDriver):
    """反洗钱报送参数"""

    def changeBscsRamlrsSave(self):
        """反洗钱报送参数-保存按钮"""
        self.Click(self.BUTTON_SAVE_RAMLRS)

    def changeBscsRamlrsGsbm(self, text):
        """反洗钱报送参数-可疑交易默认归属部门"""
        self.Click(self.INPUT_GSBM_RAMLRS.format(text))

    def changeBscsRamlrsBgjgbm(self, text):
        """反洗钱报送参数-报告机构编码"""
        self.ClearData(self.INPUT_BGJGBM_RAMLRS)
        self.Input(text, self.INPUT_BGJGBM_RAMLRS)

    def changeBscsRamlrsSjblj(self, text):
        """反洗钱报送参数-数据包文件保存路径"""
        self.ClearData(self.INPUT_SJBLJ_RAMLRS)
        self.Input(text, self.INPUT_SJBLJ_RAMLRS)

    def changeBscsRamlrsZjdq(self, text):
        """反洗钱报送参数-证件到期提醒天数"""
        self.ClearData(self.INPUT_ZJDQTXTS_RAMLRS)
        self.Input(text, self.INPUT_ZJDQTXTS_RAMLRS)

    def changeBscsRamlrsSaveOk(self):
        """反洗钱报送参数-保存成功关闭按钮"""
        self.Click(self.BUTTON_CLOSE_RAMLRS)


class BsglRamlrsKytzszKeyword(RAMLRSKytzszElement, BsglElementFrame, PubBsrwElement, WebDriver):
    """反洗钱可疑特征设置"""

    def changeKytzszRamlrsAdd(self):
        """反洗钱可疑特征设置-新增"""
        self.Click(self.BUTTON_ADD_RAMLRS_KY)

    def changeKytzszRamlrsDm(self, text):
        """反洗钱可疑特征设置-可疑交易特征代码"""
        self.Input(text, self.INPUT_KYJYTZDM_KY)

    def changeKytzszRamlrsSm(self, text):
        """反洗钱可疑特征设置-可疑交易特征说明"""
        self.Input(text, self.INPUT_KYJYTZSM_KY)

    def changeKytzszRamlrsSzlx(self):
        """反洗钱可疑特征设置-涉罪类型代码-全部"""
        self.Click(self.INPUT_SZLXDM_KY)
        self.QuiteFrame()
        self.SwitchFrame(self.XZYSSZLX_FRAME)
        self.Click(self.BUTTON_FXK_ALL_KY)
        self.Click(self.BUTTON_OK_SZ)

    def changeKytzszRamlrsJcbzm(self):
        """反洗钱可疑特征设置-监测标准码-全部"""
        self.Click(self.INPUT_JCBZM_KY)
        self.QuiteFrame()
        self.SwitchFrame(self.XZJCBZMLX_FRAME)
        self.Click(self.BUTTON_FXK_ALL_KY)
        self.Click(self.BUTTON_OK_JC)

    def changeKytzszRamlrsJszb(self, text):
        """反洗钱可疑特征设置-技术指标"""
        self.Input(text, self.INPUT_JSZB_KY)

    def changeKytzszRamlrsSave(self):
        """反洗钱可疑特征设置-保存"""
        self.Click(self.BUTTON_SAVE_RAMLRS_KY)
        self.Click(self.ALERT_QRCG1)

    def changeKytzszRamlrsDelete(self, text):
        """反洗钱可疑特征设置-删除"""
        self.Click(self.BUTTON_FXK_ALL_KYJYTZ.format(text))
        self.Click(self.BUTTON_DETELE_RAMLRS_KY)
        self.AlertAccept()


class BsglRamlrsSbwdszKeyword(RAMLRSSbwdszElement, BsglElementFrame, PubBsrwElement, WebDriver):
    """反洗钱上报网点设置"""

    def changeSbwdszRamlrsAdd(self):
        """反洗钱上报网点设置-新增"""
        self.Click(self.BUTTON_ADD_SBWD)

    def changeSbwdszRamlrsSave(self):
        """反洗钱上报网点设置-保存"""
        self.Click(self.BUTTON_SAVE_SBWD)

    def changeSbwdszRamlrsDelete(self):
        """反洗钱上报网点设置-删除"""
        self.Click(self.BUTTON_DELETE_SBWD)

    def changeSbwdszRamlrsWddm(self, text):
        """反洗钱上报网点设置-查询条件-网点代码"""
        self.Input(text, self.QUERY_WDDM_SBWD)

    def changeSbwdszRamlrsWdmc(self, text):
        """反洗钱上报网点设置-查询条件-网点名称"""
        self.Input(text, self.QUERY_WDMC_SBWD)

    def changeSbwdszRamlrsRefresh(self):
        """反洗钱上报网点设置-刷新"""
        self.Click(self.BUTTON_REFRESH_SBWD)

    def changeSbwdszRamlrsAddWddm(self, text):
        """反洗钱上报网点设置-新增网点代码"""
        self.Input(text, self.INPUT_WDDM_SBWD)

    def changeSbwdszRamlrsAddWdmc(self, text):
        """反洗钱上报网点设置-新增网点名称"""
        self.Input(text, self.INPUT_WDMC_SBWD)

    def changeSbwdszRamlrsAddHylb(self, text):
        """反洗钱上报网点设置-新增行业类别"""
        self.Click(self.INPUT_HYLB_SBWD.format(text))

    def changeSbwdszRamlrsFxkOne(self, text):
        """反洗钱上报网点设置-单个复选框"""
        self.Click(self.FXK_ONE_SBWD.format(text))


class BsglRamlrsKhzlwhKeyword(RAMLRSKhzlwhElement, BsglElementFrame, PubBsrwElement, WebDriver):
    """反洗钱客户资料维护"""

    def changeKhzlwhRamlrsKhbh(self, text):
        """反洗钱客户资料维护-查询-客户编号"""
        self.Input(text, self.QUERY_KHBH_KHZL)

    def changeKhzlwhRamlrsKhmc(self, text):
        """反洗钱客户资料维护-查询-客户名称"""
        self.Input(text, self.QUERY_KHMC_KHZL)

    def changeKhzlwhRamlrsRefresh(self):
        """反洗钱客户资料维护-刷新"""
        self.Click(self.BUTTON_REFRESH_KHZL)

    def changeKhzlwhRamlrsXq(self, text):
        """反洗钱客户资料维护-详情"""
        self.Click(self.BUTTON_XQ_KHZL.format(text))

    def changeKhzlwhRamlrsFrzmwjyxq(self, text):
        """反洗钱客户资料维护-法人证明文件有效期"""
        self.Click(self.INPUT_FR_ZMWJYXQ_KHZL)
        self.SwitchFrameByElement(self.KHZLWH_YXQ_CJ)
        self.Click(self.BUTTON_CLEAR_KHZL)
        self.SwitchFatherFrame()
        self.Input(text, self.INPUT_FR_ZMWJYXQ_KHZL)

    def changeKhzlwhRamlrsGdzmwjyxq(self, text):
        """反洗钱客户资料维护-股东或实际控制人信息证明文件有效期"""
        self.Click(self.INPUT_GDSJR_ZMWJYXQ_KHZL)
        self.SwitchFrameByElement(self.KHZLWH_YXQ_CJ)
        self.Click(self.BUTTON_CLEAR_KHZL)
        self.SwitchFatherFrame()
        self.Input(text, self.INPUT_GDSJR_ZMWJYXQ_KHZL)

    def changeKhzlwhRamlrsSave(self):
        """反洗钱客户资料维护-保存"""
        self.Click(self.BUTTON_SAVE_KHZL)


class BsglRamlrsSkhmdszKeyword(RAMLRSSkhmdszElement, BsglElementFrame, PubBsrwElement, WebDriver):
    """反洗钱-涉恐黑名单设置"""

    def changeSkhmdszRamlrsSkzzhrymc(self, text):
        """反洗钱涉恐黑名单设置-查询-涉恐组织或人员名称"""
        self.Input(text, self.QUERY_SKZZHRYMC_HMD)

    def changeSkhmdszRamlrsZjhm(self, text):
        """反洗钱涉恐黑名单设置-查询-证件号码"""
        self.Input(text, self.QUERY_ZJHM_HMD)

    def changeSkhmdszRamlrsRefresh(self):
        """反洗钱涉恐黑名单设置-刷新"""
        self.Click(self.BUTTON_REFRESH_HMD)

    def changeSkhmdszRamlrsAdd(self):
        """反洗钱涉恐黑名单设置-新增"""
        self.Click(self.BUTTON_ADD_HMD)

    def changeSkhmdszRamlrsAddSkzzhrymc(self, text):
        """反洗钱涉恐黑名单设置-新增-涉恐组织或人员名称"""
        self.Input(text, self.INPUT_SKZZHRYMC_HMD)

    def changeSkhmdszRamlrsAddZjhm(self, text):
        """反洗钱涉恐黑名单设置-新增-证件号码"""
        self.Input(text, self.INPUT_ZJHM_HMD)

    def changeSkhmdszRamlrsAddBz(self, text):
        """反洗钱涉恐黑名单设置-新增-备注"""
        self.Input(text, self.INPUT_BZ_HMD)

    def changeSkhmdszRamlrsSave(self):
        """反洗钱涉恐黑名单设置-保存"""
        self.Click(self.BUTTON_SAVE_HMD)

    def changeSkhmdszRamlrsFxkOne(self, text):
        """反洗钱涉恐黑名单设置-勾选单条数据复选框"""
        self.Click(self.FXK_ONE_HMD.format(text))

    def changeSkhmdszRamlrsDelete(self):
        """反洗钱涉恐黑名单设置-删除"""
        self.Click(self.BUTTON_DELETE_HMD)
        self.AlertAccept()


class BsglRamlrsJkzbszKeyword(RAMLRSJkzbszElement, BsglElementFrame, PubBsrwElement, WebDriver):
    """反洗钱-监控指标设置"""

    def changeJkzbszRamlrsJczb(self, text):
        """反洗钱监控指标设置-查询-监测指标"""
        self.Click(self.QUERY_JCZB_JK.format(text))

    def changeJkzbszRamlrsCsmc(self, text):
        """反洗钱监控指标设置-查询-参数名称"""
        self.Input(text, self.QUERY_CSMC_JK)

    def changeJkzbszRamlrsRefresh(self):
        """反洗钱监控指标设置-刷新"""
        self.Click(self.BUTTON_REFRESH_JK)

    def changeJkzbszRamlrsSbfw(self, text):
        """反洗钱监控指标设置-编辑-上报范围"""
        self.Click(self.BUTTON_SBFW_CSZ_JK.format(text))
        self.Click(self.FXK_SBFW_JYLX_NO_JK)
        self.Click(self.FXK_SBFW_JYLX_YES_JK)
        self.Click(self.QUERY_CSMC_JK)

    def changeJkzbszRamlrsLjjyje(self, text):
        """反洗钱监控指标设置-编辑-累计交易金额"""
        self.ClearData(self.LJJYJE_CSZ_JK)
        self.Click(self.BUTTON_OK_JK)
        self.Input(text, self.LJJYJE_CSZ_JK)

    def changeJkzbszRamlrsDbjyje(self, text):
        """反洗钱监控指标设置-编辑-单笔交易金额"""
        self.ClearData(self.DBJYJE_CSZ_JK)
        self.Click(self.BUTTON_OK_JK)
        self.Input(text, self.DBJYJE_CSZ_JK)

    def changeJkzbszRamlrsSave(self):
        """反洗钱监控指标设置-保存"""
        self.Click(self.BUTTON_SAVE_JK)
