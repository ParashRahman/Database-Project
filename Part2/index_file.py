import bsddb
from startup import *

class IndexFile(DB):

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

        return records


    def __del__(self):
        self.close()
        # self.save()

    
