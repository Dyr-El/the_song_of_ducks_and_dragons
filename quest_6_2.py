mentors = """ABCAaaaaabBBAbcbacBbCaBBbCbaAcBbcbbAbaaAaACABaccbBCbabccCABCBcBACbcBBAAaCCBCbcABAbAcbCBaCabBbaACcAbBaBBaBBccaacBbBcbACBbbcBBBCCcaacbBbaCAcaabcBaAaccAAbcBCABCAaAaBCCcbBaBbaAbAACabcbBCACBbabCabcBaaaAaABBcCAACaaaCAaAccbABcaaCAccCcCBCcbbaCcbbcbBAaccbBCcAcbBABBABCaCABbcaccbBBCbacaAAAcBAAABCBcaCBCCCBCBCCc"""

def all_mentors(data):
    total = 0
    mentors = { 'A': 0, 'B': 0, 'C': 0 }
    for c in data:
        if 'a' <= c <= 'c':
            total += mentors[chr(ord('A') + (ord(c) - ord('a')))]
        elif 'A' <= c <= 'C':
            mentors[c] += 1
    return total

def main():
    print(f"All mentors (examples): {all_mentors('ABabACacBCbca')}")
    print(f"All mentors (actual): {all_mentors(mentors)}")
if __name__ == "__main__":
    main()