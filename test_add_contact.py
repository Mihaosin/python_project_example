# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, firstname="Vasia", lastname="Petrov", address="Texas", email="perov@adress.book")
        self.return_to_first_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # выход из учетной записи
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_first_page(self, wd):
        # возврат на первую страницу
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def create_contact(self, wd, firstname, lastname, address, email):
        # начало создания нового контакта
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        # заполнение свойств котакта
        wd.find_element(by=By.NAME, value="firstname").click()
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys(firstname)
        wd.find_element(by=By.NAME, value="lastname").click()
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys(lastname)
        wd.find_element(by=By.NAME, value="address").click()
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys(address)
        wd.find_element(by=By.NAME, value="email").click()
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys(email)
        # завершение создания котакта
        wd.find_element(by=By.NAME, value="submit").click()

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

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
