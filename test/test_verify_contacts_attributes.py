import re
from random import randrange
from model.contact import Contact


def test_verify_contacts_attributes_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for index in range(0, len(contacts_from_home_page)-1):
        contact_from_home_page = contacts_from_home_page[index]
        contact_from_db = contacts_from_db[index]
        assert contact_from_home_page.id == contact_from_db.id
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_mails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    # сравниваем все номера телефона, кроме факса, так как факс на главной странице не отображается
    s1 = filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone])
    s2 = map(lambda x: clear(x), s1)
    s3 = filter(lambda x: x !='', s2)
    s4 = "\n".join(s3)
    return s4


def merge_emails_like_on_home_page(contact):
    s1 = filter(lambda x: x is not None, [contact.mail1, contact.mail2, contact.mail3])
    s2 = s1 #map(lambda x: clear(x), s1) не чистим e-mail
    s3 = filter(lambda x: x !='', s2)
    s4 = "\n".join(s3)
    return s4


# def merge_emails_like_on_home_page(contact):
#     return "\n".join(filter(lambda x: x !='',
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [contact.email1, contact.email2, contact.email3]))))
