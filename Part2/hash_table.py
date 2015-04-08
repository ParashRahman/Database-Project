import bsddb

# HashTable (subclass of DB)

class HashTable(DB):
    def __init__(self, db_address):
        # Database="Hash_table.db"
        # self.address=db.address #contains address to db file's location

        self.db = bsddb.hashopen(self.address, 'c')     
        super(Hash_table, self).__init__(self, self.db, db_address)

        return
