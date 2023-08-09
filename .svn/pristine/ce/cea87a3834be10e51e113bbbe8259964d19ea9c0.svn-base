from baseOperation.init_cls import *
from pageKeyword.keyword_bsgl_rmbtd import *
from utils.operationXml import *
import sys
from baseOperation.init_self import *
from pageKeyword.keyword_bsgl_common import *
from Common.OtherFunc import *


class BsglRmbtdTest(InitCls, BsglMainKeyword, OperationXml, BsglPubBsrwKeyword, BsglPubBsfwKeyword,
                    BsglPubFzglKeyword, BsglPubBssqKeyword, BsglPubSjsqKeyword, BsglPubSplcKeyword,
                    BsglRmbtdBmzhKeyword, BsglRmbtdCbmbglKeyword, BscsRmbtdKeyword):

    def test_01_add_bsrw_success(self):
        """征信报送任务新增+废弃报送任务成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送任务管理页签
        self.swithToBsrw()
        self.switchBspzFrame()
        bsnr_no = "MBTD290"
        bsqj_no = "20220331"
        bsqj_date = "2022年03月31日"
        response = self.queryBsrw(bsqj_date, "个人借贷账户信息记录")
        if response:
            res = self.GetTagText(self.COUNG_QUERY_RESULT_BSRW)
            if res != "共有 0 个报送任务，0 个已过期":
                self.abandonBsrw("rmbtd任务自动化废弃")
        # 6、新增报送任务
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        self.intoRmbtdTab()
        self.switchBspzFrame()
        self.swithToBsrw()
        self.switchBspzFrame()
        self.addBsrw(bsnr_no, bsqj_no, qssd_index=3, type='day')
        self.addBsrwSave()
        # 断言新增成功
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, '保存成功')
        self.closeXzrw_success()
        # 7、废弃新增的报送任务
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.switchBspzFrame()
        self.queryBsrw(bsqj_date, "个人借贷账户信息记录")
        self.abandonBsrw("废弃")
        # 断言废弃成功
        # res = self.GetTagText(self.MSG_ADD_RESULT)
        # self.assertEqual(res, '操作成功!')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_zx_bsfw_success(self):
        """征信报送范围点击是否报送成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、查询并点击是否报送按钮
        self.bsglMainFrame()
        self.queryBsnr("按日", "抵（质）押合同信息记录")
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        self.clickOkAlert()
        # 6、查询并点击是否报送按钮(是)
        self.whetherBsnr()
        # 断言点击是否报送成功
        res = self.GetTagText(self.MSG_SFBS_RESULT)
        self.assertEqual(res, '设置成功')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_change_bsfw_success(self):
        """征信报送范围修改单个报送内容设置成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送范围管理页签
        self.swithToBsfw()
        # 6、修改单个报送内容设置
        self.bsglMainFrame()
        self.checkOneBsnr()
        self.changeBsnr("上期", "0 45 /1 * * ?", "15", "天", "是", "是")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_change_bmzh_success(self):
        """征信编码转换修改报送编码成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报编码转换页签
        self.swithTo()
        # 6、修改报送参数配置信息
        self.bsglMainFrame()
        self.changeRmbtdBmzh("辛集市", "130526")
        self.GotoSleep()
        # 断言修改报送编码成功
        res = self.GetElementAttrbute(self.INPUT_MODIFY_BSBM, "value")
        self.assertEqual(res, '130526')
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_add_group_rmbtd_success(self):
        """征信分组管理--新增分组+删除分组成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签
        self.swithToFzgl()
        # 6、新增分组并断言成功
        self.bsglMainFrame()
        self.addGroup("征信自动化分组", "征信权限1", "自动化测试_征信分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 7、编辑分组并断言修改成功
        self.editeGroup("征信自动化分组", "征信自动化分组_修改", "自动化测试_征信分组描述_修改")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 8查询修改后的名称正确
        self.searchGroupName("征信自动化分组_修改")
        self.refreshGroupPage()
        res = self.GetTagText(self.DATA_FIRST_GROUP.format(1))
        self.assertEqual(res, "征信自动化分组_修改")
        # 删除分组
        self.delGroup("征信自动化分组_修改")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_bssq_success(self):
        """征信报送授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        self.addGroup("征信自动化分组", "征信权限1", "自动化测试_征信分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq("征信自动化分组")
        self.searchBsnr("企业基本信息记录")
        self.refreshBssqPage()
        # 勾选核对权限，上报权限，查询，重抽权限
        self.tickHdqx()
        self.tickSbqx()
        self.tickCxqx()
        self.tickCcqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 进入分组管理
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup("征信自动化分组")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_change_power_zx_success(self):
        """征信数据授权--修改授权成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理页签,新增分组并断言成功
        self.swithToFzgl()
        self.bsglMainFrame()
        self.addGroup("征信自动化分组", "征信权限1", "自动化测试_征信分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面选择分组
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        self.searchGroupNameBssq("征信自动化分组")
        self.searchBsnr("企业基本信息记录")
        self.refreshBssqPage()
        # 7、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 8、进入数据授权页面,选择分组
        self.SwitchFatherFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        self.searchGroupNameSjsq("征信自动化分组")
        self.searchBsnrSjsq("企业基本信息记录")
        self.refreshSjsqPage()
        # 9、点击全部，修改权限为按字段筛选+下拉框并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("存续状态")
        self.clickZdTwoBssqPage("1-正常")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 10、进入报送管理主界面，选择征信品种进入征信管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRmbtdTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 11、点击数据范围按钮，修改权限为按字段筛选+输入值并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.checkZdBssqPage()
        self.clickZdOneBssqPage("企业名称")
        self.inputZdBssqPage("自动化征信1")
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 12、进入报送管理主界面，选择征信品种进入征信管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRmbtdTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 13、点击数据范围按钮，修改权限为全部并断言成功
        self.clickAllBssqPage()
        self.bssqMainFrame()
        self.clickAllSjsq()
        self.saveSjsqPage()
        res = self.GetTagText(self.MSG_ADD_RESULT)
        self.assertEqual(res, "保存成功！")
        self.alertSucBssqPage()
        self.alertBssqPage()
        # 14、进入报送管理主界面，选择征信品种进入征信管理界面，切换到品种管理frame
        self.switchToBsglBaseFrame()
        self.intoRmbtdTab()
        self.switchBspzFrame()
        self.swithToSjsq()
        self.bsglMainFrame()
        # 15、清除查询条件并断言成功
        self.clearDataBssqPage()
        res = self.GetElementAttrbute(self.INPUT_BSNR_SJSQ, "value")
        self.assertEqual(res, "")
        # 进入分组管理删除分组
        self.SwitchFatherFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        self.delGroup("征信自动化分组")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_splc_batch_update_success(self):
        """征信审批流程批量修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入分组管理，新增一个分组
        self.swithToFzgl()
        self.bsglMainFrame()
        self.addGroup("征信自动化分组", "征信权限1", "自动化测试_征信分组描述")
        res = self.GetTagText(self.MSG_GROUP_SAVE)
        self.assertEqual(res, "保存成功！")
        self.closeGroupSaveAlert()
        # 6、进入报送授权页面
        self.SwitchFatherFrame()
        self.swithToBssq()
        self.bsglMainFrame()
        # 7、选择分组
        self.searchGroupNameBssq("征信自动化分组")
        self.searchBsnr("企业基本信息")
        self.refreshBssqPage()
        # 8、勾选核对权限
        self.tickHdqx()
        self.saveBssq()
        res = self.GetTagText(self.MSG_SAVE_BSSQ)
        self.assertEqual(res, "保存成功")
        # 9、进入审批流程页面
        self.SwitchFatherFrame()
        self.swithToSplc()
        self.bsglMainFrame()
        # 10、选择分组
        self.searchGroupNameSplc("征信自动化分组")
        self.refreshSplcPage()
        # 11、勾选报送内容，批量修改,并断言修改成功
        self.tickBoxAll()
        self.batchUpdateSplc("二代征信审批")
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.bsglMainFrame()
        res = self.GetTagText(self.MSG_BATCH_ALERT_SPLC)
        self.assertEqual(res, "保存成功")
        self.closeBatchAlertSplc()
        # 进入分组管理
        self.switchToBsglBaseFrame()
        self.bsglMainFrame()
        self.swithToFzgl()
        self.bsglMainFrame()
        # 删除分组
        self.delGroup("征信自动化分组")
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_09_cbmbgl_batch_update_success(self):
        """征信财报模板管理修改成功"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入财报模板管理页面
        self.swithToCbmbgl()
        self.bsglMainFrame()
        # 6、打开使用财报管理模板按钮，返回该模板配置好的坐标数量并分割
        self.changeCbRmbtdSykhmb()
        self.changeCbRmbtdSykhmbOK()
        # 7、进入配置页签坐标页面
        self.changeCbRmbtdQzgxY("企业资产负债表-2007版")
        self.QuiteFrame()
        self.changeCbRmbtdFrame()
        # 8、选择一个字段清除配置页签坐标并保存
        self.changeCbRmbtdSjxmc("预付账款")
        self.changeCbRmbtdRefresh()
        self.changeCbRmbtdQzdygzb("预付账款")
        self.changeCbRmbtdSave()
        self.changeCbRmbtdSykhmbOK()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        # 获取配置好的坐标数量
        a = self.GetTagText(self.QZGX_TEXT_YES.format("企业资产负债表-2007版"))
        res1 = splitStr(a, "/", 0)
        self.changeCbRmbtdQzgxY("企业资产负债表-2007版")
        self.QuiteFrame()
        self.changeCbRmbtdFrame()
        # 8、选择一个字段配置页签坐标并保存
        self.changeCbRmbtdSjxmc("预付账款")
        self.changeCbRmbtdRefresh()
        self.changeCbRmbtdQzdygzbok("B3", "预付账款")
        self.changeCbRmbtdSave()
        self.changeCbRmbtdSykhmbOK()
        self.switchToBsglBaseFrame()
        self.switchBspzFrame()
        self.bsglMainFrame()
        # 获取配置后的坐标数量并断言配置的坐标数量正确
        a = self.GetTagText(self.QZGX_TEXT_YES.format("企业资产负债表-2007版"))
        res2 = splitStr(a, "/", 0)
        self.assertEqual(int(res1) + 1, int(res2))
        # 关闭使用客户模板
        self.changeCbRmbtdSykhmb()
        self.changeCbRmbtdSykhmbOK()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_set_bscs_success(self):
        """设置征信报送参数"""
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入报送管理主界面
        self.intoBsglMainMenu()
        self.switchToBsglBaseFrame()
        # 3、选择征信品种进入征信管理界面
        self.intoRmbtdTab()
        # 4、切换到品种管理frame
        self.switchBspzFrame()
        # 5、进入报送参数页签
        self.swithToBscs()
        self.RmbtdBscsFrame()
        # 6、选择征信报送方式--手动报送
        self.setRmbtdBsfs(self.INPUT_ZXBSFS)
        # 7、存储反馈文件的目录
        self.setRmbtdCcfkwjdml("/home/resultFile")
        # 8、文件本地保存根路径
        self.setRmbtdWjbdbcgml("/home/reportFile")
        # 9、sftp服务器ip
        self.setRmbtdsftpip("192.168.20.157")
        # 10、sftp服务器端口
        self.setRmbtdsftpdk("22")
        # 11、sftp用户名
        self.setRmbtdsftpyhm("root")
        # 12、sftp密码
        self.setRmbtdsftpmm("Ninestar1571552")
        # 13、发送目录
        self.setRmbtdfsml("/home/reportFile")
        # 14、数据提供机构区段码
        self.setRmbtdsjtgjgqdm("XA345678901234")
        # 15、人行预处理程序URL
        self.setRmbtdrhyclcxURL("http://192.168.20.157:8089")
        # 16、征信中心代码
        self.setRmbtdzxdm("41494")
        # 17、业务管理机构代码
        self.setRmbtdywgljgdm("123")
        # 18、设置上报审批--否
        self.setRmbtdSbspNo()
        # 19、人工确认成功--是`
        self.setRmbtdrgqrcgYes()
        # 20、保存
        self.save()
        # 14、断言设置成功
        res = self.GetTagText(self.MSG_ADD_RESULT_zx)
        self.assertEqual(res, '保存成功')
        # 15、关闭成功弹窗
        self.successZXClose()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
