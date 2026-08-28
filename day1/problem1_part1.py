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

# print(numerical_moves)

# def mod_add(op1: int, op2: int, mod: int) -> int:
#     res = op1 + op2
#     if res > 0:
#         return res % mod

#     else:
#         while res < 0:
#             res += mod
#         return res

current_pos = 50
zeroes = 0
# keep track of when it hits zero
for num in numerical_moves:
    # lands_at = mod_add(current_pos, num, 100)
    lands_at = (current_pos + num) % MODULO

    if lands_at == 0:
        zeroes += 1
    current_pos = lands_at

    # print (f"{num}, {current_pos}")
print(zeroes)
