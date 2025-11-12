inp = """Ardenisis,Gaerxel,Ilmarthar,Glynnisis,Ardenjor,Glynnthar,Gaerural,Malnixis,Ardenthar,Maliththar,Anornixis,Glynnxel,Malithnixis,Malural,Anorcarth,Glynnjor,Ardencarth,Ilmarzyth,Malisis,Malxel,Cragnixis,Ilmarxelor,Malithzyth,Malithural,Gaerisis,Tarlthar,Tarlnixis,Ilmarjor,Anorisis,Ilmarcarth,Falthar,Gaerthar,Anorxelor,Anorural,Falural,Tarlisis,Anorxel,Cragjor,Cragthar,Glynnnixis,Falisis,Anorthar,Falthar,Maljor,Falnixis,Glynnural,Falcarth,Tarljor,Tarlcarth,Gaerzyth,Malzyth,Glynnzyth,Malthar,Malithcarth,Maliththar,Cragthar,Gaernixis,Ilmarural,Malthar,Ilmarxel,Malithxel,Falzyth,Tarlxel,Cragisis,Cragxelor,Ardenthar,Glynnthar,Tarlxelor,Ilmarisis,Glynncarth,Falxel,Malxelor,Ardenxelor,Gaercarth,Malcarth,Cragcarth,Cragxel,Gaerthar,Faljor,Anorjor,Ardenural,Cragural,Malithisis,Cragzyth,Glynnxelor,Ardenzyth,Gaerxelor,Ardennixis,Anorzyth,Malithxelor,Ilmarnixis,Tarlthar,Gaerjor,Tarlzyth,Ardenxel,Falxelor,Malithjor,Ilmarthar,Tarlural,Anorthar

g > i,t,n,x,c,z,u,j
r > u,a,t,l,i,n,x,c,z,j,v
e > r,l,n
u > r
j > o
z > y
l > v,o,i,t,n,x,c,z,u,j
F > a
o > r
y > n,t
m > a
C > r
T > a
A > n,r
t > h
d > e
h > a,i,t,n,x,c,z,u,j
s > i
a > e,l,r,v,g
x > i,e
I > l
G > a,l
c > a
M > a
n > n,i,t,x,c,z,u,j,v
i > s,x,t"""

test_inp = """Xanverax,Khargyth,Nexzeth,Helther,Braerex,Tirgryph,Kharverax

r > v,e,a,g,y
a > e,v,x,r
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

def test_name(name, rules):
    for c1, c2 in zip(name, name[1:]):
        if c1 not in rules:
            return False
        if c2 not in rules[c1]:
            return False
    return True

def problem(inp):
    total = 0
    names, rules = parse_input(inp)
    for idx, name in enumerate(names, start=1):
        if test_name(name, rules):
            total += idx
    return total
    
    # Implement the logic to solve the problem using names and rules
    return 0

def main():
    print(f"Name sum (examples): {problem(test_inp)}")
    print(f"Name sum (actual): {problem(inp)}")
    
if __name__ == "__main__":
    main()