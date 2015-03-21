from application import Application

class RecordViolation(Application):
    def start_application(self, c):
        self.cursor = c
        
        self.fields = [ "Ticket no.",
                        "Violator no.",
                        "Vehicle id",
                        "Office no.",
                        "Violation type",
                        "Violation date",
                        "Place",
                        "Descriptions",
                        "Exit: Cancel entering violation" ]
        
        self.list_of_inputs = [ None for i in range(len(self.fields)) ]

        metadata = True

        while ( True ):
            self.print_field_options( )
            choice = self.get_input( len(self.fields) )
  
            if ( choice == 1 ):
                pass 
            elif ( choice == 2 ):
                pass
            elif ( choice == 3 ):
                pass
            elif ( choice == 4 ):
                pass
            elif ( choice == 5 ):
                pass
            elif ( choice == 6 ):
                pass
            elif ( choice == 7 ):
                pass
            elif ( choice == 8 ):
                pass
            # Exit option
            elif ( choice == 9 ):
                return

    def print_field_options( self ):
        print( "Enter a field option to edit: " )
        for i in range( len( self.fields ) ):
            print ( "[{:}] ".format( i+1 ) + 
                    self.fields[i] + 
                    ("" if self.list_of_inputs[i] else " EMPTY" ) )

    # returns False if nothing is entered (user cancels)
    # else returns the integer input choice
    def get_input( self, num_choices ):
        print( "Enter a number (Enter nothing to cancel): " )

        try:
            string_input = input()
            if ( len( string_input ) == 0 ):
                return False
            choice = int(string_input)
        except:
            choice = "Invalid"
        
        while ( type( choice ) is not int 
                or choice >= num_choices + 1 
                or choice <= 0 ):
            self.print_field_options()
            print( "Enter a valid integer choice: " )
            try:
                string_input = input()
                if ( string_input == 0 ):
                    return False
                choice = int(string_input)
            except:
                choice = "Invalid"

        return choice
