t = int(input())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(t):
    n = int(input())

    order_of_solved = str(input())
    
    total = 0
    for l in sorted(alphabet):
        if l in order_of_solved:
            total = total + order_of_solved.count(l) + 1
    print(total)