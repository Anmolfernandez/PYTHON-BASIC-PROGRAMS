#Write a Python program to display a calender
import calendar
year = int(input("enter the year :"))
month = int(input("enter the month :"))
cal = calendar.month(year,month)
print(cal)