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
# adjusted_range_pairs = []
# for l, h in range_pairs:
#     dl = digit_count(l)
#     dh = digit_count(h)

#     adjusted_low = l
#     adjusted_high = h
    
#     if dl % 2 != 0:

#         if dh == dl:
#             # all digits odd. no solutions possible in range.
#             # print(f"evicted ({l},{h})")
#             continue
        
#         adjusted_low = 10 ** dl

#     if dh % 2 != 0:
#         assert dh != dl
#         adjusted_high = 10 ** (dh - 1)
        
#     adjusted_range_pairs.append((adjusted_low, adjusted_high))


def witness(digit_count: int) -> int:
    assert digit_count % 2 == 0

    trailing_zeroes = digit_count // 2
    mul = 1
    for _ in range (0, trailing_zeroes):
        mul *= 10

    return mul + 1

def general_witnesses(digit_count: int) -> list[int]:
    # figure out the max length of the repeat sequence
    max_repeat_seq_length = digit_count // 2

    res = [int("1" * digit_count)]

    if digit_count in [2, 3, 5, 7, 11, 13, 17, 23, 31]:
        return res

    dividend = int("2" * digit_count)
    for rsl in range(2, max_repeat_seq_length + 1):
        if digit_count % rsl != 0:
            continue

        divisor = int("2" * rsl)
        assert dividend % divisor == 0
        res.append(dividend // divisor)

    # res.append(witness(digit_count=digit_count))
    return res

invalid_ids = []
for l, h in range_pairs:

    for i in range(l, h + 1):
        dc = digit_count(i)

        if dc < 2:
            continue

        if any([i % w == 0 for w in general_witnesses(digit_count=dc)]):
            invalid_ids.append(i)

print(sum(invalid_ids))



# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.



# 11-22: [11, 22] (2)
# 95-115: [99, 111] (2)
# 998-1012: [999, 1010] (2)
# 1188511880-1188511890: [1188511885] (1)
# 222220-222224: [222222] (1)
# 1698522-1698528: [] (0)
# 446443-446449: [446446] (1)
# 38593856-38593862: [38593859] (1)
# 565653-565659: [565656] (1)
# 824824821-824824827: [] (0)
# 2121212118-2121212124: [2121212121] (1)




# print(sum(invalid_ids))





print(general_witnesses(1))
print(general_witnesses(2))
print(general_witnesses(3))
# print(general_witnesses(7))
# print(general_witnesses(8))
# print(general_witnesses(12))

# 12599655151

