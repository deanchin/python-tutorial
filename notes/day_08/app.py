''' Main entrypoint '''
from address import Address
from address_book import AddressBook
from contact import Contact

if __name__ == "__main__":

    #  Define a new address book
    ADDRESS_BOOK = AddressBook()

    # Add some contacts
    ADDRESS_BOOK.add_contact(
        Contact(
            name='Dean Chin',
            phone='123-456-7890',
            home_address=Address(
                street='101 Some Street',
                city='Austin',
                state='Texas',
                zipcode='33029')
        )
    )
    ADDRESS_BOOK.add_contact(
        Contact(
            name='Samuel Urso',
            phone='223-456-7890',
            home_address=Address(
                street='102 Some Street',
                city='Austin',
                state='Texas',
                zipcode='33040')
        )
    )
    ADDRESS_BOOK.add_contact(
        Contact(
            name='Ricky Chin',
            phone='323-456-7890',
            home_address=Address(
                street='103 Some Street',
                city='Austin',
                state='Texas',
                zipcode='33041')
        )
    )

    print(ADDRESS_BOOK.get())
