class Metadata:

	def __init__(self,cursor):

		self.cursor=cursor
		self.meta_owner()
		self.meta_autosale()
		self.meta_restriction()
		self.meta_ticket()
		self.meta_vehicle()
		self.meta_driving_condition()
		self.meta_ticket_type()
		self.meta_vehicle_type()
		self.meta_drive_licence()
		self.meta_people()


	def meta_owner(self):

		self.cursor.execute("select * from owner")
		self.owner_metadata=self.cursor.description


	def meta_autosale(self):

		self.cursor.execute("select * from auto_sale")
		self.auto_sale_metadata=self.cursor.description


	def meta_restriction(self):

		self.cursor.execute("select * from restriction")
		self.restriction_metadata=self.cursor.description


	def meta_driving_condition(self):

		self.cursor.execute("select * from driving_condition")
		self.driving_condition_metadata=self.cursor.description


	def meta_ticket(self):

		self.cursor.execute("select * from ticket")
		self.ticket_metadata=self.cursor.description


	def meta_ticket_type(self):

		self.cursor.execute("select * from ticket_type")
		self.ticket_type_metadata=self.cursor.description


	def meta_vehicle(self):

		self.cursor.execute("select * from vehicle")
		self.vehicle_metadata=self.cursor.description


	def meta_vehicle_type(self):

		self.cursor.execute("select * from vehicle_type")
		self.vehicle_type_metadata=self.cursor.description


	def meta_drive_licence(self):

		self.cursor.execute("select * from drive_licence")
		self.drive_licence_metadata=self.cursor.description


	def meta_people(self):

		self.cursor.execute("select * from people")
		self.people_metadata=self.cursor.description



