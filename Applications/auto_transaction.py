from application import Application
from error_checker import ErrorChecker
from errors import InvalidDateException
import add_person
import cx_Oracle

class AutoTransaction(Application):
    def start_application(self, c):
        self.cursor = c

        self.fields = [ "Seller",
                        "Buyer",
                        "Vehicle",
                        "Date",
                        "Price" ]

        self.cursor.execute( "SELECT * FROM auto_sale" )
        self.metadata = self.cursor.description

        self.list_of_inputs = [ None for i in range( 6 )  ]

        self.generate_transaction_id( 0 )
        
        while ( True ):
            choice = self.get_option_start( 7 )

            if ( choice == 1 ):
                self.get_seller(choice)
            elif ( choice == 2 ):
                self.get_buyer(choice)
            elif ( choice == 3 ):
                self.get_vehicle_id(choice)
            elif ( choice == 4 ):
                self.get_date(choice)
            elif ( choice == 5 ):
                self.get_price(choice)
            # Register vehicle option
            elif ( choice == 6 ):
                if ( self.insert_into_database() ):
                    return    
            # Exit option
            elif ( choice == 7 ):
                return

    # helper function for start_application()
    def print_options(self, fields):
        fields_length = len(fields) 
        for i in range ( fields_length ):
            print( "[{:}] {:} {:}".format( 
                    i+1, fields[i], 
                    "EMPTY" if i < 6 and self.list_of_inputs[i+1] == None else "") )
        extra_fields = [ "Register Vehicle",
                         "Exit (Cancel auto transaction entry)" ]
        for i in range ( 2 ):
            print( "[{:}] {:}".format( 
                    fields_length + i + 1, extra_fields[i] ) ) 

    # helper function for start_application()
    def get_option_start(self, num_choices):
        self.print_options( self.fields )
        try:
            choice = int(input())
        except:
            choice = "Invalid"

        while( type( choice ) is not int 
               or choice >= num_choices + 1
               or choice <= 0 ):
            self.print_options( self.fields )
            print( "Enter a valid integer choice: " )
            try:
                choice = int( input() )
            except:
                choice = "Invalid"
        
        return choice

    ###################################
    # GENERATE TRANSACTION ID
    ###################################
    def generate_transaction_id( self, index ):
        numbers = self.cursor.execute( 
            "SELECT transaction_id FROM auto_sale" ).fetchall()
        if ( len( numbers ) == 0 ):
            self.list_of_inputs[index] = 0
        else:
            self.list_of_inputs[index] = max([ ID[0] for ID in numbers ]) + 1

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

        # initial check for if vehicle exists
        exists = False
        self.cursor.execute("SELECT serial_no FROM vehicle")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the vehicle does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the vehicle serial number " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                user_input = input("The vehicle is not in the database. "
                                   "Enter the vehicle's serial number (Enter "
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
    # GET BUYER
    ###################################
    def get_buyer(self, index):
        # initial get and check
        user_input = input("Enter the violator's SIN "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if buyer exists
        exists = False
        self.cursor.execute("SELECT SIN FROM people")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the buyer does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the buyer's SIN " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                char_answer = ""
                while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
                    char_answer = input( "The buyer is not in the database. "
                                         "Would you like to add the person? (y/n): " )
                
                if ( char_answer == 'y' ):
                    a = add_person.AddPerson()
                    a.start_application()
                    self.cursor.execute("SELECT SIN FROM people")
                    rows = self.cursor.fetchall()
                    rows = [ row[0].strip().lower() for row in rows ]

                user_input = input("Enter the buyer's SIN (Enter "
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
    # GET SELLER
    ###################################
    def get_seller( self, index ):
        # initial get and check
        user_input = input("Enter the seller's serial no  "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if seller exists
        exists = False
        self.cursor.execute("SELECT SIN FROM people")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the seller does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or not exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the seller's SIN number " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                user_input = input("The vehicle is not in the database. "
                                   "Enter the seller's SIN number (Enter "
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
    # GET DATE
    ###################################
    def get_date(self, index):
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
    # GET PRICE
    ###################################
    def get_price( self, index ):
        while ( True ):
            user_input = input("Enter the price of the vehicle "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was should be numeric with two decimal places and at most 11 digits. Example: 5.34 , 12.23 , 21.00 " )

        self.list_of_inputs[index] = "{:}".format(user_input)

    ###################################
    # INSERT INTO DATABASE
    ###################################
    def insert_into_database( self ):
        unfinished = False
        for inp in self.list_of_inputs:
            if inp == None:
                unfinished = True

        if ( unfinished ):
            print( "You have not entered all the fields" )

        char_answer = ""
        while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
            char_answer = input( "Would you like to continue? (y/n): " )

        if ( char_answer.strip().lower() == 'y' ):
            if ( self.list_of_inputs[2] != None
                 and self.list_of_inputs[3] != None ):
                self.change_owner( self.list_of_inputs[2].strip().lower(),
                                   self.list_of_inputs[3].strip().lower(),
                                   'y' )

            if ( unfinished ):
                for i in range( len( self.list_of_inputs ) ):
                    if ( self.list_of_inputs[i] == None ):
                        self.list_of_inputs[i] = "NULL"

            if ( self.list_of_inputs[4] != "NULL" ):
                self.list_of_inputs[4] = "TO_DATE({:}, {:})".format(
                    self.list_of_inputs[4][0], self.list_of_inputs[4][1] )

            # Enter data into database
            stmnt = "INSERT INTO vehicle VALUES( " + \
                "{}, {}, {}, {}, {}, {} )".format(
                self.list_of_inputs[0], 
                self.list_of_inputs[1], 
                self.list_of_inputs[2], 
                self.list_of_inputs[3],
                self.list_of_inputs[4],
                self.list_of_inputs[5] )

            print(stmnt)
            self.cursor.execute( stmnt )

            return True
        else:
            return False


    # Helper function for inserting into the database
    def change_owner(self, owner_sin,  vehicle_id, is_primary_owner):
        statement="delete from owner where vehicle_id={}".format(str(vehicle_id))
        print( statement )
        self.cursor.execute(statement)
        value_statement='('+str(owner_sin)+','+str(vehicle_id)+','+"'"+str(is_primary_owner)+"'"+')'
        statement2="insert into owner values"+value_statement

        print( statement2 )
        try:
            self.cursor.execute(statement2)
        except Exception as e:
            print("Error! cannot add an owner record")
        return 
