#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/4/12 9:53
# @Author   : yangshukun
# @File     : OtherFunc.py

import datetime
import os
import json
import gzip
import time
import zipfile
import string
import random
import sys
from utils.operationXml import *
import shutil

"""读取txt文件"""


def read_file(file_name):
    '''
    按行读取txt文档数据
    :param file_name:
    :return:
    '''
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))
    f_patch = base_path + "\\BaseAutoData\\{}".format(file_name)
    with open(f_patch, encoding='utf-8') as f:
        lines = f.readlines()
    return lines


"""格式化输出打印内容"""


def log(filed):
    '''
    格式化打印日志
    :param filed:
    :return:
    '''
    print('*************** %s ***************' % filed)


"""重写json格式化输出方法，解决时间value值无法格式化输出的问题"""


class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


"""字典转为带属性的对象调用"""


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_obj(dictobj):
    if not isinstance(dictobj, dict):
        return dictobj
    new_dict = Dict()
    for k, v in dictobj.items():
        new_dict[k] = dict_to_obj(v)
    return new_dict


'''解压zip包'''


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name.split('.zip')[0]):
        pass
    else:
        os.mkdir(file_name.split('.zip')[0])
    for names in zip_file.namelist():
        zip_file.extract(names, file_name.split('.zip')[0] + '/')
    zip_file.close()


def zip_dir(dir_path, zip_name):
    """压缩某个路径下的全部文件到一个zip包中,仅支持目录下没有文件夹的情况"""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as myzip:
        arr = os.listdir(dir_path)
        for i in arr:
            myzip.write(i)


def make_zip_dir_new(base_dir_path, base_remote_path, file_name):
    """压缩某个路径下的全部文件（含文件夹）"""
    log('开始进行安装包的压缩操作，检查目录路径是否正常')
    if os.path.exists(base_dir_path) and os.path.exists(base_remote_path) and base_dir_path != base_remote_path:
        base_remote_file_path = base_remote_path + '\{}'.format(file_name)
        log('压缩源目录和目标路径正常,且路径不相同，满足条件，开始进行压缩操作，压缩中，请稍后。。。')
        shutil.make_archive(base_remote_file_path, 'zip', base_dir_path)
        log('压缩成功，请查看压缩包：{}'.format(base_remote_file_path))
    else:
        log('路径检查失败，请确保原路径：【{}】存在，目标路径：【{}】存在，且路径不相同。。。'.format(base_dir_path, base_remote_path))


def get_letter(length, isupper=False):
    '''
    生成数字加字母的随机字符串
    :param length: 生成字符串长度
    :param isupper: 是否大写，默认小写
    :return:
    '''
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, int(length)))
    if isupper:
        return ran_str.upper()
    return ran_str.lower()


def make_test_data(xml_name, class_name, parent="item", key="code", value="value", name="name", xpath="xpath"):
    """解析xml数据文件，将数据按照类属性的格式输出"""
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    data_class_path = os.path.join(base_path, 'data_class')
    class_file_name = "test.txt"
    key_list = OperationXml().getXmlUser(xml_name, parent, key)
    key_new_list = list(map(lambda x: x.replace(".", "_"), key_list))
    value_list = OperationXml().getXmlUser(xml_name, parent, value)
    name_list = OperationXml().getXmlUser(xml_name, parent, name)
    xpath_list = OperationXml().getXmlUser(xml_name, parent, xpath)
    with open(os.path.join(data_class_path, class_file_name), mode="w", encoding="utf-8") as f:
        f.truncate()
        f.write('from Common.common_map import *\n')
        f.write("class %s(object):\n" % class_name)
        for i in range(0, len(key_list)):
            f.write('   {} = "{}"   #{}\n'.format(key_new_list[i], value_list[i], name_list[i]))
            f.write(
                '   {}_XPATH = "{}".__add__(XPATH)   #{}元素表达式\n'.format(key_new_list[i], xpath_list[i], name_list[i]))
        f.close()
    with open(os.path.join(data_class_path, class_file_name), mode="r", encoding="utf-8") as f:
        print(f.read())
        f.close()


def get_now_time_to_str():
    """获取当前时间戳，转化为字符串返回"""
    return str(time.time()).split(".")[1]


def splitStr(data_str, separator, number):
    """拆分字符串"""
    spl = data_str.split(separator)[number]
    return spl


if __name__ == '__main__':
    # make_test_data("MBTD290.xml", "MBTD290DATA", parent='item')
    make_zip_dir_new(r'D:\数仓安装记录\test\CK-1.7.11.0', r'D:\数仓安装记录\test', 'CK_TEST')
