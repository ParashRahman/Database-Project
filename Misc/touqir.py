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
	# con.autocommit = 1

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


# Need to complete this function
def insert_autosale(global_cursor):

	autosale_row=input("Enter transaction_id, seller_id, buyer_id, vehicle_id, s_date, and price, separated by comma :")
	autosale_row=autosale_row.split(',')

	# error=True
	# while (error):

	# 	try:
	# 		error=False
	# 		autosale_row[0]=int(autosale_row[0])

	# 	except ValueErrror:
	# 		error=True
	# 		autosale_row[0]=input("Enter transaction_id in the integer format :")

	statement='('+str(autosale_row[0])+','+"'"+str(autosale_row[1])+"'"+','+"'"+str(autosale_row[2])+"'"+','+"'"+str(autosale_row[3])+"'"+','+"TO_DATE('2003/05/03', 'yyyy/mm/dd')"+')'


	global_cursor.execute("SELECT * from TOFFEES")

	return global_cursor

if __name__ == "__main__":

	cursor_init()