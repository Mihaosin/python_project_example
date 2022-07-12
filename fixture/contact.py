from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # начало создания нового контакта
        wd.find_element(by=By.LINK_TEXT, value="add new").click()
        self.fill_contact_form(contact)
        # завершение создания котакта
        wd.find_element(by=By.NAME, value="submit").click()
        # self.return_to_first_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # заполнение свойств котакта
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        self.fill_contact_form(contact)
        # завершение редактирования котакта
        wd.find_element(by=By.NAME, value="update").click()
        # self.return_to_first_page()

    def select_first_contact(self):
        wd = self.app.wd
        # нажимаем кнопку edit для первой строки списка контактов
        wd.find_element(by=By.CSS_SELECTOR, value="img[alt='Edit']").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # нажать на кнопуку "удалить"
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Delete']").click()
        # переключение на всплывающее окно запроса подтверждения удаления при помощи метода вебдрайвера switch_to.alert
#        alert = wd.switch_to.alert
        # подтверждение действия внутри всплывающего окна
#        alert.accept()

    # def return_to_first_page(self):
        # wd = self.app.wd
        # возврат на первую страницу
        # wd.find_element(by=By.LINK_TEXT, value="home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))
