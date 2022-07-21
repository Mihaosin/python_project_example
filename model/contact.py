from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.id = id

    def __eq__(self, other):
        EQ1 = self.id is None or other.id is None or self.id == other.id
        EQ2 = self.firstname == other.firstname
        EQ3 = self.lastname == other.lastname
        return EQ1 and EQ2 and EQ3

    def id_or_max(self):
        if self.id:
            return  int(self.id)
        else:
            return maxsize

# 8 passed, 16 warnings in 30.57s