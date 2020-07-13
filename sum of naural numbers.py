num = int(input("Enter the number :"))

if num < 0:
    print("The number is not valid ")
else:
    sum = 0
    while (num > 0):
        sum += num
        num -= 1
    print(sum)