import re
from random import randrange


def test_contact_attributes_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_mails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


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
