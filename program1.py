#Write a Python program to do arithematic operations addition and divison.

#For Addition 
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2 
print(f"sum: {num1} + { num1} = {sum_result}")

#For Divison 
num3 = float(input("Enter the first number for divison: "))
num4 = float(input("Enter the second number for divison: "))
if num4 == 0:
    print("Error:Divison by zero is not allowed.")
else:
    div_result = num3/num4
    print(f"Divison:{num3}/{num4} = {div_result}")
    