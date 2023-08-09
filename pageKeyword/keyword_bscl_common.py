#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/7/22 15:48
# @Author   : yangshukun
# @File     : keyword_bscl_common.py

from pageElement.page_bscl_common import *
from baseOperation.WebOperation import *


class BsclMainKeyword(BsclMainMenueElement, BsclMainFrame, WebDriver, ZhbbMainMenueElement):

    def clickBsclMainMenue(self):
        """进入报送处理主菜单"""
        self.Click(self.BSCL_MENUE)

    def into1104HdPage(self):
        """进入1104核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("1104核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("1104核对"))
        self.SwitchFrame(self.RN1104_HD_MAIN_FRAME)

    def into1104SpPage(self):
        """进入1104审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("1104审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("1104审批"))
        self.SwitchFrame(self.RN1104_SP_MAIN_FRAME)

    def into1104SbPage(self):
        """进入1104上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("1104上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("1104上报"))
        self.SwitchFrame(self.RN1104_SB_MAIN_FRAME)

    def into1104CxPage(self):
        """进入1104报送查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("1104报送查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("1104报送查询"))
        self.SwitchFrame(self.RN1104_CX_MAIN_FRAME)

    def into1104XxhzbdbPage(self):
        """进入1104线下汇总表对比界面"""
        self.Click(self.BUTTON_DIFF_BSPZ_COMMON.format("1104", "线下汇总表对比"))
        self.SwitchFrame(self.RN1104_XXHZBDB_MAIN_FRAME)

    def into1104KqdbPage(self):
        """进入1104跨期对比界面"""
        self.Click(self.KQDB.format("1104"))
        self.Click(self.TAG_BSPZ_COMMON.format("跨期对比"))
        self.SwitchFrame(self.RN1104_KQDB_MAIN_FRAME)

    def intoRmbtdHdPage(self):
        """进入征信核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("征信核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("征信核对"))
        self.SwitchFrame(self.RMBTD_HD_MAIN_FRAME)

    def intoRmbtdSpPage(self):
        """进入征信审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("征信审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("征信审批"))
        self.SwitchFrame(self.RMBTD_SP_MAIN_FRAME)

    def intoRmbtdSbPage(self):
        """进入征信上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("征信上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("征信上报"))
        self.SwitchFrame(self.RMBTD_SB_MAIN_FRAME)

    def intoRmbtdCxPage(self):
        """进入征信报送查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("征信报送查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("征信报送查询"))
        self.SwitchFrame(self.RMBTD_CX_MAIN_FRAME)

    def intoRmbtdSjgzPage(self):
        """进入征信数据更正界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("征信数据更正"))
        self.Click(self.TAG_BSPZ_COMMON.format("征信数据更正"))
        self.SwitchFrame(self.RMBTD_SJGZ_MAIN_FRAME)

    def intoRsafeHdPage(self):
        """进入外管局核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局核对"))
        self.SwitchFrame(self.RSAFE_HD_MAIN_FRAME)

    def intoRsafeSpPage(self):
        """进入外管局审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局审批"))
        self.SwitchFrame(self.RSAFE_SP_MAIN_FRAME)

    def intoRsafeSbPage(self):
        """进入外管局上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局上报"))
        self.SwitchFrame(self.RSAFE_SB_MAIN_FRAME)

    def intoRsafeCxPage(self):
        """进入外管局报送查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局报送查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局报送查询"))
        self.SwitchFrame(self.RSAFE_CX_MAIN_FRAME)

    def intoRpbccHdPage(self):
        """进入人行报表核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("人行报表核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("人行报表核对"))
        self.SwitchFrame(self.RPBCC_HD_MAIN_FRAME)

    def intoRpbccSpPage(self):
        """进入人行报表审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("人行报表审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("人行报表审批"))
        self.SwitchFrame(self.RPBCC_SP_MAIN_FRAME)

    def intoRpbccSbPage(self):
        """进入人行报表上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("人行报表上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("人行报表上报"))
        self.SwitchFrame(self.RPBCC_SB_MAIN_FRAME)

    def intoRpbccCxPage(self):
        """进入人行报表查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("人行报表查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("人行报表查询"))
        self.SwitchFrame(self.RPBCC_CX_MAIN_FRAME)

    def intoPbccXxhzbdbPage(self):
        """进入人行报表线下汇总表对比界面"""
        self.Click(self.BUTTON_DIFF_BSPZ_COMMON.format("人行大集中", "线下汇总表对比"))
        self.SwitchFrame(self.RPBCC_XXHZBDB_MAIN_FRAME)

    def intopbccKqdbPage(self):
        """进入人行报表跨期对比界面"""
        self.Click(self.KQDB.format("人行大集中"))
        self.Click(self.TAG_BSPZ_COMMON.format("跨期对比"))
        self.SwitchFrame(self.RPBCC_KQDB_MAIN_FRAME)

    def intoRsaferHdPage(self):
        """进入外管局报表核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局报表核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局报表核对"))
        self.SwitchFrame(self.RSAFER_HD_MAIN_FRAME)

    def intoRsaferSpPage(self):
        """进入外管局报表审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局报表审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局报表审批"))
        self.SwitchFrame(self.RSAFER_SP_MAIN_FRAME)

    def intoRsaferSbPage(self):
        """进入外管局报表上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局报表上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局报表上报"))
        self.SwitchFrame(self.RSAFER_SB_MAIN_FRAME)

    def intoRsaferCxPage(self):
        """进入外管局报表报送查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("外管局报表报送查"))
        self.Click(self.TAG_BSPZ_COMMON.format("外管局报表报送查询"))
        self.SwitchFrame(self.RSAFER_CX_MAIN_FRAME)

    def intoRfbsHdPage(self):
        """进入金融基础数据核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("金融基础数据核对"))
        self.Click(self.TAG_BSPZ_RFBS.format("金融基础数据核对"))
        self.SwitchFrame(self.RFBS_HD_MAIN_FRAME)

    def intoRfbsSpPage(self):
        """进入金融基础数据审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("金融基础数据审批"))
        self.Click(self.TAG_BSPZ_RFBS.format("金融基础数据审批"))
        self.SwitchFrame(self.RFBS_SP_MAIN_FRAME)

    def intoRfbsSbPage(self):
        """进入金融基础数据上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("金融基础数据上报"))
        self.Click(self.TAG_BSPZ_RFBS.format("金融基础数据上报"))
        self.SwitchFrame(self.RFBS_SB_MAIN_FRAME)

    def intoRfbsCxPage(self):
        """进入金融基础数据查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("金融基础数据查询"))
        self.Click(self.TAG_BSPZ_RFBS.format("金融基础数据查询"))
        self.SwitchFrame(self.RFBS_CX_MAIN_FRAME)

    def intoRfbsKqdbPage(self):
        """进入金数跨期对比界面"""
        self.Click(self.KQDB.format("金融基础数据采集"))
        self.Click(self.TAG_BSPZ_COMMON.format("跨期对比"))
        self.SwitchFrame(self.RFBS_KQDB_MAIN_FRAME)

    def intoReastHdPage(self):
        """进入EAST核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("EAST核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("EAST核对"))
        self.SwitchFrame(self.REAST_HD_MAIN_FRAME)

    def intoReastSpPage(self):
        """进入EAST审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("EAST审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("EAST审批"))
        self.SwitchFrame(self.REAST_SP_MAIN_FRAME)

    def intoReastSbPage(self):
        """进入EAST上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("EAST上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("EAST上报"))
        self.SwitchFrame(self.REAST_SB_MAIN_FRAME)

    def intoReastCxPage(self):
        """进入EAST查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("EAST查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("EAST查询"))
        self.SwitchFrame(self.REAST_CX_MAIN_FRAME)

    def intoRimasHdPage(self):
        """进入利率报备核对界面"""
        self.Click(self.BUTTON_BSPZ_RIMAS.format("利率报备核对"))
        self.Click(self.TAG_BSPZ_RIMAS.format("利率报备核对"))
        self.SwitchFrame(self.RIMAS_HD_MAIN_FRAME)

    def intoRimasSpPage(self):
        """进入利率报备审批界面"""
        self.Click(self.BUTTON_BSPZ_RIMAS.format("利率报备审批"))
        self.Click(self.TAG_BSPZ_RIMAS.format("利率报备审批"))
        self.SwitchFrame(self.RIMAS_SP_MAIN_FRAME)

    def intoRimasSbPage(self):
        """进入利率报备上报界面"""
        self.Click(self.BUTTON_BSPZ_RIMAS.format("利率报备上报"))
        self.Click(self.TAG_BSPZ_RIMAS.format("利率报备上报"))
        self.SwitchFrame(self.RIMAS_SB_MAIN_FRAME)

    def intoRimasCxPage(self):
        """进入利率报备查询界面"""
        self.Click(self.BUTTON_BSPZ_RIMAS.format("利率报备查询"))
        self.Click(self.TAG_BSPZ_RIMAS.format("利率报备查询"))
        self.SwitchFrame(self.RIMAS_CX_MAIN_FRAME)

    def intoRsazjHdPage(self):
        """进入浙江国资委核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("浙江国资委核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("浙江国资委核对"))
        self.SwitchFrame(self.RSAZJ_HD_MAIN_FRAME)

    def intoRsazjSpPage(self):
        """进入浙江国资委审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("浙江国资委审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("浙江国资委审批"))
        self.SwitchFrame(self.RSAZJ_SP_MAIN_FRAME)

    def intoRsazjSbPage(self):
        """进入浙江国资委上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("浙江国资委上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("浙江国资委上报"))
        self.SwitchFrame(self.RSAZJ_SB_MAIN_FRAME)

    def intoRsazjCxPage(self):
        """进入浙江国资委查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("浙江国资委查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("浙江国资委查询"))
        self.SwitchFrame(self.RSAZJ_CX_MAIN_FRAME)

    def intoRptcHdPage(self):
        """进入综合报表核对界面"""
        self.MouseFouce(self.ZHBB_MENUE)
        self.Click(self.BBHD_TAB)
        self.Click(self.BBHD_TAG)
        self.SwitchFrame(self.RPTC_HD_MAIN_FRAME)

    def intoRptcSpPage(self):
        """进入综合报表审批界面"""
        self.MouseFouce(self.ZHBB_MENUE)
        self.Click(self.BBSP_TAB)
        self.Click(self.BBSP_TAG)
        self.SwitchFrame(self.RPTC_SP_MAIN_FRAME)

    def intoRptcSbPage(self):
        """进入综合报表上报界面"""
        self.MouseFouce(self.ZHBB_MENUE)
        self.Click(self.BBSB_TAB)
        self.Click(self.BBSB_TAG)
        self.SwitchFrame(self.RPTC_SB_MAIN_FRAME)

    def intoRptcCxPage(self):
        """进入综合报表查询界面"""
        self.MouseFouce(self.ZHBB_MENUE)
        self.Click(self.BBCX_TAB)
        self.Click(self.BBCX_TAG)
        self.SwitchFrame(self.RPTC_CX_MAIN_FRAME)

    def intoRptcXxhzbdbPage(self):
        """进入综合报表线下汇总报对比界面"""
        self.MouseFouce(self.ZHBB_MENUE)
        self.Click(self.XXHZBDB_TAB)
        self.Click(self.XXHZBDB_TAG)
        self.SwitchFrame(self.RPTC_XXHZBDB_MAIN_FRAME)

    def intoRlctsHdPage(self):
        """进入大额监控核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("大额监控核对"))
        self.Click(self.TAG_BSPZ_COMMON.format("大额监控核对"))
        self.SwitchFrame(self.RLCTS_HD_MAIN_FRAME)

    def intoRlctsSpPage(self):
        """进入大额监控审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("大额监控审批"))
        self.Click(self.TAG_BSPZ_COMMON.format("大额监控审批"))
        self.SwitchFrame(self.RLCTS_SP_MAIN_FRAME)

    def intoRlctsSbPage(self):
        """进入大额监控上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("大额监控上报"))
        self.Click(self.TAG_BSPZ_COMMON.format("大额监控上报"))
        self.SwitchFrame(self.RLCTS_SB_MAIN_FRAME)

    def intoRlctsCxPage(self):
        """进入大额监控查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("大额监控查询"))
        self.Click(self.TAG_BSPZ_COMMON.format("大额监控查询"))
        self.SwitchFrame(self.RLCTS_CX_MAIN_FRAME)

    def intoRamlltHdPage(self):
        """进入反洗钱大额核对界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("反洗钱大额核对"))
        self.Click(self.TAG_BSPZ_RAMLLT_HD.format("反洗钱大额核对"))
        self.SwitchFrame(self.RAMLLT_HD_MAIN_FRAME)

    def intoRamlltSpPage(self):
        """进入反洗钱大额审批界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("反洗钱大额审批"))
        self.Click(self.TAG_BSPZ_RAMLLT_SP.format("反洗钱大额审批"))
        self.SwitchFrame(self.RAMLLT_SP_MAIN_FRAME)

    def intoRamlltSbPage(self):
        """进入反洗钱大额上报界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("反洗钱大额上报"))
        self.Click(self.TAG_BSPZ_RAMLLT_SB.format("反洗钱大额上报"))
        self.SwitchFrame(self.RAMLLT_SB_MAIN_FRAME)

    def intoRamlltCxPage(self):
        """进入反洗钱大额查询界面"""
        self.Click(self.BUTTON_BSPZ_COMMON.format("反洗钱大额查询"))
        self.Click(self.TAG_BSPZ_RAMLLT_CX.format("反洗钱大额查询"))
        self.SwitchFrame(self.RAMLLT_CX_MAIN_FRAME)
