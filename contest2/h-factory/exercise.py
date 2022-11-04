a, m = map(int, input().split())

for i in range(m):
    a = a + a%m
    if a%m == 0:
        print('Yes')
        exit()
print('No')