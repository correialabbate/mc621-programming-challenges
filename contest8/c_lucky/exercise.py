t = int(input())

for _ in range(t):
    ticket = str(input())
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2:
        print('YES')
    else:
        print('NO')