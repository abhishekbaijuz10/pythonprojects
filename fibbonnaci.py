nterms = int(input("How many terms :"))

n1, n2 = 0, 1
count = 0

if nterms < 0:
    print("Enter a positive integer ")
elif nterms == 0:
    print(n1)
else:
    print("Terms are :")
    while count < nterms:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1