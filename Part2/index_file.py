import bsddb
from startup import *
from b_tree import BTree
from hash_table import HashTable

class IndexFile(BTree):
    def __init__(self, db_address, index_address):
        # Constant for seperating hash table
        self.SEPERATOR = ";;;;;"

        self.inverse_index = bsddb.hashopen(index_address, 'c')
        self.index_address = index_address
        self.db =  bsddb.btopen(db_address, 'c')
        DB.__init__(self, self.db, db_address)

    # OVERRIDED
    def insert(self, records):
        for key, value in records:
            if self.db.has_key(key) == False:
                self.db[key] = value
                if ( self.inverse_index.get(value) == None ):
                    self.inverse_index[value] = key
                else:
                    self.inverse_index[value] += \
                        self.SEPERATOR + key

        self.save()

    #  OVERRIDED
    def retrieve_using_data_values( self, data_values ):
        size_db = len( self.db )
        ret = []

        for data_value in data_values:
            raw_keys = ''

            try:
                raw_keys = self.inverse_index[data_value]
            except KeyError:
                # value is not in db
                pass

            keys = raw_keys.split(self.SEPERATOR)
            keys = [ (key, data_value) for key in keys ]
            ret.extend(keys)

        return ret

    # OVERRIDED
    def save(self):
        self.db.sync()
        self.inverse_index.sync()

    # OVERRIDED
    def destroy( self ):
        bsddb.os.remove(self.db_address)
        bsddb.os.remove(self.index_address)
