""" Entry Point """
# from service.inventory import say_hello
# from data.inventory import INVENTORY
# import service.inventory as inv
from service.item import Item
from service.bottle import Bottle

if __name__ == "__main__":
    # print('Starting point')
    # inv.say_hello()
    # print(INVENTORY)
    ITEM = Item()
    print(ITEM)
    print(ITEM.get_price())
    ITEM.update_price(3.25)
    print(ITEM.get_price())
    print(ITEM)

    BOTTLE = Bottle()
    print(BOTTLE.get_bottle())
    BOTTLE.update_name('Stoli')
    print(BOTTLE.get_bottle())
    BOTTLE.update_price(10.00)
    print(BOTTLE.get_bottle())
    BOTTLE.update_type('vodka')
    print(BOTTLE.get_bottle())

    
    # Item().get_price() # This is a new instance of Item FrontLeft (1.0)
    # Item().update_price(5.25) # Another instance  - FrontWheel (5.25)
    # Item().get_price() # Third instance   - BackLeft (1.0)

