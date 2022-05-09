# Methods are blocks off code that are executed with a command
# Methods can be called anything, except keywords
# Predefined Python methods
# Methods are created at top of program in Python
# Use the keyword "def" before the method

# Method definition
# This method does not have any parameters
def foo():
    # Code to be executed when method is called
    print("Hello world!")
    print("Lizard")
    print("Strike Force")
    
# This method takes 2 parameters    
def bar(x, y):
    sum = x + y
    return(sum)
    
    
# Beginning of Python program
print("Welcome to my program.")
foo()

variable = bar(27, 27)

print(variable