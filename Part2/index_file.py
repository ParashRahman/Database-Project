import bsddb
from startup import *
from b_tree import BTree

class IndexFile(BTree):

    def __init__(self, db_address, index_address):

        self.inverse_index = {}
        self.db =  bsddb.btopen(db_address, 'c')
        DB.__init__(self, self.db, db_address)


    # OVERRIDED
    def insert(self, records):
        for key, value in records:
            if self.db.has_key(key) == False:
                self.db[key] = value
                if ( self.inverse_index.get(value) == None ):
                    self.inverse_index[value] = [key]
                else:
                    self.inverse_index[value].append(key)

    #  OVERRIDED
    def retrieve_using_data_values( self, data_values ):
        size_db = len( self.db )
        records = []

        for data_value in data_values:
            try:
                records.extend(self.inverse_index[data_value])
            except KeyError as e:
                # print e
                pass

        # format return as key value pairs
        for i in xrange( len( records ) ):
            records[i] = (records[i], data_values[0])

        return records

