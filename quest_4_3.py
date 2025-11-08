from fractions import Fraction

gears = [(545, 545), (528, 528), (524, 524), (517, 517), (505, 1010), (495, 495), (491, 1964), (482, 482), (479, 1437), (461, 461), (451, 1804), (436, 436), (423, 423), (420, 420), (418, 1254), (414, 414), (410, 410), (405, 405), (403, 403), (388, 388), (369, 1476), (361, 361), (348, 1044), (338, 338), (332, 1328), (331, 331), (317, 634), (316, 316), (300, 300), (299, 299), (282, 846), (277, 277), (267, 1068), (258, 258), (249, 498), (232, 232), (221, 442), (213, 213), (209, 418), (205, 205), (187, 374), (178, 178), (172, 688), (155, 155), (136, 272), (123, 123), (114, 342), (110, 110), (106, 424), (58, 58)]

def number_of_target_rotations(gears, source_rotations=100):
    rotations = Fraction(source_rotations)
    for gear1, gear2 in zip(gears, gears[1:]):
        inp_teeth1, out_teeth1 = gear1
        inp_teeth2, out_teeth2 = gear2
        rotations *= Fraction(out_teeth1, inp_teeth2)
        print(f"After gear {gear2}, rotations: {rotations}")
    full_rotations = int(rotations )
    print(f"Number of full rotations of the last gear: {full_rotations}")

def main():
    number_of_target_rotations([(5, 5), (5, 10), (10, 20), (5, 5)])
    number_of_target_rotations([(5, 5), (7, 21), (18, 36), (27, 27), (10, 50), (10, 50), (11, 11)])
    number_of_target_rotations(gears)

if __name__ == "__main__":
    main()