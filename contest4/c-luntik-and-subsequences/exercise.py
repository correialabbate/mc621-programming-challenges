t = int(input())

for i in range(t):
    n = int(input())

    array = [int(x) for x in input().split()]

    n_1 = array.count(1)
    n_0 = array.count(0)
    ans = n_1*(2**n_0)

    print(ans)