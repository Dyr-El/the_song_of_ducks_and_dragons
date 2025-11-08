fishbone = [52,[2,8,6,3,3,2,9,4,7,4,4,9,3,6,3,4,7,9,8,3,2,7,5,9,1,8,3,4,9,2]]

def fishbone_quality(fishbone):
    identifier, parts = fishbone
    print(f"Fishbone ID: {identifier}")
    structure = []
    for item in parts:
        found_place = False
        for s in structure:
            if item < s[1] and s[0] is None:
                s[0] = item
                found_place = True
                break
            elif item > s[1] and s[2] is None:
                s[2] = item
                found_place = True
                break
        if not found_place:
            structure.append([None, item, None])
    print(f"Final structure: {structure}")
    print(f"Quality: {''.join(str(x[1]) for x in structure)}")

def main():
    fishbone_quality([58, [5,3,7,8,9,10,4,5,7,8,8]])
    input("Press Enter to continue...\n")
    fishbone_quality(fishbone)

if __name__ == "__main__":
    main()