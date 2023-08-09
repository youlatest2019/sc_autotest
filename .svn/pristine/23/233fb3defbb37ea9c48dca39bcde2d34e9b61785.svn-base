#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/8/29 15:49
# @Author   : yangshukun
# @File     : keyword_oracle_common.py

from Common.OracleControl import *
from Common.getconf import *


class ReportTaksControl():

    def __init__(self):
        conf = Config()
        db_user_dm = conf.get("DATA_BASE", "db_user_dm")
        db_user_dw = conf.get("DATA_BASE", "db_user_dw")
        db_user_web = conf.get("DATA_BASE", "db_user_web")
        db_paswd = conf.get("DATA_BASE", "db_paswd")
        db_adress = conf.get("DATA_BASE", "db_adress")
        db_name = conf.get("DATA_BASE", "db_name")
        self.db_dm_dict = {"user": db_user_dm, "pswd": db_paswd, "adress": db_adress, "db_name": db_name}
        self.db_dw_dict = {"user": db_user_dw, "pswd": db_paswd, "adress": db_adress, "db_name": db_name}
        self.db_web_dict = {"user": db_user_web, "pswd": db_paswd, "adress": db_adress, "db_name": db_name}

    def count_report_task_for_hedui(self, bspzbh):
        """统计报送品种核对页面的数据总数"""

        ora = OracleControl(self.db_dm_dict)
        sql = "select count(1)\
                from dcab_report_state\
                where bsnrbh in (select bsnrbh from dcab_bs_bsnr where bspzbh = '{}')\
                and report_state = 0\
                and locked = 0\
                and report_task_flag = 1\
                and batch is not null".format(bspzbh)
        res = ora.get_data(sql)
        ora.close()
        return res


if __name__ == '__main__':
    ReportTaksControl().count_report_task_for_hedui("MBTD")
