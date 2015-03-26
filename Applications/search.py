from application import Application
from error_checker import ErrorChecker
from metadata import Metadata

class Search(Application):

    def start_application(self, c):
        self.cursor = c
    
    def search_id(self):
        user_input = input("Enter Driver Licence ID: ")
		user_input.strip()
	
		if( len( user_input ) == 0 ):
			return
	
		self.cursor.execute("""SELECT p.name, l.licence_no, p.addr, p.birthday, l.class, c.description, l.expiring_date
							   FROM people p, drive_licence l, driving_condition c, restriction r
							   WHERE p.sin = l.sin AND
								     l.licence_no = r.licence_no AND
									 r.r_id = c.c_id AND
									 l.licence_no =""" + user_input)

		for row in cursor:
          print(row)

    def search_name(self):
        user_input = input("Enter Driver's Name: ")
		user_input.strip()
	
		if( len( user_input ) == 0 ):
			return
	
		self.cursor.execute("""SELECT p.name, l.licence_no, p.addr, p.birthday, l.class, c.description, l.expiring_date
							   FROM people p, drive_licence l, driving_condition c, restriction r
							   WHERE p.sin = l.sin AND
								     l.licence_no = r.licence_no AND
									 r.r_id = c.c_id AND
									 p.name =""" + user_input + ";")

		for row in cursor:
          print(row)
		
    def search_violation_history(self):
        user_input = input("Enter Licence ID or SIN")         
		user_input.strip()
	
		if( len( user_input ) == 0 ):
			return
	
		self.cursor.execute("""SELECT p.name, p.sin, v.violator_no, t.ticket_no, t.vehicle_id, t.office_no, t.vtype, t.vdate, t.place, t.descriptions
							   FROM ticket t, people p
							   WHERE p.sin = t.violator_no AND
	  						   p.sin =""" + user_input + """ OR
	  						   p.name =""" + user_inputi + ";")

		for row in cursor:
          print(row)
    
	def search_vehicle(self):
        user_input = input("Enter Vehicle Serial No: ")		
		user_input.strip()
	
		if( len( user_input ) == 0 ):
			return
	
		self.cursor.execute("""
							SELECT v.serial_no, COUNT(s.transation_id), AVG(s.price), COUNT(t.icket_no)
							FROM vehicle v, auto_sale s, ticket t
							WHERE v.serial_no = s.vehicle_id AND
	  						v.serial_no = t.vehicle_id AND
	  						v.serial_no =""" + user_input + """
							GROUP BY v.serial_no;
							"""

		for row in cursor:
          print(row)

