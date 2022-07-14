year = int(input("Enter Year :- "))
if(year>=1000 and year<10000):
    if (year % 4==0 and year % 100 !=0):
        print(year, "is leap year")
    else:
        print(year, "is not leap year")
else:
    print("Enter Valid Year")