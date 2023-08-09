#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/9/13 9:37
# @Author   : yangshukun
# @File     : getconf.py

import os
from configparser import ConfigParser
from Common.getfiledir import CONFDIR
import json


class Config(ConfigParser):

    def __init__(self, conf_name='config.ini'):
        self.conf_name = os.path.join(CONFDIR, conf_name)
        super().__init__()
        super().read(self.conf_name, encoding='utf-8')

    def save_data(self, section, option, value):
        super().set(section=section, option=option, value=value)
        super().write(fp=open(self.conf_name, 'w'))


def get_json_file(file):
    with open(file, encoding='utf-8') as f:
        data_json = json.load(f)
    return data_json

if __name__ == '__main__':
    # a = dict(Config('updateservice.ini').items('Service'))
    # print(a)
    file = r'D:\SC_AUTO_Test\TestData\InputDataDir\BSGL.JSON'
    s = get_json_file(file)
    print(s['RIMAS'])
