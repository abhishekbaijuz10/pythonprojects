def convertdec(n):
    if n > 1:
        convertdec(n//2)
    print(n%2, end='')


num = 55

convertdec(num)
print()
