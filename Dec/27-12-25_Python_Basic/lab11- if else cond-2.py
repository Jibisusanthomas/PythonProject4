#Program to find max btwn 3 numbers

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
num3 = float(input("Enter number3: "))

if num1>num2 and num1>num3:
    print("max is num1: ",num1)
elif num2>num3 and num2>num1:
    print("max is num2: ",num2)
else:
    print("max is num3: ",num3)