#Write a python program to find the LCM.
#Least common multiple :is the smallest multiple that is exactly divisible by two or more numbers.

def compute_lcm(x , y):
    if x > y :
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0)and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm 

num1 = (int(input("Enter the number ")))
num2 = (int(input("Enter the number ")))
print("LCM is ", compute_lcm(num1,num2))