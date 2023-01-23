from apps.database import Database


class Data(object):
    def __init__(self):
        self.db = Database()
        self.collection_name = 'data'

        self.fields = {
            "username": "string",
            "name": "string",
            "lastName": "string",
            "public": "boolean",
            "age": "int",
        }

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def insert(self, todo):  # curd 1 data
        return self.db.insert(todo, self.collection_name)
