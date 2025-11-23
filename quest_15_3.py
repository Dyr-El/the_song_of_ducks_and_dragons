inp = """R8093763,R1899791,R9396334,R4598666,R2899159,L8599054,R9296373,R3198752,R199942,L6798028,R1999820,L9693113,R9093539,L8397564,R3299043,R8294107,R799768,R2499025,L1699337,L3999560,L8797448,R3397586,R5098011,L6099451,L4798608,R6799252,R1199652,L7094959,R6395072,R7994320,R5795534,L1399006,L7993840,L7699153,R5799362,L6299307,R8394036,R3598956,R6098231,L1199148,L6099329,R7097941,R3299703,L8397564,L8999010,R9693113,R4498695,L7594148,R7597036,R1199076,R5995380,L9896139,R5799362,L3699593,L9497245,L8993610,R9598944,L9493255,R2899681,R3098791,L7697767,R7896919,L7894391,R1999780,R6397504,L9099181,L6195226,R8493965,R8596646,L4596734,L8297593,R8297593,R6997270,L7699307,R6698057,R8394036,L5199428,L8199262,R5499505,R999910,L7197912,R6399296,L2598986,R6195226,L7199352,R2997690,R7097941,L3197728,L7397114,R6995030,L4996450,R9599136,R899649,R2898869,L4996150,L3797302,L4898089,R5498405,R3397586,L9192916,R4996150,R1899829,L1598864,L8593894,R1898651,R2298229,L3996920,R799768,R4398724,L5197972,L8899021,R2698947,L2799188,L9892971,R6697387,R4998050,L9598944,R799432,R4699577,L1598768,L7394302,R8399244,L9897129,R6395072,R3997160,L3998840,R999710,L699797,L7694071,R9392762,L9692531,R2599766,R9898911,R7197192,L5895811,L7394746,L9899109,R3097799,R4296947,L699923,R3999560,L8393532,R7299343,L2399304,L8899199,R7299343,R9799118,R1699507,L5499505,L4098811,R1398922,L7397854,R3497515,R199978,L8296763,R1399454,R3199072,L1699337,L9897129,R7897709,R599766,R2798012,L3297657,L5495765,L5197972,L9596256,R9192916,R1499835,R7694071,L8293609,L6295149,R1899791,L8593378,R7994320,R3898479,L999230,L9896139,R3598596,R9696217,L6997270,L7894391,R1798722,L9792454,R1598864,R7794462,L8294107,L8299253,R2299793,R3297459,L2498075,R4097089,L3097799,R6297543,L7297153,R3999640,L8896529,L9696217,R1599376,R5699373,L7499175,R7497075,R899649,L9198988,L9698933,R8593378,R7896919,L9698933,R9498955,L4996150,L7696997,R1398922,R8893147,L9393326,R5299523,R1699813,R1199532,L3597228,R899649,L699923,L2599246,R3996920,L1099879,L6999230,R3999640,L9493255,R9796178,L6699397,R599946,R3499685,L9298977,R1899259,L1299077,L5899351,R1399846,L5897699,R5297933,L9092993,R9592608,R5199428,R1599856"""
test_inp = """L6,L3,L6,R3,L6,L3,L3,R6,L6,R6,L6,L6,R3,L3,L3,R3,R3,L6,L6,L3"""


def map_walls(moves):
    direction = 0  # 0=up, 1=right, 2=down, 3=left
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left
    start = (0, 0)
    pos = start
    x, y = start
    walls = []

    for move in moves:
        turn = move[0]
        distance = int(move[1:])

        if turn == 'L':
            direction = (direction - 1) % 4
        elif turn == 'R':
            direction = (direction + 1) % 4

        next_pos = (pos[0] + directions[direction][0] * distance,
                    pos[1] + directions[direction][1] * distance)
        walls.append((pos, next_pos))
        pos = next_pos
    end = pos

    return walls, start, end

def create_grid(walls, start, end):
    mp = dict()
    xs, ys = set(), set()
    for (x1, y1), (x2, y2) in walls:
        xs.update([x1 - 1, x1, x1 + 1, x2 - 1, x2, x2 + 1])
        ys.update([y1 - 1, y1, y1 + 1, y2 - 1, y2, y2 + 1])
    xs = sorted(xs)
    ys = sorted(ys)
    prev_x = {x1: x2 for x1, x2 in zip(xs[1:], xs)}
    next_x = {x1: x2 for x1, x2 in zip(xs, xs[1:])}
    prev_y = {y1: y2 for y1, y2 in zip(ys[1:], ys)}
    next_y = {y1: y2 for y1, y2 in zip(ys, ys[1:])}
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        if x1 == x2:
            while True:
                mp[x1, y1] = '#'
                if y1 < y2:
                    y1 = next_y[y1]
                elif y1 > y2:
                    y1 = prev_y[y1]
                else:
                    break
        if y1 == y2:
            while True:
                mp[x1, y1] = '#'
                if x1 < x2:
                    x1 = next_x[x1]
                elif x1 > x2:
                    x1 = prev_x[x1]
                else:
                    break
    mp[start] = 'S'
    mp[end] = 'E'
    return xs, ys, prev_x, next_x, prev_y, next_y, mp


def print_mp(mp, xs, ys):
    for y in ys[::-1]:
        row = []
        for x in xs:
            row.append(mp.get((x, y), '.'))
        print(''.join(row))


from collections import deque
def find_distance(inp):
    moves = inp.split(',')
    walls, start, end = map_walls(moves)
    xs, ys, prev_x, next_x, prev_y, next_y, mp = create_grid(walls, start, end)
    # print_mp(mp, xs, ys)
    queue = deque([start])
    dist = {start: 0}
    while queue:
        x, y = queue.popleft()
        if x in prev_x:
            nx, ny = prev_x[x], y
            if (nx, ny) not in dist and mp.get((nx, ny), '.') != "#":
                dist[(nx, ny)] = dist[(x, y)] + abs(nx - x)
                queue.append((nx, ny))
        if x in next_x:
            nx, ny = next_x[x], y
            if (nx, ny) not in dist and mp.get((nx, ny), '.') != "#":
                dist[(nx, ny)] = dist[(x, y)] + abs(nx - x)
                queue.append((nx, ny))
        if y in prev_y:
            nx, ny = x, prev_y[y]
            if (nx, ny) not in dist and mp.get((nx, ny), '.') != "#":
                dist[(nx, ny)] = dist[(x, y)] + abs(ny - y)
                queue.append((nx, ny))
        if y in next_y:
            nx, ny = x, next_y[y]
            if (nx, ny) not in dist and mp.get((nx, ny), '.') != "#":
                dist[(nx, ny)] = dist[(x, y)] + abs(ny - y)
                queue.append((nx, ny))
        if end in dist:
            break
    return dist[end]

def main():
    print(f"Find distance (examples): {find_distance(test_inp)}")
    print(f"Find distance(actual): {find_distance(inp)}")
    
if __name__ == "__main__":
    main()