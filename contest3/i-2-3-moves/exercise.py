t = int(input())

for i in range(t):
    n = int(input())

    if n == 1:
        print("2")
        continue

    if n%3 == 0:
        print(int(n/3))
    else:
        print(int(n/3) + 1)
