first_input = [int(x) for x in input().split()]
n = first_input[0]
m = first_input[1]

p_list = [int(x) for x in input().split()]
p_list.sort()

number_removals = m-n
diff = p_list[-1] - p_list[0]
for i in range(number_removals+1):
    sub_list = p_list[i:i+n]
    if (sub_list[-1] - sub_list[0]) < diff:
        diff = sub_list[-1] - sub_list[0]
print(diff)