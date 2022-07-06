from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Petya", lastname="Sidorov", address="California", email="email@adress.book"))
    app.session.logout()


def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="New_Vasia"))
    app.session.logout()


def test_edit_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(lastname="New_Petrov"))
    app.session.logout()


def test_edit_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(address="New_York"))
    app.session.logout()


def test_edit_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(email="new@adress.book"))
    app.session.logout()