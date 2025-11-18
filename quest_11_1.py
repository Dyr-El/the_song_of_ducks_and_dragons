inp = """1
1
5
16
17
8"""

test_inp = """9
1
1
4
9
6"""

def parse_flock(inp):
    cols = [int(x) for x in inp.splitlines()]
    print(cols)
    return cols

def do_right_move(cols):
    change = False
    for i in range(len(cols) - 1):
        if cols[i] > cols[i+1]:
            cols[i] -= 1
            cols[i+1] += 1
            change = True
    return change

def do_left_move(cols):
    for i in range(len(cols) - 1):
        if cols[i] < cols[i+1]:
            cols[i] += 1
            cols[i+1] -= 1
            
def calc_checksum(cols):
    return sum((i + 1) * cols[i] for i in range(len(cols)))

def move_checksum(inp, rounds):
    cols = parse_flock(inp)
    phase = 1
    print(f"round 0: {cols}")
    for round in range(rounds):
        if phase == 1:
            if not do_right_move(cols):
                phase = 2
        if phase == 2:
            do_left_move(cols)
        print(f"round {round + 1} {phase=}: {cols}")
    return calc_checksum(cols)

def main():
    print(f"Moves checksum (examples): {move_checksum(test_inp, 10)}")
    print(f"Moves checksum (actual): {move_checksum(inp, 10)}")
    
if __name__ == "__main__":
    main()