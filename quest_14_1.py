inp = """######...#
#.#.....##
.#..#..#..
.#.#...###
#.....####
##..#.....
..###.#..#
..#.#..#..
.###..#.##
.####.###."""
test_inp = """.#.##.
##..#.
..##.#
.#.##.
.###..
###.##"""


def parse_input(inp):
    grid = dict()
    for y, line in enumerate(inp.splitlines()):
        for x, char in enumerate(line):
            grid[(x, y)] = char == '#'
    return grid

def step(board):
    new_board = dict()
    for (x, y), active in board.items():
        active_neighbors = sum((board.get((x + dx, y + dy), False)
                                for dx, dy in ((-1, -1), (1, 1), (-1, 1), (1, -1))))
        new_board[(x, y)] = ((active and active_neighbors % 2 == 1) or 
                             (not active and active_neighbors % 2== 0))
    return new_board

def count_active(board):
    return sum(board.values())

def count_actives_every_step(inp, steps):
    total = 0
    board = parse_input(inp)
    for i in range(steps):
        board = step(board)
        total += count_active(board)
        print(f"After step {i+1}, active cells: {count_active(board)} total: {total}")
    return total

def main():
    print(f"(examples): {count_actives_every_step(test_inp, 10)}")
    print(f"(actual): {count_actives_every_step(inp, 10)}")
    
if __name__ == "__main__":
    main()