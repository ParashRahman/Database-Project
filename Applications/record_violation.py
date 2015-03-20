from application import Application

class RecordViolation(Application):
    def start_application(self, c):
        self.cursor = c
        
        fields = [ "Ticket no.",
                   "Violator no.",
                   "Vehicle id",
                   "Office no.",
                   "Violation type",
                   "Violation date",
                   "Place",
                   "Descriptions" ]
        
        list_of_inputs = [ None for i in range(len(fields)) ]

        print_field_options( fields, list_of_inputs )
        choice = get_input( len(fields) )
        
        if ( not choice ):
            return

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

def print_field_options( fields, list_of_inputs ):
    print( "Enter a field option to edit: " )
    for i in range( len( fields ) ):
        print ( "[{:}] ".format( i+1 ) + 
                fields[i] + 
                ("" if list_of_inputs[i] else " EMPTY" ) )

# returns False if nothing is entered (user cancels)
# else returns the integer input choice
def get_input( num_choices ):
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
        print_options()
        print( "Enter a valid integer choice: " )
        try:
            string_input = input()
            if ( string_input == 0 ):
                return False
            choice = int(string_input)
        except:
            choice = "Invalid"

    return choice
