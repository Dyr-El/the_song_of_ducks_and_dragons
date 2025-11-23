inp = """L88,L99,L55,L22,L11,R44,L22,R11,R44,R77,L66,L99,L11,R33,L99,R55,L22,R99,L44,L44,R55,L88,L33,L22,R11,R44,R99,L22,L99,R22,L33,R33,R55,L55,L44,R22,L88,L11,R33,R11,L66,L77,R66,L44,L22,R88,L55,R99,L55,L99,R44,R11,L11,R33,L22,R77,L99,R88,L88,L88,L11,L11,R11,R55,R66,L66,L22,R99,L77,R77,L22,R66,L99,R99,L11,L99,R44,R55,L11,L66,R66,R11,L99,L11,R88,L11,L33,R88,L44,R66,L22,R66,L66,R88,R99,L99,L44,R99,L22,L11,R66,L55,L33,L33,R44,R55,R99,L22,R99,L22,L33,R22,L77,L44,R99,R11,L22,R11,R55,L11,R55,L44,R99,R44,L33,R44,L55,R33,L22,R44,L33,L33,R66,L22,R22,L33,L22,R11,R66,L99,L22,R88,R55,L66,L33,R77,L66,R88,L11,L11,R22,R99,L99,L55,R11,R88,L44,L11,R33,L55,R33,R22,L22,L55,R44,R77,L88,L33,L33,R55,R77,L22,R55,R44,L11,L77,R88,L22,L33,R22,L77,R33,R99,L55,L55,L44,R99,R55,R22,L77"""
test_inp = """L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"""


def draw_map(moves):
    direction = 0  # 0=up, 1=right, 2=down, 3=left
    start = (0, 0)
    x, y = start
    mp = {start: 'S'}

    for move in moves:
        turn = move[0]
        distance = int(move[1:])

        if turn == 'L':
            direction = (direction - 1) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4

        for _ in range(distance):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            mp[(x, y)] = '#'
    end = (x, y)

    return mp, start, end

from collections import deque
def calc_distance(mp, start, end):
    visited = {start}
    queue = deque([(start, 0)])  # (position, distance)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in mp and (nx, ny) not in visited or (nx, ny) == end:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

def find_distance(inp):
    moves = inp.split(',')
    mp, start, end = draw_map(moves)
    distance = calc_distance(mp, start, end)
    return distance

def main():
    print(f"Find distance (examples): {find_distance(test_inp)}")
    print(f"Find distance(actual): {find_distance(inp)}")
    
if __name__ == "__main__":
    main()