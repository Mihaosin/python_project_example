from model.group import Group

def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="new_name"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="new_header"))


def test_edit_first_group_footer(app):
    app.group.edit_first(Group(footer="new_footer"))
