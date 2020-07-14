def compute(x, y):

    while(y):
        x, y = y, x%y
    return x


hcf = compute(54, 24)
print(hcf)
