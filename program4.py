#Write a Python program to convert kilometer to miles.

kilometer = float(input("enter distance in kilometer:"))
#conversion_facctor : 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometer*conversion_factor
print(f"{kilometer} is equal to {miles} miles")