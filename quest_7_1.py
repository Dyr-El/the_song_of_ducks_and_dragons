inp = """Kycyth,Aurethyris,Mavcyth,Kyfal,Aurefal,Mavfal,Kythyris,Mavthyris,Aurecyth

c > y
v > t,f,c
i > s
h > y
u > b
t > h
a > l,b
A > u
r > i,e
y > t,r,b
M > a
e > t,f,c
f > a
K > y"""

test_inp = """Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h"""

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    names = lines[0].split(',')
    rules = {}
    for line in lines[2:]:
        src, dsts = line.split(' > ')
        rules[src] = dsts.split(',')
    return names, rules

def test_name(name, rules):
    for c1, c2 in zip(name, name[1:]):
        if c1 not in rules:
            return False
        if c2 not in rules[c1]:
            return False
    return True

def problem(inp):
    names, rules = parse_input(inp)
    for name in names:
        if test_name(name, rules):
            return name
    return None
    
    # Implement the logic to solve the problem using names and rules
    return 0

def main():
    print(f"Name (examples): {problem(test_inp)}")
    print(f"Name (actual): {problem(inp)}")
    
if __name__ == "__main__":
    main()