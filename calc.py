#Function to add two numbers  
def add(num1, num2,num3,num4):
    return num1 + num2 + num3 + num4

#Function to substract two numbers 
def sub(num1,num2, num3, num4):
    return num1-num2-num3-num4

#Function to multiply two numbers
def mul(num1,num2,num3,num4):
    return num1*num2*num3*num4

#Function to divide two numbers
def div(num1,num2,num3,num4):
    return num1/num2/num3/num4

print("Please select the option -\n"\
        "1. Add\n" \
        "2. Sub\n" \
        "3. Mul\n" \
        "4. Div\n")
        
        

# Take input from the user  
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: ") or "8") 
number_2 = int(input("Enter second number: ") or "4")
number_3 = int(input("Enter third number: ") or "2") 
number_4 = int(input("Enter fourth number: ") or "1")  

if select==1:
    print(number_1, "+", number_2, "+", number_3, "+", number_4, "=",
            add(number_1, number_2,number_3,number_4))


elif select==2:
    print(number_1, "-", number_2, "-", number_3, "-", number_4, "=",
            sub(number_1, number_2, number_3, number_4))

elif select==3:
    print(number_1, "*", number_2, "*", number_3, "*", number_4, "=",
            mul(number_1, number_2, number_3, number_4))

elif select==4:
    print(number_1, "/", number_2, "/", number_3, "/", number_4, "=",
            div(number_1, number_2, number_3, number_4))

else:
    print("Invalid option")


