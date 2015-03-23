from application import Application
from error_checker import ErrorChecker
from metadata import Metadata

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

        m = Metadata(self.cursor)
        self.metadata = m.meta_ticket()

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
                
                
                return
            # Exit option
            elif ( choice == 9 ):
                return

    def print_field_options( self, fields = None, showEmpty = True ):
        if ( fields == None ):
            fields = self.fields
        print( "Enter a field option to edit: " )
        for i in range( len( fields ) ):
            print ( "[{:}] ".format( i+1 ) + 
                    fields[i] + 
                    (" EMPTY" if showEmpty 
                     and i < 7 and not self.list_of_inputs[i+1]  
                     else "") )

    # else returns the integer input choice
    def get_input( self, num_choices, 
                   prompt = "Choose a field to edit or an option: ",
                   fields = None, showEmpty = True ):
        if ( fields == None ):
            fields = self.fields

        print( prompt )
        try:
            string_input = input()
            choice = int(string_input)
        except:
            choice = "Invalid"
        
        while ( type( choice ) is not int 
                or choice >= num_choices + 1 
                or choice <= 0 ):
            self.print_field_options(fields, showEmpty)
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
        self.cursor.execute( "SELECT * FROM ticket_type" )
        list_of_types = self.cursor.fetchall()
        prompt_types = [ row[0] + " $" + str(row[1])
                          for row in list_of_types ] 

        self.print_field_options( prompt_types, False )

        user_input = self.get_input(len( prompt_types ), 
                                    "Pick a violation type", 
                                    prompt_types, False )

        self.list_of_inputs[index] = list_of_types[user_input-1][0]

    ###################################
    # GET VIOLATION DATE
    ###################################
    def get_violation_date(self, index):
        while ( True ):
            date_input = input ( "Enter the date ( DD/MM/YYYY ) "
                                 "(Enter nothing to cancel) :")
            if ( len( date_input ) == 0 ):
                return

            date_input = date_input.split('/')
            try:
                if len(date_input) != 3:
                    raise InvalidDateException()
                for component in date_input:
                    if ( not ErrorChecker.check_str_int(component) ):
                        raise InvalidDateException()
                
                date_input = [ int(comp) for comp in date_input ]
                
                if (not ErrorChecker.check_error(self.metadata[index], date_input)):
                    raise InvalidDateException()
                
                break

            except ( InvalidDateException ):
                print( "Your date was invalid" )
            
        if ( date_input != None ):
            d = date_input[0]
            m = date_input[1]
            y = date_input[2]
            self.list_of_inputs[index] = [ "{:}/{:}/{:}".format(d,m,y), "DD/MM/YYYY" ] 

                    
    ###################################
    # GET VIOLATOR PLACE
    ###################################
    def get_violation_place(self, index):

        while ( True ):
            user_input = input("Enter the place of the violation "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = user_input

    ###################################
    # GET VIOLATOR DESCRIPTION
    ###################################
    def get_violation_description(self, index):
        while ( True ):
            user_input = input("Enter the description of the violation "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = user_input

    
class InvalidDateException(Exception):
    pass
