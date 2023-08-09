from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import win32gui
import win32con
import time
from Common.getfiledir import *
from Common.log import mylog
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class WebDriver(object):
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str(time.strftime("%Y-%m-%d %H点%M分%S秒", time.localtime())) + '.png'
        screent_path = os.path.join(SCREENSHOTDIR, pic_name)
        self.driver.get_screenshot_as_file(screent_path)
        return screent_path

    def FindElement(self, loc):
        """单个元素定位方法"""
        base_list = loc.split("$")
        loc_new = base_list[0]
        type = base_list[1]
        try:
            time.sleep(0.5)
            if type.lower() == 'xpath':
                return WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                    lambda x: x.find_element(By.XPATH, loc_new))
            elif type.lower() == 'id':
                return WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                    lambda x: x.find_element(By.ID, loc_new))
            elif type.lower() == 'name':
                return WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                    lambda x: x.find_element(By.NAME, loc_new))
            elif type.lower() == 'class':
                return WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                    lambda x: x.find_element(By.CLASS_NAME, loc_new))
            elif type.lower() == 'css':
                return WebDriverWait(self.driver, timeout=30, poll_frequency=0.5).until(
                    lambda x: x.find_element(By.CSS_SELECTOR, loc_new))
            else:
                return None, "不能识别元素类型:{}".format(type)
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素:【{}】失败，已截图:【{}】'.format(loc, screenshot_path))
            raise Exception

    def FindsElements(self, *loc):
        """多个元素定位方法"""
        try:
            time.sleep(0.5)
            return WebDriverWait(self.driver, 20).until(lambda x: x.find_elements(*loc))
        except Exception:
            raise Exception

    def MouseFouce(self, loc):
        """鼠标悬停"""
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(self.FindElement(loc)).perform()
            time.sleep(0.5)
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def Click(self, loc):
        """元素点击"""
        time.sleep(0.5)
        self.FindElement(loc).click()
        mylog.info('元素【{}】点击成功'.format(loc))

    def DoubleClick(self, loc):
        """元素双击"""
        time.sleep(0.5)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.FindElement(loc)).perform()
        mylog.info('元素【{}】双击成功'.format(loc))

    def Input(self, text, loc):
        """元素输入"""
        time.sleep(0.5)
        self.FindElement(loc).send_keys(text)
        mylog.info('元素【{}】输入【{}】成功'.format(loc, text))

    def SwitchFrame(self, frame_loc):
        """切换frame"""
        try:
            time.sleep(0.5)
            self.driver.switch_to.frame(frame_loc)
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def SwitchFrameByElement(self, loc):
        """切换frame"""
        try:
            time.sleep(0.5)
            frame_ele = self.FindElement(loc)
            self.driver.switch_to.frame(frame_ele)
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def SwitchFatherFrame(self):
        """切换到父级frame"""
        try:
            time.sleep(0.5)
            self.driver.switch_to.parent_frame()
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def QuiteFrame(self):
        """退出frame"""
        try:
            time.sleep(0.5)
            self.driver.switch_to.default_content()
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def ExcuteJs(self, func_js):
        """调用js方法"""
        try:
            time.sleep(0.5)
            self.driver.execute_script(func_js)
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def GotoSleep(self, t=3):
        """强制等待"""
        time.sleep(t)

    def UploadFile(self, file_dir):
        """
        上传文件
        :return:
        """
        time.sleep(1)
        title = "打开"
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        if dialog == 0:
            mylog.error('传入对话框的class定位器有误')
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮

        button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')  # 二级
        if button == 0:
            mylog.error('按钮text属性传值有误')
        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_dir)  # 发送文件路径
        time.sleep(1)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        mylog.info('上传文件成功')

    def GetTagText(self, loc):
        """
        获取元素标签的text值,并返回
        :param loc:
        :return:
        """
        time.sleep(0.5)
        v = self.FindElement(loc).text
        return v

    def GetElementAttrbute(self, loc, key):
        """
        获取元素属性值,并返回
        :param loc:
        :return:
        """
        try:
            time.sleep(0.5)
            v = self.FindElement(loc).get_attribute(key)
            return v
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def RefreshPage(self):
        """刷新页面"""
        try:
            time.sleep(0.5)
            self.driver.refresh()
        except Exception as e:
            mylog.error('错误信息:{}'.format(e))

    def SelectAllData(self, loc):
        """文本框全选数据"""
        try:
            self.FindElement(loc).send_keys(Keys.CONTROL, 'a')
            mylog.info('元素【{}】键盘操作全选成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))

    def ClearData(self, loc):
        """清除文本框数据"""
        try:
            time.sleep(0.5)
            self.FindElement(loc).clear()
            mylog.info('文本框【{}】清除默认数据成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))
        mylog.info('文本框【{}】清除默认数据成功'.format(loc))

    def CutData(self, loc):
        """全选后，剪切文本框数据"""
        try:
            time.sleep(0.5)
            ele = self.FindElement(loc)
            ele.send_keys(Keys.CONTROL, "a")
            ele.send_keys(Keys.CONTROL, 'x')
            time.sleep(0.5)
            mylog.info('文本框【{}】剪切数据成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))
        mylog.info('文本框【{}】剪切数据成功'.format(loc))

    def AllChoiceData(self, loc):
        """全选文本框数据"""
        try:
            time.sleep(0.5)
            ele = self.FindElement(loc)
            ele.send_keys(Keys.CONTROL, 'a')
            time.sleep(0.5)
            mylog.info('文本框【{}】全选数据成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))
        mylog.info('文本框【{}】全选数据成功'.format(loc))

    def PasteData(self, loc):
        """粘贴文本框数据"""
        try:
            time.sleep(0.5)
            ele = self.FindElement(loc)
            ele.send_keys(Keys.CONTROL, 'v')
            time.sleep(0.5)
            mylog.info('文本框【{}】粘贴数据成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))
        mylog.info('文本框【{}】粘贴数据成功'.format(loc))

    def AlertAccept(self):
        """浏览器弹窗确认"""
        try:
            time.sleep(0.5)
            alert = self.driver.switch_to.alert
            alert.accept()
            mylog.info('浏览器弹窗确定成功')
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('浏览器弹窗确定失败,已截图【{}】'.format(screenshot_path))

    def KeyBordDel(self, loc):
        """键盘全选并清理"""
        try:
            time.sleep(0.5)
            ele = self.FindElement(loc)
            ele.send_keys(Keys.CONTROL, "a")
            time.sleep(1)
            ele.send_keys(Keys.DELETE)
            time.sleep(0.5)
            mylog.info('文本框【{}】清除默认数据成功'.format(loc))
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('获取元素【{}】失败,已截图:【{}】'.format(loc, screenshot_path))
        mylog.info('文本框【{}】清除默认数据成功'.format(loc))

    def get_select_values(self, loc):
        """获取下拉列表所有value值"""
        try:
            time.sleep(0.5)
            ele = self.FindElement(loc)
            selector = Select(ele)
            options = selector.options
            options_list = []
            for s in options:
                options_list.append(s.text)
            return options_list
        except NoSuchElementException as e:
            mylog.error('错误信息:{}'.format(e.args[0]))

    def get_window_handle(self):
        """获取所有窗口句柄，切换到浏览器第二个窗口句柄"""
        try:
            time.sleep(0.5)
            window_handles = self.driver.window_handles  # 获取所有窗口句柄
            self.driver.switch_to.window(window_handles[1])  # 获取list里面第二个窗口直接切换
            mylog.info('浏览器切换第二个窗口句柄权利成功')
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            mylog.error('浏览器切换第二个窗口句柄失败,已截图【{}】'.format(screenshot_path))

    def GetNowHandle(self):
        """获取当前窗口句柄"""
        current_handle = self.driver.current_window_handle
        return current_handle

    def GetAllHandle(self):
        """获取所有窗口句柄"""
        all_handle = self.driver.window_handles
        return all_handle

    def SwitchHandle(self, handle):
        """切换窗口句柄"""
        self.driver.switch_to.window(handle)
