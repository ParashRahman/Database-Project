import cx_Oracle
import getpass



#Initializes a cursor against a logged in user and then returns the cursor.
#User enters username and password for a cursor

def cursor_init(server="gwynne.cs.ualberta.ca",port="1521",SID="CRS"):
	username = input("Enter your Oracle username: ");
	password = getpass.getpass("Enter password: ")
	try:
		con = cx_Oracle.connect(username + "/" + password + "@" + server + ':' + port + '/' + SID)

	except cx_Oracle.DatabaseError as e:
		error, =e.args
		print(error.code)

		if error.code==1017:
			print("Please Enter correct username/password combination")
			curs=cursor_init()


		if error.code==12541:
			print("Wrong port/SID combination.Please Enter correct 'port/SID' combination below")
			port = input("Enter correct port: ");
			SID = input("Enter correct SID: ");
			curs=cursor_init(server,port,SID)

		if error.code==12154:
			print("Please Enter correct server address")
			server = input("Enter correct server address: ");
			curs=cursor_init(server, port, SID)

		if error.code==12514:
			print("Please Enter correct SID");
			SID = input("Enter correct SID: ");
			curs=cursor_init(server, port, SID);

		return curs
	con.autocommit = 1

	curs = con.cursor()
	return curs


# Exception number of 1017 for wrong password/username, 12541 for wrong port, 12154 for wrong server address, 12514 for wrong SID



#Need to complete this function
def Auto_Transaction(global_cursor):
# 	global_cursor.execute("select * from people")
# 	rows = global_cursor.fetchall()
# 	print( rows )

# 	rows = [(1,"First"), (2,"Second"), (3,"Third")]
# 	global_cursor.bindarraysize = 3
# 	global_cursor.setinputsizes(int,20)
# 	global_cursor.executemany("insert into mytab(id, description) values (:1,:2)", rows)
# 	con.commit

# 	global_cursor.execute("SELECT * from TOFFEES")
# 	rows = global_cursor.description
# 	columnCount = len(rows)
# 	for row in rows:
# 	    print( row[0] )

	return global_cursor


def autosale_input():
	
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



# Need to complete this function
def insert_autosale(global_cursor):

	success=1

	input_err=1
	while(input_err):
		
		input_err=0
		
		try:

			[autosale_row,value_statement]=autosale_input();

		except Exception as e:
		
			input_err=1
			print("input error! Make sure you enter all the field values correctly!")



	if check_transaction_id(global_cursor,autosale_row[0])==1:

		print("This transaction Id is already present in the database. Make sure you enter a new transaction Id ")
		success=0

	if check_people_sin(global_cursor,autosale_row[1])==0:

		print("This seller Id is not present in the database. Make sure you add a new record in the people's table ")
		success=0

	if check_people_sin(global_cursor,autosale_row[2])==0:

		print("This buyer Id is not present in the database. Make sure you add a new record in the people's table ")
		success=0

	if check_vehicle_id(global_cursor,autosale_row[3])==0:

		print("This vehicle_id Id is not present in the database. Make sure you add a new record in the vehicle's table ")
		success=0

	if success==0:

		print("Sorry, your insert request is not successful")
		return global_cursor

	# print(statement)

	statement="insert into auto_sale values"+value_statement
	print(statement)

	try:

		global_cursor.execute(statement)

	except Exception as e:

		print("Error while inserting record. Make sure you have corrected the format and data types")
		insert_autosale(global_cursor)

	change_owner(global_cursor,autosale_row[2],autosale_row[3],autosale_row[6])

	return global_cursor



#Returns 1 if transaction_id is in the DB and returns 0 if not present.
def check_transaction_id(global_cursor,transaction_id):

	statement="SELECT * from auto_sale where transaction_id="+str(transaction_id)
	global_cursor.execute(statement)
	rows=global_cursor.fetchall()
	if len(rows)==0:
		return 0
	return 1




#Returns 1 if sin is in the DB and returns 0 if not present.
def check_people_sin(global_cursor,people_sin):

	statement="SELECT * from people where sin="+str(people_sin)
	global_cursor.execute(statement)
	rows=global_cursor.fetchall()
	if len(rows)==0:
		return 0
	return 1




#Returns 1 if vehicle_id is in the DB and returns 0 if not present.
def check_vehicle_id(global_cursor,vehicle_id):

	statement="SELECT * from vehicle where serial_no="+str(vehicle_id)
	global_cursor.execute(statement)
	rows=global_cursor.fetchall()
	if len(rows)==0:
		return 0
	return 1



#Returns 1 if vehicle_type_id is in the DB and returns 0 if not present.
def check_vehicle_type(global_cursor,vehicle_type_id):

	statement="SELECT * from vehicle_type where type_id="+str(vehicle_type_id)
	global_cursor.execute(statement)
	rows=global_cursor.fetchall()
	if len(rows)==0:
		return 0
	return 1


def vehicle_type_input():

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



def insert_vehicle_type(global_cursor):

	input_err=1
	while(input_err):
		
		input_err=0
		
		try:

			[vehicle_type_row,value_statement]=vehicle_type_input();

		except Exception as e:
		
			input_err=1
			print("input error! Make sure you enter the 2 field values seperated by comma correctly!")

	if check_vehicle_type(global_cursor,vehicle_type_row[0])==1:

		print("The record for this vehicle type already exists. Please enter a new one next time")
		return global_cursor


	statement="insert into vehicle_type values"+value_statement

	try:

		global_cursor.execute(statement)

	except Exception as e:

		print("Database insert error! Make sure you enter the field values with the correct data type")
		global_cursor=insert_vehicle_type(global_cursor)
	
	return global_cursor


def vehicle_input():

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

		


	value_statement="('"+str(vehicle_row[0])+"'"+','+"'"+str(vehicle_row[1])+"'"+ ',' + "'" + str(vehicle_row[2]) + "'" + ',' + str(vehicle_row[3]) + ',' + "'" + str(vehicle_row[4]) + "'" + ',' + str(vehicle_row[5]) + ')'
	return [vehicle_row,value_statement]	


#function for inserting vehicle records
def insert_vehicle(global_cursor):

	input_err=1
	while(input_err):
		
		input_err=0
		
		try:

			[vehicle_row,value_statement]=vehicle_input();

		except Exception as e:
		
			input_err=1
			print("input error! Make sure you enter the 6 field values seperated by comma correctly!")


	if check_vehicle(global_cursor,vehicle_row[0])==1:

		print("The record for this vehicle already exists. Please enter a new one next time")
		return global_cursor


	if check_vehicle_type(global_cursor,vehicle_row[5])==0:

		print("The database doesnt have any record of the vehicle type ID you entered. Please enter a record for that vehicle type ID first ")
		return global_cursor


	statement="insert into vehicle values"+value_statement

	try:

		global_cursor.execute(statement)

	except Exception as e:

		print("Database insert error! Make sure you enter the field values with the correct data type")
		global_cursor=insert_vehicle(global_cursor)
	
	return global_cursor



def people_input():

	
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


	print('got here')
	value_statement='('+"'"+str(people_row[0])+"'"+','+"'"+str(people_row[1])+"'"+','+str(people_row[2])+','+str(people_row[3])+','+"'"+str(people_row[4])+"'"+','+"'"+str(people_row[5])+"'"+','+"'"+str(people_row[6])+"'"+','+"'"+str(people_row[7])+"'"+','+"TO_DATE('" + people_row[8] + "', 'yyyy/mm/dd')"+')'
	return [people_row,value_statement]


#function for inserting people records
def insert_people(global_cursor):

	input_err=1
	while(input_err):

		input_err=0

		try:

			[people_row,value_statement]=people_input()
	
		except Exception as e:

			print(e)
			input_err=1
			print("input error! Make sure you enter the 9 field values seperated by comma correctly!")



	if check_people_sin(global_cursor,people_row[0])==1:

		print("The record for this person already exists. Please enter a new one")
		return global_cursor

	try:

		statement="insert into people values"+value_statement
		# print(statement)
		# return global_cursor
		global_cursor.execute(statement)

	except Exception as e:

		print('Insert Error!Please enter the data in the correct format and type')
		global_cursor=insert_people(global_cursor)

	return global_cursor



#Returns metadata incase the insert statement doesnt work
def change_owner(global_cursor,owner_sin,vehicle_id,is_primary_owner):

	statement="delete from owner where vehicle_id="+str(vehicle_id)
	global_cursor.execute(statement)
	value_statement='('+"'"+str(owner_sin)+"'"+','+"'"+str(vehicle_id)+"'"+','+"'"+str(is_primary_owner)+"'"+')'
	statement2="insert into owner values"+value_statement
	try:
		global_cursor.execute(statement2)
	except Exception as e:
		#Implement the metadata handling part and return the metadata in case some error occurs while inserting
		return 
	return 0



def new_vehicle_registration_input():

	print("Will check whether vehicle id and owner's sin is in the database.")
	vehicle_id=input("enter the vehicle_id: ")
	owner_sin=input("enter owner's sin: ")
	is_primary_owner=input("enter whether the owner is a primary owner: ")
	return [vehicle_id,owner_sin,is_primary_owner]


def new_vehicle_registration(global_cursor):

	[vehicle_id,owner_sin,is_primary_owner]=new_vehicle_registration_input()

	if check_people_sin(global_cursor,owner_sin)==0:

		print("There is no record of the owner and you need to fill up the 'person' table")
		insert_people(global_cursor)

	if check_vehicle_id(global_cursor,vehicle_id)==0:

		print("The vehicle is not registered. You will be taken to the vehicle registration page")
		insert_vehicle(global_cursor)

	metadata=change_owner(global_cursor,owner_sin,vehicle_id,is_primary_owner)
	#Use the metadata to find out the error and use a loop

	return global_cursor

if __name__ == "__main__":

	global_cursor=cursor_init() # !!!!!!!!!!!!!!!!  this is my own cursor init function
	# if global_cursor==0:
	# 	return


	# insert_autosale('s')
	# insert_vehicle_type(global_cursor)
	# insert_people(global_cursor)
	# insert_vehicle(global_cursor)
	insert_autosale(global_cursor)
	# return
	# print(check_people_sin(global_cursor,1))
