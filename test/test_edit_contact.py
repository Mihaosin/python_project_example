from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="New_Vasia", lastname="New_Petrov", address="New_York", email="new@adress.book"))
    app.session.logout()
