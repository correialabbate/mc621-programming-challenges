def check_if_won(matrix):
    for row in matrix:
        row_str = ''.join(str(x) for x in row)
        if 'xxx' in row_str:
            return True
    for j in range(len(matrix[0])):
        col_str = ''
        col_str += matrix[0][j]
        col_str += matrix[1][j]
        col_str += matrix[2][j]
        col_str += matrix[3][j]
        if 'xxx' in col_str:
            return True
    # diagonais
    dig1 = ''
    dig1 += matrix[0][0]
    dig1 += matrix[1][1]
    dig1 += matrix[2][2]
    dig1 += matrix[3][3]
    if 'xxx' in dig1:
        return True
    dig2 = ''
    dig2 += matrix[1][0]
    dig2 += matrix[2][1]
    dig2 += matrix[3][2]
    if 'xxx' in dig2:
        return True
    dig3 = ''
    dig3 += matrix[0][1]
    dig3 += matrix[1][2]
    dig3 += matrix[2][3]
    if 'xxx' in dig3:
        return True
    dig_inv1 = ''
    dig_inv1 += matrix[0][3]
    dig_inv1 += matrix[1][2]
    dig_inv1 += matrix[2][1]
    dig_inv1 += matrix[3][0]
    if 'xxx' in dig_inv1:
        return True
    dig_inv2 = ''
    dig_inv2 += matrix[0][2]
    dig_inv2 += matrix[1][1]
    dig_inv2 += matrix[2][0]
    if 'xxx' in dig_inv2:
        return True
    dig_inv3 = ''
    dig_inv3 += matrix[1][3]
    dig_inv3 += matrix[2][2]
    dig_inv3 += matrix[3][1]
    if 'xxx' in dig_inv3:
        return True
        
    return False

str1 = str(input())
str2 = str(input())
str3 = str(input())
str4 = str(input())

l1 = [c for c in str1]
l2 = [c for c in str2]
l3 = [c for c in str3]
l4 = [c for c in str4]

m = []
m.append(l1)
m.append(l2)
m.append(l3)
m.append(l4)

for i in range(len(m)):
    for j in range(len(l1)):
        if m[i][j] == '.':
            m[i][j] = 'x'
            won = check_if_won(m)
            if won:
                print('YES')
                exit()
            else:
                m[i][j] = '.'
print('NO')