""" Bottle class """
from service.item import Item


class Bottle(Item):
    ''' Bottle Class '''

    def __init__(self):
        super(Bottle, self).__init__()
        self.type = 'UNKNOWN'
        self.name = 'UNDEFINED'

    def get_bottle(self):
        ''' return the bottle info as a dictionary item '''
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price
        }

    def update_name(self, new_name):
        ''' Update a bottle name '''
        self.name = new_name

    def update_type(self, new_type):
        ''' Update a bottle type '''
        self.type = new_type.upper()
