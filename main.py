
print("~~~~~~~~~~~~~~~~~CALCULATOR~~~~~~~~~~~~~~~~~")


# Function To Add Two Number
def add(num1, num2):
    return(num1 + num2)


# Function To Subtract Two Number
def subtract(num1, num2):
    return(num1 - num2)


# Function TO Multiply Two Number
def multiply(num1, num2):
    return(num1 * num2)


# Function To Divide Two Number
def divide(num1, num2):
    return(num2 / num1)


print("please select operation -\n" 
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Take input from the user
select = int(input("select the operation from 1, 2, 3, 4 : "))

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second  number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid")

