import cx_Oracle

class Helpers:
    def __init__ (self, curs ):
        self.cursor = curs

#############################
# Table Checking Methods
# - Each take in respective integeres
# - Returns True or False depending on
#   the id is already there
#############################

    def check_transaction_id( self, transaction_id ):
        statement = "SELECT * from auto_sale where transaction_id="+str(transaction_id)
	self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            return False
        return True

    def check_people_sin( self, people_sin ):
        statement = "SELECT * from people where sin="+str(people_sin)
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        if len(rows)==0:
            return False
        return True

    def check_vehicle_id( self, vehicle_id ):
        statement="SELECT * from vehicle where serial_no="+str(vehicle_id)
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        if len(rows)==0:
            return False
        return True

    # takes in an integer owner_sin, vehicle_id
    # takes in a string is_primary_owner
    def change_owner(self, owner_sin, vehicle_id, is_primary_owner):
        statement = "delete from owner where vehicle_id="+str(vehicle_id)
        self.cursor.execute(statement)
        value_statement = "( '" + str(owner_sin) + "', '" + \
            str(vehicle_id) + "', '" + \
            str(is_primary_owner) + "' )"
        statement2 = "insert into owner values" + value_statement
        try:
            self.cursor.execute(statement2)
        except Exception as e:
            print("Error! cannot add an owner record")
        return 
