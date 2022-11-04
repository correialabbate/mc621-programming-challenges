t = int(input())

for _ in range(t):
    n = str(input())
    n = n[::-1]
    ans = []
    for i in range(len(n)):
        if int(n[i]) != 0:
            ans.append(10**i*int(n[i]))
    print(len(ans))
    print(*ans)
    