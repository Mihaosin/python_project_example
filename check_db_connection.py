import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_in_group(Group(id="274"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
