def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))



nterms = int(input("Enter the +ve integer"))
if nterms <= 10:
    print("Enter a prosiive number :")
else:
    print("Terms are :")
    for i in range(nterms):
        print(recur_fibo(i))