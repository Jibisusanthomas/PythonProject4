#traingale classifier

side1 = int(input("enter side 1: "))
side2 = int(input("enter side 2: "))
side3 = int(input("enter side 3: "))

if side1 == side2 and side2 == side3:
    print("The triangle is Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is Isoceles")
else:
    print("The triangle is Scalene")