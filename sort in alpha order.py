str = input("Enter the sentence")

words = str.split()

words.sort()

print("the sorted words are :")
for word in words:
    print(word)


