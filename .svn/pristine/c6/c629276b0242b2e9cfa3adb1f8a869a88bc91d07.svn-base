#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/11/25 9:52
# @Author   : yangshukun
# @File     : OracleDataTool.py

from Common.OracleControl import *
from Config.BaseEnv import *
from Common.getconf import *


def clear_dm_data(oracle_connect_info):  # 方法慎用！！！！！！！！！！
    '''
    默认清理157DM数据，需要清理其它库，请修改Oracle_info与BaseEnv中的对应关系
    使用前，根据需要清除的报送品种DM表，在updateservice.ini中配置（当报送品种值为True时，代表需要清理，其它值表示不清理）
    :param oracle_info:
    :return:
    '''
    db = OracleControl(oracle_info=oracle_connect_info)
    conf = dict(Config('updateservice.ini').items('bspz'))
    bspz_list = []
    for key, value in conf.items():
        if eval(value) is True:
            bspz_list.append(key.upper())
    tabe_list = []
    for bspz in bspz_list:
        tables = db.get_data("select table_name from user_tables  where table_name like 'DM_{}%'".format(bspz))
        tabe_list = tabe_list + tables
    EXCEPT_LIST = EXCEPT_TABLE
    for tab in tabe_list:
        if tab[0] in EXCEPT_LIST:
            print(tab[0])
            continue
        else:
            count_data = db.get_data('select count(1) from {}'.format(tab[0]))
            db.delete_data('delete from {}'.format(tab[0]))
            db.commit()
            log('{}数据删除成功'.format(tab[0]) + '---清理总数据量:{}条'.format(count_data[0][0]))
    db.close()


def make_big_data(oracle_connect_info, total, filed_str, value_str, is_table_key_int=False):
    """
    向数据库插入大数据
    :param oracle_name: 需要链接的数据库名称（在D:\SC_AUTO_Test\Config\BaseEnv.py中进行配置对应的链接数据，如果有，则直接使用）
    :param total: 要插入的总数据量
    :param is_table_key_int:表的主键，如果是ID且为数字，则会自增，如果为加密32位字符串，则会自动生成32字符串
    :return:
    """
    # 初始化数据库链接对象
    ora_client = OracleControl(oracle_info=oracle_connect_info)
    sql_str = filed_str + value_str
    for i in range(0, total + 1):
        if is_table_key_int:
            sql_data = sql_str.format(150007 + i)
            print(sql_data)
        else:
            # table_key = get_letter(32)
            ID = 'User' + '_' + 'test' + str(i) + '$$0'
            code = 'User' + '_' + 'test' + str(i)
            # if table_key in table_key_list:
            #     continue
            sql_data = sql_str.replace('${ID}', ID).replace('${code}', code)
            # table_key_list.append(table_key)
        ora_client.insert_data(sql_data)
        log('当前正在插入{}行数据'.format(i))
    ora_client.commit()
    ora_client.close()
    log('数据插入完成')


oracle_connect_info = {'user': 'D2021V09DM', 'pswd': '123456', 'adress': '192.168.20.119', 'db_name': 'orcl'}

# 数据库大量插入数据
# 插入语句字段，需要自行编写并替换下面的file_str变量的值
filed_str = "insert into DM_EAST_701_WTDK (ID, REPORT_ID, JRJGMC, JRXKZH, JGDM, NBJGH, MXKMBH, MXKMMC, XDHTH, WTRMC, WTRJGDM, JKRMC, JKRJGDM, WTZJZHZH, WTJE, WTYE, BZ, LL, WTDKYT, WTDKLX, SXFJE, SXFZFFDM, SXFZFFMC, HTQSRQ, HTDQRQ, YWZT, CJRQ, CREATER, CREATE_TIME, UPDATER, UPDATE_TIME, IS_CHECKED, IS_VALIDATED, V_DEPT_ID, DATA_STATE, BIZ_ID, BATCH, DATA_SOURCE)"
# 插入的值,需要自行编写复制替换下面的value_str，并且需要将主键替换为:'{}'(注意单引号)，如果不是ID数值作为主键，需要将主键替换为--'${table_key}'(注意单引号)
value_str = "values ({}, 40156, '测试财务公司全称', '202020202020', '91510100MA61RTKK6Q', '123456', '0387', '贷款', 'ZX委托贷款217222', '222高敏', '91510100MA61RTKK6Q', '222高敏', '91510100MA61RTKK6Q', '', 7775566.00, 7775566.00, 'CNY', 5.600000, 'zx汽车555', '流动资金贷款', 9000.00, '西乡塘区ffgdm001', '手续费支付方名称', 20200901, 20220806, '正常', 20210630, 'llbb1', to_date('23-06-2022 15:56:16', 'dd-mm-yyyy hh24:mi:ss'), '', null, 0, 9, '', 0, null, '20212Q1M', 1)"
table_key_list = []
make_big_data(oracle_connect_info=oracle_connect_info, total=50001, filed_str=filed_str, value_str=value_str,
              is_table_key_int=True)

# 清理某个品种全部DM表数据（慎用）
# clear_dm_data(oracle_connect_info)
