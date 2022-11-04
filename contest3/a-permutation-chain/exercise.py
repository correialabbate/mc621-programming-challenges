t = int(input())

for i in range(t):
    n = int(input())
    print(n)

    a1 = list(range(1, n+1))
    print(*a1)

    for j in range(n-1):
        temp = a1[j]
        a1[j] = a1[j+1]
        a1[j+1] = temp

        print(*a1)