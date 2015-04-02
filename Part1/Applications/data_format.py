
"""
Usage: import this using "from data_format import data_formats_info". Then data_formats_info.method_name().
Contains information about the data types of fields of the respective tables. We will use these information and notify user when they make an input error
"""

class data_formats_info:

	def people():

		print("sin : string of 15 characters atmost\n"
			+ "name : string of 40 characters atmost\n"
			+ "height : a number of atmost 5 digits and 2 decimal places\n"
			+ "weight : a number of atmost 5 digits and 2 decimal places\n"
			+ "eyecolour : string of 10 characters atmost\n"
			+ "haircolour : string of 10 characters atmost\n"
			+ "addr : string of 50 characters atmost\n"
			+ "gender : 'm' or 'f'\n"
			+ "birthday : yyyy/mm/dd format")

	#Add proper information for photo field
	def drive_licence():

		print("licence_no : string of 15 characters atmost\n"
			+ "sin : string of 15 characters atmost\n"
			+ "class : string of 10 characters atmost\n")
			+ "photo : BLOB\n"
			+ "issuing_date : yyyy/mm/dd format\n"
			+ "expiring_date : yyyy/mm/dd format\n")

	def driving_condition():

		print("c_id : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n"
			+ "description : string of 1024 characters atmost\n")

	def restriction():

		print("licence_no : string of 15 characters atmost\n"
			+ "r_id : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n")

	def vehicle_type():

		print("type_id : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n"
			+ "type : string of 10 characters atmost\n")

	def vehicle():

		print("serial_no : string of 15 characters atmost\n"
			+ "maker : string of 20 characters atmost\n"
			+ "model : string of 20 characters atmost\n"
			+ "year : a whole number of 4 digits\n"
			+ "color : string of 10 characters atmost\n"
			+ "type_id : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n")

	def owner():

		print("owner_id : string of 15 characters atmost\n"
			+ "vehicle_id : string of 15 characters atmost\n"
			+ "is_primary_owner : 'y' or 'n' ")

	def auto_sale():

		print("transaction_id : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n"
			+ "seller_id : string of 15 characters atmost\n"
			+ "buyer_id : string of 15 characters atmost\n"
			+ "vehicle_id : string of 15 characters atmost\n"
			+ "s_date : yyyy/mm/dd format\n"
			+ "price : a number of upto 9 digits and 2 decimal places")

	def ticket_type():

		print("vtype : string of 10 characters atmost\n"
			+ "fine : a number of upto 5 digits and 2 decimal places")

	def ticket():

		print("ticket_no : a whole number or an integer within -2,147,483,648 to 2,147,483,647\n"
			+ "violator_no : string of 15 characters atmost\n"
			+ "vehicle_id : a string of 15 characters atmost\n"
			+ "office_no : a string of 15 characters atmost\n"
			+ "vtype : string of 10 characters atmost\n"
			+ "vdate : yyyy/mm/dd format\n"
			+ "place : a string of 20 characters atmost\n"
			+ "descriptions : a string of 1024 characters atmost\n")