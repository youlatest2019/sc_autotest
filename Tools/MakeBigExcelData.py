#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/11/12 9:41
# @Author   : yangshukun
# @File     : MakeBigExcelData.py
import time

from Common.ExcelControl import *
import gc
import csv


def make_big_data_to_excel(base_data, big_data, num):
    '''
    通过excel造大数据的脚本
    :param base_data: 数据模板来源的excel，可以通过下载报文获得，这个参数是来源文件的路径
    :param big_data: 目标大数据excel的存储路径，如果没有该文件会自动创建
    :param num: 数据量
    :return:
    '''
    '''数据模板来源，至少保证来源的excel中存在一条数据'''
    start_tme = time.time()
    excel_instance = ExcelOperation(base_data)
    base_data_dict = excel_instance.excel_to_dict(0)

    wb = openpyxl.Workbook()
    ws = wb.active
    header_list = list(base_data_dict[0].keys())
    for row in range(1, num + 2):
        dict_data = random.choice(base_data_dict)
        value_list = list(dict_data.values())
        if row == 1:
            for col in range(1, len(base_data_dict[0]) + 1):
                ws.cell(row, col, header_list[col - 1])
        else:
            for col in range(2, len(base_data_dict[0]) + 1):
                ws.cell(row, col, value_list[col - 1])
        print('当前插入行数为：{}行'.format(row))
    wb.save(big_data)
    end_time = time.time()
    print("消耗时间:", end_time - start_tme)
    wb.close()
    gc.collect()



def get_csv_data(file_path):
    """获取csv文件数据"""
    f = open(file_path, mode='r', encoding='gbk')
    reader = csv.reader(f)
    data_list = []
    for row in reader:
        data_list.append(row)
    f.close()
    gc.collect()
    return data_list


def make_big_csv(base_csv_path, big_csv_path, num):
    """
    csv文件生成大数据方法
    :param base_csv_path: 下载一个原始文件，至少包含一条数据，目的是
    :param big_csv_path:
    :param num:
    :return:
    """
    data_list = get_csv_data(base_csv_path)
    table_head = data_list[0]
    f = open(big_csv_path, mode='w', encoding='gbk', newline='')
    writer = csv.writer(f)
    start_time = time.time()
    for i in range(1, num + 2):
        if i == 1:
            writer.writerow(table_head)
            del (data_list[0])
            print("表头写入成功")
        else:
            row_data = random.choice(data_list)
            row_data[0] = ''
            writer.writerow(row_data)
            print("写入第{}行数据成功".format(i))

    f.close()
    end_time = time.time()
    print("消耗时间：", end_time - start_time)
    gc.collect()


make_big_data_to_excel(base_data=r'E:\7月测试\非同业单位存款发生额信息.xlsx',
                       big_data=r'E:\7月测试\非同业单位存款发生额信息(10w).xlsx',
                       num=100000)
# make_big_csv(base_csv_path=r'C:\Users\DELL\Desktop\性能测试相关\csv数据\存量单位贷款信息.csv',
#              big_csv_path=r'C:\Users\DELL\Desktop\性能测试相关\csv数据\存量单位贷款信息(130W).csv',
#              num=1300000)
