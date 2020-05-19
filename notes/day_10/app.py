''' app functions '''
from address import Address
# Scenario One:
# Regular Contact with an option for adding in work information.
# Name:
# Phone Number:
# Home Address:
# No work Address

# Prompting the user for information:
# Always get name?
# Ask if they want to put in home information?
# Ask if they want to put in work information?

# Dean Chin
# 123-456-7890
# 111 street
# Austin, TX 78732

#  Get full name
# while True:
#     FULL_NAME = input('What is your first name and last name? ').split()
#     if len(FULL_NAME) != 2:
#         print(
#             '[ERROR] Must enter your first and last name seperated by a space')
#     else:
#         break

# if input('Do you want to enter your home address (Y/N)? ').upper() == 'Y':
#     HOME_STREET = input('What is your home street name? ')
#     HOME_CITY = input('What is your home city? ')
#     HOME_STATE = input('What is your home state? ')
#     HOME_ZIP = input('What is your home zip? ')
#     HOME_ADDRESS = Address(
#         street=HOME_STREET,
#         city=HOME_CITY,
#         state=HOME_STATE,
#         zipcode=HOME_ZIP
    # )

#  Get full name
# while True:
#     FULL_NAME = input('What is your first name and last name? ').split()
#     if len(FULL_NAME) != 2:
#         print(
#             '[ERROR] Must enter your first and last name seperated by a space')
#     else:
#         break


def get_name_from_user():
    ''' get name from user '''
    while True:
        full_name = input('What is your first name and last name? ').split()
        if len(full_name) != 2:
            print(
                '[ERROR] Must enter your first and last name seperated by a space')
        else:
            break
    return full_name


def get_address_from_user():
    ''' Returns a Address class with the data entered from user '''
    return Address(
        street=input('Street Address? '),
        city=input('City? '),
        state=input('State? '),
        zipcode=input('Zipcode? ')
    )


HOME_ADDRESS = None
WORK_ADDRESS = None
FULL_NAME = get_name_from_user()
if input('Do you want to enter your home address (Y/N)? ').upper() == 'Y':
    HOME_ADDRESS = get_address_from_user()
if input('Do you want to enter your work address (Y/N)? ').upper() == 'Y':
    WORK_ADDRESS = get_address_from_user()

print('-------------------------')
print(' CONTACT INFO')
print('-------------------------')
print(f'First Name: {FULL_NAME[0]}')
print(f'Last Name: {FULL_NAME[1]}')
if HOME_ADDRESS:
    print(f'Home Address: {HOME_ADDRESS.get()}')
if WORK_ADDRESS:
    print(f'Work Address: {WORK_ADDRESS.get()}')
