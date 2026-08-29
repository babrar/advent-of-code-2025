SIZE = 12

with open("input.txt") as f:
    batteries = [n for n in f.read().splitlines()]

# print(f"batteries: {batteries}")

res: list[int] = []
for bank in batteries:
    # print(f"bank: {bank}")
    max_idx: list[int] = [-1] * SIZE
    max_nums: list[str] = [""] * SIZE

    # dynamic programming (1D?)
    for i in range(len(max_idx)):
        prev_idx = max_idx[i - 1] + 1 if i > 0 else 0
        current_max_idx = prev_idx
        for j in range(prev_idx, len(bank) - (SIZE - i - 1)):
            if bank[current_max_idx] < bank[j]:
                current_max_idx = j
        max_idx[i] = current_max_idx
        max_nums[i] = bank[current_max_idx]

    res.append(int("".join(max_nums)))

print(res)
print(sum(res))
