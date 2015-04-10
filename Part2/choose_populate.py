from rand import Random
from io_helpers import IOHelpers
from b_tree import BTree
from hash_table import HashTable

# Returns the database that main will 
# be the keeper of
# database_obj is a list containing the objects of the databases. [B_tree obj, Hashtable obj, Index_file obj]

class ChoosePopulate:

    def __init__(self, database_loc):
        self.database_location = database_loc

    def generate_data(self, quantity):

        #Retrieve the key value pairs to be injected
        r = Random()
        self.vals =  r.get_keys_and_values(quantity) 

        # self.vals=[("1","a"),("1","b"),("3","c"),("75","d"),("7","e"),("432","f"),("857","g"),("293","h"),("2382","i"),("492","j"),("124","k"),("943","l"),("82","m"),("912","n")]


    # return True if option chosen
    # return False if exited
    def start_application(self, database):
        # Print the options for the user
        self.print_options()
        
        # Get user input option
        choice = IOHelpers.get_input( 3 )

        self.generate_data(100)

        if ( choice == 1 ):
            # database = B-Tree
            if database != None:
                database.destroy()
                database = BTree(self.database_location)
                database.insert(self.vals)
                return database
            else:
                database = BTree(self.database_location)
                database.insert(self.vals)
                return database

        elif ( choice == 2 ):
            # database = Hash Table
            if database != None:
                database.destroy()
                database = HashTable(self.database_location)
                database.insert(self.vals)
                return database
            else:
                database = HashTable(self.database_location)
                database.insert(self.vals)
                return database

        elif ( choice == 3 ):
            # database = Index File
            print "Exiting"

        elif (choice == 4 ):
            print "Exiting"


        


    # Helper function to print options
    def print_options( self ):
        print  "What kind of database would you like to try?"         
        print  "[1] B-Tree" 
        print  "[2] Hash Table" 
        print  "[3] Index File" 
        print  "[4] Exit"
