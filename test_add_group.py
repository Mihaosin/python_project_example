# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
import unittest
# time, re
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name="third", header = "header", footer = "footer"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group(name = "", header = "", footer = ""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # выход из учетной записи
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_groups_page(self, wd):
        # возврат на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def create_group(self, wd, group):
        # начало создания новой группы
        wd.find_element(by=By.NAME, value="new").click()
        # заполнение атрибутов группы
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys(group.name)
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys(group.header)
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys(group.footer)
        # завершение создания группы
        wd.find_element(by=By.NAME, value="submit").click()

    def open_groups_page(self, wd):
        # переход на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def login(self, wd, username, password):
        # авторизация в учетной записи
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_home_page(self, wd):
        # открытие домашней страницы
        wd.get("http://localhost/addressbook/")

    #    def is_element_present(self, how, what):
#        try:
#            self.wd.find_element(by=how, value=what)
#        except NoSuchElementException as e:
#            return False
#        return True

#   def is_alert_present(self):
#       try:
#          self.wd.switch_to_alert()
#        except NoAlertPresentException as e:
#            return False
#       return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
