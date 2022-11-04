t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    s = m*["B"]
    for i in range(n):
        v = a[i]
        if v < m+1-v:
            if s[v-1] == 'B':
                s[v-1] = 'A'
            else:
                s[m-v] = 'A'
        else:
            if s[m-v] == 'B':
                s[m-v] = 'A'
            else:
                s[v-1] = 'A'
    print(*s, sep='')