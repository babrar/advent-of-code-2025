with open('input.txt') as f:
    buf = f.read().splitlines()

grid: list[list[str]] = []
counts: list[list[int]] = []

for row in buf:
    grid.append(list(row))
    counts.append([0] * len(row))


# count rows above
for row in range(1, len(grid)):
    for col in range(0, len(grid[0])):

        assert row > 0

        start = col - 1 if col > 0 else 0
        end = col + 2 if col < len(grid[0]) - 1 else col + 1

        count = 0
        for c in range(start, end):
            if grid[row - 1][c] == '@':
                count += 1

        counts[row][col] += count

# count the middle row
for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):

        start = col - 1 if col > 0 else 0
        end = col + 2 if col < len(grid[0]) - 1 else col + 1

        count = 0
        for c in range(start, end):
            # ignore current item
            if c == col:
                continue

            if grid[row][c] == '@':
                count += 1

        counts[row][col] += count

# count the bottom row
for row in range(0, len(grid) - 1):
    for col in range(0, len(grid[0])):

        assert row < len(grid[0]) - 1

        start = col - 1 if col > 0 else 0
        end = col + 2 if col < (len(grid[0]) - 1) else col + 1

        count = 0
        for c in range(start, end):
            if grid[row + 1][c] == '@':
                count += 1

        counts[row][col] += count

spots = 0
for item in grid:
    print(item)
for item in counts:
    print(item)
for row in range(len(counts)):
    for col in range(len(counts[0])):
        if grid[row][col] == '@' and counts[row][col] < 4:
            spots += 1
print(spots)

# def adjacent_roll_count(row: int, col: int, grid: list[list[str]] ) -> int:

#     def rolls_in_row_above(row: int, col: int) -> int:
#         count = 0
#         for c in range(col - 1, col + 2):
#             if grid[row - 1][c] == '@'
#                 count += 1
#         return count

#     def rolls_in_middle_row(row: int, col: int) -> int:
#         count = 0
#         for c in range(col - 1, col + 2):
#             # ignore current item
#             if c == col:
#                 continue

#             if grid[row][c] == '@':
#                 count += 1
#         return count

#     def rolls_in_row_below(row: int, col: int) -> int:
#         count = 0
#         for c in range(col - 1, col + 2):
#             if grid[row + 1][c] == '@'
#                 count += 1

#         return count


#     # General case
#     # check the row above
#     count = 0


#     # check the middle row


#     # check last row
