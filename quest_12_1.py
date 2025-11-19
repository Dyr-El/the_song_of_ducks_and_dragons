inp = """98088471036466134229
99036844442712037499
39900880156762003997
65993377726033619976
28199018272553899555
67149988110758990282
48158992128019950542
28466699426799310151
12436649978998213226
28702864999901104253
87266844699884741110
60623706999971750110
17748139943998676030
05321899553699733444
20150990234319931768
67279963707367995240
36199833174542799310
58994835111722479910
39901210668305836994
99860536100008435599"""

test_inp = """989601
857782
746543
766789"""


from collections import deque


def parse_barrels(inp):
    result = {}
    for lidx, line in enumerate(inp.splitlines()):
        for cidx, c in enumerate(line):
            result[(lidx, cidx)] = int(c)
    return result


def ignite_barrel(barrels, position):
    ignited = {position}
    queue = deque([position])
    while queue:
        pos = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            npos = (pos[0] + dx, pos[1] + dy)
            if npos in barrels and npos not in ignited:
                if barrels[npos] <= barrels[pos]:
                    ignited.add(npos)
                    print(f"Igniting barrel at {npos} with height {barrels[npos]} from {pos} with height {barrels[pos]}")
                    queue.append(npos)
    return len(ignited)

def main():
    print(f"Barrels destroyed (example): {ignite_barrel(parse_barrels(test_inp), (0, 0))}")
    print(f"Barrels destroyed (actual): {ignite_barrel(parse_barrels(inp), (0, 0))}")
    
if __name__ == "__main__":
    main()