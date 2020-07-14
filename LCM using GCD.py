def gcd(x, y):

    while(y):
        x, y = y, x%y
    return x


def compute_lcm(x, y):
    lcm = (x*y) // gcd(x, y)
    return lcm


num1 = 54
num2 = 24

print(compute_lcm(num1, num2))