from pymongo import MongoClient

class MongoConnection:
    def __init__(self,url='mongodb+srv://buseayazoglu:buse123ayz@deneme1.hxzz7.mongodb.net/'):
        self.client = MongoClient(url)


    def database_getir(self,db_name):
        return self.client[db_name]