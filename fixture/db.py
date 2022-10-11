import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self. user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address, home, mobile, work, fax, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, homephone, mobilephone, workphone, faxphone, mail1, mail2, mail3) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname, address=address,
                       mail1=mail1, mail2=mail2, mail3=mail3,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, faxphone=faxphone))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self, group):
        contacts_id = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id = %s" % group.id)
            for row in cursor:
                (id) = row
                contacts_id.append(str(list(id)[0]))
            contacts = []
            if len(contacts_id) > 0:
                cursor.execute("select id, lastname, firstname from addressbook where id in (" + ','.join(contacts_id) + ")")
                for row in cursor:
                    (id, lastname, firstname) = row
                    contacts.append(Contact(id=str(id), lastname=lastname, firstname=firstname))
        finally:
            cursor.close()
        return contacts


    def destroy(self):
        self.connection.close()