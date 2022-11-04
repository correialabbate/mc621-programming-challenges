first_input = [int(x) for x in input().split()]
n = first_input[0]
m = first_input[1]

second_input = [int(x) for x in input().split()]

list = []
for i in range(n):
    list.append(0)
for j in second_input:
    list[j-1] += 1
print(min(list))