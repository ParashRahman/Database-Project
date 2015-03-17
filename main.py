import cx_Oracle
import getpass

def main():
    print( "Choose one of the following actions: ")
    print( "[1] Register a new vehicle" )
    print( "[2] Complete an auto transaction" )
    print( "[3] Register a driver's licence" )
    print( "[4] Record a violation" )
    print( "Enter a number: " )
    
    try:
        choice = int(input())
    except:
        choice = "Invalid"

    while ( type( choice ) is not int 
            or choice >= 5 
            or choice <= 0 ):
        print( "Enter a valid integer choice: " )
        try:
            choice = int(input())
        except:
            choice = "Invalid"

main()
