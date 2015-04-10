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

    def retrieve_range( self, low_key, high_key ):

        ret = []
        current = self.db.first()

        while ( True ):
            if ( low_key <= current[0] and high_key >= current[0] ):
                ret.append( current )
            try:
                current = self.db.next()
            except KeyError:
                break

        return ret
