from application import Application
from error_checker import ErrorChecker
from metadata import Metadata

class Search(Application):

    def start_application(self, c):
        self.cursor = c
        self.list_of_inputs = [ None for i in range(8) ]
        self.fields = [ "Search Driver", # 1
                        "Search Driver Violation History",   # 2
                        "Search Vehicle History",
                        "Exit" ] 
        while ( True ):
            self.print_field_options( )
            choice = self.get_input( len(self.fields) )

            if (choice == 1):
                self.search_driver()
            elif (choice == 2):
                self.search_violation_history()
            elif (choice ==  3):
                self.search_vehicle()
            elif (choice == 4):
                return


    def print_field_options( self, fields = None, showEmpty = False ):
        if ( fields == None ):
            fields = self.fields
        print( "Select a search: " )
        for i in range( len( fields ) ):
            print ( "[{:}] ".format( i+1 ) + 
                    fields[i] + 
                    (" EMPTY" if showEmpty 
                     and i < 7 and not self.list_of_inputs[i+1]  
                     else "") )


    def get_input( self, num_choices, 
                   prompt = "Choose a search: ",
                   fields = None, showEmpty = False ):

        if ( fields == None ):
            fields = self.fields

        print( prompt )
        try:
            string_input = input()
            choice = int(string_input)
        except:
            choice = "Invalid"

        while ( type( choice ) is not int 
                or choice >= num_choices + 1 
                or choice <= 0 ):
            self.print_field_options(fields, showEmpty)
            print( "Enter a valid integer choice: " )
            try:
                string_input = input()
                choice = int(string_input)
            except:
                choice = "Invalid"

        return choice
    
    def search_driver(self):
        """ SEARCH DRIVER BY NAME/ID"""
        user_input = input("Enter Driver Licence ID or Name: ")
        user_input.strip()
    
        if( len( user_input ) == 0 ):
            return

        self.cursor.execute("""
                            SELECT p.name, l.licence_no, p.addr, p.birthday, l.class, r.r_id, l.expiring_date
                            FROM people p, drive_licence l
                            LEFT JOIN restriction r
                            ON l.licence_no = r.licence_no
                            WHERE p.sin = l.sin
                            AND (l.licence_no = '{}' OR p.name = '{}')""".format(user_input, user_input))

        rows = self.cursor.fetchall()

        licence_dict = {}
        for row in rows:
            licence_dict[row[1]] = []
        for row in rows:
            licence_dict[row[1]].append(row[5])

        print("")
        if len(rows) == 0:
            print("Driver Not Found")
        printed = []
        for row in rows:
            if row[1] not in printed:
                print("-------------------------------------------")
                print("Driver               : " + str(row[0]))
                print("Licence Number       : " + str(row[1]))
                print("Driver Address       : " + str(row[2]))
                print("Driver Birthday      : " + str(row[3]))
                print("Class                : " + str(row[4]))
                print("Driving Condition    : " + str(licence_dict[row[1]]))
                print("Expiration Date      : " + str(row[6]))
                printed.append(row[1])
        print("-------------------------------------------")
        print("")

    def search_violation_history(self):
        """ SEARCH VIOLATION HISTORY DRIVER BY NAME OR ID"""
        user_input = input("Enter Licence ID or SIN: ")
        user_input.strip()
    
        if( len( user_input ) == 0 ):
            return
    
        self.cursor.execute("""
                            SELECT t.ticket_no, p.name, t.violator_no, t.vehicle_id, p2.name, t.office_no, t.vtype, y.fine, t.vdate, t.place, t.descriptions
                            FROM ticket t, people p, ticket_type y, people p2, drive_licence l
                            WHERE p.sin = t.violator_no
                            AND p2.sin = t.office_no
                            AND t.vtype = y.vtype
                            AND l.sin = p.sin
                            AND (p.sin ='{}' OR l.licence_no ='{}')""".format(user_input,user_input))

        rows = self.cursor.fetchall()
        print("")
        print("{} Results Found".format(len(rows)))
        for row in rows:
            print("-------------------------------------------")
            print("Ticket ID            : " + str(row[0]))
            print("Violator             : " + str(row[1]))
            print("Violator SIN         : " + str(row[2]))
            print("Vehicle Serial No    : " + str(row[3]))
            print("Officer              : " + str(row[4]))
            print("Officer Sin          : " + str(row[5]))
            print("Ticket Type          : " + str(row[6]))
            print("Ticket Fine          : $" + str(row[7]))
            print("Ticket Date          : " + str(row[8]))
            print("Ticket Location      : " + str(row[9]))
            print("Ticket Descriptons   : " + str(row[10]))

        print("-------------------------------------------")
        print("")
    
    def search_vehicle(self):
        """ SEARCH VEHICLE BY SERIAL NO"""
        user_input = input("Enter Vehicle Serial No: ")
        user_input.strip()
    
        if( len( user_input ) == 0 ):
            return
    
        self.cursor.execute("""
                            SELECT v.serial_no, COUNT(s.transaction_id), AVG(s.price), COUNT(t.ticket_no)
                            FROM vehicle v, auto_sale s, ticket t
                            WHERE v.serial_no = s.vehicle_id 
                            AND v.serial_no = t.vehicle_id 
                            AND v.serial_no = '{}'
                            GROUP BY v.serial_no
                            """.format(user_input))

        rows = self.cursor.fetchall()

        print("")
        print("{} Results Found".format(len(rows)))
        for row in rows:
            print("-------------------------------------------")
            print("Serial Number                    : " + row[0])
            print("Times that vehicle has been sold : " + str(row[1]))
            print("Average Price                    : $" + str(row[2]))
            print("Number of violations             : " + str(row[3]))
        print("-------------------------------------------")
        print("")