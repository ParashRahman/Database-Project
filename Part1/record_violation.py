from application import Application
from error_checker import ErrorChecker
from errors import InvalidDateException
import add_person

class RecordViolation(Application):
    def start_application(self, c):
        self.cursor = c

        self.list_of_inputs = [ None for i in range(8) ]

        self.get_violation_no(0)

        self.fields = [ "Violator no.", # 1
                        "Vehicle id",   # 2
                        "Office no.",   # 3
                        "Violation type", # 4
                        "Violation date", # 5
                        "Place",        # 6
                        "Description", # 7
                        "Insert into database", # 8
                        "Exit: Cancel entering violation" ] # 9

        self.cursor.execute( "SELECT * FROM ticket" )
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
            # Enter data into db option
            elif ( choice == 8 ):
                inserted = self.insert_into_database()
                if ( inserted ):
                    return
                else:
                    continue
            # Exit option
            elif ( choice == 9 ):
                return
    
    # helper function for printing options
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

    # returns the integer input choice
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
    # GENERATE VIOLATION NO.
    ###################################
    def get_violation_no( self, index ):
        # gets the list of ids and adds 1 to the max
        numbers = self.cursor.execute( "SELECT ticket_no FROM ticket" ).fetchall()
        self.list_of_inputs[index] = max([ ID[0] for ID in numbers ]) + 1  

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
                    a = add_person.AddPerson()
                    a.start_application(self.cursor)
                    self.cursor.execute("SELECT SIN FROM people")
                    rows = self.cursor.fetchall()
                    rows = [ row[0].strip().lower() for row in rows ] 

                user_input = input("Enter the violator's SIN (Enter "
                                   "nothing to cancel): ")

            if ( len( user_input ) == 0 ):
                return

            if ( user_input.strip().lower() in rows ):
                exists = True
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = "'{:}'".format(user_input.strip().lower())
    
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
        
        self.list_of_inputs[index] = "'{:}'".format(user_input.strip().lower())

    
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
        
        self.list_of_inputs[index] = "'{:}'".format(user_input.strip().lower())

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

        self.list_of_inputs[index] = "'{:}'".format(list_of_types[user_input-1][0])

    ###################################
    # GET VIOLATION DATE
    ###################################
    def get_violation_date(self, index):
        while ( True ):
            date_input = input ( "Enter the date ( DD/MM/YYYY ) "
                                 "(Enter nothing to cancel): ")
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
            self.list_of_inputs[index] = [ "'{:}/{:}/{:}'".format(d,m,y), "'DD/MM/YYYY'" ] 

                    
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

        self.list_of_inputs[index] = "'{:}'".format(user_input)

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

        self.list_of_inputs[index] = "'{:}'".format(user_input)
    
    ###################################
    # INSERT INTO DATABASE
    ###################################
    def insert_into_database(self):
        
        # check if fields are empty
        unfinished = False
        for inp in self.list_of_inputs:
            if ( inp == None ):
                unfinished = True
                
        if ( unfinished ):
            print( "You have left some fields blank." )

        char_answer = ""
        while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
            char_answer = input( "Would you like to continue saving (y/n)? " )

        if ( char_answer == 'n' ):
            return False        

        # change all Nones in input to "NULL"
        for i in range( len( self.list_of_inputs ) ):
            if ( self.list_of_inputs[i] == None ):
                self.list_of_inputs[i] = "NULL" 
                
        # prepare date for insertion
        if ( self.list_of_inputs[5] != "NULL" ):
            self.list_of_inputs[5] = "TO_DATE( {:}, {:} )".format( 
                self.list_of_inputs[5][0], 
                self.list_of_inputs[5][1] )

        # attempt to charge primary owner if vehicle entered 
        #     and violator is not
        if ( self.list_of_inputs[2] != "NULL" 
             and self.list_of_inputs[1] == "NULL" ):
            statement = "SELECT o.owner_id FROM owner o, " \
                "vehicle v where v.serial_no = o.vehicle_id " \
                "and o.is_primary_owner = 'y' and v.serial_no = " + \
                self.list_of_inputs[2]
            primary_owner = self.cursor.execute( statement ).fetchall()
            if ( len( primary_owner ) == 0 ):
                # Do nothing
                pass
            else:
                primary_owner = "'{:}'".format( primary_owner[0][0] )
                self.list_of_inputs[1] = primary_owner

        statement = "INSERT INTO ticket VALUES( " \
            "{:}, {:}, {:}, {:}, {:}, {:}, {:}, {:} )".format( 
            self.list_of_inputs[0], 
            self.list_of_inputs[1], 
            self.list_of_inputs[2], 
            self.list_of_inputs[3], 
            self.list_of_inputs[4], 
            self.list_of_inputs[5], 
            self.list_of_inputs[6], 
            self.list_of_inputs[7] )
            
        self.cursor.execute( statement ) 
        return True

    def change_owner(self,owner_sin,vehicle_id,is_primary_owner):
        statement="delete from owner where vehicle_id='{}'".format(str(vehicle_id))
        self.cursor.execute(statement)
        value_statement='('+"'"+str(owner_sin)+"'"+','+"'"+str(vehicle_id)+"'"+','+"'"+str(is_primary_owner)+"'"+')'
        statement2="insert into owner values"+value_statement

        try:
            self.cursor.execute(statement2)
        except Exception as e:
            print("Error! cannot add an owner record")
        return 
