#!/usr/bin/env python
# coding=utf-8
import logging
from time import sleep
from selenium.webdriver.common.by import By
from basepages.login_page import Wework


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class ContactPage(Wework):
    _username = (By.NAME, "username")
    _alias = (By.NAME, "english_name")
    _id = (By.NAME, "acctid")
    _mobile = (By.NAME, "mobile")
    _email = (By.CSS_SELECTOR, "#memberAdd_mail")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.XPATH, "//*[text()='离开此页']")
    _search = (By.ID, "memberSearchInput")
    _add = (By.CSS_SELECTOR, '.js_add_member')
    _city = (By.CSS_SELECTOR, '#memberEdit_address')
    _title = (By.CSS_SELECTOR, '#memberAdd_title')
    _save = (By.XPATH, '//a[text()="保存"]')
    _sendInvite =(By.NAME,'sendInvite')

    def __init__(self):
        Wework.__init__(self)
        URL = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.open_url(URL)
        sleep(1)

    def add_member(
            self,
            name,
            alias,
            id,
            mobile,
            email,
            city,
            title,
            **kwargs):
        self.auto_driver.click_by_js(self._add)
        logging.info("click add member success")
        self.auto_driver.find_element(self._username).send_keys(name)  # 姓名
        self.auto_driver.find_element(self._alias).send_keys(alias)  # 别名
        self.auto_driver.find_element(self._id).send_keys(id)  # id
        self.auto_driver.find_element(self._mobile).send_keys(mobile)  # 手机
        self.auto_driver.find_element(self._email).send_keys(email)  # 邮箱
        self.auto_driver.find_element(self._city).send_keys(city)  # 地址
        self.auto_driver.find_element(self._title).send_keys(title)  # 职务
        self.auto_driver.find_element(self._sendInvite).click()
        self.auto_driver.find_element(self._save).click()  # 保存
        logging.info('save success')

    def cancel_add_member(self):
        self.auto_driver.click_by_js(self._add)
        logging.info("click add member success")
        self.auto_driver.click_by_js(self._cancel)  # 取消
        logging.info("cancel success")

    def delete_member(self):
        pass

    def search_member(self, key):
        self.auto_driver.find_element(self._search).send_keys(key)


if __name__ == "__main__":
    contact = ContactPage()
    # contact.cancel_add_member()
    fake_name = 'Jack'
    fake_id = '1231231142112312'
    fake_mobile = '14000000001'
    fake_email = '12345abc@126.com'
    contact.add_member(fake_name, fake_name, fake_id, fake_mobile, fake_email, '杭州', '测试工程师')
