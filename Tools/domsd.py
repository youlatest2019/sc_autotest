#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2022/11/14 13:44
# @Author   : yangshukun
# @File     : domsd.py
import time
import requests

base_url = "http://192.168.20.157:1003/portal/main.do"
login_url = "http://192.168.20.157:1003/portal/login_Product.do?t={}"
domsd_url = "http://192.168.20.157:1003/SmartPage/DOM-Web@DCab_AjaxAction.sf?buss=com.nstc.dom.business.reExtract.ReExtractBusiness"
headers = {"Host": "192.168.20.157:1003",
           "Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Referer": "http://192.168.20.157:1003/portal/main.do"
           }
session_1 = requests.session()
# 打开网页
res1 = session_1.get(base_url, headers=headers)

# 登录
form_data = {"userno": "llbb1",
             "sign_uno": "",
             "scc": "false",
             "plain_uno": "LOGONDATA:1479850569",
             "PE": "830150",
             "password": "",
             "MDS": "830150"}
res2 = session_1.post(login_url.format(time.time()), data=form_data, headers=headers)
print(res2.content.decode(encoding="UTF-8"))

start_time = time.time()
# 调用调度接口下发抽数请求
domsd_data = {"reportIds": "['324318', '229275', '275943','298645']",
              "method": "doReExtractDataByReportIds"}

res0 = session_1.post(url=domsd_url, data=domsd_data, headers=headers)

# 轮询所有抽数任务的抽数状态，如果全部抽数完成（状态不存在status！=1），则循环结束，如果存在，则继续查询
report_no_list = ["A3301-2022Q1",
                  "A3327-2022Q1",
                  "G0700-3000H1",
                  "A1302-2022Q1"]
count_task = len(report_no_list)
fail_list = []
while True:
    status_list = []
    for rep_no in report_no_list:
        print("剩余取数中的任务：", report_no_list)
        getresult_data = {"flag": "", "status": "", "endDate": "", "reportName": "", "startDate": "",
                          "reportNo": rep_no, "method": "getReportList", "bspzbh": "",
                          "treeListFlag": "Y"}

        res3 = session_1.post(url=domsd_url, data=getresult_data, headers=headers)
        status = eval(res3.json()["data"])[2]["status"]
        status_list.append(status)
        if status == -1:
            fail_list.append(rep_no)
        # 抽数成功的不再查询
        elif status == 2 or status == -1:
            report_no_list.remove(rep_no)
    print("当前所有抽数任务的状态：", status_list)
    if 1 not in status_list:
        break
end_time = time.time()
t = end_time - start_time
print(t)
print("抽数失败的报送任务编号：", fail_list)
print("抽数的失败率为：", len(fail_list) / count_task)
