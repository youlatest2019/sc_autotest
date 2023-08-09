#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/9 9:25
# @Author   : yangshukun
# @File     : keyword_rmbtd_hedui.py
from baseOperation.WebOperation import *
from data.data_class.mbtd290_data import *
from pageElement.page_bscl_common import *
from data.data_class.mbtd_data import *


class MbtdAddData(WebDriver, MBTD290DATA, MBTD210DATA, MBTD250DATA):

    def dm_mbtd_grjd_jcd(self):
        """征信-个人借贷账户信息记录，新增数据"""
        self.Click(self.ACCTTYPE_XPATH)
        self.Input(self.ACCTCODE, self.ACCTCODE_XPATH)
        self.Input(self.RPTDATE, self.RPTDATE_XPATH)
        self.Click(self.RPTDATECODE_XPATH)
        self.Input(self.NAME, self.NAME_XPATH)
        self.Click(self.IDTYPE_XPATH)
        self.Input(self.IDNUM, self.IDNUM_XPATH)
        self.Input(self.MNGMTORGCODE, self.MNGMTORGCODE_XPATH)

    def dm_mbtd_qyjb_jcd(self, BUSINESS_NAME):
        """征信-企业基本信息记录-基础段，新增数据"""
        self.Input(BUSINESS_NAME, self.BUSINESS_NAME_XPATH)
        self.Click(self.IDENTITY_TYPE_XPATH)
        self.Input(self.IDENTITY_NUMBER, self.IDENTITY_NUMBER_XPATH)
        self.Input(self.INFORMATION_SOURCE_CODE, self.INFORMATION_SOURCE_CODE_XPATH)
        self.Input(self.REPORT_DATE, self.REPORT_DATE_XPATH)
        self.Click(self.REPORT_TIME_CODE)
        self.Input(self.CUSTOMER_DATA_CODE, self.CUSTOMER_DATA_CODE_XPATH)
        self.Click(self.CUSTOMER_DATA_TYPE)
        self.Click(self.ORGANIZATION_TYPE)
        self.Click(self.STATUS)

    def dm_mbtd_qydbzh_jcd(self, DEBTOR_NAME):
        """征信-企业担保账户信息记录-基础段、基本信息段，新增数据"""
        self.Click(self.ACCOUNT_TYPE)
        self.Input(self.ACCOUNT_CODE, self.ACCOUNT_CODE_TYPE)
        self.Input(self.REPORT_DATE250, self.REPORT_DATE250_XPATH)
        self.Click(self.REPORT_TIME_CODE250)
        self.Input(DEBTOR_NAME, self.DEBTOR_NAME)
        self.Click(self.DEBTOR_TYPE)
        self.Input(self.DEBTOR_CODE, self.DEBTOR_CODE_XPATH)
        self.Input(self.ORGAN_CODE, self.ORGAN_CODE_XPATH)
        self.Click(self.DBYW_MAJOR)
        self.Click(self.DBYW_BREAK)
        self.Click(self.ORGAN_CODE_XPATH)
        self.Input(self.ACC_OPEN_DATE, self.ACC_OPEN_DATE_XPATH)
        self.Input(self.GUARANTEE_AMOUNT, self.GUARANTEE_AMOUNT_XPATH)
        self.Click(self.BZ)
        self.Click(self.ORGAN_CODE_XPATH)
        self.Input(self.DUEDATE, self.DUEDATE_XPATH)
        self.Click(self.FDB_METHOD)
        self.Click(self.OTHERS_HK_METHOD)
        self.Input(self.BOND_PERCENT, self.BOND_PERCENT_XPATH)
        self.Input(self.DBHT_TEXT_NUMBER, self.DBHT_TEXT_NUMBER_XPATH)
