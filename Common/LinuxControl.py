#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/6/8 20:40
# @Author   : yangshukun
# @File     : LinuxControl.py

import paramiko
from Config import BaseEnv
from Common.OtherFunc import *


class LinuxControl():

    def __init__(self):
        pass

    def operate_server(self, command_list):
        '''
        根据环境参数链接对应的服务器
        :param env_name: 环境名称
        :return:
        '''
        trans = paramiko.Transport((BaseEnv.server_157['url'], BaseEnv.common_ssh_port))
        trans.connect(username='root', password='Ninestar1552')
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        result_list = []
        for cmd in command_list:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result_list.append(stdout.read().decode('utf-8'))
        return result_list


if __name__ == '__main__':
    cl = LinuxControl()
    command_list = read_file('test_01')
    re = cl.operate_server(command_list)
    print(re)
