from rand import Random
from io_helpers import IOHelpers
from b_tree import BTree
from hash_table import HashTable
from index_file import IndexFile

# Returns the database that main will 
# be the keeper of
# database_obj is a list containing the objects of the databases. [B_tree obj, Hashtable obj, Index_file obj]

class ChoosePopulate:
    
    def __init__(self, database_loc, quantity):
        # number of data points must be passed through quantity
        self.database_location = database_loc
        self.b_tree_location = self.database_location + "b_tree.db"
        self.hash_table_location = self.database_location + "hash_table.db"
        self.index_file_location_1 = self.database_location + "index_file_bt.db"
        self.index_file_location_2 = self.database_location + "index_file_ii.db"
        self.generate_data( quantity )

    def generate_data(self, quantity):
        #Retrieve the key value pairs to be injected
        r = Random()
        print "Generating data"
        self.vals = r.get_keys_and_values(quantity) 

    # return True if option chosen
    # return False if exited
    def start_application(self, database):
        # Print the options for the user
        self.print_options()
        
        # Get user input option
        choice = IOHelpers.get_input( 4 )
        
        return self.populate(choice, database)

    def populate( self, choice, database ):
        if ( choice == 1 ):
            # database = B-Tree
            if database != None:
                database.destroy()

            database = BTree(self.b_tree_location)
            database.insert(self.vals)
            return database
 

        elif ( choice == 2 ):
            # database = Hash Table
            if database != None:
                database.destroy()

            database = HashTable(self.hash_table_location)
            database.insert(self.vals)
            return database
            
        elif ( choice == 3 ):
            # database = Index File
            if database != None:
                database.destroy()

            database = IndexFile(self.index_file_location_1,
                                 self.index_file_location_2)
            database.insert(self.vals)
            return database
            
        elif (choice == 4 ):
            print "Exiting"


    # Helper function to print options
    def print_options( self ):
        print  "What kind of database would you like to try?"         
        print  "[1] B-Tree" 
        print  "[2] Hash Table" 
        print  "[3] Index File" 
        print  "[4] Exit"
