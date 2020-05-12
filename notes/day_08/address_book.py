''' Address Book class '''
from contact import Contact


class AddressBook():
    ''' Address Book class '''

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact=Contact()):
        ''' Add a new contact to the address book '''
        #  Make sure that they passed a Contact class
        if not isinstance(contact, Contact):
            print('[ERROR] contact is not a Contact class')
            return

        #  Add the contact to the list of contacts
        self.contacts.append(contact.get())

        # This is just an extra line for fun
        # self.contacts.append('--------------')

    def get(self):
        ''' Return list of contacts '''
        return self.contacts
