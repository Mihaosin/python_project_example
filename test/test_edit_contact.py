from model.contact import Contact
from random import randrange
import random


# def test_edit_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(firstname="Petya", lastname="Sidorov", address="California", email="email@adress.book"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#

def test_edit_random_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="Pasha"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = "New_Vasia"
    app.contact.edit_by_id(contact)
    new_contacts = db.get_contact_list()
    for i in (0, len(old_contacts)-1):
        if old_contacts[i].id == contact.id:
            old_contacts[i].firstname = "New_Vasia"
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_edit_random_contact_firstname(app, db):
#     if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = db.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="New_Vasia")
#     contact.id = old_contacts[index].id
#     contact.lastname = old_contacts[index].lastname
#     app.contact.edit_by_index(index, contact)
#     new_contacts = db.get_contact_list()
#     for i in (0, len(old_contacts)-1):
#         if old_contacts[i].id == contact.id:
#             old_contacts[i].firstname = "New_Vasia"
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
# def test_edit_first_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(lastname="New_Petrov"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_first_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(address="New_York"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_first_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(email="new@adress.book"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
