from application import Application

class AutoTransaction(Application):
    def start_application(self, c):
        self.cursor = c

        self.fields = [ "Seller",
                        "Buyer",
                        "Vehicle",
                        "Date",
                        "Price",
                        "Is Primary Owner?" ]

        self.list_of_inputs = [ None for i in range( 7 )  ]

        generate_transaction_id( 0 )

    ###################################
    # GENERATE TRANSACTION ID
    ###################################
    def generate_transaction_id( self, index ):
        numbers = self.cursor.execute( "SELECT transaction_id FROM auto_sale" )
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
    # GET BUYER
    ###################################
    def get_buyer(self, index):
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
                                   "Enter the buyer's SIN " 
                                   "(Enter nothing to cancel): ")
            elif ( not exists ):
                char_answer = ""
                while ( char_answer.strip().lower() not in [ 'y', 'n' ] ):
                    char_answer = input( "The buyer is not in the database. "
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
        
        self.list_of_inputs[index] = "'{:}'".format(user_input.strip().lower())
