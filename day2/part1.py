def digit_count(num: int) -> int:
    digits = 0
    while num != 0:
        num = num // 10
        digits += 1
    return digits


# nums = [1002, 100003, 502, 1234556]
# for num in nums:
#     print(digit_count(num=num))


with open("input.txt") as f:
    ranges = f.read().split(",")

range_pairs = []
for r in ranges:
    low, high = r.split('-')[0], r.split('-')[1]
    range_pairs.append((int(low), int(high)))


# range adjustments
# TBD: optimize to start on 1010 ...
adjusted_range_pairs = []
for l, h in range_pairs:
    dl = digit_count(l)
    dh = digit_count(h)

    adjusted_low = l
    adjusted_high = h
    
    if dl % 2 != 0:

        if dh == dl:
            # all digits odd. no solutions possible in range.
            # print(f"evicted ({l},{h})")
            continue
        
        adjusted_low = 10 ** dl

    if dh % 2 != 0:
        assert dh != dl
        adjusted_high = 10 ** (dh - 1)
        
    adjusted_range_pairs.append((adjusted_low, adjusted_high))


def witness(digit_count: int) -> int:
    assert digit_count % 2 == 0

    trailing_zeroes = digit_count // 2
    mul = 1
    for _ in range (0, trailing_zeroes):
        mul *= 10

    return mul + 1

invalid_ids = []
for l, h in adjusted_range_pairs:
    for i in range(l, h + 1):
        dc = digit_count(i)

        # TBD, optimize this away later
        if dc % 2 != 0:
            continue

        if i % witness(dc) == 0:
            invalid_ids.append(i)

print(sum(invalid_ids))

# 12599655151