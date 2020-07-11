from cmath import sqrt as s
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

d = (b**2) - (4*a*c)

sol1 = (-b-s(d)) / (2*a)
sol2 = (-b+s(d)) / (2*a)

print("The solution are {0} and {1}".format(sol1,sol2))