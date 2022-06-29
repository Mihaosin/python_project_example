# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Vasia", lastname="Petrov", address="Texas", email="perov@adress.book"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", address="", email=""))
    app.logout()
