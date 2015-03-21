import cx_Oracle
import getpass
import error_checker

password = getpass.getpass()
con = cx_Oracle.connect("parash/" + password + "@gwynne.cs.ualberta.ca:1521/CRS")

con.autocommit = 1

curs = con.cursor()
curs.execute("select * from people")
rows = curs.fetchall()
print( rows )

"""
rows = [(1,"First"), (2,"Second"), (3,"Third")]
curs.bindarraysize = 3
curs.setinputsizes(int,20)
curs.executemany("insert into mytab(id, description) values (:1,:2)", rows)
con.commit 
"""

curs.execute("SELECT * from whatisup")
rows = curs.description
length = len(rows)
print()
for row in rows:
    print( row )

x = [
    error_checker.ErrorChecker.check_error( rows[0], "100000000000000" ),
    error_checker.ErrorChecker.check_error( rows[0], "12.122121" ),
    error_checker.ErrorChecker.check_error( rows[1], "2348923489.234234"),
    error_checker.ErrorChecker.check_error( rows[1], "2341.21" ),
    error_checker.ErrorChecker.check_error( rows[1], "23" ),
    error_checker.ErrorChecker.check_error( rows[2], ( 1,2,3 ) ),
    error_checker.ErrorChecker.check_error( rows[2], (2012, 13, 2) ),
    error_checker.ErrorChecker.check_error( rows[3], "afdiodfsaiosdfa" ),
    error_checker.ErrorChecker.check_error( rows[3], "sdfasdfasdfasdafsdfasdfasdfadfasf" )
    ]

print( x )
