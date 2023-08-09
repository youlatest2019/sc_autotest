#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/14 13:44
# @Author   : yangshukun
# @File     : domsd.py
import json
import os
import re
import time
import requests
from requests_toolbelt import MultipartEncoder


class ImportYwbl():

    def __init__(self, base_url, commit_date):
        self.base_url = base_url
        self.commit_date = commit_date
        self.session = requests.session()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.base_path = os.path.join(os.path.join(base_dir, 'data'), '补录')

    def login(self):
        # 打开网页进入数仓登录页面
        base_url = self.base_url + "/portal/main_new.do"
        login_url = self.base_url + "/portal/login_Product.do?t={}"
        headers = {"Host": self.base_url,
                   "Connection": "keep-alive",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9",
                   "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "Referer": self.base_url + "/portal/main.do"
                   }
        # 打开网页
        self.session.get(base_url, headers=headers)
        # 登录
        form_data = {"userno": "llbb1",
                     "sign_uno": "",
                     "scc": "false",
                     "plain_uno": "LOGONDATA:1669601353",
                     "PE": "830150",
                     "password": "",
                     "MDS": "830150"}
        res2 = self.session.post(login_url.format(time.time()), data=form_data, headers=headers)
        print(res2.content.decode(encoding="UTF-8"))
        return

    def get_moduleid(self):
        module_id_dict = dict()
        get_ywlx_url = self.base_url + '/SmartPage/DOM-Web@DCab_DOMAjaxAction.sf?buss=supplement.LoadYWLXGroupBusiness'
        get_ywlx_headers = {"Host": self.base_url,
                            "Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                            "Accept": "application/json, text/javascript, */*; q=0.01",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "zh-CN,zh;q=0.9",
                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                            "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                            }
        get_ywlx_body = {"onlyAttribution": "true"}
        res = self.session.post(url=get_ywlx_url, data=get_ywlx_body, headers=get_ywlx_headers)

        for k in res.json()['data'].keys():
            get_module_url = self.base_url + '/SmartPage/DOM-Web@DCab_DOMAjaxAction.sf?buss=supplement.LoadYWLXByGroupIdBusiness'
            get_module_headers = {"Host": self.base_url,
                                  "Connection": "keep-alive",
                                  "Upgrade-Insecure-Requests": "1",
                                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                                  "Accept": "application/json, text/javascript, */*; q=0.01",
                                  "Accept-Encoding": "gzip, deflate",
                                  "Accept-Language": "zh-CN,zh;q=0.9",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                                  }
            get_module_body = {"onlyAttribution": "true",
                               "bussTypeGroup": k}
            r = self.session.post(url=get_module_url, data=get_module_body, headers=get_module_headers).json()
            new_dict = dict()
            for s in r['YWLXList']:
                new_dict[s['value']] = s['key']
            module_id_dict[k] = new_dict
        return module_id_dict

    def upload_file(self, dir_name, file_name, module_id):
        # 上传文件导入
        upload_url = self.base_url + '/SmartPage/DOM-Web@importExcelData.do'
        upload_headers = {"Host": self.base_url,
                          "Connection": "keep-alive",
                          "Upgrade-Insecure-Requests": "1",
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                          "Accept": "application/json, text/javascript, */*; q=0.01",
                          "Accept-Encoding": "gzip, deflate",
                          "Accept-Language": "zh-CN,zh;q=0.9",
                          # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary6awksKxJSm3li3ga",
                          "Referer": self.base_url + "/SmartPage/DOM-Web-ROOT/page/dataSupplementImport.jsp"
                          }

        file_home = os.path.join(os.path.join(self.base_path, dir_name), file_name)
        upload_body = MultipartEncoder(
            fields=[
                ("loadPth", "C:\fakepath\{}".format(file_name)),
                ("supType", "BL"),
                ("sjlxId", ""),
                ("moduleId", module_id),
                ("tabCode", ""),
                ("sjrq", "3000-12-31"),
                ("filePath", (
                    file_name, open(file_home, "rb"),
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
            ])
        upload_headers['Content-Type'] = upload_body.content_type
        upload_res = self.session.post(url=upload_url, headers=upload_headers, data=upload_body)
        # print(upload_res.json())
        return upload_res.json()
        # print(json.dumps(upload_res.json(), ensure_ascii=False, indent=4))

    def get_all_data_list(self, module_id):
        get_all_url = self.base_url + "/SmartPage/DOM-Web@DCab_AjaxAction.sf?buss=QueryPreListBusiness&moduleType=supplementForm"
        get_all_headers = {"Host": self.base_url,
                           "Connection": "keep-alive",
                           "Upgrade-Insecure-Requests": "1",
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                           "Accept": "application/json, text/javascript, */*; q=0.01",
                           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                           "Accept-Encoding": "gzip, deflate",
                           "Accept-Language": "zh-CN,zh;q=0.9",
                           "Origin": self.base_url,
                           "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                           }
        get_all_body = {"paging_totalPage": 1,
                        "paging_current": 1,
                        "paging_pageSize": 200,
                        "supType": "BL",
                        "moduleId": module_id,
                        "BtnQry": "批量导入",
                        "btnBatchExport": "批量导出",
                        "ywlx": module_id.split('_')[0],
                        "sjrq": "3000-12-31",
                        "makeupStatus": "noSubmit"}
        get_all_res = self.session.post(url=get_all_url, headers=get_all_headers, data=get_all_body)
        module_identity_str = ""
        for ide_str in get_all_res.json()["data"]:
            module_identity_str = module_identity_str + "," + ide_str["MODULE_IDENTITY_"]
        # print(module_identity_str[1:])
        return module_identity_str[1:]

    def load_check_data_list(self, module_id, biz_values):
        load_data_url = self.base_url + "/SmartPage/DOM-Web@DCab_DOMAjaxAction.sf?buss=LoadPreListCheckDataBusiness"
        load_data_headers = {"Host": self.base_url,
                             "Connection": "keep-alive",
                             "Upgrade-Insecure-Requests": "1",
                             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                             "Accept": "application/json, text/javascript, */*; q=0.01",
                             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "zh-CN,zh;q=0.9",
                             "Origin": self.base_url,
                             "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                             }
        load_data_body = {"moduleId": module_id,
                          "dataDate": "3000-12-31",
                          "bizValue": biz_values
                          }
        get_all_res = self.session.post(url=load_data_url, headers=load_data_headers, data=load_data_body)

    def check_ods_data(self, module_id):
        # 校验导入数据
        check_ods_url = self.base_url + '/SmartPage/DOM-Web@DCab_DOMAjaxAction.sf?buss=supplement.CheckODSDataBusiness'
        check_ods_headers = {"Host": self.base_url,
                             "Connection": "keep-alive",
                             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                             "Accept": "application/json, text/javascript, */*; q=0.01",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "zh-CN,zh;q=0.9",
                             "Origin": self.base_url,
                             "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                             }
        check_ods_body = {"moduleId": module_id,
                          "sjlxId": module_id,
                          "sjrq": "3000-12-31",
                          "supType": "BL"
                          }
        # check_ods_headers['Content-Type'] = check_ods_body.content_type
        check_ods_res = self.session.post(url=check_ods_url, headers=check_ods_headers, data=check_ods_body)
        # print(check_ods_res.json())
        return check_ods_res.json()

    def get_check_state(self, module_id):
        # 获取校验结果状态
        check_state_url = self.base_url + '/SmartPage/DOM-Web@DCab_DOMAjaxAction.sf?buss=supplement.QueryODSCheckStateBusiness'
        check_state_headers = {"Host": self.base_url,
                               "Connection": "keep-alive",
                               "Upgrade-Insecure-Requests": "1",
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                               "Accept": "application/json, text/javascript, */*; q=0.01",
                               "Accept-Encoding": "gzip, deflate",
                               "Accept-Language": "zh-CN,zh;q=0.9",
                               "Origin": self.base_url,
                               "Referer": self.base_url + "/SmartPage/DOM-Web@dataSupplement.do"
                               }

        check_state_body = {"moduleId": module_id,
                            "sjlxId": module_id,
                            "supType": "BL"
                            }

        check_state_res = self.session.post(url=check_state_url, headers=check_state_headers, data=check_state_body)
        # print(check_state_res.json())

    def commit_ods_data(self, module_id):
        # 提交全部业务数据
        commit_url = self.base_url + '/SmartPage/DOM-Web@DCab_AjaxAction.sf'
        commit_headers = {"Host": self.base_url,
                          "Connection": "keep-alive",
                          "Upgrade-Insecure-Requests": "1",
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                          "Accept": "application/json, text/javascript, */*; q=0.01",
                          "Accept-Encoding": "gzip, deflate",
                          "Accept-Language": "zh-CN,zh;q=0.9",
                          "Origin": self.base_url,
                          "Referer": self.base_url + "/SmartPage/DOM-Web-ROOT/page/supDataSubmit.html"
                          }
        commit_params = {"buss": "DataSubmitBusiness",
                         "supType": "BL",
                         "moduleId": module_id,
                         "submitDataDate": self.commit_date,
                         "pks": "",
                         "dataDate": "undefined",
                         "BtnQry": "批量导入",
                         "btnBatchExport": "批量导出",
                         "ywlx": module_id.split('_')[0],
                         "sjrq": "3000-12-31",
                         "makeupStatus": "noSubmit",
                         "isSubmitAll": 1
                         }

        commit_res = self.session.post(url=commit_url, headers=commit_headers, params=commit_params)
        # print(commit_res.json())
        return commit_res.json()

    def batch_import_files(self):
        start_time = time.time()
        code_list = ['CWXX', 'JCXX', 'CKYW', 'DKYW', 'TYYW', 'TZYW', 'RZYW', 'WHYW', 'WTDL', 'PJYW']
        self.login()
        s = self.get_moduleid()
        # print(s)
        dir_list = os.listdir(self.base_path)
        dir_list.sort(key=lambda x: int(re.match(r'(\d+)', x).group()))
        # print(dir_list)
        failed_list = []
        for dir in dir_list:
            file_list = os.listdir(os.path.join(self.base_path, dir))
            file_list.sort(key=lambda x: int(re.match(r'(\d+)', x).group()))
            code = code_list[int(dir.split('-')[0]) - 1]
            module_id_dict = s[code]
            # print(module_id_dict)
            for f in file_list:
                module_id = module_id_dict[f.split('.')[0].split('-')[1]]
                upload_result = self.upload_file(dir_name=dir, file_name=f, module_id=module_id)
                if upload_result['resInfo']['msg'] == '数据获取成功':
                    print(f, ":导入数据成功，准备开始校验.....")
                    biz_values = self.get_all_data_list(module_id)
                    self.load_check_data_list(module_id, biz_values)
                    check_ods_result = self.check_ods_data(module_id=module_id)
                    if check_ods_result["msg"] == "数据校验执行完成":
                        print(f, "：校验完成，准备开始提交数据.....")
                        commit_res = self.commit_ods_data(module_id)
                        if commit_res["code"] == '00':
                            print(f, ":数据导入、校验、提交完成.....\n")
                        else:
                            failed_list.append(f)
                            print(f, "提交失败", commit_res)
                    else:
                        print(f, ":校验失败", check_ods_result)
                        failed_list.append(f)
                        continue
                else:
                    print(f, ":导入数据失败", upload_result)
                    failed_list.append(f)
                    continue
        end_time = time.time()
        excuse_time = end_time - start_time
        print("补录耗时：", excuse_time, "\n失败的模型有：", failed_list)


if __name__ == '__main__':
    base_url = 'http://192.168.20.157:5553'
    commit_date = "2023-03-31"
    a = ImportYwbl(base_url, commit_date)
    a.batch_import_files()
