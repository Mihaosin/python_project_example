from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def return_to_first_page(self):
        wd = self.wd
        # возврат на первую страницу
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def create_contact(self, contact):
        wd = self.wd
        # начало создания нового контакта
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        # заполнение свойств котакта
        wd.find_element(by=By.NAME, value="firstname").click()
        wd.find_element(by=By.NAME, value="firstname").clear()
        wd.find_element(by=By.NAME, value="firstname").send_keys(contact.firstname)
        wd.find_element(by=By.NAME, value="lastname").click()
        wd.find_element(by=By.NAME, value="lastname").clear()
        wd.find_element(by=By.NAME, value="lastname").send_keys(contact.lastname)
        wd.find_element(by=By.NAME, value="address").click()
        wd.find_element(by=By.NAME, value="address").clear()
        wd.find_element(by=By.NAME, value="address").send_keys(contact.address)
        wd.find_element(by=By.NAME, value="email").click()
        wd.find_element(by=By.NAME, value="email").clear()
        wd.find_element(by=By.NAME, value="email").send_keys(contact.email)
        # завершение создания котакта
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_first_page()

    def open_home_page(self):
        wd = self.wd
        # открытие домашней страницы
        wd.get("http://localhost/addressbook/")

    def return_to_groups_page(self):
        wd = self.wd
        # возврат на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def create_group(self, group):
        wd = self.wd
        # начало создания новой группы
        self.open_groups_page()
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
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        # переход на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def destroy(self):
        self.wd.quit()
