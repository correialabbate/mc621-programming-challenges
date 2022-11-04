def calculate_value(a, b):
    print(f'a: {a}, b: {b}')
    if a < b:
        return 1
    else:
        v1 = calculate_value(int(a/b), b)
        v2 = calculate_value(a, b+1)
        print(min(v1, v2) + 1)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(calculate_value(a, b))