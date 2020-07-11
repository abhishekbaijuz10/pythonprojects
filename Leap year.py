leap_year = int(input("Enter the year :"))
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 ==0:
            print("Year is a leap year ")
        else:
            print("year is not a leap year")
    else:
        print("The year is not a leap year ")
else:
    print("The year is not a leap year")
