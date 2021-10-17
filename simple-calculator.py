print("Hello, I am the basic calculator!\n")
num1 = ""
operation = ""
num2 = ""
num1 = input("Enter the first number!\n")
operation = input("Enter the operation! (+, -, *, /)?\n")
num2 = input("Enter the second number!\n")

a = float(num1)
b = float(num2)

output = 0

if operation == "+":
    output=a+b
if operation == "-":
    output=a-b
if operation == "*":
    output=a*b
if operation == "/":
    output=a/b
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
    print("The Answer is: " + str(output))

else:
    print("Invalid things are entered, sorry!")
