names = "Nyfeth,Pylaronar,Voraxidris,Xarcalyx,Urakzral,Drazxal,Zarathidris,Drakaes,Cyndoth,Oronthyris,Drethroth,Kharsor,Torthel,Quorthar,Heldrith,Naldmyr,Shaemnar,Belath,Ascalcoryx,Thyrosadir"
instructions = "L8,R14,L12,R7,L9,R17,L8,R6,L18,R12,L5,R12,L5,R19,L5,R18,L5,R16,L5,R13,L6,R17,L8,R13,L19,R18,L16,R19,L10"

def follow_instruction(no_names, position, instruction):
    print(f"Processing instruction: {instruction}")
    if instruction.startswith("L"):
        position = (position - int(instruction[1:])) % no_names
    elif instruction.startswith("R"):
        position = (position + int(instruction[1:])) % no_names
    print(f"Current position: {position}")
    return position

def follow_instructions(names, instructions):
    # Placeholder for instruction processing logic
    print(f"Following instructions: {instructions} [{len(instructions.split(','))}]")
    print(f"Names: {names} [{len(names.split(','))}]")
    names = names.split(",")
    position = 0
    no_names = len(names)
    for instruction in instructions.split(","):
        position = follow_instruction(no_names, position, instruction)
    print(f"Final position: {position}")
    print(f"Name at final position: {names[position]}")

def main():
    follow_instructions(names, instructions)

if __name__ == "__main__":
    main()