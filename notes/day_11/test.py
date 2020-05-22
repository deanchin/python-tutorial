from address import Address
from contact import Contact

new_address = Address()
another_address = None

if another_address and not isinstance(another_address, Address):
    print('ERROR')
else:
    print('ALL GOOD')



    # True                  False == False
if ('dean' != 'dean') and ('ricky' == 'samuel'):
    print('They both are true')
else:
    print('at least one of them is false')

HOME_ADDRESS = Address(
    street='12345 something way',
    city='Austin',
    state='TX',
    zipcode='12345'
)
WORK_ADDRESS = Address(
    street='12345 work way',
    city='Austin',
    state='TX',
    zipcode='14325'
)
CONTACT = Contact(
    name=['Dean', 'Chin'],
    phone='1234567890',
    home_address=HOME_ADDRESS,
    work_address=WORK_ADDRESS
)

print(CONTACT.get())
print('------------------')
CONTACT.display()
print('------------------')

HOME_ADDRESS.display()

# Address Book
# - List of Contacts
#   - Name
#   - Home Address
#       - Address Class
#   - Work Address
