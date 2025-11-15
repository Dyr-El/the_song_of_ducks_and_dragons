inp = """..SSSSS
.......
....##.
##.#.#.
######.
###D###"""
test_inp1 = """SSS
..#
#.#
#D."""
test_inp2 = """SSS
..#
..#
.##
.D#"""
test_inp3 = """..S..
.....
..#..
.....
..D.."""
test_inp4 = """.SS.S
#...#
...#.
##..#
.####
##D.#"""
test_inp5 = """SSS.S
.....
#.#.#
.#.#.
#.D.#"""


def parse_board(inp):
    board = {}
    for y, line in enumerate(inp.splitlines()):
        for x, c in enumerate(line):
            board[(x, y)] = c
            if c == 'D':
                dragon_pos = (x, y)
    return board, dragon_pos


def dragon_moves(board, pos):
    moves = [(2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (-2, -1), (-2, 1)]
    positions = list()
    for dx, dy in moves:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if new_pos in board:
            positions.append(new_pos)
    return positions


def sheep_moves(board, sheeps, dragon_pos):
    moves = []
    for sheep in sheeps:
        new_pos = (sheep[0], sheep[1] + 1)
        if new_pos in board and board[new_pos] == '#':
            moves.append((sheep, new_pos))
        elif new_pos not in board:
            moves.append((sheep, None))
        elif new_pos == dragon_pos:
            continue
        else:
            moves.append((sheep, new_pos))
    return moves
        

dm_cache = {}
def find_dragon_moves(board, sheeps, dragon_pos, moves=[]):
    if (dragon_pos, frozenset(sheeps)) in dm_cache:
        return dm_cache[(dragon_pos, frozenset(sheeps))]
    possible_moves = dragon_moves(board, dragon_pos)
    total = 0
    for move in possible_moves:
        if move in sheeps and board[move] != '#':
            sheeps = sheeps - {move}
            if sheeps == set():
                total += 1
            else:
                total += find_sheep_moves(board, sheeps, move, moves + ["D>" + chr(ord('A') + move[0]) + str(move[1] + 1)])
            sheeps = sheeps | {move}
        else:
            total += find_sheep_moves(board, sheeps, move, moves + ["D>" + chr(ord('A') + move[0]) + str(move[1] + 1)])
    dm_cache[(dragon_pos, frozenset(sheeps))] = total
    return total


def sheep_positions(board):
    return {pos for pos, c in board.items() if c == 'S'}


sm_cache = {}
def find_sheep_moves(board, sheeps, dragon_pos, moves=[]):
    if (dragon_pos, frozenset(sheeps)) in sm_cache:
        return sm_cache[(dragon_pos, frozenset(sheeps))]
    possible_moves = sheep_moves(board, sheeps, dragon_pos)
    if not possible_moves:
        sm_cache[(dragon_pos, frozenset(sheeps))] = find_dragon_moves(board, sheeps, dragon_pos, moves)
        return sm_cache[(dragon_pos, frozenset(sheeps))]
    total = 0
    for move in possible_moves:
        if move[1] is None:
            continue
        sheeps = sheeps - {move[0]} | {move[1]}
        total += find_dragon_moves(board, sheeps, dragon_pos, moves + ["S>" + chr(ord('A') + move[1][0]) + str(move[1][1] + 1)])
        sheeps = sheeps - {move[1]} | {move[0]}
    sm_cache[(dragon_pos, frozenset(sheeps))] = total
    return total


def calculate_moves(inp):
    dm_cache.clear()
    sm_cache.clear()
    board, dragon_pos = parse_board(inp)
    sheeps = sheep_positions(board)
    return find_sheep_moves(board, sheeps, dragon_pos)


def main():
    print(f"Sheep (examples): {calculate_moves(inp=test_inp1)}")
    print(f"Sheep (examples): {calculate_moves(inp=test_inp2)}")
    print(f"Sheep (examples): {calculate_moves(inp=test_inp3)}")
    print(f"Sheep (examples): {calculate_moves(inp=test_inp4)}")
    print(f"Sheep (examples): {calculate_moves(inp=test_inp5)}")
    print(f"Sheep (actual): {calculate_moves(inp=inp)}")
    

if __name__ == "__main__":
    main()