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
            print "Enter a key to search for: "
            user_input = raw_input()
            results = self.database.retrieve_using_key( [user_input] )

        elif ( self.search_type == "data" ):
            print "Enter data to search for: "
            user_input = raw_input()
            results = self.database.retrieve_using_data_values( [user_input] )

        elif ( self.search_type == "range" ):
            print "Enter lower bound of search: "
            user_input_lower = raw_input()
            print "Enter upper bound of search: "
            user_input_upper = raw_input()
            if ( user_input_lower <= user_input_upper ):
                results = self.database.retrieve_range( user_input_lower,
                                                        user_input_upper )
            else:
                print( "Lower bound must be less than upper bound" )

        self.print_results( results )
        print "Returning to main menu"
        return results

    def print_results( self, results ):
        print "RESULTS"
        if ( len( results ) == 0 ):
            print( "** no results to show **" )
        elif ( self.search_type == "range" or
                 self.search_type == "key" ):
            for res in results:
                print( res[1] )
        else:
            for res in results:
                print( res[0] )

        
