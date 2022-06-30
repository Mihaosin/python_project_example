from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def create(self, group):
        wd = self.app.wd
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

    def edit_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # выбрать первую группу (чек-бокс)
        wd.find_element(by=By.NAME, value="selected[]").click()
        wd.find_element(by=By.NAME, value="edit").click()
        # изменить содержимое полей - name, header, footer
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys(group.name)
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys(group.header)
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys(group.footer)
        # нажать на кнопку подтвердить изменения
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        # выбрать первую группу (чек-бокс)
        wd.find_element(by=By.NAME, value="selected[]").click()
        # нажать на кнопуку "удалить группу"
        wd.find_element(by=By.NAME, value="delete").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        # переход на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # возврат на страницу "Группы"
        wd.find_element(by=By.LINK_TEXT, value="groups").click()
