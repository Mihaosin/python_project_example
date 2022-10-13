from model.group import Group
from model.contact import Contact
from generator.contact import random_string

def test_add_contact_to_group(app, db):
    # блок предусловий
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pasha"))

    # блок поиска подходящего контакта и группы
    proper_contact_and_group = find_proper_contact_and_group(app, db)
    contact = proper_contact_and_group['contact']
    group = proper_contact_and_group['group']

    # блок получения old_contacts в выбранной группе
    old_contacts_in_group = db.get_contacts_in_group(group)
    # блок модификации
    app.contact.add_contact_to_group(contact, group)
    # блок получения new_contacts и редактирования old_contacts в выбранной группе
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    # блок проверок
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


def find_proper_contact_and_group(app, db):
    # ищем контакт, который не входит хотя бы в одну группу; запоминаем контакт и группу
    # если такого контакта нет, создаем новый контакт
    found = False
    while not found:
        all_contacts = db.get_contact_list()
        all_groups = db.get_group_list()
        contact_index = 0
        while (not found) and (contact_index <= len(all_contacts) - 1):
            contact = all_contacts[contact_index]
            group_index = 0
            while (not found) and (group_index <= len(all_groups) - 1):
                group = all_groups[group_index]
                if contact not in db.get_contacts_in_group(group):
                    found = True
                group_index += 1
            contact_index += 1
        if found == False:
            contact = Contact(firstname=random_string("", 8))
            app.contact.create(contact)
    # конец болка поиска подходящих контакта и группы
    return {'contact': contact, 'group': group}