from application import Application
from errors import InvalidDateException
from error_checker import ErrorChecker

class AddPerson(Application):
    def start_application(self, c):
        self.cursor = c
        
        self.list_of_inputs = [None for i in range(9)]
        self.cursor.execute( "SELECT * FROM people" )
        self.metadata = self.cursor.description

        self.fields = [ 'SIN',
                        'Name',
                        'Height',
                        'Weight',
                        'Eye Color',
                        'Hair Color',
                        'Address',
                        'Gender',
                        'Birthday' ]

        while ( True ):
            choice = self.get_option_start(11)

            if ( choice == 1 ):
                self.get_SIN(choice-1)
            elif ( choice == 2 ):
                self.get_name(choice-1)
            elif ( choice == 3 ):
                self.get_height(choice-1)
            elif ( choice == 4 ):
                self.get_weight(choice-1)
            elif ( choice == 5 ):
                self.get_eye_color(choice-1)
            elif ( choice == 6 ):
                self.get_hair_color(choice-1)
            elif ( choice == 7 ):
                self.get_address(choice-1)
            elif ( choice == 8 ):
                self.get_gender(choice-1)
            elif ( choice == 9 ):
                self.get_birthday(choice-1)
    
            # Insert into db option
            elif ( choice == 10 ):
                if ( self.list_of_inputs[0] == None ):
                    print( "ERROR: SIN number is required" )
                    continue
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
                    if ( unfinished ):
                        for i in range( len( self.list_of_inputs ) ):
                            if ( self.list_of_inputs[i] == None ):
                                self.list_of_inputs[i] = "NULL"
                    
                    # Enter data into database
                    stmnt = "INSERT INTO people VALUES (" \
                        "{:}, {:}, {:}, {:}, {:}, {:}, " \
                        "{:}, {:}, TO_DATE( {:}, {:} ) )".format(
                        self.list_of_inputs[0],
                        self.list_of_inputs[1],
                        self.list_of_inputs[2],
                        self.list_of_inputs[3],
                        self.list_of_inputs[4],
                        self.list_of_inputs[5],
                        self.list_of_inputs[6],
                        self.list_of_inputs[7],
                        self.list_of_inputs[8][0],
                        self.list_of_inputs[8][1] )
                
                    self.cursor.execute( stmnt )
                    return
                else:
                    continue
    
            # Exit option
            elif ( choice == 11 ):
                return

    # helper function for start_application()
    def print_options(self, fields):
        fields_length = len(fields) 
        for i in range ( fields_length ):
            print( "[{:}] {:} {:}".format( 
                    i+1, fields[i], 
                    "EMPTY" if i < 9 and self.list_of_inputs[i] == None else "") )
        extra_fields = [ "Add person to database",
                         "Exit (Cancel person entry)" ]
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
    # GET SIN
    ###################################
    def get_SIN( self, index ):
        # initial get and check
        user_input = input("Enter person's SIN "
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

        # While the input string is too long or the SIN exists
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the owner SIN " 
                                   "(Enter nothing to cancel): ")
            elif ( exists ):
                user_input = input( 
                    "The person is already in the database. "
                    "Enter the person's SIN "
                    "(Enter nothing to cancel): " )

            if ( len( user_input ) == 0 ):
                return

            if ( user_input.strip().lower() in rows ):
                exists = True
            else:
                exists = False
                
            short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        
        self.list_of_inputs[index] = "'{:}'".format(user_input.strip().lower())

    ###################################
    # GET NAME
    ###################################
    def get_name( self, index ):
        while ( True ):
            user_input = input("Enter the name of the person "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET HEIGHT
    ###################################
    def get_height( self, index ):
        pass

    ###################################
    # GET WEIGHT
    ###################################
    def get_weight( self, index ):
        pass

    ###################################
    # GET EYE COLOR
    ###################################
    def get_eye_color( self, index ):
        while ( True ):
            user_input = input("Enter the eye color of the person "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET HAIR COLOR
    ###################################
    def get_hair_color( self, index ):
        while ( True ):
            user_input = input("Enter the hair color of the person "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET ADDRESS
    ###################################
    def get_address( self, index ):
        while ( True ):
            user_input = input("Enter the address of the person "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)
    
    ###################################
    # GET GENDER
    ###################################
    def get_gender( self, index ):
        char_answer = ""
        
        while ( char_answer.strip().lower() not in [ 'm', 'f' ] ):
            char_answer = input( "Enter gender of person (m/f): " )
    
        if ( char_answer.strip().lower() == 'm' ):
            self.list_of_inputs[index] = "'{:}'".format(char_answer)
        else:
            self.list_of_inputs[index] = "'{:}'".format(char_answer)

    ###################################
    # GET BIRTHDAY
    ###################################
    def get_birthday( self, index ):
        while ( True ):
            date_input = input ( "Enter the birthday ( DD/MM/YYYY ) "
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
