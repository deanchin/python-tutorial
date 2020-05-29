""" Entry Point """
# from service.example import Example
from service.contact import Contact


if __name__ == "__main__":

    # Example().add_item(
    #     {
    #         "name": "Ricky Chin",
    #         "address": "909 Golden Palomino Ct",
    #         "city": "Boynton Beach",
    #         "somthing": {
    #             "do": "stuff"
    #         }
    #     })

    # Contact().add_item(
    #     {
    #         'firstName': 'Dean',
    #         'lastName': 'Chin',
    #         'address': '909 Golden Palomino Court',
    #         'city': 'Austin',
    #         'state': 'TX',
    #         'zipcode': '78732'
    #     }
    # )

    CONTACT = Contact().find_item({'lastName': 'Chin'})
    print(CONTACT)
    Contact().delete_item({'lastName': 'Chin'})
    CONTACT = Contact().find_item({'lastName': 'Chin'})
    print(CONTACT)
