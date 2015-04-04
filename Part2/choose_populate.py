from rand import Random
from io_helpers import IOHelpers

NUMBER_OF_PAIRS = 1000

# Returns the database that main will 
# be the keeper of
class ChoosePopulate:
    def start_application(self):

        # Retrieve the key value pairs to be injected
        r = Random()
        vals =  r.get_keys_and_values(NUMBER_OF_PAIRS) 

        # Print the options for the user
        self.print_options()
        
        # Get user input option
        choice = IOHelpers.get_option( 3 )

        # Instantiate the proper database type
        database = None
        if ( choice == 1 ):
            # database = B-Tree
            pass
        elif ( choice == 2 ):
            # database = Hash Table
            pass
        elif ( choice == 3 ):
            # database = Index File
            pass
        
        # Inject values into database
        # database.insert_values( vals )

        return database

    # Helper function to print options
    def print_options( self ):
        print ( "What kind of database would you like to try?" )        
        print ( "[1] B-Tree" )
        print ( "[2] Hash Table" )
        print ( "[3] Index File" )