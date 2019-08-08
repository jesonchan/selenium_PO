#!/usr/bin/env python
# coding=utf-8
import logging
from time import sleep
from selenium.webdriver.common.by import By
from basepages.login_page import Wework
from basepages.contact_page import ContactPage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ProfilePage(ContactPage):
    _edit = (By.CSS_SELECTOR, ".ww_operationBar .js_edit")
    _save = (By.CSS_SELECTOR, ".js_save")
    _disable = (By.CSS_SELECTOR, '.ww_operationBar .js_disable')
    _enable = (By.XPATH, '//a[text()="启用"]')
    _submit = (By.XPATH, '//a[text()="确认"]')
    _alias = (By.NAME, "english_name")
    _leave = (By.XPATH, "//*[text()='离开此页']")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")

    def __init__(self):
        ContactPage.__init__(self)

    def update(self, **kwargs):
        self.auto_driver.click_by_js(self._edit)
        element = self.auto_driver.find_element(self._alias)
        element.clear()
        element.send_keys(kwargs["name"])
        sleep(1)
        self.auto_driver.click_by_js(self._save)

    def disable(self):
        self.auto_driver.click_by_js(self._disable)
        sleep(1)
        self.auto_driver.find_element(self._submit).click()

    def enable(self):
        self.auto_driver.find_element(self._enable).click()
        sleep(1)

    def leave_without_save(self):
        element = self.auto_driver.find_element(self._alias)
        element.clear()
        element.send_keys("little sheep")
        self.auto_driver.click_by_js(self._cancel)  # 取消
        self.auto_driver.find_element(self._leave).click()  # 资料未存储确认离开
        logging.info("edit file and leave without save")

    def delete(self):
        pass

if __name__ == '__main__':
    profile = ProfilePage()
    profile.search_member("jack")
    profile.update(name = 'little sheep')
    # profile.disable()


