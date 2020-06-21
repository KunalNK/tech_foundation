#Function to add two numbers  
def add(num1, num2):
    return num1 + num2

#Function to substract two numbers 
def sub(num1,num2):
    return num1-num2

#Function to multiply two numbers
def mul(num1,num2):
    return num1*num2

#Function to divide two numbers
def div(num1,num2):
    return num1/num2

print("Please select the option -\n"\
        "1. Add\n" \
        "2. Sub\n" \
        "3. Mul\n" \
        "4. Div\n")
        
        

# Take input from the user  
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

if select==1:
    print(number_1, "+", number_2, "=",
            add(number_1, number_2))

elif select==2:
    print(number_1, "-", number_2, "=",
            sub(number_1, number_2))

elif select==3:
    print(number_1, "*", number_2, "=",
            mul(number_1, number_2))

elif select==4:
    print(number_1, "/", number_2, "=",
            div(number_1, number_2))

else:
    print("Invalid option")


