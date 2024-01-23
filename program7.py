#write a python program to solve a quadratic equation 
# The standard form of quadratic equation is : ax2 + bx + c = 0
# where a,b,c are real numbers and a =/ 0


import math

a = float(input("Enter coeffecient a : "))
b = float(input("Enter coeffecient b : "))
c = float(input("Enter coeffecient c : "))

#calculate the discriminant
discriminant = b**2 - 4*a*c
#check if the discriminant is positive, negative or zero
if discriminant > 0:
    root1 =(-b + math.sqrt(discriminant))/(2*a)
    root2 =(-b - math.sqrt(discriminant))/(2*a)
    print(f"root 1 :{root1}")
    print(f"root 2 :{root2}")
elif discriminant ==0:
    root = -b/ (2*a)
    print(f"root:{root}")
else:
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(discriminant))/(2*a)
    print(f"root 1:{real_part}+{imaginary_part}i")
    print(f"root 2:{real_part}+{imaginary_part}i")