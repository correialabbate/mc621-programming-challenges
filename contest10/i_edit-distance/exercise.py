t = int(input())

for _ in range(t):
    b = input()
    a = input()

    matrix_distance = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    
    for i in range(len(b)+1):
        matrix_distance[0][i] = i
    for j in range(len(a)+1):
        matrix_distance[j][0] = j
    
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
            matrix_distance[i][j] = min(matrix_distance[i-1][j] + 1, matrix_distance[i][j-1] + 1, matrix_distance[i-1][j-1] + cost)
    
    print(matrix_distance[len(a)][len(b)])