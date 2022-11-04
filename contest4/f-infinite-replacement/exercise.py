t = int(input())

for i in range(t):
    first_str = str(input())
    second_str = str(input())

    if second_str.count('a') > 0:
        if len(second_str) > 1: 
            ans = -1
        else:
            ans = 1
    else:
        ans = 2**(first_str.count('a'))
    print(ans)
    