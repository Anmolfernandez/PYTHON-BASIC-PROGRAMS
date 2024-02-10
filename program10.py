#Write a Python program to print the Fibonacci sequence.
# The Fibonacci sequence is is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1.So the dequence begins with 0 and 1, and the next number is obtained by adding the previous 2 numbers.

nterms = int(input("how many terms to be displayed ?"))
#first two terms are written 
n1,n2 = 0,1
count = 0 
#check if the number ofterms is valid 
if nterms <= 0:
    print("Please enter a positive integer ")
#if there is only one term,return n1
elif nterms == 1:
    print("FIbonaccisequence upto",nterms,":")
    print(n1)
#generate fibonacci sequence 
else:
    print("fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2 
        # update values 
        n1 = n2 
        n2 = nth 
        count += 1