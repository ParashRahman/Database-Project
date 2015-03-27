from application import Application
from error_checker import ErrorChecker
from errors import InvalidDateException
import add_person
import cx_Oracle

class RegisterLicense(Application):
    def start_application(self, c):
        self.cursor = c

        self.list_of_inputs = [None for i in range(6)]
        self.cursor.execute( "SELECT * FROM drive_licence" )
        self.metadata = self.cursor.description

        self.fields = [ "License no.",
                        "Person's SIN",
                        "License Class",
                        "Photograph",
                        "Issuing Date",
                        "Expiring Date" ]
        
        while( True ):
            choice = self.get_option_start( 8 )
            
            if ( choice == 1 ):
                self.get_license_no(choice-1)
            elif ( choice == 2 ):
                self.get_SIN(choice-1)
            elif ( choice == 3 ):
                self.get_license_type(choice-1)
            elif ( choice == 4 ):
                self.get_photograph(choice-1)
            elif ( choice == 5 ):
                self.get_issuing_date(choice-1)
            elif ( choice == 6 ):
                self.get_expiry_date(choice-1)
            # Register license option
            elif ( choice == 7 ):
                if ( self.enter_into_database() ):
                    return
            # Exit option
            elif ( choice == 8 ):
                return
        
    # helper function for start_application()
    def print_options(self, fields):
        fields_length = len(fields) 
        for i in range ( fields_length ):
            print( "[{:}] {:} {:}".format( 
                    i+1, fields[i], 
                    "EMPTY" if i < 6 and self.list_of_inputs[i] == None else "") )
        extra_fields = [ "Register License",
                         "Exit (Cancel license entry)" ]
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
    # GET LICENSE NO
    ###################################
    def get_license_no(self, index):
        # initial get and check
        user_input = input("Enter the license number "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if license exists
        exists = False
        self.cursor.execute("SELECT licence_no FROM drive_licence")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # While the input string is too long or the license exists
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the license no. " 
                                   "(Enter nothing to cancel): ")
            elif ( exists ):
                user_input = input("The license is in the database. "
                                   "Enter the license no. (Enter "
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
    # GET LICENSE TYPE
    ###################################
    def get_license_type(self, index):
        pass

    ###################################
    # GET PHOTOGRAPH
    ###################################
    def get_photograph(self, index):
        name = input( "Enter name of file with extension: " ).strip()
        self.list_of_inputs[index] = name

    ###################################
    # GET SIN NUMBER
    ###################################
    def get_SIN(self, index):
        # initial get and check
        user_input = input("Enter the person's SIN "
                           "(Enter nothing to cancel): ")

        # initial check if user wants to cancel
        if ( len( user_input ) == 0 ):
            return

        # initial check for if person exists
        exists = False
        self.cursor.execute("SELECT SIN FROM people")
        rows = self.cursor.fetchall()
        rows = [ row[0].strip().lower() for row in rows ]
        if ( user_input.strip().lower() in rows ):
            exists = True

        # initial check for if person has license
        person_licensed = False
        if ( exists ):
            licences = self.cursor.execute( 
                "SELECT * FROM drive_licence WHERE SIN = {}"
                .format( user_input.strip().lower() ) ).fetchall()
            if ( len( licences ) > 0 ):
                person_licensed = True

        # initial check for if number is short enough
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        # While the input string is too long or the person does not exist
        # or the person has a license
        while ( not short_enough or not exists or person_licensed ):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the person's SIN " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                char_answer = ""
                while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
                    char_answer = input( "The person is not in the database. "
                                         "Would you like to add the person? (y/n): " )
                
                if ( char_answer == 'y' ):
                    a = add_person.AddPerson()
                    a.start_application(self.cursor)
                    self.cursor.execute("SELECT SIN FROM people")
                    rows = self.cursor.fetchall()
                    rows = [ row[0].strip().lower() for row in rows ] 

                user_input = input("Enter the person's SIN (Enter "
                                   "nothing to cancel): ")
            
            elif ( person_licensed ):
                print( "ERROR: person is licensed. " )
                user_input = input("Enter the person's SIN (Enter "
                                   "nothing to cancel): ")

            # Check if user wants to cancel
            if ( len( user_input ) == 0 ):
                return

            # Check if person exists
            if ( user_input.strip().lower() in rows ):
                exists = True
                # Check if person is licensed
                licences = self.cursor.execute( 
                    "SELECT * FROM drive_licence WHERE SIN = {}"
                    .format( user_input.strip().lower() ) ).fetchall()
                if ( len( licences ) > 0 ):
                    person_licensed = True
                else:
                    person_licensed = False
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = user_input.strip().lower()

    ###################################
    # GET EXPIRY DATE
    ###################################
    def get_expiry_date( self, index ):
        while ( True ):
            date_input = input ( "Enter the expiry date ( DD/MM/YYYY ) "
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
            self.list_of_inputs[index] = "{:}/{:}/{:}".format(d,m,y) 


    ###################################
    # GET ISSUING DATE
    ###################################
    def get_issuing_date( self, index ):
        while ( True ):
            date_input = input ( "Enter the issuing date ( DD/MM/YYYY ) "
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
            self.list_of_inputs[index] = "{:}/{:}/{:}".format(d,m,y) 

    ###################################
    # ENTER INTO DATABASE
    ###################################
    def enter_into_database( self ):
        # check if license no. is None
        if ( self.list_of_inputs[0] == None ):
            print( "ERROR: Driver License No. is required" )
            return False
        
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
            # Fix up photo
            if ( self.list_of_inputs[3] != None ):
                f_image = open( self.list_of_inputs[3], 'rb' )
                photo = f_image.read()
            self.cursor.setinputsizes(photo=cx_Oracle.BLOB)
            if ( self.list_of_inputs[3] != None ): 
                f_image.close()
            else:
                photo = ""

            insert = """insert into drive_licence(licence_no, sin, class, photo, issuing_date, expiring_date) 
values ( :licence_no, :sin, :class, :photo, to_date(:issuing_date, 'DD/MM/YYYY'), to_date(:expiring_date, 'DD/MM/YYYY') )"""
            self.cursor.execute(
                insert, {'licence_no':self.list_of_inputs[0],
                         'sin':self.list_of_inputs[1],
                         'class':self.list_of_inputs[2],
                         'photo':photo,
                         'issuing_date':self.list_of_inputs[4],
                         'expiring_date':self.list_of_inputs[5]
                         } )
            return True
        else:
            return False
