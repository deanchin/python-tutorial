''' app.py '''
# AddressBook
# - List of contacts

# Contact <-- Object/Class
# - name
#     - first_name (string)
#     - last_name (string)
# - home_address (Address)
# - home_phone  (string > PhoneNumber)
# - work_address (Address)
# - work_phone (string > PhoneNumber)
from address_book import AddressBook
from contact import Contact
from address import Address


def get_name_from_user():
    ''' get name from user '''
    while True:
        full_name = input('What is the first name and last name? ').split()
        if len(full_name) != 2:
            print(
                '[ERROR] Must enter the first and last name seperated by a space')
        else:
            break
    return ' '.join(full_name)


def get_address_from_user():
    ''' Returns a Address class with the data entered from user '''
    return Address(
        street=input('Street Address? '),
        city=input('City? '),
        state=input('State? '),
        zipcode=input('Zipcode? ')
    )


def get_contact_from_user():
    ''' Returns a Address class with the data entered from user '''
    contact = Contact(name=get_name_from_user())
    if input('Do you want to enter your home address (y/n): ').lower() == 'y':
        contact.set_home_address(get_address_from_user())
    if input('Do you want to enter your work address (y/n): ').lower() == 'y':
        contact.set_work_address(get_address_from_user())
    return contact


ADDRESS_BOOK = AddressBook()

while True:
    ACTION = input(
        'What do you want to do (list/search/add/edit/delete/exit)? ').lower()
    if ACTION == 'add':
        ADDRESS_BOOK.add_contact(get_contact_from_user())
    elif ACTION == 'edit':
        print('Editing')
    elif ACTION == 'list':
        ADDRESS_BOOK.display()
    elif ACTION == 'search':
        CONTACT = ADDRESS_BOOK.get_by_name(get_name_from_user())
        if CONTACT:
            CONTACT.display()
        else:
            print('Contact not found')
    elif ACTION == 'delete':
        ADDRESS_BOOK.delete_contact(get_name_from_user())
    elif ACTION == 'exit':
        print('exit')
        break
    else:
        print('invalid')


# print the contact with keys to edit
# [n] name
# [ha] home address
# [hp] home phone: 123-456-7890
# 
# original_name = 'name that was passed in from the input'
# contact that has just the fields that you want to change.
#   all other fields will be None.
# ADDRESS_BOOK.edit_contact(name, contact_update_object)