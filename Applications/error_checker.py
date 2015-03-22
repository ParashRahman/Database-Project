import cx_Oracle
import decimal
import datetime

class ErrorChecker:
    # to call this function import ErrorChecker and call error_checker.ErrorChecker.check_error( respective parameters )
    # returns True if data is valid
    # returns False otherwise

    """

    To check if DATETIME/DATE objects are correct: 
    meta_data_fragment: same as usual
    user_input: tuple ( DD, MM, YYYY ) where DD, MM, and YYYY are integers
    If you want to check if DD, MM, or YYYY are integers use the check_if_string_is_integer() function
    
    """
    def check_error( meta_data_fragment, user_input ):
        # Check if empty string is ok
        null_ok = meta_data_fragment[6]
        if ( null_ok and len(user_input) == 0 ):
            return True

        # Get the data_type to do the proper check
        data_type = meta_data_fragment[1]

        # Check the integer type
        if data_type == cx_Oracle.NUMBER:
            try:
                float( user_input )
            except (ValueError): 
                return False
            
            precision = meta_data_fragment[5]
            
            # integer types should not have any precision
            if ( precision == 0 ):
                float_user_input = float( user_input )
                int_user_input = int( float(user_input) )
                if ( float_user_input > int_user_input ):
                    return False
            # check if float type has proper precision
            else:
                decimal_user_input = decimal.Decimal( user_input )
                uinput_precision = decimal_user_input.as_tuple().exponent
                if ( abs ( uinput_precision ) > precision ):
                    return False

            print ( user_input + " " + str(1) )

            # integer types should correspond to the internal size
            internal_size = meta_data_fragment[4]
            if ( 10**internal_size < int( float(user_input) ) ):
                return False

        # Check string objects
        elif data_type == cx_Oracle.STRING:
            desired_length = meta_data_fragment[3]
            if ( len( user_input ) > desired_length ):
                return False
            
        # Check datetime objects
        elif data_type == cx_Oracle.DATETIME:
            try:
                dd = user_input[0]
                mm = user_input[1]
                yyyy = user_input[2]
                date = datetime.datetime( yyyy, mm, dd )
            except( ValueError ):
                return False


        return True


    def check_if_string_is_integer( string ):
        try:
            int( string )
        except( ValueError ): 
            return False
        
        return True
