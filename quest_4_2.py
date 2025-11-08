from fractions import Fraction

gears = [931, 919, 894, 881, 867, 843, 827, 817, 802, 794, 772, 748, 730, 708, 705, 679, 662, 657, 639, 626, 625, 620, 600, 590, 587, 570, 552, 529, 505, 502, 500, 492, 487, 477, 475, 473, 463, 439, 435, 410, 383, 365, 345, 319, 297, 273, 253, 230, 201, 168]

def number_of_source_rotations(gears, target_rotations=10000000000000):
    rotations = Fraction(target_rotations)
    for i in range(len(gears) - 1, 0, -1):
        rotations = rotations * gears[i] / gears[i - 1]
        print(f"After gear {i + 1} ({gears[i]} to {gears[i - 1]}): {rotations} rotations")
    full_rotations = round(rotations + Fraction(1, 2))
    print(f"Number of full rotations of the last gear: {full_rotations}")

def main():
    number_of_source_rotations([128, 64, 32, 16, 8])
    number_of_source_rotations([102, 75, 50, 35, 13])
    number_of_source_rotations(gears)

if __name__ == "__main__":
    main()