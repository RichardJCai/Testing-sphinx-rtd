"""
Author: Richard Cai
Date: 19 Nov 2014
Description: Displays a menu that allows the user to choose between validating ISBN-10, ISBN-13, UPC number or quit.  """

import checkdigits

def main():
    """Mainline logic, prints the menu, accepts the user choice and calls the appropriate function to validate the number"""
    print "CHECK DIGIT VALIDATOR"
    print
    print "What code would you like to validate:"
    print
    print "1. ISBN-10"
    print "2. ISBN-13"
    print "3. UPC"
    print "Q. Quit Program"
    print ""
    
    user_input = raw_input("")
    #Calls the appropriate function to validate the number or quits the program.
    if user_input == "1":
        number = input("Enter an ISBN-10 number: ")
        if checkdigits.is_ISBN10(number):
            print "The ISBN-10 number is valid!"
            print
        else: 
            print "The ISBN-10 number is invalid!"
            print
        main()
        
    elif user_input == "2":
        number = input("Enter an ISBN-13 number: ")
        if checkdigits.is_ISBN13(number):
            print "The ISBN-13 number is valid!"
            print
        else:
            print "The ISBN-13 number is invalid!"
            print
        main()
        
    elif user_input == "3":
        number = input("Enter a UPC number: ")
        if checkdigits.is_UPC(number):
            print "The UPC number is valid!"
            print
        else:
            print "The UPC number is invalid!"
            print
        main()
        
    elif user_input == "Q" or user_input == "q":
        print "Exiting the program"
        
    else:
        #Input validation, asks again if the input is not valid.
        print "ERROR: Invalid Input. Try again"
        print 
        main()
            
main()