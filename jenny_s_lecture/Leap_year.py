# leap year logic
# year is not divisible by 4 => not a leap year
# if divisible by 4 =>  and if not divisible by 100 => leap year
# if divisible by 100 => and if divisible by 400 => leap year
year=int(input("Enter the year "))
if year%4==0:
    if year%100==0:
        if year % 400 ==0:
            print(year,'is a leap year')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
else:
    print(year,'not a leap year')