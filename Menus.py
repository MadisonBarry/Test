# Mehtod definitions
def menu():
    print("Welcome to my program")
    print("Please enter a choice")
    print("1. Tell me a funny joke")
    print("2. Tell me a riddle")
    print("3. Exit")
    print("Please enter your choices")
    
    choice = int(input())
    return choice
    
    
    
# Main program
menuChoice = 0

while menuChoice != 3:


    menuChoice = menu()
    
    if menuChoice == 1:
            print("Why did the chicken cross the road")
    
    elif menuChoice == 2:
            print("Little red riding hood...")
    
    