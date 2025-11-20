inp = """3306-9017
1708-8742
8796-15781
3813-4950
9885-11696
5360-10592
7403-13152
5754-13074
1231-10980
3598-7020
5249-13711
7727-9520
7977-16094
5942-15744
2677-9167
5759-8504
5712-7557
8775-18641
3638-12551
1881-5351
6271-9188
8988-11195
5746-14928
7453-15511
8528-13660
5663-6903
3424-8152
8157-17015
3348-9473
2835-6673
1627-7292
6968-13740
8039-14844
1040-10451
6392-8083
1342-6532
8446-15952
2748-9982
1108-5612
8386-13445
5915-15064
5761-9211
5474-15147
3500-13222
8749-13319
6481-12052
1522-9974
2950-10291
1516-6258
5423-9885"""
test_inp = """10-15
12-13
20-21
19-23
30-37"""


def create_wheel(inp):
    ranges = [tuple(map(int, line.split('-'))) for line in inp.split()]
    wheel: list[tuple[int, int]] = [(1, 1)]
    for idx, rng in enumerate(ranges):
        if idx % 2 == 0:
            wheel.append((rng[0], rng[1]))
        else:
            wheel = [(rng[1], rng[0])] + wheel
    return wheel

def turn_wheel(inp, steps):
    wheel = create_wheel(inp)
    pos = wheel.index((1, 1))
    numbers_around = sum((max(rng) - min(rng) + 1) for rng in wheel)
    local_pos = steps % numbers_around
    while local_pos >= max(wheel[pos]) - min(wheel[pos]) + 1:
        local_pos -= max(wheel[pos]) - min(wheel[pos]) + 1
        pos = (pos + 1) % len(wheel)
    if wheel[pos][0] < wheel[pos][1]:
        result = min(wheel[pos]) + local_pos
    else:
        result = max(wheel[pos]) - local_pos
    return result


def main():
    print(f"Wheel setting (examples): {turn_wheel(test_inp, 20252025)}")
    print(f"Wheel setting (actual): {turn_wheel(inp, 20252025)}")

    
if __name__ == "__main__":
    main()