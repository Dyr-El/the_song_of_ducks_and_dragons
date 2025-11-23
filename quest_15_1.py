inp = """L6,L6,L3,L3,R6,L3,R3,L3,L3,R6,L3,L3,R6,L3,R6,L6,L3,R3,R3,L3,L6,R6,L3,L3,R3,L6,R3,R3,L6,L6,R3,L3,R6,L6,L6,R6,L6,R3,L3,L3,R6,L3,R3,R3,L3,L3,R3,L3,R6,L6,L3,R3,R3,L3,R6,L3,L3,R3,L3,R6"""
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