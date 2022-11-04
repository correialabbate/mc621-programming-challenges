def sort_custom(list):
    return list[0]

def calculate_n_pieces()

n_pieces = int(input())
pieces = []

idx = 0
for i in range(n_pieces):
    piece_coordinates = [int(x) for x in input().split()]
    piece_coordinates.append(idx)
    pieces.append(piece_coordinates)
    idx += 1

ordered_n_pieces = []
sorted_pieces = sorted(pieces, key=sort_custom)
for pos in len(sorted_pieces):
    n_pieces_down = calculate_n_pieces(pos, sorted_pieces)