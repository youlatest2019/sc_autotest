#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/5/10 10:14
# @Author   : yangshukun
# @File     : Auto_Install_oracle.py
import sys
import time
import datetime
from Common.OracleControl import *
from Config.BaseEnv import *
from Common.SSH_Control import *
from Common.Sftp_Control import *
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Common.getconf import *


class Atuo_Install():
    def __init__(self):
        database_conf = dict(Config('upgrade_install.ini').items('DataBase'))
        dir_conf = dict(Config('upgrade_install.ini').items('Dir'))
        self.adress = database_conf['adress']
        self.driver_path = database_conf['chrome_driver_path']
        self.ssh_passwd = database_conf['ssh_passwd']
        self.web_user = database_conf['web_user']
        self.dw_user = database_conf['dw_user']
        self.dm_user = database_conf['dm_user']
        self.base_dir = dir_conf['base_dir']
        self.local_package_path = dir_conf['local_package_path']
        self.ssh_info = {'url': self.adress, 'port': 22, 'username': 'root', 'password': self.ssh_passwd}
        self.dom_domain_port = dir_conf['dom_domain_port']
        self.dcab_domain_port = dir_conf['dcab_domain_port']
        self.web_domain_port = dir_conf['web_domain_port']
        self.yw_name = dir_conf['yw_name']
        self.yw_user = dir_conf['yw_user']
        self.yw_passwd = dir_conf['yw_passwd']
        self.yw_ip = dir_conf['yw_ip']
        self.yw_prot = dir_conf['yw_prot']
        self.yw_dbname = dir_conf['yw_dbname']
        self.standalone_ip = dir_conf['standalone_ip']
        self.standalone_port = dir_conf['standalone_port']
        self.fail_dict = {}
        self.is_old_env = dir_conf['is_old']
        self.is_upload = dir_conf['is_upload']
        self.upgrade_package_path = dir_conf['upgrade_package_path']
        self.upgrade_dir = 'upgrade_package' + str(time.strftime('%m%d%H%M', time.localtime(time.time())))

    def create_dir_and_upload_files_and_unzip_file(self):
        """
        创建目录，创建域，上传安装包，解压
        :return:
        """
        if self.is_upload != "NO":
            user_command = input('【根据配置信息，直接使用服务器上已有的安装包，请确认是否配置正确（Y/N）】：')
            if user_command == 'Y':
                log('-----已确认配置正确，不需要上传安装包，直接开始进入下一步-----')

            else:
                log('-----配置错误，退出安装程序，重新进行配置-----')
                sys.exit()
        else:
            user_command = input('【根据配置信息，使用本地安装包，请确认是否开始上传（Y/N）】：')
            if user_command == 'Y':
                log('-----已确认配置正确，开始上传安装包步骤-----')
                # 创建目录
                ssh = SSH_Control(self.ssh_info)
                sftp = SftpController(self.ssh_info)
                log('-----开始创建安装目录-----')
                ssh.ssh_exec_cmd('mkdir {base_dir}/{upgrade_dir}'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir))
                log('-----安装目录创建完成-----')
                package_name_list = os.listdir(r'{local_package_path}'.format(local_package_path=self.local_package_path))
                self.base_package_dict = {}
                self.pz_package_list = []
                for package_name in package_name_list:
                    if package_name.endswith('.zip'):
                        dir_name = package_name.split('.zip')[0]
                        if dir_name.startswith('JC-') or dir_name.startswith('PT-') or dir_name.startswith('CK'):
                            key = dir_name.split('-')[0]
                            self.base_package_dict[key] = dir_name
                        else:
                            self.pz_package_list.append(dir_name)

                        # 创建与安装包同名的目录
                        ssh.ssh_exec_cmd(
                            'mkdir {base_dir}/{upgrade_dir}/{dir_name}'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir, dir_name=dir_name))
                        log('-----创建安装包目录{}成功-----'.format(dir_name))
                        # 上传安装包到对应的目录
                        sftp.put_file(r'{local_package_path}\{package_name}'.format(local_package_path=self.local_package_path,
                                                                                    package_name=package_name),
                                      '{base_dir}/{upgrade_dir}/{dir_name}/{package_name}'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir,
                                                                                                  dir_name=dir_name,
                                                                                                  package_name=package_name))
                        log('-----上传安装包{}成功-----'.format(package_name))
                        # 解压对应目录下的安装包
                        log('-----开始解压：安装包{}-----'.format(package_name))
                        ssh.ssh_exec_cmd(
                            'cd {base_dir}/{upgrade_dir}/{dir_name} && unzip {package_name}'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir,
                                                                                                    dir_name=dir_name,
                                                                                                    package_name=package_name))
                        log('-----解压完成：安装包{}-----'.format(package_name))
                        # # 如果是平台安装包，解压后需要进入目录下删除掉(安装包已不存在改文件目录)
                        # if dir_name.startswith('PT-'):
                        #     log('-----进入平台安装包目录中，删除portal目录-----')
                        #     time.sleep(2)
                        #     ssh.ssh_exec_cmd('cd {base_dir}/{upgrade_dir}/{dir_name}/bs/BASE && rm -rf portal/')
                        #     log('-----删除portal目录完成-----')
                    else:
                        continue
                # 文件夹授权
                ssh.ssh_exec_cmd('cd /home && chmod -R 777 {base_dir}'.format(base_dir=self.base_dir))
                log('-----对文件主目录及子级文件授权成功-----')
                ssh.ssh_close()
            else:
                log('-----配置错误，退出安装程序，重新配置-----')
                sys.exit()

    def start_install(self, module_name):
        self.kill_process_with_port(8080)
        time.sleep(2)
        try:
            ssh = SSH_Control(self.ssh_info)
            url = 'http://{adress}:8080'.format(adress=self.adress)
            if self.is_upload == 'YES':
                ssh.ssh_exec_cmd_without_wait(
                    'cd {upgrade_package_path}/{dir_name} && ./start.sh'.format(upgrade_package_path=self.upgrade_package_path,
                                                                                dir_name=module_name))
            else:
                ssh.ssh_exec_cmd_without_wait(
                    'cd {base_dir}/{upgrade_dir}/{dir_name} && ./start.sh'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir,
                                                                                  dir_name=module_name))
            time.sleep(5)
            log('【开始执行安装】:{}'.format(module_name))
            t = 0
            while t < 20:
                try:
                    driver = webdriver.Chrome(
                        executable_path=os.path.join(r'{driver_path}'.format(driver_path=self.driver_path),
                                                     'chromedriver.exe'))
                    driver.get(url)
                    log('-----登录{}安装平台成功，登录地址{}-----'.format(module_name, url))
                    break
                except Exception:
                    log('-----第{}次，尝试登录{}安装平台失败，等待3秒，尝试重新登录-----'.format(t, module_name))
                    driver.close()
                time.sleep(3)
                t += 1
            driver.maximize_window()
            time.sleep(2)
            """
            基础信息填写
            """
            WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//table[@id="web-install-path"]//tr[1]/td[3]')))
            # 输入web-应用安装路径
            driver.find_element(By.XPATH, '//table[@id="web-install-path"]//tr[1]/td[3]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@id="path"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@id="path"]').clear()
            time.sleep(0.5)
            web_path = '{base_dir}/DCAB/WEB'.format(base_dir=self.base_dir)
            if self.is_old_env == 'YES':
                web_path = '{base_dir}/dcab/WEB/bs'.format(base_dir=self.base_dir)
            driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                web_path)
            time.sleep(0.5)
            # 手动输入路径需要点击两次确定
            driver.find_element(By.XPATH, '//input[@value="确认"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//input[@value="确认"]').click()
            time.sleep(1)

            # 如果是JC模块，说明没有安装过，因此，要填写全部信息
            if module_name.startswith('JC-'):
                # 输入数仓平台数据源（WEB）
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceUserName"]').send_keys(
                    '{web_user}'.format(web_user=self.web_user))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourcePassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourcePassWord"]').send_keys('123456')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceIp"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceIp"]').send_keys(
                    '{adress}'.format(adress=self.adress))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourcePort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourcePort"]').send_keys('1521')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceDbName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabwebDataSourceDbName"]').send_keys('orcl')
                # 测试连接
                driver.find_element(By.XPATH, '//input[@id="connectDataSource"]').click()
                time.sleep(2)
                WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[3]/div/button')))
                ele = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/button')
                driver.execute_script("arguments[0].click();", ele)
                time.sleep(1)
                # 输入DCab-Service-应用安装路径
                driver.find_element(By.XPATH, '//tr[@class="dcabInstallPath"]/td[3]/input').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                    '{base_dir}/DCAB/DCab-Service'.format(base_dir=self.base_dir))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(1)
                # 输入Dom-Service-应用安装路径
                driver.find_element(By.XPATH, '//tr[@class="domInstallPath"]/td[3]/input').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                    '{base_dir}/DCAB/DOM-Service'.format(base_dir=self.base_dir))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                # 输入数舱仓库数据源（DW）
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceUserName"]').send_keys(
                    '{dw_user}'.format(dw_user=self.dw_user))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourcePassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourcePassWord"]').send_keys('123456')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceIp"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceIp"]').send_keys(
                    '{adress}'.format(adress=self.adress))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourcePort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourcePort"]').send_keys('1521')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceDbName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdwDataSourceDbName"]').send_keys('orcl')
                time.sleep(0.5)
                # 输入数舱仓库数据源（DM）
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceUserName"]').send_keys(
                    '{dm_user}'.format(dm_user=self.dm_user))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourcePassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourcePassWord"]').send_keys('123456')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceIp"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceIp"]').send_keys(
                    '{adress}'.format(adress=self.adress))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourcePort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourcePort"]').send_keys('1521')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceDbName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabdmDataSourceDbName"]').send_keys('orcl')
                time.sleep(0.5)

                """
                WEBLOGIC域信息填写
                """
                # 切换到域信息填写界面
                driver.find_element(By.XPATH, '//div[@class="page-tool-bar"]/ul/li[2]').click()
                time.sleep(1)
                # 填写web-域信息
                driver.find_element(By.XPATH, '//table[@id="web-web-logic"]//tr[1]/td[3]/input').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                    '{base_dir}/domains/web-domain'.format(base_dir=self.base_dir))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="webWebLogicPort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="webWebLogicPort"]').send_keys(self.web_domain_port)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="webWebLogicUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="webWebLogicUserName"]').send_keys('weblogic')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="webWebLogicPassWord"]').clear()
                driver.find_element(By.XPATH, '//input[@id="webWebLogicPassWord"]').send_keys('12345678')
                time.sleep(1)
                # 填写DCab-Service-域信息
                driver.find_element(By.XPATH, '//table[@id="dcab-web-logic"]//tr[1]/td[3]/input').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                    '{base_dir}/domains/dcab-domain'.format(base_dir=self.base_dir))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicPort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicPort"]').send_keys(self.dcab_domain_port)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicUserName"]').send_keys('weblogic')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicPassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="dcabWebLogicPassWord"]').send_keys('12345678')
                time.sleep(1)
                # 填写DCab-Service-域信息
                driver.find_element(By.XPATH, '//table[@id="dom-web-logic"]//tr[1]/td[3]/input').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.CONTROL, "a")
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(Keys.DELETE)
                time.sleep(1)
                driver.find_element(By.XPATH, '//input[@id="path"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="path"]').send_keys(
                    '{base_dir}/domains/dom-domain'.format(base_dir=self.base_dir))
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@value="确认"]').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicPort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicPort"]').send_keys(self.dom_domain_port)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicUserName"]').send_keys('weblogic')
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicPassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="domWebLogicPassWord"]').send_keys('12345678')
                time.sleep(0.5)

                """
                业务系统信息填写（不在代码中写死，可以通过配置指定对应的服务器，但默认值为135数据库，可以不做修改）
                """
                driver.find_element(By.XPATH, '//input[@id="ywNameText"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywNameText"]').send_keys(self.yw_name)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceUserName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceUserName"]').send_keys(self.yw_user)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourcePassWord"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourcePassWord"]').send_keys(self.yw_passwd)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceIp"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceIp"]').send_keys(self.yw_ip)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourcePort"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourcePort"]').send_keys(self.yw_prot)
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceDbName"]').clear()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//input[@id="ywDataSourceDbName"]').send_keys(self.yw_dbname)
                time.sleep(2)

                # 点击依赖检查
                driver.find_element(By.XPATH, '//input[@id="dependencyCheck"]').click()
                time.sleep(1)

            # 无果不是JC模块，则说明基础模块肯定已安装过，则不需要再填写全部信息，输入web信息，就会把所有已保存的信息带出来，则可以直接点击依赖校验
            else:
                """
                安装平台模块时，需要填写独立服务信息，根据传入的参数进行判断，如果时平台模块，才进入此步骤
                """
                if module_name.startswith('PT-'):
                    driver.find_element(By.XPATH, '//div[@class="page-tool-bar"]/ul/li[2]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//div[@class="page-tool-bar"]/ul/li[2]').click()
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '//table[@id="standalone-apps"]//tr[2]/td[2]/div/input[@class="ip"]').send_keys(
                        Keys.CONTROL, 'a')
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '//table[@id="standalone-apps"]//tr[2]/td[2]/div/input[@class="ip"]').send_keys(
                        Keys.DELETE)
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '//table[@id="standalone-apps"]//tr[2]/td[2]/div/input[@class="ip"]').send_keys(
                        self.standalone_ip)
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '//table[@id="standalone-apps"]//tr[2]/td[2]/div/input[@class="port"]').clear()
                    time.sleep(0.5)
                    driver.find_element(By.XPATH,
                                        '//table[@id="standalone-apps"]//tr[2]/td[2]/div/input[@class="port"]').send_keys(
                        self.standalone_port)
                    time.sleep(0.5)

                # 点击依赖检查
                driver.find_element(By.XPATH, '//input[@id="dependencyCheck"]').click()
                time.sleep(1)

            """
            进入版本依赖检查界面，点击开始安装
            """
            WebDriverWait(driver=driver, timeout=60, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@class="install"]')))
            time.sleep(0.5)
            # 点击开始安装
            driver.find_element(By.XPATH, '//input[@class="install"]').click()
            time.sleep(0.5)
            # 勾选更新日志确认阅读
            WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="read"]')))
            driver.find_element(By.XPATH, '//input[@id="read"]').click()
            time.sleep(0.5)
            # 点击下一步
            WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="next"]')))
            driver.find_element(By.XPATH, '//input[@id="next"]').click()
            time.sleep(0.5)
            # 安装内容选择，不做任何选择，使用默认全选，直接下一步
            WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@id="next"]')))
            driver.find_element(By.XPATH, '//input[@id="next"]').click()
            time.sleep(0.5)
            # 等待安装完成，每5秒查询一次安装结果
            WebDriverWait(driver=driver, timeout=30, poll_frequency=0.5).until(
                EC.element_to_be_clickable((By.XPATH, '//progress[@id="fetching_installation_progress"]')))
            while True:
                progress = driver.find_element(By.XPATH,
                                               '//progress[@id="fetching_installation_progress"]').get_attribute(
                    'value')
                log('当前正在执行安装模块：{}，sql执行进度为:{}%'.format(module_name, progress))
                time.sleep(3)
                if progress == '100':
                    time.sleep(1)
                    driver.close()
                    log('-----【模块：{}安装成功】-----'.format(module_name))
                    ssh.ssh_exec_cmd(
                        'cd {base_dir}/{upgrade_dir}/{dir_name} && ./stop.sh'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir,
                                                                                     dir_name=module_name))
                    time.sleep(5)
                    break
                else:
                    try:
                        status = driver.find_element(By.XPATH, '//div[@id="errorImage"]/p').text
                        if status == '安装失败':
                            d = time.strftime('%Y年%m月%d日_%H点%M分', time.localtime())
                            pic_name = module_name + '_' + str(d) + '.png'
                            screent_path = os.path.join(
                                os.path.join(os.path.dirname(__file__), 'install_fail_screenshosts'), pic_name)
                            driver.get_screenshot_as_file(screent_path)
                            time.sleep(1)
                            self.fail_dict[module_name] = '安装失败，截图路径：{}'.format(screent_path)
                            if module_name.split('-')[0] in ('JC', 'PT', 'CK'):
                                log('必要模块{}安装失败，安装结束，请检查并重新更新安装包'.format(module_name))
                                sys.exit()
                            else:
                                ssh.ssh_exec_cmd('cd {base_dir}/{upgrade_dir}/{dir_name} && ./stop.sh'.format(
                                    base_dir=self.base_dir, upgrade_dir=self.upgrade_dir, dir_name=module_name))
                                log('报送应用品种{}安装失败，失败报错已截图，跳过该品种，继续下一个品种的安装'.format(module_name))
                                time.sleep(5)
                                break
                    except:
                        continue
        except Exception as e:
            d = time.strftime('%Y年%m月%d日_%H点%M分', time.localtime())
            pic_name = module_name + '_' + str(d) + '.png'
            screent_path = os.path.join(os.path.join(os.path.dirname(__file__), 'install_fail_screenshosts'), pic_name)
            driver.get_screenshot_as_file(screent_path)
            self.fail_dict[module_name] = '安装失败，截图路径：{}'.format(screent_path)
            print(e)
            if module_name.split('-')[0] in ('JC', 'PT', 'CK'):
                sys.exit()
            else:
                ssh.ssh_exec_cmd('cd {base_dir}/{upgrade_dir}/{dir_name} && ./stop.sh'.format(base_dir=self.base_dir, upgrade_dir=self.upgrade_dir,
                                                                                              dir_name=module_name))
                time.sleep(5)

    def restart_weblogic(self):
        """重启三个域的公共方法"""

        """
        分别kill掉已经启动的域进程
        """
        ssh = SSH_Control(self.ssh_info)
        port_list = [self.dcab_domain_port, self.dom_domain_port, self.web_domain_port]
        for port in port_list:
            log('-----开始kill进程：端口号{}-----'.format(port))
            stdin, stdout, stderr = ssh.ssh_exec_cmd_without_wait('cd /home && lsof -i:{port}'.format(port=port))
            for i in stdout.readlines():
                if i.split(' ')[2] == 'PID':
                    continue
                else:
                    pid = i.split(' ')[4]
                    ssh.ssh_exec_cmd('cd /home && kill -9 {pid}'.format(pid=pid))
            log('-----结束kill进程：端口号{}-----'.format(port))
        time.sleep(2)

        """
        重新启动三个域
        """
        log('-----dcab域开始启动-----')
        ssh.ssh_exec_cmd_without_wait(
            'cd {base_dir}/domains/dcab-domain && nohup sh startWebLogic.sh >dcab.log 2>&1 &tail -f dcab.log'.format(
                base_dir=self.base_dir))
        time.sleep(5)
        log('-----dcab域启动完成，dom域开始启动-----')
        ssh.ssh_exec_cmd_without_wait(
            'cd {base_dir}/domains/dom-domain && nohup sh startWebLogic.sh >dom.log 2>&1 &tail -f dom.log'.format(
                base_dir=self.base_dir))
        time.sleep(5)
        log('-----dom域启动完成，web域开始启动-----')
        ssh.ssh_exec_cmd_without_wait(
            'cd {base_dir}/domains/web-domain && nohup sh startWebLogic.sh >web.log 2>&1 &tail -f web.log'.format(
                base_dir=self.base_dir))
        time.sleep(5)
        log('-----web域启动完成-----')
        time.sleep(10)

    def kill_process_with_port(self, port):
        """
        通过端口杀掉进程
        """
        ssh = SSH_Control(self.ssh_info)
        log('-----开始kill进程：端口号{}-----'.format(port))
        stdin, stdout, stderr = ssh.ssh_exec_cmd_without_wait('cd /home && lsof -i:{port}'.format(port=port))
        for i in stdout.readlines():
            if i.split(' ')[2] == 'PID':
                continue
            else:
                pid = i.split(' ')[4]
                ssh.ssh_exec_cmd('cd /home && kill -9 {pid}'.format(pid=pid))
        log('-----结束kill进程：端口号{}-----'.format(port))
        time.sleep(2)

    def install_pt_app(self):
        base_package_dict, _ = self.get_pz_list()
        if 'PT' in base_package_dict.keys():
            module_name = base_package_dict['PT']
            if module_name:
                self.start_install(module_name)

    def install_ck_app(self):
        base_package_dict, _ = self.get_pz_list()
        if 'CK' in base_package_dict.keys():
            module_name = base_package_dict['CK']
            if module_name:
                self.start_install(module_name)

    def install_all_pz(self):
        _, pz_list = self.get_pz_list()
        # pz_list = ['RSAFE-1.1.0.0']  # 调试代码，忽略
        for pz in pz_list:
            self.start_install(pz)

    def get_fail_data(self):
        if self.fail_dict:
            log('【安装失败的品种】：{}'.format(json.dumps(self.fail_dict, ensure_ascii=False, indent=4)))
        else:
            log('【安装结束，所有品种均已安装成功，请重启三个域并登录系统进行初始化操作】')

    def get_pz_list(self):
        self.base_package_dict = {}
        self.pz_package_list = []
        if self.is_upload == 'NO':
            package_name_list = os.listdir(r'{local_package_path}'.format(local_package_path=self.local_package_path))
        else:
            sftp = SftpController(self.ssh_info)
            package_name_list = sftp.get_sftp_dir(self.upgrade_package_path)
        for package_name in package_name_list:
            if package_name.endswith('.zip'):
                dir_name = package_name.split('.zip')[0]
            elif package_name.endswith('.py'):
                continue
            elif package_name.endswith('.bak'):
                continue
            else:
                dir_name = package_name
            if dir_name.startswith('JC-') or dir_name.startswith('PT-') or dir_name.startswith('CK'):
                key = dir_name.split('-')[0]
                self.base_package_dict[key] = dir_name
            else:
                self.pz_package_list.append(dir_name)
        return self.base_package_dict, self.pz_package_list

    def pz_of_faild_retry(self):
        '''
        考虑到有时候由于网络或者环境原因导致执行失败，安装失败的品种允许重试一次，重试前询问是否重试，可根据截图报错判断
        :return:
        '''
        if self.fail_dict:
            user_command = input('【当前存在安装失败的品种，请确认是否重试（Y/N）】：')
            if user_command == 'Y':
                pz_list = self.fail_dict.keys()
                for pz in pz_list:
                    self.start_install(pz)
            elif user_command == 'N':
                log('【已放弃重试，程序运行完毕】')
            else:
                log('【输入错误，请注意字母大小写】')
                self.pz_of_faild_retry()


def install_main():
    """
    安装全过程执行main方法，按照顺寻进行安装
    :param self:
    :return:
    """
    # #初始化安装类实例
    start_time = datetime.datetime.now()
    log('【第一步：开始--初始化安装配置信息，实例化安装类】')
    obj = Atuo_Install()
    log('【第一步：结束--初始化安装配置信息，实例化安装类】')
    # 创建目录并上传文件，自动创建domains，并且自动解压
    log('【第三步：开始--创建目录，上传本地安装包，解压安装包到对应目录下】')
    obj.create_dir_and_upload_files_and_unzip_file()
    log('【第三步：结束--创建目录，上传本地安装包，解压安装包到对应目录下】')
    # 安装平台模块
    log('【第七步：开始--安装平台模块】')
    obj.install_pt_app()
    log('【第七步：结束--安装平台模块】')
    # 安装仓库模块
    log('【第八步：开始--安装仓库模块】')
    obj.install_ck_app()
    log('【第八步：结束--安装仓库模块】')
    # 安装品种
    log('【第九步：开始--安装品种模块】')
    obj.install_all_pz()
    log('【第九步：结束--安装品种模块】')
    # 安装完成，如果存在失败的品种，则打印失败品种列表，如果全部成功，则打印安装完成结束语
    obj.get_fail_data()
    # 失败品种，允许重试一次，重试
    obj.pz_of_faild_retry()
    # 计算安装总耗时
    end_time = datetime.datetime.now()
    excuse_time = round((end_time - start_time).seconds / 60, 2)
    print('【安装运行总耗时】： ' + str(excuse_time) + '分')


if __name__ == '__main__':
    install_main()
