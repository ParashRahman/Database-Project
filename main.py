import cx_Oracle
import getpass

class Main:
    cursor = None

    def main():
        Main.cursor_init()

        NUM_CHOICES = 5
        print( "Choose one of the following actions: ")
        print( "[1] Register a new vehicle" )
        print( "[2] Complete an auto transaction" )
        print( "[3] Register a driver's licence" )
        print( "[4] Record a violation" )
        print( "[5] Exit" )
        print( "Enter a number: " )
        
        try:
            choice = int(input())
        except:
            choice = "Invalid"
            
        while ( type( choice ) is not int 
                or choice >= NUM_CHOICES + 1 
                or choice <= 0 ):
            print( "Enter a valid integer choice: " )
            try:
                choice = int(input())
            except:
                choice = "Invalid"
    
    # initializes cursor
    def cursor_init(server="gwynne.cs.ualberta.ca",port="1521",SID="CRS"):
        username = input("Enter your Oracle username: ")
        password = getpass.getpass("Enter password: ")
        try:
            con = cx_Oracle.connect(username + "/" + password + "@" + server + ':' + port + '/' + SID)

        except cx_Oracle.DatabaseError as e:
            error, =e.args
            print(error.code)

            if error.code==1017:
                print("Please Enter correct username/password combination")

            if error.code==12541:
                print("Wrong port/SID combination.Please Enter correct 'port/SID' combination below")
                port = input("Enter correct port: ");
                SID = input("Enter correct SID: ");
                    
            if error.code==12154:
                print("Please Enter correct server address")
                server = input("Enter correct server address: ");

            if error.code==12514:
                print("Please Enter correct SID");
                SID = input("Enter correct SID: ");
            
            Main.cursor_init(server, port, SID)
            return

        con.autocommit = 1
        cursor = con.cursor()
        
    # use this function to get the cursor ( Main.get_cursor() )
    def get_cursor():
        return cursor
