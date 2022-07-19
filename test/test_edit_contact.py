from model.contact import Contact


# def test_edit_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Pasha"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(firstname="Petya", lastname="Sidorov", address="California", email="email@adress.book"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="Pasha"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_Vasia")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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
