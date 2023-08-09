#!/usr/bin/env python
# _*_ coding: utf-8 _*-
# @Time     : 2021/6/4 9:53
# @Author   : yangshukun
# @File     : BaseEnv.py
import os

"""服务器地址，端口，数据库，账户，密码等配置"""

# 公用测试环境
system_test_base_url = 'http://192.168.20.157:1003/portal/main_new.do'
system_test_dcab_port = '1002'
system_test_dom_port = '1001'

# 公用测试数据库
oracle_157_dm = {'user': 'TA0859QXAZ_DM', 'pswd': '123456', 'adress': '192.168.20.157', 'db_name': 'orcl'}
oracle_157_dw = {'user': 'TA0859QXAZ_DW', 'pswd': '123456', 'adress': '192.168.20.157', 'db_name': 'orcl'}
oracle_157_web = {'user': 'TA0859QXAZ_WEB', 'pswd': '123456', 'adress': '192.168.20.157', 'db_name': 'orcl'}
oracle_134_dm = {'user': 'D2021V8_dm', 'pswd': '123456', 'adress': '192.168.20.134', 'db_name': 'orcl'}
oracle_119_dm = {'user': 'D2021V09DM', 'pswd': '123456', 'adress': '192.168.20.119', 'db_name': 'orcl'}
oracle_135_dm = {'user': 'D226QXAZ_DM', 'pswd': '123456', 'adress': '192.168.20.135', 'db_name': 'orcl'}


# 服务器环境
common_ssh_port = 22
server_134 = {'url': '192.168.20.134', 'dcab_port': '4002', 'dom_port': '4001', 'web_port': '4003'}
server_119 = {'url': '192.168.20.119', 'dcab_port': '2002', 'dom_port': '2001', 'web_port': '2003'}
server_157 = {'url': '192.168.20.157', 'dcab_port': '1002', 'dom_port': '1001', 'web_port': '1003'}

# sftp参数
sftp_119 = {'url': '192.168.20.119', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}
sftp_135 = {'url': '192.168.20.135', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}
sftp_134 = {'url': '192.168.20.134', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}
sftp_62 = {'url': '192.168.20.62', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}
sftp_117 = {'url': '192.168.20.117', 'port': 22, 'username': 'fjny0201', 'password': '11111111'}
sftp_212 = {'url': '192.168.20.212', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}
sftp_157 = {'url': '192.168.20.157', 'port': 22, 'username': 'root', 'password': 'Ninest@r123'}

# 批量删除DM数据需要排除的表
EXCEPT_TABLE = ['DM_EAST_211_CONFIG',
                'DM_EAST_SUBJECT_CONFIG',
                'DM_IMAS_DATA_OTHER_INFO',
                'DM_IMAS_REPORTSTATE',
                'DM_IMAS_LCXCTJ_PRE',
                'DM_IMAS_LCXCTJ_PRE20220625',
                'DM_IMAS_LCXCTJ_PRE20220525',
                'DM_IMAS_VERIFYRESULT',
                'DM_IMAS_JGFZXX_HIS',
                'DM_IMAS_REPORT_FILE',
                'DM_IMAS_DATA_REPORT_RECORD',
                'DM_IMAS_JGFRXX_HIS',
                'DM_RFBS_JGFRJB_KEY',
                'DM_RFBS_JGFRJB_VALUE',
                'DM_RFBS_RATING_MAPPING',
                'DM_RFBS_JGFRZF_KEY',
                'DM_RFBS_JGFRLR_VALUE',
                'DM_RFBS_JGFRZF_VALUE',
                'DM_RFBS_JGFRLR_KEY',
                'DM_MBTD_CHECK_RULE',
                'DM_MBTD_RECORD_DATA',
                'DM_MBTD_BUSCODE_CONTRAST',
                'DM_MBTD_RPSET',
                'DM_MBTD_FEEDBACK_RULE',
                'DM_MBTD_REGOIN',
                'DM_MBTD_MESSAGE',
                'DM_MBTD_RECORD',
                'DM_MBTD_SEGMENT',
                'DM_RGEC_REPORT',
                'DM_RGEC_RESULTMSG_INFO',
                'DM_RGEC_RPT_DATAZIP_INFO',
                'DM_RGEC_RESULTMSG',
                'DM_RGEC_ORGAN_INFO_HANDLE',
                'DM_SAZJ_BATCH_RECORD']


# sftp应用路径配置
class BasePath:
    base_local_path = os.path.dirname(os.path.dirname(__file__)) + '\\ServiceHome'
    base_dcab_target_path = '/home/{}/dcab/DCAB-Service/bs/DCab-Service/WEB-INF'
    base_dom_target_path = '/home/{}/dcab/DOM-Service/bs/DOM-Service/WEB-INF'
    base_web_target_root_path = '/home/{}/dcab/WEB/bs/SmartPage/'
    base_web_target_cfg_path = '/home/{}/dcab/WEB/bs/SmartPage/WEB-INF/classes'
    base_web_target_com_path = '/home/{}/dcab/WEB/bs/SmartPage/WEB-INF/classes/com/nstc/'


class RMM_SERVICE:
    cfg_local_path = "\\RMM-Service_1.0.0\\RMM-Service_1.0.0\\RMM-Service\\WEB-INF\\classes\\RMM-Service-CFG"
    cfg_target_path = '/classes/RMM-Service-CFG'
    lib_local_path = '\\RMM-Service_1.0.0\\RMM-Service_1.0.0\\RMM-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class DOM_SERVICE:
    cfg_local_path = '\\DOM-Service_1.0.0\\DOM-Service_1.0.0\\DOM-Service\\WEB-INF\\classes\\DOM-Service-CFG'
    cfg_target_path = '/classes/DOM-Service-CFG'
    lib_local_path = '\\DOM-Service_1.0.0\\DOM-Service_1.0.0\\DOM-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class REAST_SERVICE:
    cfg_local_path = '\\REAST-Service_1.0.0\\REAST-Service_1.0.0\\REAST-Service\\WEB-INF\\classes\\REAST-Service-CFG'
    cfg_target_path = '/classes/REAST-Service-CFG'
    lib_local_path = '\\REAST-Service_1.0.0\\REAST-Service_1.0.0\\REAST-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RFBS_SERVICE:
    cfg_local_path = '\\RFBS-Service_1.0.0\\RFBS-Service_1.0.0\\RFBS-Service\\WEB-INF\\classes\\RFBS-Service-CFG'
    cfg_target_path = '/classes/RFBS-Service-CFG'
    lib_local_path = '\\RFBS-Service_1.0.0\\RFBS-Service_1.0.0\\RFBS-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RMBTD_SERVICE:
    cfg_local_path = '\\RMBTD-Service_1.0.0\\RMBTD-Service_1.0.0\\RMBTD-Service\\WEB-INF\\classes\\RMBTD-Service-CFG'
    cfg_target_path = '/classes/RMBTD-Service-CFG'
    lib_local_path = '\\RMBTD-Service_1.0.0\\RMBTD-Service_1.0.0\\RMBTD-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RIMAS_SERVICE:
    cfg_local_path = '\\RIMAS-Service_1.0.0\\RIMAS-Service_1.0.0\\RIMAS-Service\\WEB-INF\\classes\\RIMAS-Service-CFG'
    cfg_target_path = '/classes/RIMAS-Service-CFG'
    lib_local_path = '\\RIMAS-Service_1.0.0\\RIMAS-Service_1.0.0\\RIMAS-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RSAZJ_SERVICE:
    cfg_local_path = '\\RSAZJ-Service_1.0.0\\RSAZJ-Service_1.0.0\\RSAZJ-Service\\WEB-INF\\classes\\RSAZJ-Service-CFG'
    cfg_target_path = '/classes/RSAZJ-Service-CFG'
    lib_local_path = '\\RSAZJ-Service_1.0.0\\RSAZJ-Service_1.0.0\\RSAZJ-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RAMLRS_SERVICE:
    cfg_local_path = '\\RAMLRS-Service_1.0.0\\RAMLRS-Service_1.0.0\\RAMLRS-Service\\WEB-INF\\classes\\RAMLRS-Service-CFG'
    cfg_target_path = '/classes/RAMLRS-Service-CFG'
    lib_local_path = '\\RAMLRS-Service_1.0.0\\RAMLRS-Service_1.0.0\\RAMLRS-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RGEC_SERVICE:
    cfg_local_path = '\\RGEC-Service_1.0.0\\RGEC-Service_1.0.0\\RGEC-Service\\WEB-INF\\classes\\RGEC-Service-CFG'
    cfg_target_path = '/classes/RGEC-Service-CFG'
    lib_local_path = '\\RGEC-Service_1.0.0\\RGEC-Service_1.0.0\\RGEC-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RN1104_SERVICE:
    cfg_local_path = '\\RN1104-Service_1.0.0\\RN1104-Service_1.0.0\\RN1104-Service\\WEB-INF\\classes\\RN1104-Service-CFG'
    cfg_target_path = '/classes/RN1104-Service-CFG'
    lib_local_path = '\\RN1104-Service_1.0.0\\RN1104-Service_1.0.0\\RN1104-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class RPBCC_SERVICE:
    cfg_local_path = '\\RPBCC-Service_1.0.0\\RPBCC-Service_1.0.0\\RPBCC-Service\\WEB-INF\\classes\\RPBCC-Service-CFG'
    cfg_target_path = '/classes/RPBCC-Service-CFG'
    lib_local_path = '\\RPBCC-Service_1.0.0\\RPBCC-Service_1.0.0\\RPBCC-Service\\WEB-INF\\lib'
    lib_target_path = '/lib'


class DOM_WEB:
    root_local_path = '\\DOM-Web_1.0.0\\DOM-Web_1.0.0\\DOM-Web\\DOM-Web-ROOT'
    cfg_local_path = '\\DOM-Web_1.0.0\\DOM-Web_1.0.0\\DOM-Web\\WEB-INF\\classes\\DOM-Web-CFG'
    nstc_local_path = '\\DOM-Web_1.0.0\\DOM-Web_1.0.0\\DOM-Web\\WEB-INF\\classes\\com\\nstc\\dom'
    root_target_path = '/DOM-Web-ROOT'
    cfg_target_path = '/DOM-Web-CFG'
    nstc_target_path = '/dom'


class RMM_WEB:
    root_local_path = '\\RMM-Web_1.0.0\\RMM-Web_1.0.0\\RMM-Web\\RMM-Web-ROOT'
    cfg_local_path = '\\RMM-Web_1.0.0\\RMM-Web_1.0.0\\RMM-Web\\Web-INF\\classes\\RMM-Web-CFG'
    nstc_local_path = '\\RMM-Web_1.0.0\\RMM-Web_1.0.0\\RMM-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RMM-Web-ROOT'
    cfg_target_path = '/RMM-Web-CFG'
    nstc_target_path = '/rmm'


class REAST_WEB:
    root_local_path = '\\REAST-Web_1.0.0\\REAST-Web_1.0.0\\REAST-Web\\REAST-Web-ROOT'
    cfg_local_path = '\\REAST-Web_1.0.0\\REAST-Web_1.0.0\\REAST-Web\\Web-INF\\classes\\REAST-Web-CFG'
    nstc_local_path = '\\REAST-Web_1.0.0\\REAST-Web_1.0.0\\REAST-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/REAST-Web-ROOT'
    cfg_target_path = '/REAST-Web-CFG'
    nstc_target_path = '/rmm/reast'


class RIMAS_WEB:
    root_local_path = '\\RIMAS-Web_1.0.0\\RIMAS-Web_1.0.0\\RIMAS-Web\\RIMAS-Web-ROOT'
    cfg_local_path = '\\RIMAS-Web_1.0.0\\RIMAS-Web_1.0.0\\RIMAS-Web\\Web-INF\\classes\\RIMAS-Web-CFG'
    nstc_local_path = '\\RIMAS-Web_1.0.0\\RIMAS-Web_1.0.0\\RIMAS-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RIMAS-Web-ROOT'
    cfg_target_path = '/RIMAS-Web-CFG'
    nstc_target_path = '/rmm/rimas'


class RFBS_WEB:
    root_local_path = '\\RFBS-Web_1.0.0\\RFBS-Web_1.0.0\\RFBS-Web\\RFBS-Web-ROOT'
    cfg_local_path = '\\RFBS-Web_1.0.0\\RFBS-Web_1.0.0\\RFBS-Web\\Web-INF\\classes\\RFBS-Web-CFG'
    nstc_local_path = '\\RFBS-Web_1.0.0\\RFBS-Web_1.0.0\\RFBS-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RFBS-Web-ROOT'
    cfg_target_path = '/RFBS-Web-CFG'
    nstc_target_path = '/rmm/rfbs'


class RMBTD_WEB:
    root_local_path = '\\RMBTD-Web_1.0.0\\RMBTD-Web_1.0.0\\RMBTD-Web\\RMBTD-Web-ROOT'
    cfg_local_path = '\\RMBTD-Web_1.0.0\\RMBTD-Web_1.0.0\\RMBTD-Web\\Web-INF\\classes\\RMBTD-Web-CFG'
    nstc_local_path = '\\RMBTD-Web_1.0.0\\RMBTD-Web_1.0.0\\RMBTD-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RMBTD-Web-ROOT'
    cfg_target_path = '/RMBTD-Web-CFG'
    nstc_target_path = '/rmm/mbtd'


class RSAZJ_WEB:
    root_local_path = '\\RSAZJ-Web_1.0.0\\RSAZJ-Web_1.0.0\\RSAZJ-Web\\RSAZJ-Web-ROOT'
    cfg_local_path = '\\RSAZJ-Web_1.0.0\\RSAZJ-Web_1.0.0\\RSAZJ-Web\\Web-INF\\classes\\RSAZJ-Web-CFG'
    nstc_local_path = '\\RSAZJ-Web_1.0.0\\RSAZJ-Web_1.0.0\\RSAZJ-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RSAZJ-Web-ROOT'
    cfg_target_path = '/RSAZJ-Web-CFG'
    nstc_target_path = '/rmm/rsazj'


class RAMLRS_WEB:
    root_local_path = '\\RAMLRS-Web_1.0.0\\RAMLRS-Web_1.0.0\\RAMLRS-Web\\RAMLRS-Web-ROOT'
    cfg_local_path = '\\RAMLRS-Web_1.0.0\\RAMLRS-Web_1.0.0\\RAMLRS-Web\\Web-INF\\classes\\RAMLRS-Web-CFG'
    nstc_local_path = '\\RAMLRS-Web_1.0.0\\RAMLRS-Web_1.0.0\\RAMLRS-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RAMLRS-Web-ROOT'
    cfg_target_path = '/RAMLRS-Web-CFG'
    nstc_target_path = '/rmm/ramlrs'


class RGEC_WEB:
    root_local_path = '\\RGEC-Web_1.0.0\\RGEC-Web_1.0.0\\RGEC-Web\\RGEC-Web-ROOT'
    cfg_local_path = '\\RGEC-Web_1.0.0\\RGEC-Web_1.0.0\\RGEC-Web\\Web-INF\\classes\\RGEC-Web-CFG'
    nstc_local_path = '\\RGEC-Web_1.0.0\\RGEC-Web_1.0.0\\RGEC-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RGEC-Web-ROOT'
    cfg_target_path = '/RGEC-Web-CFG'
    nstc_target_path = '/rmm/rgec'


class RN1104_WEB:
    root_local_path = '\\RN1104-Web_1.0.0\\RN1104-Web_1.0.0\\RN1104-Web\\RN1104-Web-ROOT'
    cfg_local_path = '\\RN1104-Web_1.0.0\\RN1104-Web_1.0.0\\RN1104-Web\\Web-INF\\classes\\RN1104-Web-CFG'
    nstc_local_path = '\\RN1104-Web_1.0.0\\RN1104-Web_1.0.0\\RN1104-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RN1104-Web-ROOT'
    cfg_target_path = '/RN1104-Web-CFG'
    nstc_target_path = '/rmm/rn1104'


class RPBCC_WEB:
    root_local_path = '\\RPBCC-Web_1.0.0\\RPBCC-Web_1.0.0\\RPBCC-Web\\RPBCC-Web-ROOT'
    cfg_local_path = '\\RPBCC-Web_1.0.0\\RPBCC-Web_1.0.0\\RPBCC-Web\\Web-INF\\classes\\RPBCC-Web-CFG'
    nstc_local_path = '\\RPBCC-Web_1.0.0\\RPBCC-Web_1.0.0\\RPBCC-Web\\Web-INF\\classes\\com\\nstc\\rmm'
    root_target_path = '/RPBCC-Web-ROOT'
    cfg_target_path = '/RPBCC-Web-CFG'
    nstc_target_path = '/rmm/rpbcc'
