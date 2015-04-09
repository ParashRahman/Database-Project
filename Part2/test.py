import bsddb
from timer import timer
from DB import DB
from hash_table import HashTable
from b_tree import BTree
from choose_populate import ChoosePopulate

if __name__ == "__main__":

	BTree_obj=BTree("B_tree.db")
	hash_table_obj=HashTable("Hash_table.db")

	populating_obj=ChoosePopulate([BTree_obj,hash_table_obj,None])
	populating_obj.generate_data()

	while (populating_obj.start_application()==False):

		pass

	testing_keys=[populating_obj.vals[75][0],populating_obj.vals[7][0],populating_obj.vals[432][0],populating_obj.vals[857][0],populating_obj.vals[293][0]] #I randomly chose them

	print "Records from B_tree key search: "

	print BTree_obj.retrieve_using_key(testing_keys)

	print "Records from Hashtable key search: "

	print hash_table_obj.retrieve_using_key(testing_keys)

