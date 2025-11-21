inp = """.######.
#..##..#
#......#
##....##
##....##
#......#
#..##..#
.######."""
test_inp = """#......#
..#..#..
.##..##.
...##...
...##...
.##..##.
..#..#..
#......#"""


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


def compare_centre(board, pattern):
    for x in range(8):
        for y in range(8):
            if board.get((x + 13, y + 13), False) != pattern[x, y]:
                return False
    return True


def count_actives_selected_step(inp, steps):
    board = {(x, y): False for x in range(34) for y in range(34)}
    pattern = parse_input(inp)
    matches = []
    for i in range(steps):
        board = step(board)
        if compare_centre(board, pattern):
            cactive = count_active(board)
            if len(matches) > 1 and matches[0][1] == cactive:
                cycle = i + 1 - matches[0][0]
                offest = matches[0][0]
                print(f"Cycle detected! Cycle length: {cycle}, offset: {offest}")
                completed_cycles = (steps - offest) // cycle
                actives_in_cycle = sum(m[1] for m in matches) * completed_cycles
                remaining_steps = (steps - offest) % cycle
                print(f"Completed cycles: {completed_cycles}, actives in cycles: {actives_in_cycle}")
                remaining_actives = 0
                for m in matches:
                    if m[0] - offest <= remaining_steps:
                        remaining_actives += m[1]
                print(f"Remaining steps: {remaining_steps}, remaining actives: {remaining_actives}")
                return actives_in_cycle + remaining_actives
            matches.append((i + 1, cactive))
            print(f"Match at step {i+1}, active cells: {cactive}")    
    
    return matches

def main():
    print(f"(examples): {count_actives_selected_step(test_inp, 1000000000)}")
    print(f"(actual): {count_actives_selected_step(inp, 1000000000)}")
    
if __name__ == "__main__":
    main()