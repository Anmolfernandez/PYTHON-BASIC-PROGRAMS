#Write a Python program to swap two variables.

#Input two variables 
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Orignal values :a = {a},b = {b}")
#Swap the values using a temporary variable 
temp = a
a = b 
b = temp
print(f"Swapped values :a = {a},b = {b}")



#Write a Python program to generate random numbers

import random
print(f"Random number: {random.randint(1,100)}")


