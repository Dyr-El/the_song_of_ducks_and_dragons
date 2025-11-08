names = "Zraalxar,Jorathhynd,Draithzion,Zarathkael,Maralnoris,Lorzal,Mavnyn,Quortyr,Skarurath,Quororath,Belhynd,Yndendris,Rylarjoris,Norakeldrith,Adalxaril,Drelox,Mavgnar,Elarnor,Ulkaxar,Vornsar,Brythlyr,Caloth,Morgyth,Rythtaril,Morkris,Quarnindor,Urithiral,Xendfeth,Naldthel,Brynsor"
instructions = "L42,R16,L26,R20,L15,R47,L32,R42,L32,R31,L43,R16,L16,R42,L20,R23,L30,R43,L36,R41,L5,R5,L5,R37,L5,R27,L5,R30,L5,R31,L5,R40,L5,R42,L5,R7,L5,R43,L5,R32,L10,R28,L22,R23,L28,R39,L18,R22,L46,R13,L24,R16,L25,R45,L6,R5,L42,R15,L35"
# names = "Vyrdax,Drakzyph,Fyrryn,Elarzris"
# instructions = "R3,L2,R3,L3"

def follow_instruction(names, instruction):
    print(f"Processing instruction: {instruction}")
    if instruction.startswith("L"):
        swap_pos = -int(instruction[1:]) % len(names)
    elif instruction.startswith("R"):
        swap_pos = int(instruction[1:]) % len(names)
    print(f"Swapping {names[0]} with {names[swap_pos]}")
    names[0], names[swap_pos] = names[swap_pos], names[0]
    print(names)

def follow_instructions(names, instructions):
    # Placeholder for instruction processing logic
    print(f"Following instructions: {instructions} [{len(instructions.split(','))}]")
    print(f"Names: {names} [{len(names.split(','))}]")
    names = names.split(",")
    no_names = len(names)
    for instruction in instructions.split(","):
        follow_instruction(names, instruction)
    print(f"Name at top: {names[0]}")

def main():
    follow_instructions(names, instructions)

if __name__ == "__main__":
    main()