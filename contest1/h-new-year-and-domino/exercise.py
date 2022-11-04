def get_grid_section(grid, r1, c1, r2, c2):
    r1_grid = r1 - 1
    c1_grid = c1 - 1
    r2_grid = r2 - 1
    c2_grid = c2 - 1
    n_rows_grid_sec = r2_grid - r1_grid + 1
    n_col_grid_sec = c2_grid - c1_grid + 1
    
    grid_section = []
    for i in range(n_rows_grid_sec):
        row = []
        for j in range(n_col_grid_sec):
            row.append(grid[r1_grid+i][c1_grid+j])
        grid_section.append(row)
    return grid_section

def transpose_matrix(matrix):
    t_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return t_matrix

def calculate_n_ways_h(grid):
    n = 0
    for row in grid:
        for j in range(len(row)-1):
            if row[j] == '.' and row[j+1] == '.':
                n += 1
    return n

def calculate_n_ways(grid):
    x = calculate_n_ways_h(grid)
    t_grid = transpose_matrix(grid)
    y = calculate_n_ways_h(t_grid)
    return x + y

first_l = [int(x) for x in input().split()]

n_r = first_l[0]
n_c = first_l[1]

grid = []
# read grid
for i in range(n_r):
    r_str = str(input())
    r = [c for c in r_str]
    grid.append(r)

n_q = int(input())
# for each querie, calculate
for i in range(n_q):
    raw_coords = [int(k) for k in input().split()]
    r1 = raw_coords[0]
    c1 = raw_coords[1]
    r2 = raw_coords[2]
    c2 = raw_coords[3]

    grid_section = get_grid_section(grid, r1, c1, r2, c2)

    n_ways = calculate_n_ways(grid_section)

    print(n_ways)
