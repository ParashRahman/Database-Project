from rand import Random
from io_helpers import IOHelpers

# Returns the database that main will 
# be the keeper of
# database_obj is a list containing the objects of the databases. [B_tree obj, Hashtable obj, Index_file obj]

class ChoosePopulate:

    def __init__(self, database_obj):

        self.Hashtable_obj=database_obj[1]
        self.B_tree_obj=database_obj[0]
        self.Index_file_obj=database_obj[2]

    def generate_data(self, quantity):
        Retrieve the key value pairs to be injected
        r = Random()
        self.vals =  r.get_keys_and_values(quantity) 

        self.vals=[("1","a"),("2","b"),("3","c"),("75","d"),("7","e"),("432","f"),("857","g"),("293","h"),("2382","i"),("492","j"),("124","k"),("943","l"),("82","m"),("912","n")]

    # return True if option chosen
    # return False if exited
    def start_application(self):
        # Print the options for the user
        self.print_options()
        
        # Get user input option
        # choice = IOHelpers.get_option( 3 )

        choice=int(input())

        # Instantiate the proper database type
        database = None
        if ( choice == 1 ):
            # database = B-Tree
            if self.B_tree_obj != None:
                self.B_tree_obj.insert(self.vals)

        elif ( choice == 2 ):
            # database = Hash Table
            if self.Hashtable_obj != None:
                self.Hashtable_obj.insert(self.vals)

        elif ( choice == 3 ):
            # database = Index File
            if self.Index_file_obj != None:
                self.Index_file_obj.insert(self.vals)

        elif (choice == 4 ):
            return False
        
        # Inject values into database
        # database.insert_values( vals )
        return True

    # Helper function to print options
    def print_options( self ):
        print  "What kind of database would you like to try?"         
        print  "[1] B-Tree" 
        print  "[2] Hash Table" 
        print  "[3] Index File" 
        print  "[4] For Exit"
