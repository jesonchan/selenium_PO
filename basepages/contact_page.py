#!/usr/bin/env python
# coding=utf-8
import logging
from time import sleep
from selenium.webdriver.common.by import By
from util.AutoDriver import AutomateDriver
from basepages.login_page import Wework


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ContactPage():
    _username=(By.NAME, "username")
    _alias=(By.NAME, "english_name")
    _id=(By.NAME, "acctid")
    _mobile=(By.NAME, "mobile")
    _email =(By.CSS_SELECTOR,"#memberAdd_mail")
    _cancel=(By.CSS_SELECTOR, ".js_btn_cancel")
    _leave=(By.XPATH, "//*[text()='离开此页']")
    _search=(By.ID, "memberSearchInput")
    _add =(By.CSS_SELECTOR, ".js_has_member .ww_operationBar .js_add_member")

    def __init__(self):
        self.auto_driver = AutomateDriver()
        self.driver = self.auto_driver.driver
        self.we_work = Wework()
        self.we_work.login()

    def add_member(self, name, alias, id, mobile,email, **kwargs):
        self.driver.get(
            'https://work.weixin.qq.com/wework_admin/frame#contacts')
        sleep(1)

        ele_add = self.driver.find_element(
            By.CSS_SELECTOR, '.js_add_member')
        self.driver.execute_script("arguments[0].click();", ele_add)
        logging.info('点击添加成员操作成功')
        self.driver.find_element(self._username).send_keys(name)  # 姓名
        self.driver.find_element(self._alias).send_keys(alias)  # 别名
        self.driver.find_element(self._id).send_keys(id)  # id
        self.driver.find_element(self._mobile).send_keys(mobile)  # 手机
        self.driver.find_element(self._email).send_keys(email)  # 邮箱
        self.driver.find_element(
            By.CSS_SELECTOR,
            '#memberEdit_address').send_keys('杭州市')  # 地址
        self.driver.find_element(
            By.CSS_SELECTOR,
            '#memberAdd_title').send_keys('测试工程师')  # 职务
        self.driver.find_element(
            By.XPATH, '//a[text()="保存"]').click()  # 保存

# if __name__ == "__main__":

