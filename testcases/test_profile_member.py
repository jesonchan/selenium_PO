#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import logging
from time import sleep
from basepages.profile_page import ProfilePage
from faker import Faker

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@allure.feature("搜索结果页Profile 编辑 禁用 启动")
class TestProfileMember:
    def setup(self):
        self.profile = ProfilePage()
        self.driver = self.profile.auto_driver.driver
        self.fake = Faker(locale='zh_CN')

    def teardown(self):
        sleep(2)
        self.profile.auto_driver.quit_browser()

    @allure.story('编辑用户并更新保存')
    def test_search_member(self):
        self.profile.search_member('Jack')
        fake_alias = self.fake.name()
        sleep(1)
        self.profile.update(name = fake_alias)
        assert fake_alias in self.driver.page_source

    @allure.story('禁用用户')
    def test_search_member(self):
        self.profile.search_member('Jack')
        self.profile.disable()
        assert '启用' in self.driver.page_source

    @allure.story('启用用户')
    def test_search_member(self):
        self.profile.search_member('Jack')
        self.profile.enable()
        assert '禁用' in self.driver.page_source

if __name__ == "__main__":
    pytest.main(['test_profile_member.py'])

