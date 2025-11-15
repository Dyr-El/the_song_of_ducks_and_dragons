inp = """.S.SSS.S.SS.....SSSSS
.SS.SSSSSS.S.SSSSSSSS
SSSSSSS.SSSSSSSSSS.SS
...SSSS.SS..SSSSSSSS.
S.S...S.SSSS..SSSS.S.
...SSS.SSS.SS..SSSS.S
SSSSS.S..SS.SSSS..SSS
SSSS.SSSSSSSSSS..SSSS
SSSS.SSSS.SSSS.SS.S.S
SSS.SSSSS.SSS.SS.SS.S
SSS.SS.SS.D...S.SSSSS
SSS.SSSSSSSSSSSSSSSSS
SS.SSSSSS.S.SS.SSSSS.
SS...SSSSSSSSSSSS.SSS
SSSS..S.SSSSS.SSSS...
.SSSSS.SSSS.SS..S.SS.
S.SS.S.S..SSSSSSS..SS
.SS.S..SSS.S..SSSSSSS
SSSS.SSS...SSSS.S..SS
S.S.SSSSS.SSS.SS.S.SS
S..SSSSSSSSSSSSS.SS.S"""
test_inp = """...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S.."""


def parse_board(inp):
    board = {}
    for y, line in enumerate(inp.splitlines()):
        for x, c in enumerate(line):
            board[(x, y)] = c
            if c == 'D':
                dragon_pos = (x, y)
    return board, dragon_pos


def find_no_sheep(board, start_pos, moves):
    positions = {start_pos}
    sheep = set()
    for i in range(moves):
        new_positions = set()
        for x, y in positions:
            for dx, dy in [(2, 1), (-2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2), (2, -1), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in board:
                    new_positions.add((nx, ny))
                    if board[(nx, ny)] == 'S':
                        sheep.add((nx, ny))
        positions = new_positions
    return len(sheep)


def find_sheep(inp, steps=4):
    board, dragon_pos = parse_board(inp)
    return find_no_sheep(board, dragon_pos, moves=steps)


def main():
    print(f"Sheep (examples): {find_sheep(inp=test_inp, steps=3)}")
    print(f"Sheep (actual): {find_sheep(inp=inp)}")
    

if __name__ == "__main__":
    main()