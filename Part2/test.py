import bsddb
from timer import timer
from DB import DB
from hash_table import HashTable
from b_tree import BTree
from choose_populate import ChoosePopulate


def wrapper(function, *args, **kwargs):

	def wrapped():

		return function(*args, **kwargs)

	return wrapped


if __name__ == "__main__":

	BTree_obj=BTree("B_tree.db")
	hash_table_obj=HashTable("Hash_table.db")

	populating_obj=ChoosePopulate([BTree_obj,hash_table_obj,None])
	populating_obj.generate_data(10000)

	while True:

		if populating_obj.start_application()==False:
			
			break
		

	# testing_keys=[populating_obj.vals[75][0],populating_obj.vals[7][0],populating_obj.vals[432][0],populating_obj.vals[857][0],populating_obj.vals[293][0]] #I randomly chose them

	testing_keys=["75","7","432","857","293"]
	testing_values=["a","b","g"]
	range_keys=["82","943"]
	
	# print "Records from B_tree key search: "

	# print BTree_obj.retrieve_using_key(testing_keys)

	# print "Records from Hashtable key search: "

	# print hash_table_obj.retrieve_using_key(testing_keys)

	# print "Records from B_tree value search:"

	# print BTree_obj.retrieve_using_data_values(testing_values)

	# print "Records from hashtable_tree value search:"

	# print hash_table_obj.retrieve_using_data_values(testing_values)

	# print "Records from B_tree range search : "

	# print  BTree_obj.retrieve_range_btree(range_keys[0],range_keys[1])

	# print "Records from hashtable range search : "

	# print  hash_table_obj.retrieve_range_hash(range_keys[0],range_keys[1])

	names=["Records from B_tree key search: ","Records from Hashtable key search: ","Records from B_tree value search:","Records from hashtable_tree value search:","Records from B_tree range search : ","Records from hashtable range search : "]

	functions=[]
	
	wrapped=wrapper(BTree_obj.retrieve_using_key,testing_keys)
	functions.append(wrapped)

	wrapped=wrapper(hash_table_obj.retrieve_using_key,testing_keys)
	functions.append(wrapped)

	wrapped=wrapper(BTree_obj.retrieve_using_data_values,testing_values)
	functions.append(wrapped)

	wrapped=wrapper(hash_table_obj.retrieve_using_data_values,testing_values)
	functions.append(wrapped)

	wrapped=wrapper(BTree_obj.retrieve_range_btree,range_keys[0],range_keys[1])
	functions.append(wrapped)

	wrapped=wrapper(hash_table_obj.retrieve_range_hash,range_keys[0],range_keys[1])
	functions.append(wrapped)

	# wrapped=wrapper(BTree_obj.retrieve_using_key,testing_keys)
	# functions.append(wrapped)


	# functions=[BTree_obj.retrieve_using_key(testing_keys), hash_table_obj.retrieve_using_key(testing_keys), BTree_obj.retrieve_using_data_values(testing_values), hash_table_obj.retrieve_using_data_values(testing_values), BTree_obj.retrieve_range_btree(range_keys[0],range_keys[1]), hash_table_obj.retrieve_range_hash(range_keys[0],range_keys[1])]

	no_times=[1,1,1,1,1,1]

	[execution_time,names]=timer(functions,names,no_times)