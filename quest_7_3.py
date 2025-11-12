inp = """Ny,Nyl,Nyth,Nyss,Nyrix,Elvar,Kal,Grim,Lorn,Cal,Cael,Quir,Urak,Cynvar,Rythan,Xyr,Bryl,Selk,Draith,Rael

a > r,g,t,v,k,n,i
h > z,d,e,m,s,a,c,t
Q > u
m > i,z,d,e,m,s,a,c,t
N > y
B > r
X > y
y > r,v,l
E > l
U > r
z > o
K > a
k > z,d,e,m,s,a,c,t
s > y,s,z,d,e,m,a,c,t
r > c,t,a,o,d,i,z,e,m,s,v,n
v > a
C > a,y
x > z,d,e,m,s,a,c,t
t > h,o
D > r
c > a
l > d,z,e,m,s,a,c,t,v,k
G > r
i > r,t,x,m
g > r
d > r,i
S > e
o > r,n,v
n > z,d,e,m,s,a,c,t,v
e > o,l,v
R > y,a
u > v
L > o"""

test_inp = """Xaryt

X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t"""

test2_inp = """Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i"""

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    names = lines[0].split(',')
    rules = {}
    for line in lines[2:]:
        src, dsts = line.split(' > ')
        rules[src] = dsts.split(',')
    return names, rules

from collections import deque

def generate_names(start, rules):
    seed = deque([start])
    while seed:
        current = seed.pop()
        yield current
        if len(current) >= 11:
            continue
        if current[-1] in rules:
            for nxt in rules[current[-1]]:
                seed.append(current + nxt)
        # print(seed)
        # input()

def test_name(prefix, rules):
    for c1, c2 in zip(prefix, prefix[1:]):
        if c1 not in rules:
            return set()
        if c2 not in rules[c1]:
            return set()
    result = deque()
    for gen_name in generate_names(prefix, rules):
        if 7 <= len(gen_name) <= 11:
            # print(gen_name)
            result.append(gen_name)
    return set(result)

def problem(inp):
    total = set()
    names, rules = parse_input(inp)
    for name in names:
        total = total | test_name(name, rules)
    return len(total)

def main():
    print(f"Number of names (example 1): {problem(test_inp)}")
    print(f"Number of names (example 2): {problem(test2_inp)}")
    print(f"Number of names (actual): {problem(inp)}")
    
if __name__ == "__main__":
    main()