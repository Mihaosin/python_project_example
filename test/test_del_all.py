

def test_dell_all(app):
    # len_contacts = len(app.contact.get_contact_list())
    # for i in range(0, len_contacts):
    #     app.contact.delete_by_index(0)
    app.contact.erase_contats()
    # len_groups = len(app.group.get_group_list())
    # for i in range(0, len_groups):
    #     app.group.delete_by_index(0)
    app.group.erase_groups()
