t = int(input())

for test in range(t):
    n = int(input())

    list = [int(x) for x in input().split()]

    count = 0
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if (list[j] - list[i]) == (j - i):
    #             count += 1
    # print(count)
    sub_list = []
    for i in range(n):
        sub_list.append(list[i]-i)
    for i in range(n-1):
        for j in range(i+1,n):
            if (sub_list[i] == sub_list[j]):
                count += 1
    print(count)