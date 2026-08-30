with open('input.txt') as f:
    buf = f.read().splitlines()

grid: list[list[str]] = []
counts: list[list[int]] = []

for row in buf:
    grid.append(list(row))


def count_and_update_grid(grid: list[list[str]], counts: list[list[int]]) -> int:
    spots = 0
    for row in range(len(counts)):
        for col in range(len(counts[0])):
            if grid[row][col] == '@' and counts[row][col] < 4:
                grid[row][col] = 'x'
                spots += 1
    return spots

def remove_rolls(grid: list[list[str]])-> int:

    # init counts for this round
    counts: list[list[int]] = []
    for _ in grid:
        counts.append([0] * len(grid[0]))

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

    removed = count_and_update_grid(grid, counts)
    return removed


# def pg(grid):
#     for item in grid:
#         print(item)

# pg(grid)
# for _ in range(10):
#     removed = remove_rolls(grid)
#     print(removed)
#     pg(grid)

removed = 0
# while remove_rolls(grid) > 0:
#    removed = remove_rolls(grid)
#    print(removed)

total = 0
while True:
    removed = remove_rolls(grid)
    total += removed
    if removed == 0:
        break
print(total)
