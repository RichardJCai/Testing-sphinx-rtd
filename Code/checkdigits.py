"""
Author: Richard Cai
Date: 19 Nov 2014
Description: Validates an ISBN10, ISBN13, or UPC number and returns if the number is valid or not  """

def get_digit(number,position):
    """This function accepts two parameters, number and position, it retrieves the digit in the desired position, and returns the digit."""
    return (number / 10 ** position % 10) 

def is_ISBN10(number):
    """This function accepts an ISBN10 number, adds the sum of each digit multiplied by a weighted value, if the remainder of the sum divided by 11 is equal, the function returns True otherwise this function returns False."""
    
    sum_num = 0
    counter = 0

    #The sum of each digit in the ISBN10 integer multiplied by a weighted value (counter). 
    for x in range (9,0,-1):    
        #The value each digit gets mulitplied by.
        counter = counter + 1
        sum_num = sum_num + get_digit(number,x) * counter
    return sum_num % 11 == get_digit(number,0)

def is_ISBN13(number):
    """This function accepts an ISBN13 number, adds the sum of the even numbers and the sum of the odd numbers multiplied by 3, then subtracts the remainder the sum divided by 10 from 10. Returns True if the value is equal to the checkdigit and false otherwise."""
    odd_sum = 0
    even_sum = 0
    
    #The sum for all the of even numbers multiplied by 3
    for even in range (1,13,2):
        even_sum = even_sum + get_digit(number,even) * 3
    #The sum of all the odd numbers
    for odd in range (2,14,2):
        odd_sum = odd_sum + get_digit(number,odd)
    
    return 10 - ((odd_sum + even_sum) % 10) == get_digit(number,0)

def is_UPC(number):
    """This function accepts an UPC number, adds the sum of the even number multiplied by 3 to the sum of the odd numbers, then subtracts the right digit of the value from 10. Returns True if the remainder is equal to the check digit and returns false otherwise."""
    even_sum = 0
    odd_sum = 0
    
    #Add up all the even numbers
    for even in range (2,11,2):
        even_sum = even_sum + get_digit(number,even)
    #Add up all the odd numbers
    for odd in range (1,12,2):
        odd_sum = odd_sum + get_digit(number,odd)
        
    return (even_sum + odd_sum*3) % 10 == get_digit(number,0)