# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from model.group import Group
import  pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*2
    # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
            Group(name=random_string("name"+str(i), 10), header=random_string("header", 10), footer=random_string("footer", 10))
            for i in range(5)
]

# тест будет падать, если в имени группы будут присутствовать "'", "\" или более чем один пробел подряд или пробел в конце имени
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # готовим old_groups и new_groups к сравнению по элементам
    # new_groups = sorted(new_groups, key= lambda group: int(group.id))
    # new_groups[len(new_groups)-1:len(new_groups)] = []
    # old_groups = sorted(old_groups, key=lambda group: int(group.id))
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
