import cx_Oracle

class ErrorChecker:
    def check_error( meta_data_fragment, user_input ):
        # First check if the types are valid
        data_type = meta_data_fragment[1]
        if type(data_type) == cx_Oracle.NUMBER:
            try:
                int( user_input )
            except (ValueError): 
                return False

        
