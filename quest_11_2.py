inp = """604975
7354
387444
3030
198274
268257
222754
198812
3610
874280
943767
437478
621375
237715
98143
624748
9930
916377
870883
512275
418041
5337
247160
225862
9314
4009
210563
9466
575156
394278
2652
407453
425363
373533
997270
899308
528919
60049
7581
578860
706746
155458
499954
470584
678552
291403
233044
244382
677658
398857
51696
201845
10247
480398
720626
397237
349528
671464
850899
737347"""

test_inp1 = """9
1
1
4
9
6"""

test_inp2 = """805
706
179
48
158
150
232
885
598
524
423"""


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

def is_balanced(cols):
    return all(cols[i] == cols[i+1] for i in range(len(cols) - 1))

def moves_until_balanced(inp, rounds):
    cols = parse_flock(inp)
    phase = 1
    print(f"round 0: {cols}")
    round = 0
    while True:
        if phase == 1:
            if not do_right_move(cols):
                phase = 2
                print(cols)
        if phase == 2:
            do_left_move(cols)
        round += 1
        # print(f"round {round + 1} {phase=}: {cols}")
        if is_balanced(cols):
            break
    return round

def main():
    print(f"Moves checksum (examples): {moves_until_balanced(test_inp1, 10)}")
    print(f"Moves checksum (examples): {moves_until_balanced(test_inp2, 10)}")
    print(f"Moves checksum (actual): {moves_until_balanced(inp, 10)}")
    
if __name__ == "__main__":
    main()