from model.group import Group
import random


def test_edit_group_name_by_id(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "new_name"
    app.group.edit_by_id(group)
    new_groups = db.get_group_list()
    for i in (0, len(old_groups)-1):
        if old_groups[i].id == group.id:
            old_groups[i].name = "new_name"
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Sasha", footer="Masha"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header="new_header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Sasha", footer="Masha"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(footer="new_footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
