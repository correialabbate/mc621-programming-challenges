def transpose_matrix(matrix):
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t_matrix

n = int(input())

m = []
for i in range(n):
    m.append(list(k for k in input()))

count = 0
t_m = transpose_matrix(m)
for i in range(n):
    m_c_count = m[i].count('C')
    t_m_c_count = t_m[i].count('C')
    count = count + (int(m_c_count*(m_c_count-1))/2) + (int(t_m_c_count*(t_m_c_count-1))/2)
print(int(count))
