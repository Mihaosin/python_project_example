from model.group import Group
from model.contact import Contact
import random

def test_add_contact_to_group(app, db):
    # блок предусловий
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Sasha", footer="Masha"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pasha"))
    # блок выбора добавляемого контакта
    all_contacts = db.get_contact_list()
    contact = random.choice(all_contacts)
    # блок выбора модифицируемой группы
    all_groups = db.get_group_list()
    group = random.choice(all_groups)
    # блок получения old_contacts в группе
    old_contacts_in_group = db.get_contacts_in_group(group)
    # блок модификации
    app.contact.add_contact_to_group(contact, group)
    # блок получения new_contacts и редактирования old_contacts в группе
    new_contacts_in_group = db.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)
    # блок проверок
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)