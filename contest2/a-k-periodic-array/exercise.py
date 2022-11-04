n, k = map(int, input().split())

array = [int(x) for x in input().split()]
arrays_splited = []
n_sub_arrays = int(n/k)
aux = 0

for i in range(n_sub_arrays):
    sub_array = []
    for j in range(k):
        sub_array.append(array[aux + j])
    aux += k
    arrays_splited.append(sub_array)

total = 0
for i in range(k):
    n_1 = 0
    n_2 = 0
    for j in range(n_sub_arrays):
        if arrays_splited[j][i] == 1:
            n_1 += 1
        else:
            n_2 += 1
    total = total + min(n_1, n_2)
print(total)
