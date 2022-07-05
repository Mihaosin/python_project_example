from model.group import Group

def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="new_name"))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header="new_header"))
    app.session.logout()

def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer="new_footer"))
    app.session.logout()