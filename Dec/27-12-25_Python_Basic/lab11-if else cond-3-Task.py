#Grade calculator

Score = int(input("Enter Score:"))

if Score >= 90 and Score <= 100:
    print("Grade = A")
elif Score >= 80 and Score <= 89:
    print("Grade = B")
elif Score >= 70 and Score <= 79:
    print("Grade = C")
elif Score >= 60 and Score <= 69:
    print("Grade = D")
elif Score <= 50:
    print("Grade = F")
else:
    print("Gb is a super women")
