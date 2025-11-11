year = int(input("enter year:"))

if(year%400 == 0) or (year%100 == 0) or (year%4==0):
    print("its a leap year")
else:
    print("it is leap year")
