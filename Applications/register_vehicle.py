from application import Application
from error_checker import ErrorChecker

class RegisterVehicle(Application):
    def start_application(self, c):
        self.cursor = c
        
        self.list_of_inputs = [ None for i in range(6) ]
        self.cursor.execute( "SELECT * FROM vehicle" )
        self.metadata= self.cursor.description
        
        self.list_of_inputs = 
    
    ###################################
    # GET SERIAL NO.
    ###################################
    def get_serial_no(self, index):
        # initial get and check
        user_input = input("Enter the vehicle's serial "
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

        # While the input string is too long or the violator does not exist
        short_enough = ErrorChecker.check_error(self.metadata[index], user_input)
        while ( not short_enough or exists):
            if ( not short_enough ):
                user_input = input("Your input was too long. "
                                   "Enter the vehicle's serial " 
                                   "(Enter nothing to cancel): ")
            elif ( exists ):
                user_input = input( 
                    "The vehicle is already in the database. "
                    "Enter the vehicle's serial "
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
    # GET VEHICLE MAKER
    ###################################
    def get_vehicle_maker(self, index):

        while ( True ):
            user_input = input("Enter the maker of the vehicle "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET VEHICLE MODEL
    ###################################
    def get_vehicle_model(self, index):

        while ( True ):
            user_input = input("Enter the model of the vehicle "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET VEHICLE YEAR
    ###################################
    def get_vehicle_year( self, index ):
        user_input = input( "Enter the year of the vehicle: " )
        while ( not ErrorChecker.check_error( 
                self.metadata[index], user_input.strip() ) ):
            user_input = input( 
                "Your year input was invalid. Enter the year of the vehicle." )

        if ( len( user_input.strip() > 0 ) ):
            self.list_of_inputs[index] = user_input

    
    ###################################
    # GET VEHICLE COLOR
    ###################################
    def get_vehicle_color(self, index):

        while ( True ):
            user_input = input("Enter the color of the vehicle "
                               "(Enter nothing to cancel): ")
            if ( len( user_input ) == 0 ):
                return

            if ( ErrorChecker.check_error( self.metadata[index], user_input ) ):
                break
            else:
                print( "Your input was too long" )

        self.list_of_inputs[index] = "'{:}'".format(user_input)

    ###################################
    # GET VEHICLE TYPE
    ###################################
    def get_vehicle_type( self, index ):
        self.print_vehicle_types()
        

    # Helper function for get_vehicle_type(self, index)
    def print_vehicle_types( self ):
        self.cursor.execute( "SELECT type FROM vehicle_type" )
        list_of_types = self.cursor.fetchall()
        prompt_types = [ row[0] for row in list_of_types ]
        for i in range( len( prompt_types ) ):
            print ( "[{:}] {:}".format( i, prompt_types[i] )

