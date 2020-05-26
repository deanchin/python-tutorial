''' Contact class '''
from address import Address


class Contact():
    ''' Contact class '''

    def __init__(self,
                 name='UNDEFINED',
                 home_phone='UNDEFINED',
                 home_address=None,
                 work_phone='UNDEFINED',
                 work_address=None):

        # Check if home address is a valid address
        if home_address and not isinstance(home_address, Address):
            print('[ERROR] home_address is not a Address class')
            return

        # Check if work address is a valid address
        if work_address and not isinstance(work_address, Address):
            print('[ERROR] work_address is not a Address class')
            return

        # Set class variables
        self.name = name
        self.home_phone = home_phone
        self.home_address = home_address
        self.work_address = work_address
        self.work_phone = work_phone

    def get(self):
        ''' Return contact '''
        contact = {
            'name': self.name,
            'home_phone': self.home_phone,
            'work_phone': self.work_phone
        }
        if self.home_address:
            contact['home_address'] = self.home_address.get()
        if self.work_address:
            contact['work_address'] = self.work_address.get()

        return contact

    def get_name(self):
        ''' return contact name '''
        return self.name

    def set_home_address(self, address):
        ''' Set the work address for the contact '''
        self.home_address = address

    def set_work_address(self, address):
        ''' Set the work address for the contact '''
        self.work_address = address

    def display(self):
        ''' Print out contact '''
        print(f'Name: {self.name}')
        print(f'Home Phone: {self.home_phone}')
        print(f'Work Phone: {self.work_phone}')
        if self.home_address:
            print('Home Address:')
            self.home_address.display(indent=4)
        if self.work_address:
            print('Work Address:')
            self.work_address.display(indent=4)
        print('')
