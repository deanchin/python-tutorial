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
        # self.contacts.append(contact.get())
        self.contacts.append(contact)

    def delete_contact(self, name):
        ''' delete contact '''
        original = self.get_by_name(name)
        self.contacts.remove(original)

    def get(self):
        ''' Return list of contacts '''
        return self.contacts

    def get_by_name(self, name):
        ''' Return list of contacts '''
        for contact in self.contacts:
            if contact.get_name().lower() == name.lower():
                return contact
        return None

    def display(self):
        ''' Print contacts from address book '''
        for contact in self.contacts:
            contact.display()
