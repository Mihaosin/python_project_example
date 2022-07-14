# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="third", header="header", footer="footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    # готовим old_groups и new_groups к сравнению по элементам
    new_groups = sorted(new_groups, key= lambda group: int(group.id))
    new_groups[len(new_groups)-1:len(new_groups)] = []
    old_groups = sorted(old_groups, key=lambda group: int(group.id))
    assert old_groups == new_groups



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    # готовим old_groups и new_groups к сравнению по элементам
    new_groups = sorted(new_groups, key=lambda group: int(group.id))
    new_groups[len(new_groups) - 1:len(new_groups)] = []
    old_groups = sorted(old_groups, key=lambda group: int(group.id))
    assert old_groups == new_groups
