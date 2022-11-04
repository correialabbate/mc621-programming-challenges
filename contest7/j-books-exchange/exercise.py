q = int(input())

for i in range(q):
    n = int(input())
    childs = [int(x) for x in input().split()]
    childs.insert(0,0)
    ans = []

    for i in range(1,len(childs)):
        total = 1
        i = childs[i]
        original_i = i
        while childs[i] != original_i:
            i = childs[i]
            total += 1
        ans.append(total)
    print(*ans)