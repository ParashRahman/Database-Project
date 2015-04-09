import bsddb
from DB import DB

# HashTable (subclass of DB)

class HashTable(DB):
    def __init__(self, db_address):
        # Database="Hash_table.db"
        # self.address=db.address #contains address to db file's location

        self.db = bsddb.hashopen(db_address, 'c')     
        DB.__init__(self, self.db, db_address)

        return


    def __del__(self):
		
		self.close()

		return

