from application import Application
from error_checker import ErrorChecker

class RecordViolation(Application):
    current_number = 0
    
    def start_application(self, c):
        self.cursor = c

        self.my_number = RecordViolation.current_number
        RecordViolation.current_number += 1

        self.fields = [ "Violator no.", # 1 
                        "Vehicle id",   # 2
                        "Office no.",   # 3
                        "Violation type", # 4
                        "Violation date", # 5
                        "Place",        # 6
                        "Descriptions", # 7
                        "Insert into database", # 8
                        "Exit: Cancel entering violation" ] # 9
        
        self.list_of_inputs = [ None for i in range(len(self.fields)) ]

        self.cursor.execute("SELECT * FROM ticket" )
        self.metadata = self.cursor.description

        while ( True ):
            self.print_field_options( )
            choice = self.get_input( len(self.fields) )
            index = choice - 1

            if ( choice == 1 ):
                self.get_violator_no(index)
            elif ( choice == 2 ):
                self.get_vehicle_id(index)
            elif ( choice == 3 ):
                self.get_office_no(index)
            elif ( choice == 4 ):
                self.get_violation_type(index)
            elif ( choice == 5 ):
                self.get_violation_date(index)
            elif ( choice == 6 ):
                self.get_violation_place(index)
            elif ( choice == 7 ):
                self.get_violation_description(index)
            # Enter data into db
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

    # else returns the integer input choice
    def get_input( self, num_choices ):
        print( "Choose a field to edit or an option: " )
        try:
            string_input = input()
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
                choice = int(string_input)
            except:
                choice = "Invalid"

        return choice

    def get_violator_no(self, index):
        pass
    
    def get_vehicle_id(self, index):
        pass
    
    def get_office_no(self, index):
        pass

    def get_violation_type(self, index):
        pass

    def get_violation_date(self, index):
        pass

    def get_violation_place(self, index):
        pass
    
    def get_violation_description(self, index):
        pass

    
