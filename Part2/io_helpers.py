class IOHelpers:
    @staticmethod
    def get_input( max_option, min_option = 1 ):
        while ( True ):
            try:
                user_input = raw_input( "Enter a valid option number: ")
                user_input = int ( user_input )
                if ( user_input >= min_option and 
                     user_input <= max_option ):
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print( "Enter a valid option: " )
