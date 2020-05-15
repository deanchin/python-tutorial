''' Liqour class '''
# Requirements
# Write an application that can lookup a liqour type for a give liqour name
# Vodka Tuesdays promotion
# The user should get a discount if they are purchasing Vodka on Tuesdays
#

ALL_VODKA_BRANDS = ['Stoli', 'Titos', 'Grey Goose', 'absolute']
TODAY = 'Tuesday'
REGULAR_PRICE = 5.00
DISCOUNT_AMOUNT = 2.00


class Liqour():
    ''' Liqour class '''

    def get_price(self, liqour_name, day_of_week):
        ''' return the price (with/without discount) '''
        #  The n.lower()... piece is a list comprehension pattern
        if liqour_name.lower() in (n.lower() for n in ALL_VODKA_BRANDS) \
                and day_of_week.lower() == TODAY.lower():
            return self.get_regular_price(liqour_name) - DISCOUNT_AMOUNT
        return REGULAR_PRICE

    def get_regular_price(self, liqour_name):
        ''' always return the regular price '''
        return REGULAR_PRICE
