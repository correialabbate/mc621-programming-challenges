n_tests = int(input())

for n in range(n_tests):
    n_col = int(input())
    h = [int(x) for x in input().split()]
    if n_col == 1:
        print('YES')
    else:
        if h[0] % 2 == 0:
            even = True
        else:
            even = False
        possible = True
        for i in h:
            if even:
                if i % 2 != 0:
                    print('NO')
                    possible = False
                    break
                else:
                    continue
            else:
                if i % 2 != 0:
                    continue
                else:
                    print('NO')
                    possible = False
                    break
        if possible:
            print('YES')