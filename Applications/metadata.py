class Metadata:

	def __init__(self,cursor):
		self.cursor = cursor

	def meta_owner(self):
		self.cursor.execute("select * from owner")
		return self.cursor.description


	def meta_autosale(self):
		self.cursor.execute("select * from auto_sale")
		return self.cursor.description


	def meta_restriction(self):
		self.cursor.execute("select * from restriction")
		return self.cursor.description


	def meta_driving_condition(self):
		self.cursor.execute("select * from driving_condition")
		return self.cursor.description


	def meta_ticket(self):
		self.cursor.execute("select * from ticket")
		return self.cursor.description


	def meta_ticket_type(self):
		self.cursor.execute("select * from ticket_type")
		return self.cursor.description


	def meta_vehicle(self):
		self.cursor.execute("select * from vehicle")
		return self.cursor.description


	def meta_vehicle_type(self):
		self.cursor.execute("select * from vehicle_type")
		return self.cursor.description


	def meta_drive_licence(self):
		self.cursor.execute("select * from drive_licence")
		return self.cursor.description


	def meta_people(self):
		self.cursor.execute("select * from people")
		return self.cursor.description



