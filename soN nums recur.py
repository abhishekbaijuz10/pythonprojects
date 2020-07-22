def sum_recur(n):
    if n<=1:
        return n
    else:
        return n + sum_recur(n-1)

num = int(input("Enter the number :"))

if num<=0:
    print("Wrond number ")
else:
    print(sum_recur(num))