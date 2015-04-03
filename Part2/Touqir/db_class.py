#Python 2.7 code!!!!!


import bsddb

Database="cstudents.db"

db=bsddb.hashopen(Database, 'c') #creates a hash db in file "cstudents.db"

# db=bsddb.btopen(Database,'c') #creates a B-Tree DB

# db=bsddb.rnopen(Database,'c') #creates a record format file 


#Below is the code for inserting
print type(db)

sid="123"
Name="James"
db[sid]=Name

#For retrieval, below is the code

sid="123"

if db.has_key(sid):
	
	name=db[sid]
	print "name:{} corresponds to sid:{}".format(name,sid)

else:

	print "sid:{} doesnt exist".format(sid)

#For deleting a key/data pair:

del db[sid]
db.sync()

#For closing Database

db.close()


#This is the parent class for searching, inserting records. Child classes will have to call the DB class's constructor and pass onto it the initialized db_object(B_tree,hashtable,etc)
class DB:


	parse_letter=":::"

	def __init__(self, db_obj):

		self.db=db_obj

		return

		

	def record_parser(self,records):
		
		return records.split(parse_letter)


	def retrieve_using_key(self,keys):

		key_values=[] #list containing tuples of key-value pair

		for key in keys:

			if self.db.has_key(key):
			
				key_values.append((key,self.db[key]))

		return key_values


	def retrieve_using_data_values(self, data_values):

		size_db=len(self.db) #Number of records in db

		records=[]

		for data_value in data_values:

			for count in range(size_db):

				if count==0:

					if 
					records.append()

		return 

	def retrieve_range(self):

		return

	def insert(self):



		return