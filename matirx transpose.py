x = [
    [12, 7],
    [4, 5],
    [3, 8]
]

result = [
    [0,0,0],
    [0,0,0]
]

result = [[x[j][i] for j in range(len(x))] for i in range(len(result))]
for i in result:
    print(i)