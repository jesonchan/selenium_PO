# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import sys
import time


class AutomateDriver:

    def __init__(self):
        driver = webdriver.Chrome()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Driver Not Found!")

    def clear_cookies(self):
        """
        clear all cookies
        """
        self.driver.delete_all_cookies()

    def refresh_browser(self):
        self.driver.refresh()

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close_browser(self):
        self.driver.close()

    def find_element(self, locator, value=None):
        """
        重封装的find方法，接受元祖类型的参数，默认等待元素5秒，寻找失败时自动截图
        :param locator:元组类型,必须是(By.NAME, 'username')这样的结构
        :return:元素对象web element
        """
        try:
            if value is None:
                web_element = WebDriverWait(
                    self.driver, 5).until(
                    expected_conditions.visibility_of_any_elements_located(
                        *locator))
                return web_element
            else:
                web_element = WebDriverWait(
                    self.driver, 5).until(
                    expected_conditions.visibility_of_any_elements_located(
                        locator, value))
                return web_element

        except (TimeoutException, NoSuchElementException) as e:
            # 寻找失败时自动截图，截图名称为 时间戳 + png后缀
            self.driver.get_screenshot_as_file(
                sys._getframe(1).f_code.co_name +
                time.strftime(
                    time.localtime(
                        time.time())) +".png")

    def click_by_js(self, by, locator):
        WebDriverWait(
            self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (by, locator)))
        self.driver.execute_script(
            "arguments[0].click();",
            self.driver.find_element(
                by,
                locator))

    def getTitle(self):
        '''
        Get window title
        '''
        return self.driver.title

    def get_current_url(self):
        """
        Get the URL of current page
        """
        return self.driver.current_url

    def accept_alert(self):
        '''
        Accept warning box
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available
        '''
        self.driver.switch_to.alert.dismiss()

    def open_new_window(self, selector):
        '''
        Open the new window and switch the handle to the newly opened window
        '''
        original_windows = self.driver.current_window_handle
        el = self.find_element(selector)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)


