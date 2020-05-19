''' Address class '''


class Address():
    ''' Address class '''

    def __init__(self,
                 street='UNDEFINED',
                 city='UNDEFINED',
                 state='UNDEFINED',
                 zipcode='UNDEFINED'):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get(self):
        ''' returns address '''
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode
        }
