from model.contact import Contact
import random
import time


def test_delete_random_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pasha"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    # задержка в выполнении программы перед считыванием списка контактов из БД после удаления одного
    time.sleep(1)
    # возможно считывание контактов из БД происходит быстрее, чем обновление БД по операции удаления
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
