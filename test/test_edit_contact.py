from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pasha"))
    app.contact.edit_first(Contact(firstname="Petya", lastname="Sidorov", address="California", email="email@adress.book"))


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pasha"))
    app.contact.edit_first(Contact(firstname="New_Vasia"))


def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pasha"))
    app.contact.edit_first(Contact(lastname="New_Petrov"))


def test_edit_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pasha"))
    app.contact.edit_first(Contact(address="New_York"))


def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pasha"))
    app.contact.edit_first(Contact(email="new@adress.book"))
