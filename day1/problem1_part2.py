MODULO = 100
# buf: list = []
with open("input.txt") as f:
    moves = f.read().splitlines()

numerical_moves = []
for move in moves:

    assert move.startswith("R") or move.startswith("L")

    if move.startswith("R"):
        numerical_moves.append(int(move.removeprefix("R")))
    else:
        numerical_moves.append(int(move.removeprefix("L")) * - 1)

current_pos = 50
zeroes = 0

for num in numerical_moves:
    # print(f"current pos: {current_pos}")
    # print(f"zeroes: {zeroes}")
    
    res = current_pos + num
    
    # R case
    if res >= MODULO:
        while res >= MODULO:   
            res -= MODULO
            zeroes += 1
    
    # L case
    elif res <= 0:
        if current_pos == 0:
            res += MODULO
        while res <= 0:
            res += MODULO
            zeroes += 1
    
    # General case
    else:
        pass
    
    current_pos = (current_pos + num) % MODULO
    # print("")

print(f"zeroes: {zeroes}")


# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82; during this rotation, it points at 0 once. (1)
# The dial is rotated L30 to point at 52. (1)
# The dial is rotated R48 to point at 0. (2)
# The dial is rotated L5 to point at 95. (2)
# The dial is rotated R60 to point at 55; during this rotation, it points at 0 once. (3)
# The dial is rotated L55 to point at 0. (4)
# The dial is rotated L1 to point at 99. (4)
# The dial is rotated L99 to point at 0. (5)
# The dial is rotated R14 to point at 14.(5)
# The dial is rotated L82 to point at 32; during this rotation, it points at 0 once. (6)
