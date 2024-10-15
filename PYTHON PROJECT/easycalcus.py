name = input("What's your name please? ")
print(f"Hey!{name} Welcome to easy calcus,please enter your two figures")
first_value = int(input("Kindly enter your first value: "))
second_value = int(input("Kindly enter your second value: "))

def easy_calculator():
        print("What calculation would you like to perform? ")
        option = int(input("Please enter 1 for multiplication, 2 for additon, 3 for subtraction, 4 for division and 0 for exit: "))
        if option == 1 :
            multiplication()
        elif option == 2:
            addition()
        elif option == 3:
            subtraction()
        elif option == 4:
             division()
        else:
            if option == 0:
             print("Thank you, Come again!")
                
     
    
def multiplication():
        multy_value = first_value * second_value
        print(f"The result of the values are: " + str(multy_value))  


def addition():
        summed_value = first_value + second_value
        print(f"The result of the values are: " + str(summed_value))


def subtraction():
        subt_value = first_value - second_value
        print(f"The result of the values are: " + str(subt_value))

def division():        
    division_value = first_value / second_value
    print(f"The result of the values are: " + str(division_value))


easy_calculator()

