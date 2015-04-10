import bsddb
from DB import DB

# BTree (Subclass of DB)

class BTree(DB):

    def __init__(self, db_address):
        # Database="B_tree.db"
        # self.address=db.address #contains address to db file's location
        self.db = bsddb.btopen(db_address, 'c')           
        DB.__init__(self, self.db, db_address)

    def retrieve_range( self, low_key, high_key ):
        ret = []
        keys = self.db.keys()

        # Finds the minimum key greater than low_key
        low_key_index = lowest_ge( keys, low_key )

        if ( low_key_index == len( self.db ) ):
            return ret

        current = self.db.set_location( keys[low_key_index] )
        
        while ( current[0] <= high_key ):
            ret.append(current)
            try:
                current = self.db.next()
            except KeyError:
                break

        return ret


# Used for finding lowest key greater than
# lower bound
# Returns size_of_list if key is greater than all values
def lowest_ge( list_of_keys, low_key ):
    start = 0
    end = len( list_of_keys ) - 1
    middle = ( start + end + 1) / 2
    
    while ( start < end ):
        if ( list_of_keys[middle] < low_key ):
            start = middle 
        else:
            end = middle - 1
        middle = (start + end + 1) / 2

    # edge case for beginning
    if ( middle == 0 and list_of_keys[middle] >= low_key ):
        return middle

    return middle + 1
