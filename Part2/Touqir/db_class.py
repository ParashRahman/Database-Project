#Python 3 code!!!!!


import bsddb3 as bsddb
from bisect import bisect_left

Database="cstudents.db"

db=bsddb.hashopen(Database, 'c') #creates a hash db in file "cstudents.db"

# db=bsddb.btopen(Database,'c') #creates a B-Tree DB

# db=bsddb.rnopen(Database,'c') #creates a record format file 


#Below is the code for inserting
print(type(db))

sid="123"
Name="James"
db[sid]=Name

#For retrieval, below is the code

sid="123"

if db.has_key(sid):
	
	name=db[sid]
	print ("name:{} corresponds to sid:{}".format(name,sid))

else:

	print("sid:{} doesnt exist".format(sid))

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



	#Retrieves records based on key search
	def retrieve_using_key(self,keys):

		records=[] #list containing tuples of key-value pair

		#Iterates through all the keys and then sees if the key is present in db. 
		#If a key is present, then the record corresponding to the key is appended to record.
		
		for key in keys:

			if self.db.has_key(key):
			
				records.append((key,self.db[key]))

		return records





	#Retrieves records containing the input data_values fed
	def retrieve_using_data_values(self, data_values):

		size_db=len(self.db) #Number of records in db

		records=[] #Will return this list containing all the records that has the given input data_values

		#The loops below searches through the db dictionary to compare the records with the given input data_values


		#Iterates through given input data_values
		for data_value in data_values:

			#Iterates through the all the records in the db
			for count in range(size_db):

				if count==0:

					current_record=self.db.first() #current record points to the record being currently compared with the data_value

					#If the current record matches the current data_value, then that record is appended in the record list
					if current_record[1]==data_value:
						
						records.append(current_record)

				else:

					current_record=self.db.next() #current record points to the record being currently compared with the data_value

					#If the current record matches the current data_value, then that record is appended in the record list										
					if current_record[1]==data_value:		

						records.append(current_record)

		return records




	#Retrieves records based on range search
	def retrieve_range(self,low_key,high_key):

		#Gets the list of db's keys which is sorted and then finds out the position of the high and low key in that list.
		#Once found, it uses a loop to extract the records corresponding to the keys in that high-low key range.
		
		key_list=self.db.keys()

		records=[]

		#Finding out the position of the low key in key_list
		[low_pos,low_found]=binary_search(key_list,low_key)
		
		#Finding out the position of the high key in key_list
		[high_pos,high_found]=binary_search=(key_list,high_key)

		if high_found==False:

			high_pos=high_pos-1

		index=low_pos #setting loop index
		
		while True:

			key=key_list[index]
			records.append(self.db[key])
			
			if index==high_key:
				break

			index+=1

		return key_list

	def insert(self):



		return



	#Returns a list with variables telling you wether key is found in the list and if found tells you position.
	#Otherwise it gives out the position of the immediate latter key and also tells you that original key was not found using "found" variable.
	def binary_search(self,key_list,key,low=0,high=len(key_list)):

		found=False #Flag which tells if key is found or not
		position = bisect_left(key_list,key,low,high)
		
		if key_list[position]==key:
			found=True

		return [position,found]