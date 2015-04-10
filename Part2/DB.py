# This is the parent class for searching, inserting records. 
# Child classes will have to call the DB class's constructor
# and pass onto it the initialized db_object (B_tree,hashtable,etc)
import bsddb

class DB:

    def __init__(self, db_obj, db_address):
        self.db = db_obj
        self.db_address = db_address

    # Retrieves records based on key search
    def retrieve_using_key(self,keys):
        records=[] # list containing tuples of key-value pair
        
        for key in keys:
            try:
                records.append((key,self.db[key]))
            except KeyError:
                pass

        return records

    # Retrieves records containing the input data_values fed
    def retrieve_using_data_values(self, data_values):
        # return list of keys and values
        records=[] 

        current = self.db.first()
        
        while( True ):
            if ( current[1] in data_values ):
                records.append( current )
            try:
                current = self.db.next()
            except KeyError:
                break

        return records

    # TO BE OVERIDDEN BY SUBCLASSES
    def retrieve_range(self,low_key,high_key):
        pass
    
    # Takes a records list which contains a tuple eg, (key,value).
    # Stores the values against the corresponding key
    def insert(self,records):
        for key,value in records:
            if self.db.has_key(key) == False:
                self.db[key] = value

        self.save()

        return True

    # For deleting a database from a harddrive
    def destroy(self):
        self.close()
        bsddb.os.remove(self.db_address)

    # Should be called when saving into a database, aka syncing
    def save(self):
        self.db.sync()

    # Should be called when closing a database
    # Closing means flushing to disk and stopping access
    def close(self):
        self.db.close()
