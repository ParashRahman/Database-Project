from io_helpers import IOHelpers
import timer

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

            start_time = timer.current_micro_time()
            results = self.database.retrieve_using_key( [user_input] )
            end_time = timer.current_micro_time()
            self.print_results( results )
            self.print_time( end_time - start_time )


        elif ( self.search_type == "data" ):
            print "Enter data to search for: "
            user_input = raw_input()

            start_time = timer.current_micro_time()
            results = self.database.retrieve_using_data_values( [user_input] )
            end_time = timer.current_micro_time()
            self.print_results( results )
            self.print_time( end_time - start_time )


        elif ( self.search_type == "range" ):
            print "Enter lower bound of search: "
            user_input_lower = raw_input()
            print "Enter upper bound of search: "
            user_input_upper = raw_input()

            if ( user_input_lower <= user_input_upper ):
                start_time = timer.current_micro_time()
                results = self.database.retrieve_range( user_input_lower,
                                                        user_input_upper )
                end_time = timer.current_micro_time()

                self.print_results( results )
                self.print_time( end_time - start_time )
            else:
                print "Lower bound must be less than upper bound" 
                return

        print "Returning to main menu"


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

    def print_time( self, microseconds ):
        print "The query took " + str(microseconds) + " microseconds."
