from choose_populate import ChoosePopulate
from io_helpers import IOHelpers
from search_database import SearchDatabase

class Main: 
    def __init__(self):
        self.database = None

    def start_application(self):
        # print options for the user
        self.print_options()

        # get the user's choice
        choice = IOHelpers.get_input( 6 )

        if ( choice == 1 ):
            # Create and populate the database
            c = ChoosePopulate()
            self.database = c.start_application()
        elif ( choice == 2 ):
            # key search of database
            s = SearchDatabase(self.database, "key")
            s.start_application()
        elif ( choice == 3 ):
            # data search of database
            s = SearchDatabase(self.database, "data")
            s.start_application()
        elif ( choice == 4 ):
            # range search of database
            s = SearchDatabase(self.database, "range")
            s.start_application()
        elif ( choice == 5 ):
            # destroy the database
            pass
        elif ( choice == 6 ):
            return

    def print_options( self ):
        print( "Choose an option:" )
        print( "[1] Create and populate a database" )
        print( "[2] Retrieve record with a key" )
        print( "[3] Retrieve records with data" )
        print( "[4] Retrieve records within a key range" )
        print( "[5] Destroy the database" )
        print( "[6] Quit" )
