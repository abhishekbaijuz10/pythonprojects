my_str = str(input("Enter the string"))

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("It is a palindrome ")
else:
    print("It is not a palindrome")