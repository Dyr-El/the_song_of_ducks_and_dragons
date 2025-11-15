inp = """1,32,16,32,16,3,18,2,15,31,15,31,19,3,19,3,19,2,18,2,20,5,21,5,21,4,23,8,24,8,27,11,27,9,25,9,27,11,29,9,24,8,24,4,20,4,20,2,18,2,18,4,21,5,23,7,19,31,19,32,16,28,12,28,8,24,8,24,8,20,4,18,1,21,5,21,1,17,2,15,31,15,28,12,28,12,30,14,2,18,30,14,32,16,32,19,7,23,7,19"""
test_inp = """1,5,2,6,8,4,1,7,3"""

def through_center(inp, nails):
    result = 0
    positions = [int(x) for x in inp.split(',')]
    for p1, p2 in zip(positions, positions[1:]):
        if abs(p1 - p2) == nails // 2:
            result += 1
    return result

def main():
    print(f"Through center (examples): {through_center(test_inp, 8)}")
    print(f"Through center (actual): {through_center(inp, 32)}")
    
if __name__ == "__main__":
    main()