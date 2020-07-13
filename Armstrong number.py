arm_num = int(input("Enter the number to check :"))

num = arm_num
sum = 0
while num!=0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if sum == arm_num:
    print("The number is a armstrong number")
else:
    print("The  number is not a armstrong number")