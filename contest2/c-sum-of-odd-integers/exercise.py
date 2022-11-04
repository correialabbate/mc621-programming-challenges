t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    if k > n:
        print('NO')
    elif n%2 == 0 and k%2 == 1:
        print('NO')
    elif n%2 == 1 and k%2 == 0:
        print('NO')
    else:
        if n >= k*k:
            print('YES')
        else:
            print('NO')
