#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/7/8 9:26
# @Author   : yangshukun
# @File     : test.py
import xlrd
import requests
import csv
from bs4 import BeautifulSoup
import xlwt

# def demo():
data = xlrd.open_workbook(r'D:\SC_AUTO_Test\Tools\热门楼盘.xls')  # 读2.xls
table = data.sheets()[0]  # 打开第一个工作表，索引
row_n = table.nrows  # 获取全部行数
headers = {
        'Cookie': '__customer_trace_id=9084AA31-5EB6-46E6-AFA4-74C53D644D6B'
    }

for i in range(1, row_n):
        # print(type(table.row_values(i)))
        a = table.row_values(i)
        url = a[3]
        ret = requests.get(url, headers=headers)

        soup = BeautifulSoup(ret.content, 'html.parser')

        all_products = []

        products = soup.select('div.baseInfo box')
        for product in products:

            url_info = soup.select('div.imgText > div:nth-child(7) > a')[0].attrs['href']  # url详情页

            all_products.append({
                "跳转": url_info
                })

        print(all_products)

        keys = all_products[0].keys()

        with open('楼盘详情跳转.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_products)

