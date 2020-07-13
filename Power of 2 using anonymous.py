terms = int(input("Enter the number :"))

result = list(map(lambda x: x * 2, range(terms + 1)))

print("The total terms are :")
for i in range(terms):
    print(result[i])