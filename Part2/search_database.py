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
            user_input = str(raw_input()).strip()

            start_time = timer.current_micro_time()
            results = self.database.retrieve_using_key( [user_input] )
            end_time = timer.current_micro_time()
            self.print_results( results )
            self.print_anwser_file(results)
            self.print_time( end_time - start_time )


        elif ( self.search_type == "data" ):
            print "Enter data to search for: "
            user_input = str(raw_input()).strip()

            start_time = timer.current_micro_time()
            results = self.database.retrieve_using_data_values( [user_input] )
            end_time = timer.current_micro_time()
            self.print_results( results )
            self.print_answers_file(results)
            self.print_time( end_time - start_time )


        elif ( self.search_type == "range" ):
            print "Enter lower bound of search: "
            user_input_lower = raw_input().strip()
            print "Enter upper bound of search: "
            user_input_upper = raw_input().strip()

            if ( user_input_lower <= user_input_upper ):
                start_time = timer.current_micro_time()
                results = self.database.retrieve_range( user_input_lower,
                                                        user_input_upper )
                end_time = timer.current_micro_time()

                self.print_results( results )
                self.print_answers_file(results)
                self.print_time( end_time - start_time )
            else:
                print "Lower bound must be less than upper bound" 
                return

        print "Returning to main menu"


    def print_results( self, results ):
        print "RESULTS"
        if ( len( results ) == 0 ):
            print( "** no results to show **" )
            return
        elif ( self.search_type == "range" or
                 self.search_type == "key" ):
            for res in results:
                print( res[1] )
                print "__________________"
        else:
            for res in results:
                print( res[0] )
                print "____________________"
        print("Number of Results:" + str(len(results)))
        
        f = open('answers','a')
        f.write('hi there\n')
        f.close()
    
    def print_answers_file(self, results):
        f = open('answers','a')
        for res in results:
            f.write(res[0]+'\n'+res[1]+'\n'+'\n')
        

    def print_time( self, microseconds ):
        print "The query took " + str(microseconds) + " microseconds."
