# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
import unittest
from contact import Contact
from application import Application


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Vasia", lastname="Petrov", address="Texas", email="perov@adress.book"))
        # тест добавления пустого контакта
        # self.create_contact(wd, Contact(firstname="", lastname="", address="", email=""))
        self.app.logout()

    def test_add_empty_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="", lastname="", address="", email=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
