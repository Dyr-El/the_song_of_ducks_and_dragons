inp = """1:TTTGCAATAAATGACGAATTCTCGCAAGTCCGCATTGTCGGGAATCCCTATACAACCCTCCAGGGTAATCCAGCGGGCACCCACGCACCGTGATCCTTTATCGTAGAATGCGTTGCCCACATGCGGAC
2:ATTCACCTAGCTGAGAGACCTTGGTGTCATCATCTTGCTGCTGCCAAGCCTTTGTACGCGACCAACCAACTCGATCGAATCTGCTGCATCCGTCCAGAGTTCTAAGGAACTTCCTAAGGTTGCGGGGC
3:TTTGAACTAGATGAGGAATCCTGGCGAGTTCGTCTTGTCGCTACCCACTATTTGTCCGTCCCGGACCATCCCGATGGAATCCGCTGCATCCGACCCGAGATCTAAGGAACCGTTTCCCATAGCCGGGC"""
inp_test = """1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG"""


def check_child(child, parent1, parent2):
    return all(c in (p1, p2) for c, p1, p2 in zip(child, parent1, parent2))


def child_similarity(child, parent):
    matches = sum(c == p for c, p in zip(child, parent))
    return matches


def find_similarity(inp):
    lines = inp.strip().split('\n')
    sequences = [line.split(':')[1] for line in lines]
    if check_child(sequences[0], sequences[1], sequences[2]):
        child, p1, p2 = sequences[0], sequences[1], sequences[2]
    elif check_child(sequences[1], sequences[0], sequences[2]):
        child, p1, p2 = sequences[1], sequences[0], sequences[2]
    elif check_child(sequences[2], sequences[0], sequences[1]):
        child, p1, p2 = sequences[2], sequences[0], sequences[1]
    else:
        print("No valid child found")
    return child_similarity(child, p1) * child_similarity(child, p2)

def main():
    print(f"Child similarity (examples): {find_similarity(inp_test)}")
    print(f"Child similarity (actual): {find_similarity(inp)}")
    
if __name__ == "__main__":
    main()