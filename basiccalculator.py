import os
os. system ("cls")
first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))
operator = input("Enter operator you want to use(+ , - , / , * , %) : ")
if operator == "+":
    print("Addition is: ", first_value + second_value)
elif operator == "-":
    print("Subtraction is: ", first_value - second_value)
elif operator == "*":
    print("Multiplication is: ", first_value * second_value)
elif operator == "/":
    print("Division is: ", first_value / second_value)
elif operator == "%":
    print("Modulus is: ", first_value % second_value)
else:
    print("Do not get result? Try again with valid input!")
