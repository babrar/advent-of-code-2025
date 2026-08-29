with open("input.txt") as f:
    batteries = [n for n in f.read().splitlines()]

res: list[int] = []

for bank in batteries:
    first_digit: int = -1
    first_digit_index: int = -1
    for i, digit in enumerate(bank):
        # keep at least one digit available for 2nd pass later
        if i == len(bank) - 1:
            break

        if int(digit) > first_digit:
            first_digit = int(digit)
            first_digit_index = i

    second_digit: int = -1
    for i in range(first_digit_index + 1, len(bank)):
        second_digit = max(second_digit, int(bank[i]))

    res.append(int(f"{first_digit}{second_digit}"))

print(sum(res))
