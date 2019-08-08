#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import logging
from time import sleep
from basepages.contact_page import ContactPage
from faker import Faker

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@allure.feature("通讯录Page 新增")
class TestAddMember:
    def setup(self):
        self.contact = ContactPage()
        self.driver = self.contact.auto_driver.driver
        self.fake = Faker(locale='zh_CN')

    def teardown(self):
        sleep(2)
        self.contact.auto_driver.quit_browser()


    @allure.story('添加成员并保存')
    @pytest.mark.skip()
    def test_add_member(self):
        fake_name = self.fake.name()
        fake_id = self.fake.ssn()
        fake_mobile = self.fake.random_int(min=14000000000,max=14099999999)
        fake_email = self.fake.email()
        self.contact.add_member(fake_name,fake_name,fake_id,fake_mobile,fake_email,'杭州','测试工程师')
        sleep(2)
        assert fake_name in self.driver.page_source

    @allure.story('取消添加成员')
    @pytest.mark.skip()
    def test_cancel_add_member(self):
        self.contact.cancel_add_member()
        assert '微信邀请' in self.driver.page_source

    @allure.story('搜索成员')
    @pytest.mark.skip()
    def test_search_member(self):
        self.contact.search_member('Jack')
        assert '禁用' in self.driver.page_source

if __name__ == "__main__":
    pytest.main(['-s', '-q', '--alluredir', '../report/xml'])

