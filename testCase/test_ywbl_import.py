from baseOperation.init_cls import *
from pageKeyword.keyword_ywbl import *
from utils.operationXml import *
import sys
from baseOperation.init_self import *


class YwblImportTest(InitCls, YwblKeyword, OperationXml):

    def test_01_import_kjkm(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：会计科目'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CWXX)
        self.choiceYwmx(self.YWMX_KJKM)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_KJKM)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_02_import_fzhsx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：辅助核算项'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CWXX)
        self.choiceYwmx(self.YWMX_FZHSX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_FZHSX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_03_import_ftpdj(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：FTP定价变动明细'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CWXX)
        self.choiceYwmx(self.YWMX_FTPDJBDMX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_FTPDJBDMX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_04_import_qykh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：企业客户'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_QYKH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_QYKH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_05_import_jrjg(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：金融机构'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_JRJG)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_JRJG)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_06_import_nbzh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：内部账户'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_NBZH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_NBZH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_07_import_grkh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：个人客户'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_GRKH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_GRKH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_08_import_yhzh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：银行账户'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_YHZH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_YHZH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_09_import_dbrxx_zzjg(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：担保人信息（组织机构）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_DBRXXZZJG)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DBRXXZZJG)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_10_import_ygxx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：员工信息'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_YGXX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_YGXX)
        # 5、校验数据
        self.checkData()
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_11_import_hl(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：汇率'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_HL)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_HL)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllDataForHl()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_12_import_jzll(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：基准利率'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_JZLL)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_JZLL)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_13_import_dbrxx_zrr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：担保人信息（自然人）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_DBRXXZRR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DBRXXZRR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_14_import_jtzh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：集团账户'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_JCXX)
        self.choiceYwmx(self.YWMX_JTZHXX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_JTZHXX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_15_import_hqck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：活期存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_HQCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_HQCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_16_import_dqck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：定期存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_DQCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DQCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_17_import_tzck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：通知存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_TZCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TZCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_18_import_xyck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：协议存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_XYCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_XYCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_19_import_bzjck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：保证金存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_BZJCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_BZJCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_20_import_ckzbj(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：存款准备金'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_CKZBJ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_CKZBJ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_21_import_wtck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：委托存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_CKYW)
        self.choiceYwmx(self.YWMX_WTCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_WTCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_22_import_ldzjdk(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：流动资金贷款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_LDZJDK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_LDZJDK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_23_import_xmdk(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：项目贷款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_XMDK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_XMDK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_24_import_xypj_dw(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：信用评级（单位）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_XYPJ_DW)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_XYPJ_DW)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_25_import_zrr_rzzl(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：自然人融资租赁'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_RZZL_ZRR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_RZZL_ZRR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_26_import_zrr_xfxd(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：自然人消费信贷'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_ZRRXFXD)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZRRXFXD)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_27_import_rzdb(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：融资担保'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_RZDB)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_RZDB)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_28_import_sx_zrr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：授信（自然人）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_SX_ZRR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_SX_ZRR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_29_import_xypj_zrr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：信用评级（自然人）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_XYPJ_ZRR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_XYPJ_ZRR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_30_import_cydw_cprzzl_zrr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：成员单位产品融资租赁（自然人）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_CYDWCPDRZZL_ZRR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_CYDWCPDRZZL_ZRR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_31_import_frzhtz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：法人账户透支'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_FRZHTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_FRZHTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_32_import_gdzcdk(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：固定资产贷款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_GDZCDK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_GDZCDK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_33_import_bgdk(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：并购贷款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_BGDK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_BGDK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_34_import_dw_rzzl(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：单位融资租赁'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_DW_RZZL)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DW_RZZL)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_35_import_bl(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：保理'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_BL)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_BL)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_36_import_mfxd(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：买方信贷'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_MFXD)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_MFXD)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_37_import_bh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：保函'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_BH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_BH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_38_import_dbht(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：担保合同'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_DBHT)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DBHT)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_39_import_sx_dw(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：授信（单位）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_SX_DW)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_SX_DW)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_40_import_frxfxd(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：法人消费信贷'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_FRXFXD)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_FRXFXD)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_41_import_cydw_cprzzl_fr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：成员单位产品融资租赁（法人）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_CYDWCPDRZZL_FR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_CYDWCPDRZZL_FR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_42_import_myrz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：贸易融资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_DKYW)
        self.choiceYwmx(self.YWMX_MYRZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_MYRZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_43_import_tysx_hd(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业授信（获得）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYSXHD)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYSXHD)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_44_import_tysx_sy(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业授信（授予）'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYSXSY)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYSXSY)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_45_import_tykh_xypj(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业客户信用评级'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYKHXYPJ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYKHXYPJ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_46_import_tyjr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业借入'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYJR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYJR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_47_import_tyjc(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业借出'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYJC)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYJC)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_48_import_tycf(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业存放'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYCF)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYCF)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_49_import_tycr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业拆入'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYCR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYCR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_50_import_tycc(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业拆出'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_TYCC)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYCC)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_51_import_cfty(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：存放同业'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TYYW)
        self.choiceYwmx(self.YWMX_CFTY)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_CFTY)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_52_import_zqtz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：债券投资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_ZQTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZQTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_53_import_zqhg(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：债券回购'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_ZQHG)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZQHG)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_54_import_qytz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：权益投资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_QYTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_QYTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_55_import_gmjj(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：公募基金'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_GMJJTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_GMJJTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_56_import_smjj(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：私募基金'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_SMJJTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_SMJJTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_57_import_zgcp(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：资管产品'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_ZGCP)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZGCP)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_58_import_jgxck(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：结构性存款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_JGXCK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_JGXCK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_59_import_tycdtz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业存单投资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_TYCDTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYCDTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_60_import_bblc(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：保本理财'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_TZYW)
        self.choiceYwmx(self.YWMX_BBLC)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_BBLC)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_61_import_xdzczr(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：信贷资产转让'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_RZYW)
        self.choiceYwmx(self.YWMX_XDZCZR)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_XDZCZR)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_62_import_zqfx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：债券发行'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_RZYW)
        self.choiceYwmx(self.YWMX_ZQFX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZQFX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_63_import_tycdrz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：同业存单融资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_RZYW)
        self.choiceYwmx(self.YWMX_TYCDRZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TYCDRZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_64_import_wh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：外汇'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_WHYW)
        self.choiceYwmx(self.YWMX_WH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_WH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_65_import_jsh(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：结售汇'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_WHYW)
        self.choiceYwmx(self.YWMX_JSH)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_JSH)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_66_import_wtdk(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：委托贷款'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_WTDLYW)
        self.choiceYwmx(self.YWMX_WTDK)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_WTDK)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_67_import_dldx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：代理代销'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_WTDLYW)
        self.choiceYwmx(self.YWMX_DLDX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_DLDX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_68_import_wttz(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：委托投资'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_WTDLYW)
        self.choiceYwmx(self.YWMX_WTTZ)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_WTTZ)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_69_import_pjjbxx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：票据基本信息'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_PJYW)
        self.choiceYwmx(self.YWMX_PJJBXX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_PJJBXX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_70_import_tx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：贴现'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_PJYW)
        self.choiceYwmx(self.YWMX_TX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_TX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_71_import_zhuantx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：转贴现'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_PJYW)
        self.choiceYwmx(self.YWMX_ZHUANTX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZHUANTX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_72_import_zaitx(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：再贴现'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_PJYW)
        self.choiceYwmx(self.YWMX_ZAITX)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_ZAITX)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))

    def test_73_import_pjcd(self):
        mylog.info('\n************开始执行案例：【{}】************'.format(sys._getframe().f_code.co_name))
        commit_date = self.getXmlData('ywbl.xml', 'commitDate')
        '''补录模型导入：票据承兑'''
        # 1、登录(已在Init类中进行了登录，无需在案例中再次进行登录)
        # 2、进入补录主界面
        self.intoMainMenu()
        self.switchMainFrame()
        # 3、选择业务模型
        self.choiceYwlx(self.YWLX_PJYW)
        self.choiceYwmx(self.YWMX_PJCD)
        self.ywblRefresh()
        # 4、导入数据
        self.importData(self.FILE_PATH_PJCD)
        # 5、校验数据
        self.checkData()
        # self.GotoSleep(5)
        # 切换到补录主框架
        self.switchMainFrame()
        # 提交全部
        self.commitAllData(commit_date)
        # 关闭调度任务进度弹窗
        self.GotoSleep(3)
        self.closeProcessAlert()
        mylog.info('\n************案例：【{}】执行结束************'.format(sys._getframe().f_code.co_name))
