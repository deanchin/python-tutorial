''' Movies class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Movies():
    ''' Movies class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self):
        ''' get all movies '''
        self.logger.info(list(self.collection.find({})))
        return {
            'result': list(self.collection.find({}, {'_id': 0}))
        }, 200

    def get_one(self, name):
        ''' get one movie by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})
        if result:
            return result, 200
        return {'message': f'{name} not found'}, 404

    def create_one(self, payload):
        ''' Create an movie '''
        self.collection.insert_one(payload)
        return {
            'message': f'Created movie: {payload}'
        }, 201

    def update_one(self, name, payload):
        ''' update one movie by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})

        if result:
            self.collection.update_one({"name": name}, {"$set": payload})
            return {'message': f'Updated {name}'}, 200
        return {
            'message': f'{name} not found'
        }, 404

    def delete_one(self, name):
        ''' delete one movie by name '''
        return {
            'message': f'Delete {name}'
        }, 200
