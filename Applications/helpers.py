import cx_Oracle
import getpass
from metadata import Metadata
from data_format import data_formats_info
from error_checker import ErrorChecker

"""

Methods in this class:

check_transaction_id: For checking if a transaction_id is already in the autosale table or not

check_people_sin : For checking whether a people sin is already in the people table or not

check_vehicle_id : For checking whether a vehicle ID is already in the vehicle table or not

check_vehicle_type : For checking whether a vehicle type is already in the vehicle type table or not

autosale_input : For taking user input specific to autosale table record entry

vehicle_type_input : For taking user input specific to vehicle_type table record entry

vehicle_input : For taking user input specific to vehicle table record entry 

people_input : For taking user input specific to people table record entry

new_vehicle_registration_input : For taking user input specific to owner table record entry

insert_autosale : Inserts autosale records after taking user input using autosale_input

insert_people : Inserts people records after taking user input using people_input

insert_vehicle : Inserts vehicle records after taking user input using vehicle_input

insert_vehicle_type : Inserts vehicle type records after taking user input using vehicle_type_input

change_owner : Accepts [vehicle ID, owner ID, is_primary_owner] tuple and then deletes any entries of that vehicle in the owner table and then inserts the record in the tuple

new_vehicle_registration : Performs new_vehicle_registration task assigned in the project using change_owner and new_vehicle_registration_input methods

date_parse_error : Takes in datetime data in the string format.Returns True if there is no error in the datatime format otherwise False


"""
class Helpers:


	def __init__(self, cursor, metadata):

		self.cursor=cursor
		self.metadata=metadata


#***************************************************************************************************



	#  ********   Table checking methods    *************



	#Returns 1 if transaction_id is in the DB and returns 0 if not present.
	def check_transaction_id(self,transaction_id):

		statement="SELECT * from auto_sale where transaction_id="+str(transaction_id)
		self.cursor.execute(statement)
		rows=self.cursor.fetchall()
		if len(rows)==0:
			return 0
		return 1




	#Returns 1 if sin is in the DB and returns 0 if not present.
	def check_people_sin(self,people_sin):

		statement="SELECT * from people where sin="+str(people_sin)
		self.cursor.execute(statement)
		rows=self.cursor.fetchall()
		if len(rows)==0:
			return 0
		return 1




	#Returns 1 if vehicle_id is in the DB and returns 0 if not present.
	def check_vehicle_id(self,vehicle_id):

		statement="SELECT * from vehicle where serial_no="+str(vehicle_id)
		self.cursor.execute(statement)
		rows=self.cursor.fetchall()
		if len(rows)==0:
			return 0
		return 1



	#Returns 1 if vehicle_type_id is in the DB and returns 0 if not present.
	def check_vehicle_type(self,vehicle_type_id):

		statement="SELECT * from vehicle_type where type_id="+str(vehicle_type_id)
		self.cursor.execute(statement)
		rows=self.cursor.fetchall()
		if len(rows)==0:
			return 0
		return 1




#*************************************************************************************************



	#  ********    User Input methods    *************



	def autosale_input(self):

		autosale_row=["None"]*7
		fields=["transaction_id","seller_id","buyer_id","vehicle_id","s_date(yyyy/mm/dd)","price","is_primary_owner"]
		while(1):
			i=input("Type 1 for transaction_id, 2 for seller_id, 3 for buyer_id, 4 for vehicle_id, 5 for s_date(yyyy/mm/dd), 6 for price, 7 for is_primary_owner,8 for checking what you have entered, 9 for finalizing : ")
			i.strip()
			try:
				i=int(i)
			except Exception as e:
				continue
			i=i-1

			#for finalizing
			if i==(9-1):
				break

			#For displaying
			elif i==(8-1):
				j=0
				for value in fields:
					print(value+" : "+str(autosale_row[j]))
					j=j+1


			#loading in input field values
			else:

				try:
					autosale_row[i]=input(fields[i]+" : ")

				except Exception as e:
					continue


		value_statement='('+str(autosale_row[0])+','+"'"+str(autosale_row[1])+"'"+','+"'"+str(autosale_row[2])+"'"+','+"'"+str(autosale_row[3])+"'"+','+"TO_DATE('" + autosale_row[4] + "', 'yyyy/mm/dd'),"+autosale_row[5]+')'

		return [autosale_row,value_statement]





	def vehicle_type_input(self):

		vehicle_type_row=[None]*2
		fields=["type_id","type"]
		while(1):
			i=input("Press 1 for type_id, 2 for type, 3 for checking what you have entered, 4 for finalizing : ")
			i.strip()
			try:
				i=int(i)
			except Exception as e:
				continue
			i=i-1

			#for finalizing
			if i==(4-1):
				break

			#For displaying
			elif i==(3-1):
				j=0
				for value in fields:
					print(value+" : "+str(vehicle_type_row[j]))
					j=j+1


			#loading in input field values
			else:

				try:
					vehicle_type_row[i]=input(fields[i]+" : ")

				except Exception as e:
					continue


		value_statement='('+str(vehicle_type_row[0])+','+"'"+str(vehicle_type_row[1])+"'"+')'
		return [vehicle_type_row,value_statement]






	def vehicle_input(self):

		# vehicle_row=input("Enter serial_no,maker,model,year,color and type_id. Seperate them by comma: ")
		vehicle_row=[None]*6
		fields=["serial_no","maker","model","year","colour","type_id"]
		while(1):
			i=input("Press 1 for serial_no, 2 for maker, 3 for model, 4 for year, 5 for color and 6 for type_id and 7 if you want to check what you entered: ")
			i.strip()
			try:
				i=int(i)
			except Exception as e:
				continue

			i=i-1

			#For finalizing
			if i==(8-1):
				break

			#For displaying
			elif i==(7-1):
				j=0
				for value in fields:
					print(value+" : "+str(vehicle_row[j]))
					j=j+1


			else:
				#loading in input field values
				try:
					vehicle_row[i]=input(fields[i]+" : ")

				except Exception as e:
					continue





	def people_input(self):


		people_row=["None"]*9
		fields=["sin", "name", "height","weight","eyecolor", "haircolor","addr","gender","birthday"]
		while(1):
			i=input("Press 1 for sin, 2 for name, 3 for height, 4 for weight, 5 for eyecolor, 6 for haircolor, 7 for addr, 8 for gender, 9 for birthday, 10 for checking what you have entered, 11 for finalizing: ")
			i.strip()
			try:
				i=int(i)
			except Exception as e:
				continue
			i=i-1

			#for finalizing
			if i==(11-1):
				break

			#For displaying
			elif i==(10-1):
				j=0
				for value in fields:
					print(value+" : "+str(people_row[j]))
					j=j+1


			else:
				#loading in input field values
				try:
					people_row[i]=input(fields[i]+" : ")

				except Exception as e:
					continue


		# print('got here')
		value_statement='('+"'"+str(people_row[0])+"'"+','+"'"+str(people_row[1])+"'"+','+str(people_row[2])+','+str(people_row[3])+','+"'"+str(people_row[4])+"'"+','+"'"+str(people_row[5])+"'"+','+"'"+str(people_row[6])+"'"+','+"'"+str(people_row[7])+"'"+','+"TO_DATE('" + people_row[8] + "', 'yyyy/mm/dd')"+')'
		return [people_row,value_statement]




	def new_vehicle_registration_input(self):

		print("Will check whether vehicle id and owner's sin is in the database.")
		vehicle_id=input("enter the vehicle_id: ")
		owner_sin=input("enter owner's sin: ")
		is_primary_owner=input("enter whether the owner is a primary owner (y/n): ")
		return [vehicle_id,owner_sin,is_primary_owner]




#*************************************************************************************************



	#  ********    Insert table methods    *************




	def insert_autosale(self):

		success=1

		input_err=1

		while(input_err or correct!=True):

			input_err=0

			try:

				[autosale_row,value_statement]=self.autosale_input();

				if (ErrorChecker.check_error(self.metadata.auto_sale_metadata,autosale_row[0:4]+autosale_row[5]) and date_parse_error(self.metadata.auto_sale_metadata,autosale_row[4])):
					
					correct=True
			
				else:
			
					correct=False
		
				if (correct!=True):
		
					print("Please enter the data in the correct format")
					data_formats_info.auto_sale()

			except Exception as e:

				input_err=1
				print("input error! Make sure you enter all the field values correctly!")

			carry_on=input("type 'y' if you want to continue or 'n' if you want to stop adding a record (y/n): ")

			if carry_on=='n':
				
				return




		if self.check_transaction_id(autosale_row[0])==1:

			print("This transaction Id is already present in the database. Make sure you enter a new transaction Id ")
			success=0

		if self.check_people_sin(autosale_row[1])==0:

			print("This seller Id is not present in the database. Make sure you add a new record in the people's table ")
			success=0

		if self.check_people_sin(autosale_row[2])==0:

			print("This buyer Id is not present in the database. Make sure you add a new record in the people's table ")
			success=0

		if self.check_vehicle_id(autosale_row[3])==0:

			print("This vehicle_id Id is not present in the database. Make sure you add a new record in the vehicle's table ")
			success=0

		if success==0:

			print("Sorry, your insert request is not successful")
			return

		# print(statement)

		statement="insert into auto_sale values"+value_statement
		# print(statement)

		try:

			self.cursor.execute(statement)

		except Exception as e:

			print("Error while inserting record. Make sure you have corrected the format and data types")
			self.insert_autosale()

		self.change_owner(autosale_row[2],autosale_row[3],autosale_row[6])

		return





	def insert_vehicle_type(self):

		input_err=1

		while(input_err or correct!=True):

			input_err=0

			try:

				[vehicle_type_row,value_statement]=self.vehicle_type_input();
				correct=ErrorChecker.check_error(self.metadata.vehicle_type_metadata,vehicle_type_row)
				
				if (correct!=True):

					print("Please enter the data in the correct format")
					data_formats_info.vehicle_type()

			except Exception as e:

				input_err=1
				print("input error! Make sure you enter the 2 field values seperated by comma correctly!")

			carry_on=input("type 'y' if you want to continue or 'n' if you want to stop adding a record (y/n): ")

			if carry_on=='n':
				
				return


		if self.check_vehicle_type(vehicle_type_row[0])==1:

			print("The record for this vehicle type already exists. Please enter a new one next time")
			return


		statement="insert into vehicle_type values"+value_statement

		try:

			self.cursor.execute(statement)

		except Exception as e:

			print("Database insert error! Make sure you enter the field values with the correct data type")
			self.insert_vehicle_type()

		return





	def insert_vehicle(self):

		input_err=1
		while(input_err or correct!=True):

			input_err=0

			try:

				[vehicle_row,value_statement]=self.vehicle_input();
				correct=ErrorChecker.check_error(self.metadata.vehicle_metadata,vehicle_row)
				
				if (correct!=True):

					print("Please enter the data in the correct format")
					data_formats_info.vehicle()


			except Exception as e:

				input_err=1
				print("input error! Make sure you enter the 6 field values seperated by comma correctly!")

			carry_on=input("type 'y' if you want to continue or 'n' if you want to stop adding a record (y/n): ")

			if carry_on=='n':
				
				return



		if self.check_vehicle(vehicle_row[0])==1:

			print("The record for this vehicle already exists. Please enter a new one next time")
			return


		if self.check_vehicle_type(vehicle_row[5])==0:

			print("The database doesnt have any record of the vehicle type ID you entered. Please enter a record for that vehicle type ID first ")
			return


		statement="insert into vehicle values"+value_statement

		try:

			self.cursor.execute(statement)

		except Exception as e:

			print("Database insert error! Make sure you enter the field values with the correct data type")
			self.insert_vehicle()

		return





	def insert_people(self):

		input_err=1
		while(input_err or correct!=True):

			input_err=0

			try:

				[people_row,value_statement]=self.people_input()

				if (ErrorChecker.check_error(self.metadata.people_metadata,people_row[0:8]) and date_parse_error(self.metadata.people_metadata,people_row[8])):
					
					correct=True
			
				else:
			
					correct=False
		
				if (correct!=True):
		
					print("Please enter the data in the correct format")
					data_formats_info.people()


			except Exception as e:

				print(e)
				input_err=1
				print("input error! Make sure you enter the 9 field values seperated by comma correctly!")

			carry_on=input("type 'y' if you want to continue or 'n' if you want to stop adding a record (y/n): ")

			if carry_on=='n':
				
				return



		if self.check_people_sin(people_row[0])==1:

			print("The record for this person already exists. Please enter a new one")
			return

		try:

			statement="insert into people values"+value_statement
			# print(statement)
			# return self.cursor
			self.cursor.execute(statement)

		except Exception as e:

			print('Insert Error!Please enter the data in the correct format and type')
			self.insert_people()

		return




	def change_owner(self,owner_sin,vehicle_id,is_primary_owner):

		statement="delete from owner where vehicle_id="+str(vehicle_id)
		self.cursor.execute(statement)
		value_statement='('+"'"+str(owner_sin)+"'"+','+"'"+str(vehicle_id)+"'"+','+"'"+str(is_primary_owner)+"'"+')'
		statement2="insert into owner values"+value_statement
		
		try:

			self.cursor.execute(statement2)

		except Exception as e:

			print("Error! cannot add an owner record")

		return 




	def new_vehicle_registration(self):


		while(correct!=True):

			[vehicle_id,owner_sin,is_primary_owner]=self.new_vehicle_registration_input()
			correct=ErrorChecker.check_error(self.metadata,[vehicle_id,owner_sin,is_primary_owner])
			
			if (correct!=True):

				print("Please enter the data in the correct format")
				data_formats_info.owner()


		p_sin=True
		v_id=True


		while(p_sin and v_id):

			carry_on=input("type 'y' if you want to continue or 'n' if you want to stop new_vehicle_registration here (y/n): ")

			if carry_on=='n':
				
				break


			if self.check_people_sin(owner_sin)==0:

				p_sin=False
				
				fill_people=input("There is no record of the owner and you need to fill up the 'person' table. Do you want to fill in now? (y/n): ")
				
				if fill_people=='y':
					
					self.insert_people()

			if self.check_vehicle_id(vehicle_id)==0:

				v_id=False
				
				print("The vehicle is not registered. Do you want to register vehicle now? (y/n): ")
				
				if fill_vehicle=='y':
					
					self.insert_vehicle()



		self.change_owner(owner_sin,vehicle_id,is_primary_owner)

		return



	#takes in date string of format yyyy/mm/dd and returns a tuple like (dd,mm,yyyy)
	def date_parse_error(self, meta, date_string):

		correct=False
		try:

			date_tuple=( int(data_string[0:4]) , int(date_string[5:7]) , int(date_string[8:10]) )

			correct=ErrorChecker.check_error(meta,date_tuple)

		except ValueError:

			print("date string doesnt contain number or not in the correct data format")
			return correct

		return correct

