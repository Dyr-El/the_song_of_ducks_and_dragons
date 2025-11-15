inp = """SS#.SS..S##SSS#..........SS..#S..#...S.S.....S...#SSSS...#.#.S.#....SSS.S#SS#..S##..#S......#....S#..
..S.S.S.SS.S#.##S#SSS.SSS#.#SS.#S#...SS#S#S.#.SS....#..###SSS#S.S#S.SSS.....S.....SSSSS.#.SSS.....SS#
.S...S##S#.SSS#....SS##S#SSSS...#..S##.SSS.SS..S.##....#....###.SS#..S.S#.......S#S.##.SS...#...S.#.#
#SS#S......S..#.SSS.S..S#SS.S...S..S..#S.##SS#...SSS#......S#S#SSS..SS...S#S..SSS.S##.#S#S#SS.SS.S.S.
#SS.#SS#....#SSSSSS#.S##S..#...#SS#.S.#S.S##S.SSSSSSS....S..SSS##.#.S#....S..S#SS...SS..#..S....##..#
S.#.S...#...SS.#S###S#S..S...#.S#.SSSS#..S.#..S#.###S.S..###SS....S.#..S#...##.#.....S..SSS.#.#SSS...
S....#S...SS.SS.#....#.S##S..SS.##....#.SSSS.#.S..#S..#.S.SSS..#..SS..#S..##...SS#..#..##..##.S.S##..
.#S##S#SSSSSSSSS#.S..S#S.S.SS.SS#SSSS..S....S#S.#.SS...SS...S..S.SSS#..S.#S.S.SS....SSS.SS##..S.S..#S
SS#S..#.#S.S#S..S..SS#.S#SSS...#..SS#S.##SS#.##S..SS#.SSS.###S..#.S.#..SSS..#.....S.S#...S..S.SS..SSS
###SSS.SSS....S.#SS....##.S.#.##S..S.###.....S..S#.S.SS#.#SSS.S#S#.SSS.#SSS..S..#..S.SS#..#...S..#SS.
...#S.S.S.#S..S#...##SSS.....S#.S...S...#SSSS..S.S.#.SS#..S...#..#SSS.S.S#.......SS....SS.SSS##.#SSS#
##.S....#S..#S.....#S#..#S..S#.#.#S.#S.SSSS.#.SSS#.#..##...S..#SS.#.S.S.S....#S.SSS.SS.S#..#.S.SS#.SS
.#.S.#.##SS..S#..SSS##S...S.S..S.S.SS#.SSS.#..S##.S.S.S.#...SS.S#SSS##.SS#SS##....SS...SS#SSSS#.S..#S
SSSSS.##S#S.S.S.#....#.S....##S..S#..S.S..###...S#...S..S.#.S.#.#.SSS.SS.S#S.SSS.....SSS..SS..S.SS..S
##SS..S#.##.#SS##S.S#SSSSSS..SSS...##...#SSS##..S.S..#.#.#..#S.S.#..#..#.SSS#..S.S#S...##...SS..S.##S
S#.S.SSSS.S..S.#...#..#......S...S.S...SS..S.##SS.S#S#..S..S#..SS.#..#...#S#....S#S###..S..SS...S.SSS
..##S....#...#S#.##..##.S.S.....#####.SS.##.SSS.SS##.S.#.S#.S#.....SS#..S#.#SSS##S.S#.##...S.S.S#.#SS
...#..S.S..#.#.S##.S.S#.SS.S#S#.S..S.S..SSS#...##.S#..S....S..S.S...SS#.SS.......SS.#S#.#....#SSSS#.#
#S#.#.S.S.#S.S..S..#S##.S......S...S#...S....S..SSS##S#..#S.#..SS#..SS#...S.S#..SS.S..SSSS.SS.S#..SS.
#SS##.SS.S.S..S#...##..#.SS...S###.S.S#S..S#SSS...#.##.S.S#.S...S#..##S..S##...SSSSSS#SSS..#S#S#S#S#S
S..##.##SS.S##..#...S#SS.S#SSS#SS##...SSS#.SS#.S.#S.SS..##...S##....##..S.#SS..#.S#..#.#S.#S#.SSS..S#
..S...S#.#S..S..#S...S.SS.SSS#..S...##.S.#S..S.S..SS.#.#..#S..S....#S#SS.SS.#S..S#SSS.S.SS.S..#..#.S.
SS#S.SS##.S.##.S#S..S.#S.S..S.S.#S.#.S..#.###...SS..S.#..SS....SS.##..S.S..S#.SS#SS.S.SS.#.S#....#S.#
SS..#..SS.#....SS#..S....S#..##SS.#.SSS.SS#.S.S..S.#S..S..##S..S#.#.S#.#.S.S.##S.##S.SS#..S#....S#S..
S...SS.#...#S...S...#SS.#S.S####S#S.S..#...#S.SS...S#.##SSSSS##.SS#S..S..#.SSS#S..#.S.#SS#..#..SS.S#S
S.S#S..S.#..SS.#.#.SS##.S.S..S......SS.SS#S.S##S.S..#SS....S.#S..S###..#.S..S...S.##..#..SS..S#..#.#S
S...SS.SS...##S.S#..S.SSS.SS#SS.#SS..S#S#...#S.#.##..#S#.S.SS#.SS.S#S.SSSS#...SS.#......S....#.#.#SS#
SS.S...SS.#.#S.SS....#.##S.#.#....S....SS.SS#..SS.....#SS..S.S#SS.#S.SS..####SS#SS.#.SS#..SSSS#...#S.
S.S#.SSS.S.#S.SS.#..#S.#.S.#.#.S.#S#SS.#SS#..##S.S#..S#.SS.SSS#..#SS.#S#S.....S..#...#.S....S.S.#S.SS
S.SS#SS#S...SSS.SS.......S.##SSSS..S#...#S.S.SSS#..S.S#S..S...S.SSS.#.#.S.S.S#S.SS#.S.SS..#.#.##SSSS.
#.#S#.SS.SS.S...S#..#.S.S..#S#S.S.#SS#S.S#S.S.#..S.SSS.S...##.SSS##S..S#SS.S#.S.#..S..SSS#.#S#S.##.##
.S#.##...S.#S..S.#SS.##..SS.#..S.S.#S.SSS.S#SSS..S..S...#..#.S...#....##SSS.S...S#..#..S##..S...#SS.#
....#......SS.#SS.#..S.S....SS...#SS.SS#S.SS#.S..#.#.#S.#...S##SSS.SSSSS#.S....##S.#SSS.S.#.#SSSSS#.#
SS.##.SSS#.S.S.###.SS...S....S.#..#.#S...SS..#S#S#SS##S.....#.##S...#.S..S..SS##.S..S.SS.#SS.S#S#.#S.
S.##..S....SS.S.S.S..S#SS......S#.S#S#S##.SS.......SSS.SS..S#S..SS#.S.#S.S.S.S...#.S...#SS#.SSS..#.#.
SS.S#SSS....S##.S.S#S..S#S.SSSS#..S....S.S.S.SS.#S#.SS#...S.S##S...#S...SS..#..S.SS#S.S.#S#.SSS....S.
#..S.S.##....S.#SSSS....SS.#.SSS...S.SSSS##.#.#.S.#.#SS.#S..S##.S#S.#.#S..SS.#..S##..S#..S.SS.##S..S#
SS.S#SSS.###..S..#S##.SS.S#.#S.SS###S##..S..SS#.##SS.SS.#S.##SS.S#S#S##.....S##SS......#S##SS#.S#SS.S
.S#S....#SS#..S#....#..SS.S#.#S.....##SS..##S...S...S#S.##S.S#S.....#S.SSS....S.S##SSS#..S#SS.SSS.S.S
.#.#SS.S#SS#S.S####S#.SS......#SS.....#S....#S..S#.S#S...S.S...###S....##.SS#..S#S##.SS..#S..SS.S....
S.S.#SS.SS.S.###.S##SS.SSS.##S....#..S.#S.##SS.##S.#S#.SS..S.S##..#...#SSS.S..#.SS.#....S#SS.S#..S##.
S#...S#S.#S..#S.S#S.S.#SSS.......#...S.S.#S#.S#SS..#SS#SS.....#SS..SSS.#.S..S..S.#.S.#.SS...SS...#.#.
.S.SSS.S..SSSSSS.SS#.SS.SS.S.SS....S#S.SS#..S#S.SSS.S...S..#....#....#..#SS.#......#SS#SS#S.#S...S#SS
.#..#SS#....SS##S#S#S..SS#.SS#SS..#..#.#..S#S.##S.#SSS...S#.S#S##.#S...S#S...S#.#..S.S.##S.S.S..#.S##
S..#S#.SSS..#..#.#S..S###S.#..#..SS#.S#.#..S....#S.#S.####..S#SS..#S#SS.S#..S..S#.#..#..S.S.SS##S#.##
#SS.......S......SS#.SS.#S.#.#S#.....#S.SS.SS#S.S.#.#.S...#SS#...SSS..S.S..S##S..SS#...#S#.SSS#S.S.S#
S#S...#...S##S.......S#.##.S.S.#S.#S#..#SS..SSS.S#....S.S.S..#.S..#S..S..SSSS..S..S#S..S#SSS.SS..#..#
S.S..S..S##....S#.#.S..S#.S....##SSSSS.#.#SSS..###.##S#.#S.#S##.#S.#..#.SS.##..S#..#S##S...S.S.S....S
S..##SS##.S#.S.S##SS.S.#.S.SS...#S.##...SS...S...S.SS####S..S...SS.S#.S.S...S..S#.#.S.....SS.S.SS.S..
.S#S.##.S..#.##.SS.##.SS.#S.#S#...SSS...S#S.###....#SSSS..S#SS##S#.#S.SSS#..S#..S..SS.S..SS..SS#SS...
S#SS......##....S..S...S#S.SS..S..S##.#SS..S.S#.S.D.S##S.#....#S.....S.#.#S#S....##..S...S.##.S.SS#.S
.#..##..SS#..S.S#.....#.S.S..##.S.#.SSS.#S#SS.S.#SS.S..S..S.S...SSS...SSS..#.SS#..#...S.#....###..S.#
##..S.#S.....#SS.S#S#..S.S..SS#.SSS.S.#.SS...#S#S.S#.S#....##S.#S.S.#SS.S.#.S..S#...S.S..SS..S..S...S
.#.S....S...SS#..#.SSSS.#..S...S#S..S.##SSSSS##.....SS.SS.S.##..#SS...#.SSS.S..S..#SS..#...S.S#SS#...
..#S.S##S.#.S..S.SSSSS.S###.S.#S#.SS..SSS..S.SS#S..S......SS.#SS.S#.###SS.#S.S..SS.S.##S.S...S..S...S
..#.S...#..#...##.SSSS.S.S..#.S.SS##..S.#..SS.SS##S#..##SS...#S..SS.S.#SS#......S....#.S.SS.S.SS#..#S
#SS..S..S#.S..#S.S..S.SS###.S.....S.SSS..#.#S#...S##.S.S##SS.S#S#.#SS#SS#.SS.SSSS#SS.S..S##....S..S..
##.S..#.#..#S.S##.S#..#S#.#S#SS..#SS...SSSS#...#..SS.#S#S#..SS..SS.SSSS..#S.#S.S...S.#..S..S.#SS..S..
#S#.S...#......#..#.S...S#SSS.#S#S.S...#.#S..#.#.S..#...S..S...###S.S....##.SS#.S..#S.#SS..#SS#SS..S.
...S.SS.#.S##.S#...#.#...S.S.#..#.S.#.#.......SS.#.S##..#S..#.S.......S#S...#S..S.#S....#SS#SS..#S.#.
S#..##..S...S.S.SSS#SS....SSSS..S....S....SSS.###SSS##S#.S###S........SSSS.#..S.S..#..SS.........S..S
SSS.S.S#S.S...S#S.S...##...S.S.#.#.#SS##...S..S.#..#.....#.#.S.SS#...SS.S####..#..S#SSS.S.SS..##S...S
...S.#.S..#SSSS...SSS##S.S.S..#.#....SSSS.##.S.S.SSS.#S..SS#.#S.SSS##...S.#S.S.S##S...SSS.#SS.S#..#..
#.SS.#S#SSS.#.#.#SS##.S..SS#..#.#SS..#......#S#.#S..S.#S#...#.S#.##..#...S#SS#S.S..SS........S#.#....
#.S.S.S...#SS.SS.SS.S#.###.##...##.S..#..#.#S.#SS.SS#.##S#.#..#..S...S..S.SS..S...S.SSSS..S.#.SSS.#S#
..SS.SS.###.SS.S#.SS.SS...S.S##S#SS.S..#S..S..S#..##SS#SS#.S.#.S#S..SS#.S#S.SS##.....S#S....SSSS#...S
.#.#S##.SS.S.SS.SSSS.SS#S..##S.SSSSS.SSS.##.S.#.SS##...SS#S.#.......S.#SS#S###S#.S#...##.S.#.SS..S.S.
SS....#S.SSSS.#SSS.#.SS.#.SS#.S#.#..#S.SS#...S.S#...S#.SSSS.S..S....S..#S.SS##..###S..#SSSSSSS.S.S#S.
S.#..#...#.S##.#SS#S#SS....S#.S.####..SSS.S..S##..SSS.S...#.#S.#SSS##SS#.SS#S.#S.#.#SS..S..#S..#.S.#S
.S..S.SSS#S.#SS...SS..#.S.#SSS#.S..S#...S.S##SS..SS...SS.....SS.S.#....S.S...#.S....S#SS..SS..#S.S.SS
#.....##....SS.S..##...SSS#....#.SSSS.S.S#..##S#.SS#S##SS#SSS.###S#S#.S.SS..SSSSSS###SSS##...S.S...S#
..S#S##S#...#.#S..##..SSS.#SSS#.S....S###S..S#.S#SSS.####..#S.SS##....#S..S..#...SS#SS#S#SS##..#SS#.S
##SSS...SSSSSSSS##.S#SSSS.SS..#SSS..##S.S..#SS.S.SSS#S..#.#SS...S..##.#...#S.....#..#SS.SS#S#.S##..S.
..S.#..#.#..S.S#SSS###...#.SS#.#....S#SSSSS#SS.SS#SSSS.#S.....SS.##.SSS..S....#..S..S#.SSSSSS#S....#.
SS....S.S#.S....#S.#S..SSS..S....#S##SSS#S...##..SSS##..SS.SS...##.##..SSSSS#...S...#...#..#..S#S.#SS
S..SS###.#...##.S.S......S#..S.##.S#S#...S#S.#SS.S...S..#.SSS.SS.#S.#.S##.....##....##.SSS.#SS.S#.S.S
...SSS...#.....S...#.#S.##S..#S##.#.S....S#S#.SS..#S##S.S#.SS#...S....SS.....S#.##.....S.S.SSS.#SS.#S
S..SSS#.SSS.S##SS.#.SS#S#.S....##.##S##S.##.#.SS.#.S.SS.#S.S..S.#S.SSS#..SS.#..S#S.S.#.#..SSSSS#S.#..
#S.#S.S.SS..SS#.SS.....#.###.#S####.##.S.SSSS#..S....S..S...SS.S##.SS..S##S.S......#SS#...S#...SSS#..
S.....#S#.S.S.S.SSS...S.S.S...S.##..S#.SS#....S..S#.#S##S.S...S.S...#......S....S.#.###.SS#.SSS#..S#S
S..#.##S...SSSSS.....S..S#S#S#S#.SS##..S..S#..#...S........SS#S.#S#S#.#.#.S.S#..SS#.S.S.##.#.#S.#.S.#
S..#..S...#S###S..##..#S..SSSS..SSS.#S##S#S####.SS.#..S.S...#.S.S.#.....#..SS..S#......#.SS.S.S.#SSS.
S#.#S...SSS...#..#S#S##S.SSS....S....#S..S#.#S#S.........S..#S#S.S..#SSS.S###S.SS#S.#S#.S.S..SS...S..
SSSS..#.S.S.S.#S#.SS.S#.SS.S..#S#..S....S#..S...#.S.S.S#.SS#....#SS#SS...SS...#S#.#...#S.SS#S.S..S.#.
###.#..#.S...SSSS#S.SS.SS..#..##SSS.#SS#..S..SS#S#S..#..###.S.SSS...S#S#S..S...#S#.SSSSSSS#S....#....
###..S.##SSS.#SS..##S.#S.SS.S#SSS.#....#S...S..#S..#..#..S..S..S.SS..S.S...SS.S##.##SSS..S#...#SS.S.#
S#.#.#S.S#SS.#..S...SS#S#S..SS.#SS##S.S.#S..#S..S...###S...#.S..##..S..SSS.##..#S..S.S.S#..S.S.#SSS#.
SSS##.SSSSSSS.S###.SS.S.##...SS#S.#S.....SSS..S.#S.SSS.#S###S.S.S##S...##.S.....#SS..#.S#SS..SS#S.SS.
S..#S..S#.SS#SS##SS...S....#.#SS.SS.S.S.SS.S###....#S###S#S...SS..###.SSSS.S#SS..#.SSS..#.S#SSS##SS.S
SS..SSS.#..S...#.S#S..S##SSSS#...S.#...S.SS.SSS..#.#SS.###.S.S#SS.SSS#.S...S#S...SS.####S..S#.#S.SS#.
S##.S##.....SS#SS.S#.SS..#.S..S..SS#S#S##S.#SSS.#S...#S#..#S..S##.##S##SS#...S.#.##SSS#.#.##.SS##.S.#
..#..##..SS.S...SS...#S.S..#SSS..####SS.SSSS.#..#S#S.#S.S..S.S..S.SSSS###S..##S..S.S.#S.#..S..##.SS#S
S.#SS...#S.SS.SSSS#S.#S##..S....S.S.S....#SS..#.S.#S.S...S#...S.SSSSS...#..S#.#SSS#..#SS..SSS..##.S#.
SSS#..##.S###.....#S#.S.S#....SSSS.#..SS...SSS#.#S...#S..#S.###.#SSSSS....##SS#..#S.S.#.S..SS#.SS.#.S
S...S.#....S#...##S.#S.S#S##S....##.S..S.#.##.SSS..SSSS..S..S.SSSSS.S..SSS#..S##S...S#SS##SS.#.SSS...
.S..#SS.#...#.S.##......S....SS#S.S..SS.S.#..S.#S#.S..#.S#S#S...#...SS###..S..SS.#...#.S...SSS...SS#.
#SSSS.S#S####S..###...SS#S..##..SS.SS#.S.S.S..#..S.SSSS.S#....SSS..#SSSS.SSS.S#S#SSS.S..S#.#.S.###S#.
.S##..#SSS..S.S.SSS.#.#....S.S..#SS.....#SS....SS.S#S.S.#S.#...S.S#S...#S#S.S.#...S.#S#.#..S.#S.SS##.
#SS.S...S.....#S.#..#.SS..S###.#.#.##.SS...#.#.#S#.#.SS.S#..#SS.......#....S.#S.....S.#.S#.SS#S..#.##
..SS.##S##S.#.#.S....S......S.#.S.S#.SSS.SSSS.#S..S.#...#.S##...SSSS.S.S..#..SS.S..SSSS.S#..##.SS.#.#
#..SS.SSSSS.S#SS..S.S..S#.##S.SSS#.#SS.S.SS.#.S.S.###SS..SS.SS....S..SS.SSS..SSS...##...S..#S.SS#S..S"""
test_inp = """...SSS##.....
.S#.##..S#SS.
..S.##.S#..S.
.#..#S##..SS.
..SSSS.#.S.#.
.##..SS.#S.#S
SS##.#D.S.#..
S.S..S..S###.
.##.S#.#....S
.SSS.#SS..##.
..#.##...S##.
.#...#.S#...S
SS...#.S.#S.."""


def parse_board(inp):
    board = {}
    for y, line in enumerate(inp.splitlines()):
        for x, c in enumerate(line):
            board[(x, y)] = c
            if c == 'D':
                dragon_pos = (x, y)
    return board, dragon_pos


def dragon_moves(board, start_pos, moves):
    positions = [{start_pos}]
    for _ in range(moves):
        new_positions = set()
        for x, y in positions[-1]:
            for dx, dy in [(2, 1), (-2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2), (2, -1), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in board:
                    new_positions.add((nx, ny))
        positions.append(new_positions)
    return positions


def sheep_positions(board):
    return {pos for pos, c in board.items() if c == 'S'}


def eat_sheep(board, dragon_position, sheep_positions):
    total = 0
    for pos in dragon_position:
        if pos in sheep_positions:
            if board[pos] != '#':
                print(f"Eating sheep at {pos}")
                total += 1
                sheep_positions.remove(pos)
            else:
                print(f"Sheep at {pos} is protected by a rock")
    return total


def move_sheep(board, sheep_positions):
    new_sheep_positions = set()
    for x, y in sheep_positions:
        nx, ny = x, y + 1
        if (nx, ny) in board:
            new_sheep_positions.add((nx, ny))
    return new_sheep_positions


def eaten_sheep(inp, steps=4):
    board, dragon_pos = parse_board(inp)
    dragon_positions = dragon_moves(board, dragon_pos, steps)
    sheeps = sheep_positions(board)
    total_eaten = 0
    for step in range(steps):
        print(f"Before step {step+1}: No of sheep left: {len(sheeps)}")
        total_eaten += eat_sheep(board, dragon_positions[step + 1], sheeps)
        print(f"Eat step {step+1}: No of sheep left: {len(sheeps)}")
        sheeps = move_sheep(board, sheeps)
        print(f"Move sheep {step+1}: No of sheep left: {len(sheeps)}")
        total_eaten += eat_sheep(board, dragon_positions[step + 1], sheeps)
        print(f"Eat sheep {step+1}: No of sheep left: {len(sheeps)}")
    return total_eaten


def main():
    print(f"Sheep (examples): {eaten_sheep(inp=test_inp, steps=3)}")
    print(f"Sheep (actual): {eaten_sheep(inp=inp, steps=20)}")
    

if __name__ == "__main__":
    main()