from mongodb_connect import MongoDbConnection

class BooksDB(MongoDbConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)['Books']

    def kitaplar_ekleme(self,data:dict):
        self.collection.insert_many(data)

    def kitap_id_ve_isim_sorgulama(self):
        return self.collection.aggregate([
            {'$project':{'title':1, 'isbn':1}}
        ])



