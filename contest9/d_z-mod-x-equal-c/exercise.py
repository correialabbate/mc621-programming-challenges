t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    x = a + b + c
    y = b + c
    z = c
    print(f'{x} {y} {z}')