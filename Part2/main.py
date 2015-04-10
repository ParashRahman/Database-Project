from choose_populate import ChoosePopulate
from io_helpers import IOHelpers
from search_database import SearchDatabase
import os

class Main: 
    def __init__(self):
        self.database_location = "tmp/my_db/tianzhi_db/"
        if not os.path.exists(self.database_location):
            os.makedirs(self.database_location)
        self.database = None

    def start_application(self):
        # print options for the user
        while True:

            self.print_options()

            # get the user's choice
            choice = IOHelpers.get_input( 6 )

            if ( choice == 1 ):
                # Create and populate the database
                c = ChoosePopulate(self.database_location)
                self.database = c.start_application(self.database)
            elif ( choice == 2 ):
                # key search of database
                if ( self.database != None ):
                    s = SearchDatabase(self.database, "key")
                    s.start_application()
                else:
                    print "You have not set a database" 
            elif ( choice == 3 ):
                # data search of database
                if ( self.database != None ):
                    s = SearchDatabase(self.database, "data")
                    s.start_application()
                else:
                    print "You have not set a database" 
            elif ( choice == 4 ):
                # range search of database
                if ( self.database != None ):
                    s = SearchDatabase(self.database, "range")
                    s.start_application()
                else:
                    print "You have not set a database"
            elif ( choice == 5 ):
                # destroy the database
                if ( self.database != None ):
                    self.database.destroy()
                    self.database = None
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

if __name__ == '__main__':
    x = Main()
    x.start_application()
