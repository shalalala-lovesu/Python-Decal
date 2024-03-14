#3 Check Leap Year
#Write a function that takes a year as input and returns 
#True if it’s a leapyear, and False otherwise. A leap year 
#is divisible by 4 but not divisible by 100 unless it is also
#divisible by 400.
def if_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0):
        leap = False
    elif (year % 100 == 0) and (year % 400 == 0):
        leap = True
    return leap

year = int(1984)
print(if_leap(year))