from model.contact import Contact
from data.add_group import random_string


constant = [
    Contact(firstname="firstname1", lastname="lastname1"),
    Contact(firstname="firstname2", lastname="lastname2"),
]


testdata = [Contact(firstname="", lastname="")] + [
            Contact(firstname=random_string("firstname"+str(i), 10), lastname=random_string("lastname", 20))
            for i in range(5)
]