from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def return_to_first_page(self):
        wd = self.app.wd
        # возврат на первую страницу
        wd.find_element(by=By.LINK_TEXT, value="home").click()

    def create(self, contact):
        wd = self.app.wd
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