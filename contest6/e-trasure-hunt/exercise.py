x1, y1, x2, y2 = map(int, input().split())

x, y = map(int, input().split())

x2 -= x1
y2 -= y1

if x2%(2*x) == 0:
    multiple_2x = True
else:
    multiple_2x = False

if y2%(2*y) == 0:
    multiple_2y = True
else:
    multiple_2y = False

if multiple_2x and multiple_2y:
    print("YES")
    exit()

if (not multiple_2x) and x2%x == 0:
    if (not multiple_2y) and y2%y == 0:
        print("YES")
        exit()

print("NO")
