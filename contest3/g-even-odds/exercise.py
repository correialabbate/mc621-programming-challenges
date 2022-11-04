n, k = map(int, input().split())

if n%2 == 0:
    even_start_pos = int(n/2)
else:
    even_start_pos = int(n/2) + 1

if k > even_start_pos:
    print(2*(k-even_start_pos))
else:
    print(2*(k-1) + 1)