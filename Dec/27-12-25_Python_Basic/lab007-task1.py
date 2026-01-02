#find the quotient and reminder
# Convert input values to int because input() returns strings
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
ans = divmod(num1, num2)
print(ans)

#or
quotient = num1//num2
reminder = num1%num2
print(f"quotient (Q) ->", quotient)
print(f"reminder (R) ->", reminder)
