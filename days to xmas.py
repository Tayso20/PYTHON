# to get date in dd/mm/yyyy
"""
from datetime import date
import datetime

now = datetime.datetime.now()

today = date.today()
d3 = today.strftime("%m/%d/%y")

#d3 = input("What is the date: ")

# find differnce in days
Start = date.today()
End = date(2020, 12, 25)
Gap = (End-Start).days

# store xmas as a variable
xmas = "25/12/2020"

if d3 != xmas:
    #print("Not xmas")

elif d3 == xmas:
    #print("It is Xmas!!!")

#print("There are", Gap, "Days to Xmas")

print(now)





import datetime

now = datetime.datetime.now()

print(now.year)

print(now.month)

print(now.day)

print(now.hour)

print(now.minute)

print(now.second)


"""
import datetime
now = datetime.datetime.now()

print("What is ur name?")
x=input()
print("Welcome" +  x)
print("Wat is your age?")
age=str(input())
leeftijd=input()
print("you will be 100 years old in " + (now.year-age+100))
