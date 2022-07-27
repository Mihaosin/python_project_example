from selenium.webdriver.common.by import By
from model.contact import Contact


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
        self.contact_cache = None

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
        self.edit_by_index(0, contact)

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(contact)
        # завершение редактирования котакта
        wd.find_element(by=By.NAME, value="update").click()
        # self.return_to_first_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # нажимаем кнопку edit для заданной по индексу строки из списка контактов
        wd.find_elements(by=By.CSS_SELECTOR, value="img[alt='Edit']")[index].click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # нажать на кнопуку "удалить"
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Delete']").click()
        self.contact_cache = None
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

    contact_cache = None

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.app.open_home_page()
    #         self.contact_cache = []
    #         # records = wd.find_elements(by=By.CSS_SELECTOR, value="tr")
    #         for element in wd.find_elements(by=By.CSS_SELECTOR, value="tr"):
    #             fields = element.find_elements(by=By.CSS_SELECTOR, value="td")
    #             if len(fields) > 1:
    #                 id = fields[0].find_element(by=By.NAME, value="selected[]").get_attribute("value")
    #                 # last_name = fields[1].text
    #                 # first_name = fields[2].text
    #                 self.contact_cache.append(Contact(firstname=fields[2].text, lastname=fields[1].text, id=id))
    #     return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements(by=By.NAME, value="entry"):
                cells = row.find_elements(by=By.TAG_NAME, value="td")
                id = cells[index_id].find_element(by=By.NAME, value="selected[]").get_attribute("value")
                lastname = cells[index_lastname].text
                firstname = cells[index_firstname].text
                all_phones = cells[index_phones].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="td")[index_edit_button]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="td")[index_view_button]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(by=By.NAME, value="firstname").get_attribute("value")
        lastname = wd.find_element(by=By.NAME, value="lastname").get_attribute("value")
        id = wd.find_element(by=By.NAME, value="id").get_attribute("value")
        homephone = wd.find_element(by=By.NAME, value="home").get_attribute("value")
        mobilephone = wd.find_element(by=By.NAME, value="mobile").get_attribute("value")
        workphone = wd.find_element(by=By.NAME, value="work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone)

# структура таблица контактов в HTML-коде главной страницы
index_id = 0
index_lastname = 1
index_firstname = 2
index_adress = 3
index_emails = 4
index_phones = 5
index_view_button = 6
index_edit_button = 7
index_save_contact_button = 8
