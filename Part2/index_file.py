import bsddb

class IndexFile(DB):

    def __init__(self, db_address):
        self.inverse_index = {}
        self.db =  bsddb.btopen(db_address, 'c')

    # OVERRIDED
    def insert(self, records):
        for key, value in records:
            if self.b_tree.db_has_key(key) == False:
                self.b_tree[key] = value
                if ( inverse_index.get(value) == None ):
                    inverse.index[value] = [key]
                else:
                    inverse.index[value].append(key)

    #  OVERRIDED
    def retrieve_using_data_values( self, data_values ):
        size_db = len( self.db )
        records = []

        for data_value in data_values:
            records.extend(inverse_index[data_value])

        return records

    
