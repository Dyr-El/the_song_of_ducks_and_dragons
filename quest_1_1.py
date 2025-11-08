names = "Ardenisis,Grimindor,Silirin,Quorthyn,Kalxeth,Xildar,Kharpyr,Hyracion,Thyrosdaros,Havoris"
instructions = "L9,R1,L5,R9,L1,R3,L2,R9,L9,R4,L6"

def follow_instruction(no_names, position, instruction):
    print(f"Processing instruction: {instruction}")
    if instruction.startswith("L"):
        position = max(0, position - int(instruction[1:]))
    elif instruction.startswith("R"):
        position = min(no_names - 1, position + int(instruction[1:]))
    print(f"Current position: {position}")
    return position

def follow_instructions(names, instructions):
    # Placeholder for instruction processing logic
    print(f"Following instructions: {instructions}")
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