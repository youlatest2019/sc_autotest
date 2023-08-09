#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/6/21 16:51
# @Author   : yangshukun
# @File     : AutoUpdateService.py
import os
import re

from Common.Sftp_Control import *
from Config.BaseEnv import *
from Common.getconf import *


class AutoUpdateService():
    def __init__(self, sftp_name, target_install_name):
        '''
        初始化方法
        :param sftp_name: 按照sftp_135格式传入对应的服务器配置信息，链接服务器
        :param target_install_name: 安装目录，如：/home/xxx，不需要传/home
        '''
        self.sftp = SftpController(sftp_name)
        self.target_instanll_name = target_install_name
        self.service_list = self.get_service_list()
        # self.unzip_all_file()
        print(f"本次更新的服务包括：", self.service_list)

    def update_app_comm_func(self):

        '''
        更新常用web,service的通用方法包括：rmm,reast,rfbs,rmbtd,rimas,dom,rsazj
        :param service_list: 需要更新的service，以列表形式传入
        :return:
        '''
        if self.service_list:
            for service in self.service_list:
                jar_match = service.upper()
                service_obj = eval(service.upper())
                app_name = jar_match.split('_')[0]
                app_type = jar_match.split('_')[1]
                if app_type == 'SERVICE':
                    try:
                        cfg_local_path = BasePath.base_local_path + service_obj.cfg_local_path
                        lib_local_path = BasePath.base_local_path + service_obj.lib_local_path
                        '''判断是dcab域还是dom域，取不同的配置路径'''
                        if app_name == 'DOM':
                            cfg_target_path = BasePath.base_dom_target_path.format(
                                self.target_instanll_name) + service_obj.cfg_target_path
                            lib_target_path = BasePath.base_dom_target_path.format(
                                self.target_instanll_name) + service_obj.lib_target_path
                        else:
                            cfg_target_path = BasePath.base_dcab_target_path.format(
                                self.target_instanll_name) + service_obj.cfg_target_path

                            lib_target_path = BasePath.base_dcab_target_path.format(
                                self.target_instanll_name) + service_obj.lib_target_path

                        '''更新传入的service对应的CFG文件'''
                        self.sftp.upload_main(cfg_local_path, cfg_target_path, replace=True)
                        '''更新对应service的jar包'''
                        list_jar = os.listdir(lib_local_path)
                        for name in list_jar:
                            if re.match(app_name, name):
                                jar_name = name
                                log(jar_name)
                                break
                        new_lib_local_path = lib_local_path + '\\{}'.format(jar_name)
                        '''先删除对应的jar包，再上传最新的jar包，避免jar包重复'''
                        self.sftp.delete_sftp_file(lib_target_path, jar_name)
                        self.sftp.upload_main(new_lib_local_path, lib_target_path, replace=False)
                    except Exception as e:
                        log(e)
                elif app_type == 'WEB':
                    try:
                        '''从配置文件中获取组装对应web的本地目录和远程目录'''
                        root_local_path = BasePath.base_local_path + service_obj.root_local_path
                        cfg_local_path = BasePath.base_local_path + service_obj.cfg_local_path
                        nstc_local_path = BasePath.base_local_path + service_obj.nstc_local_path
                        root_target_path = BasePath.base_web_target_root_path.format(
                            self.target_instanll_name) + service_obj.root_target_path
                        cfg_target_path = BasePath.base_web_target_cfg_path.format(
                            self.target_instanll_name) + service_obj.cfg_target_path
                        nstc_target_path = BasePath.base_web_target_com_path.format(
                            self.target_instanll_name) + service_obj.nstc_target_path
                        '''更新web应用的xxx-web-root目录文件'''
                        self.sftp.upload_main(root_local_path, root_target_path, replace=True)
                        '''更新web应用的xxx-web-cfg目录文件'''
                        self.sftp.upload_main(cfg_local_path, cfg_target_path, replace=True)
                        '''更新web应用的nstc目录对应的文件'''
                        self.sftp.upload_main(nstc_local_path, nstc_target_path, replace=True)
                    except Exception as e:
                        log(e)
                else:
                    log('要更新的应用格式不正确{}'.format(service))
        else:
            log("没有需要更新的service，请检查是否入参")

    def unzip_all_file(self):
        '''批量解压应用,根据需要选择,如果相同的文件夹已存在，会自动覆盖替换'''
        zip_list = os.listdir(BasePath.base_local_path)
        zip_list.remove('__init__.py')
        for file in zip_list:
            if file[-4:].lower() == '.zip':
                un_zip(os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ServiceHome'), file))
                log('{}解压完成'.format(file))

    def get_service_list(self):
        '''
        获取要更新的应用列表
        :return:
        '''
        conf = dict(Config('updateservice.ini').items('Service'))
        service_list = []
        for key, value in conf.items():
            if eval(value) is True:
                service_list.append(key)
        return service_list


if __name__ == '__main__':
    '''仅需将jekins打包下载的zip包放到指定的目录下并输入需要更新的应用如：xxx_service,xxx_web,即可实现自动解压并替换对应的目录和文件到服务器上'''
    # sftp_name替换为要更新的服务器比如sftp_name=sftp_119,target_install_name替换为服务器上对应的安装目录名称
    sf = AutoUpdateService(sftp_name=sftp_134, target_install_name='D2021V08QXAZ')
    sf.update_app_comm_func()
