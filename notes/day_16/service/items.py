''' Items class '''


class Items():
    ''' Items class '''

    def get_all(self):
        ''' get all items '''
        return {
            'items': [
                {'name': 'item1'},
                {'name': 'item2'},
            ]
        }, 200

    def get_one(self, name):
        ''' get one item by name '''
        return {
            'message': f'get {name}'
        }, 200

    def update_one(self, name, payload):
        ''' update one item by name '''
        return {
            'message': f'Update {name}'
        }, 200

    def delete_one(self, name):
        ''' delete one item by name '''
        return {
            'message': f'Delete {name}'
        }, 200
