#Write a Python program to check prime number.
num = int(input("Enter a number : "))

#define a flag variable 
flag = False

if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True #if factor is found, set flag to True 
            #break the loop
            break
if flag:
    print(f"{num},is not a prime number")
else:
    print(f"{num},is a prime number")