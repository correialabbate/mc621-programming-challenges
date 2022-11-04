row_lenght = int(input())

str = str(input())

list = []

seq = 0
last_added = True
for c in str:
    if c == 'B':
        seq += 1
        last_added = False
    else:
        if seq > 0:
            list.append(seq)
            seq = 0
            last_added = True
if not last_added:
    list.append(seq)
print(len(list))
print(*list)