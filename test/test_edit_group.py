from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    app.group.edit_first(Group(name="new_name"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    app.group.edit_first(Group(header="new_header"))


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    app.group.edit_first(Group(footer="new_footer"))
