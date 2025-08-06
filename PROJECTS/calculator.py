def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply (num1,num2):
    return num1*num2

def divide (num1,num2):
    return num1/num2

def average(num1,num2):
    return (num1+num2)/2

select = input("Please select the iperation :\n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Average \n") 
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the secpnd number :"))

if select == '1':
    print("The sum of", num1, "and", num2, "is :", add(num1,num2))
elif select == '2':
     print("The difference of", num1, "and", num2, "is :", subtract(num1,num2))
elif select == '3':
    print("The product of", num1, "and", num2, "is :", multiply(num1,num2))
elif select == '4':
    print("The quotient of", num1, "and", num2, "is :", divide(num1,num2))
elif select == '5':
    print("The average of", num1, "and", num2, "is :", average(num1,num2))
else:
    print("Invalid selection, please try again.")



