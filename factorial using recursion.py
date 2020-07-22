def fact_num(n):
    if n==1:
        return n
    else:
        return n*fact_num(n-1)


num = int(input("Enter the number"))

if num<0:
    print("Doesnt exits")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("factorial is", num, "is", fact_num(num))