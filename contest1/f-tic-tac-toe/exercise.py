def verify_if_won(matrix, simb):
    for row in matrix:
        if (row[0] == simb) and (row[1] == simb) and (row[2] == simb):
            return True
    for i in range(len(matrix[0])):
        if (matrix[0][i] == simb) and (matrix[1][i] == simb) and (matrix[2][i] == simb):
            return True
    if (matrix[0][0] == simb) and (matrix[1][1] == simb) and (matrix[2][2] == simb):
        return True
    if (matrix[0][2] == simb) and (matrix[1][1] == simb) and (matrix[2][0] == simb):
        return True
    return False

matrix = []
for i in range(3):
    row_str = str(input())
    row = [c for c in row_str]
    matrix.append(row)

# verify if game is valid (number of X's = number of 0's || number of 0's + 1)
n_x = 0
n_o = 0
for row in matrix:
    for i in range(len(row)):
        if row[i] == 'X':
            n_x += 1
        elif row[i] == '0':
            n_o += 1
if not (n_x == n_o or n_x == n_o + 1):
    print('illegal')
    exit()

# verify if first player won
first_won = verify_if_won(matrix, 'X')
if first_won:
    if n_x == n_o + 1:
        print('the first player won')
        exit()
    else:
        print('illegal')
        exit()

# verify if second player won
second_won = verify_if_won(matrix, '0')
if second_won:
    if n_x == n_o:
        print('the second player won')
        exit()
    else:
        print('illegal')
        exit()

# verify draw
full_grid = True
for row in matrix:
    if '.' in row:
        full_grid = False
        break
if full_grid:
    print('draw')
    exit()

# verify next player
if n_x == n_o:
    print('first')
else:
    print('second')
