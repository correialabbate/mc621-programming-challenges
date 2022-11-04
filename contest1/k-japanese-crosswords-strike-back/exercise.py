first_line = [int(x) for x in input().split()]
n = first_line[0]
x = first_line[1]

encod = [int(x) for x in input().split()]

sum_encod = sum(encod)
if (sum_encod + len(encod) - 1) == x:
    print('YES')
else:
    print('NO')