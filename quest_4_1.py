gears = [1000, 976, 970, 962, 938, 926, 903, 877, 859, 848, 826, 803, 785, 778, 777, 752, 729, 703, 687, 671, 645, 630, 601, 584, 576, 569, 552, 523, 513, 491, 465, 455, 429, 415, 397, 379, 375, 350, 338, 325, 307, 297, 288, 261, 243, 230, 226, 202, 198, 174]

def number_of_full_rotations(gears, source_rotations=2025):
    rotations = source_rotations
    for i in range(len(gears) - 1):
        rotations = rotations * gears[i] / gears[i + 1]
        print(f"After gear {i + 1} ({gears[i]} to {gears[i + 1]}): {rotations} rotations")
    full_rotations = int(rotations)
    print(f"Number of full rotations of the last gear: {full_rotations}")

def main():
    number_of_full_rotations([128, 64, 32, 16, 8])
    number_of_full_rotations([102, 75, 50, 35, 13])
    number_of_full_rotations(gears)

if __name__ == "__main__":
    main()