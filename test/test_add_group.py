# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="third", header="header", footer="footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
