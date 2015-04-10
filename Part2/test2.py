from rand import Random
import time
from b_tree import BTree
from hash_table import HashTable
from index_file import IndexFile

current_milli_time = lambda: time.time() * 1000000

def are_equal ( r1, r2, r3 ):
    if ( set(r1) == set(r2) ):
        print( "r1 == r2" )
    if ( set(r2) == set(r3) ):
        print( "r2 == r3" )


b = BTree("1.db")
h = HashTable("2.db")
i = IndexFile("3.db", "4.db")

b.destroy()
h.destroy()
i.destroy()

r = Random()
data = r.get_keys_and_values( 1000 )

to_key_search = [data[250][0]]
to_data_search = [data[250][1]]
to_range_search = ('g', 'w')

b.insert( data )
h.insert( data )
i.insert( data )

print "Key Search" 
print "b"
start = current_milli_time() 
result1 = b.retrieve_using_key( to_key_search )
end = current_milli_time() 
print (end - start)
print "h"
start = current_milli_time() 
result2 = h.retrieve_using_key( to_key_search )
end = current_milli_time() 
print (end - start)
print "i"
start = current_milli_time() 
result3 = i.retrieve_using_key( to_key_search )
end = current_milli_time() 
print (end - start)
are_equal ( result1, result2, result3 ) 

print

print "Value Search"
print "b"
start = current_milli_time() 
result1 = b.retrieve_using_data_values( to_data_search )
end = current_milli_time() 
print (end - start)
print "h"
start = current_milli_time() 
result2 = h.retrieve_using_data_values( to_data_search )
end = current_milli_time() 
print (end - start)
print "i"
start = current_milli_time() 
result3 = i.retrieve_using_data_values( to_data_search )
end = current_milli_time() 
print (end - start)
are_equal ( result1, result2, result3 )

print

print "Range Search"
print "b"
start = current_milli_time() 
result1 = b.retrieve_range( to_range_search[0], to_range_search[1] )
end = current_milli_time() 
print( end - start )
print "h"
start = current_milli_time() 
result2 = h.retrieve_range( to_range_search[0], to_range_search[1] )
end = current_milli_time() 
print( end - start )
print "i"
start = current_milli_time() 
result3 = i.retrieve_range( to_range_search[0], to_range_search[1] )
end = current_milli_time() 
print( end - start )
are_equal ( result1, result2, result3 )
