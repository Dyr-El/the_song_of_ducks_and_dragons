mentors = """ABCcCBAacAcAbcACBBaACAaBcbBBAcccBabAcbaCCCbAbAbbaCaCCccCAccaCBBBCbCBcabABbaCcBaBaBaCcCcCaBBBCccBbCbc"""

def sword_mentors(data):
    total = 0
    mentors = 0
    for c in data:
        if c == 'a':
            total += mentors
        elif c == 'A':
            mentors += 1
    return total

def main():
    print(f"Sword mentors (examples): {sword_mentors('ABabACacBCbca')}")
    print(f"Sword mentors (actual): {sword_mentors(mentors)}")
if __name__ == "__main__":
    main()