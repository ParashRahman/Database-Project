import cx_Oracle
import getpass

password = getpass.getpass()
con = cx_Oracle.connect("parash/" + password + "@gwynne.cs.ualberta.ca:1521/CRS")

con.autocommit = 1

curs = con.cursor()
curs.execute("select * from people")
rows = curs.fetchall()
print( rows )

rows = [(1,"First"), (2,"Second"), (3,"Third")]
curs.bindarraysize = 3
curs.setinputsizes(int,20)
curs.executemany("insert into mytab(id, description) values (:1,:2)", rows)
con.commit

curs.execute("SELECT * from TOFFEES")
rows = curs.description
columnCount = len(rows)
for row in rows:
    print( row[0] )
