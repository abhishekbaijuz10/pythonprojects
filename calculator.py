print("1. Subtraction")
print("2. Division")
print("3. Addition")
print("4. Multiplication")


def multiply(x, y):
    return x * y


def division(x, y):
    return x / y


def add(x, y):
    return x +y


def subtract(x, y):
    return x -y


while True:

    choice = (input("Enter the choice"))

    if choice in ('1', '2', '3', '4'):

        num1 = float(input("Enter the first number :"))
        num2 = float(input("Enter the second number :"))

        if choice == '1':
            print(num1, "-", num2, '=', subtract(num1, num2))

        elif choice == '2':
            print(num1, "+", num2, '=', add(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, '=', division(num1, num2))
        break

    else:
        print("Invalid input")



