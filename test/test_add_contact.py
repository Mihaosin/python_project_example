# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Vasia", lastname="Petrov", address="Texas", email="perov@adress.book"))
    app.session.logout()


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", email=""))
