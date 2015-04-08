# Python 2.7

import bsddb
from bisect import bisect_left

Database="cstudents.db"

db=bsddb.hashopen(Database, 'c') #creates a hash db in file "cstudents.db"

# db=bsddb.btopen(Database,'c') #creates a B-Tree DB

# db=bsddb.rnopen(Database,'c') #creates a record format file 


#Below is the code for inserting
print "type(db))"

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



