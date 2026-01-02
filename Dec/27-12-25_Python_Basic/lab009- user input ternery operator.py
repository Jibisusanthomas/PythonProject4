
user_age = int(input("enter your age: "))

if user_age >= 18:
    print("user can take license")

else:
    print("user can not take license")

#ternery operator

print("user can take license" if user_age>=18 else "user cannot take license")