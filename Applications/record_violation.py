from application import Application
from error_checker import ErrorChecker

class RecordViolation(Application):
    current_number = 0
    
    def start_application(self, c):
        self.cursor = c

        self.list_of_inputs = [ None for i in range(8) ]

        self.list_of_inputs[0] = RecordViolation.current_number
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

        self.cursor.execute("SELECT * FROM ticket" )
        self.metadata = self.cursor.description

        while ( True ):
            self.print_field_options( )
            choice = self.get_input( len(self.fields) )

            if ( choice == 1 ):
                self.get_violator_no(choice)
            elif ( choice == 2 ):
                self.get_vehicle_id(choice)
            elif ( choice == 3 ):
                self.get_office_no(choice)
            elif ( choice == 4 ):
                self.get_violation_type(choice)
            elif ( choice == 5 ):
                self.get_violation_date(choice)
            elif ( choice == 6 ):
                self.get_violation_place(choice)
            elif ( choice == 7 ):
                self.get_violation_description(choice)
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
                    (" EMPTY" if i < 7 and not self.list_of_inputs[i+1]  else "") )

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

    ###################################
    # GET VIOLATOR NO.
    ###################################
    def get_violator_no(self, index):
        # initial get and check
        user_input = input("Enter the violator's SIN "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if violator exists
        exists = False
        self.cursor.execute("SELECT SIN FROM people")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the violator does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the violator's SIN " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                char_answer = ""
                while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
                    char_answer = input( "The violator is not in the database. "
                                         "Would you like to add the person? (y/n): " )
                
                if ( char_answer == 'y' ):
                    # TODO: Call add person
                    pass

                user_input = input("Enter the violator's SIN (Enter "
                                   "nothing to cancel): ")

            if ( len( user_input ) == 0 ):
                return

            if ( user_input.strip().lower() in rows ):
                exists = True
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = user_input.strip().lower()
    
    ###################################
    # GET VEHICLE ID
    ###################################
    def get_vehicle_id(self, index):
        # initial get and check
        user_input = input("Enter the vehicle serial number "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if violator exists
        exists = False
        self.cursor.execute("SELECT serial_no FROM vehicle")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the violator does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the vehicle serial number " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                user_input = input("The vehicle is not in the database. "
                                   "Enter the violator's SIN (Enter "
                                   "nothing to cancel): ")

            if ( len( user_input ) == 0 ):
                return

            if ( user_input.strip().lower() in rows ):
                exists = True
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = user_input.strip().lower()

    
    ###################################
    # GET OFFICE NO.
    ###################################
    def get_office_no(self, index):
        # initial get and check
        user_input = input("Enter the office number "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if violator exists
        exists = False
        self.cursor.execute("SELECT SIN FROM people")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the violator does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the office number " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                user_input = input("The office is not in the database. "
                                   "Enter the office number (Enter "
                                   "nothing to cancel): ")

            if ( len( user_input ) == 0 ):
                return

            if ( user_input.strip().lower() in rows ):
                exists = True
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = user_input.strip().lower()

    ###################################
    # GET VIOLATION TYPE
    ###################################
    def get_violation_type(self, index):
        pass

    ###################################
    # GET VIOLATION DATE
    ###################################
    def get_violation_date(self, index):
        pass

    ###################################
    # GET VIOLATOR PLACE
    ###################################
    def get_violation_place(self, index):
        pass

    ###################################
    # GET VIOLATOR DESCRIPTION
    ###################################
    def get_violation_description(self, index):
        pass

    
