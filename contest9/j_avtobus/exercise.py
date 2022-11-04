t = int(input())

for _ in range(t):
    n = int(input())

    no_ans = False

    if n >= 4 and n%2 == 0:
        max = n//4
        if n%6 == 0:
            min = n//6
        else:
            min = n//6 + 1
    else:
        no_ans = True

    if no_ans:
        print("-1")
    else:
        print(f'{min} {max}')