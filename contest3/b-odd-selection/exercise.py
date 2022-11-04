t = int(input())

for i in range(t):
    n, x = map(int, input().split())

    a = [int(k) for k in input().split()]

    n_odd = 0
    n_even = 0
    for j in range(len(a)):
        if a[j] % 2 == 0:
            n_even += 1
        else:
            n_odd += 1
    
    if x % 2 == 0:
        test_times = int(x/2)
    else:
        test_times = int(x/2) + 1
    
    n_odd_test = 1
    ans = False
    for m in range(test_times):
        if n_odd >= n_odd_test and n_even >= (x - n_odd_test):
            ans = True
            break
        n_odd_test += 2
    if ans:
        print('Yes')
    else:
        print('No')
