from io_helpers import IOHelpers

# This class is an application that
# allows the user to search the database
class SearchDatabase:
    def __init__(self, db, s_type):
        self.database = db
        self.search_type = s_type

    def start_application( self ):
        results = None

        if ( self.search_type == "key" ):
            print( "Enter a key to search for: ")
            user_input = input()
        elif ( self.search_type == "data" ):
            print( "Enter data to search for: ")
            user_input = input()
        elif ( self.search_type == "range" ):
            print( "Enter lower bound of search: ")
            user_input_lower = input()
            print( "Enter upper bound of search: ")
            user_input_upper = input()

        return results
