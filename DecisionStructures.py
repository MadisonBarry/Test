#Placing a hash tag in front of a line will make the 
#line not execute
#This is referred to as a "comment"
from email._header_value_parser import Comment
from http.server import BaseHTTPRequestHandler
from lib2to3.pgen2.token import EQUAL

"""
Line one of block comment
line two of block comment
line 3 of block comment
"""


"""
A condition is a comparison.
Conditions evaluate a boolean value to be true or false.
If a condition is true, the following block of code will run.
A block of code will be indented.

COMPARISONS: 
> Greater than 
< less than 
>= Great than or equal to 
<= Less than or equal to 
== Equal to 
!= Not EQUAL

"""

mark = int(input("Please enter your test mark"))
print(mark)

#if mark > 49:
#if mark >= 50:
    #print("you passed!")
    
#if mark <= 49:
    #print("You failed")
    
#if mark >= 90:
    #print("You aced it")
    
#if mark >=100:
    #print("You got perfect!")
    
    
if mark >= 90:
    print("you aced it!")
    
elif mark >= 70:
    print("You got a B! Good job!")
    
elif mark >= 60:
    print("You got a C")
    
elif mark >= 50:
    print("You barely made it!")
    
#elif mark <= 49:
    #print("You failed.")
    
else:
    print("You suck.")
    
if (mark > 0 and mark <= 100):
    print("you have a valid mark")
    
if (mark > 100 or mark <0):
    print("This is an invalid mark")