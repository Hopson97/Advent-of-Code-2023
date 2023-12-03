from typing import List, Tuple, Dict


def has_symbol(grid: List[str], grid_x: int, grid_y: int, specific=None):
    for y in range(-1, 2, 1):
        for x in range(-1, 2, 1):
            ny = grid_y + y
            nx = grid_x + x
            if ny < 0 or ny >= len(grid) or nx < 0 or nx >= len(grid[0]):
                continue

            compare = grid[ny][nx]
            if not specific and not compare.isalnum() and compare != ".":
                return True, nx, ny
            elif specific and compare == specific:
                return True, nx, ny
    return False, nx, ny


def part_one():
    grid = []
    with open("AOC2023/day3.txt") as file:
        for line in file:
            grid.append(line.strip("\n"))
    sums = 0
    for grid_y in range(0, len(grid)):
        current_num = ""
        symbol = False

        for grid_x in range(0, len(grid[0])):
            c: str = grid[grid_y][grid_x]

            if c.isdigit():
                current_num += c
                if not symbol:
                    symbol, _, _ = has_symbol(grid, grid_x, grid_y)

            if current_num.isdigit() and (
                grid_x == len(grid[0]) - 1 or not grid[grid_y][grid_x + 1].isdigit()
            ):
                sums += int(current_num) if symbol else 0
                current_num = ""
                symbol = False

    print(sums)


def part_two():
    grid = []
    with open("AOC2023/day3.txt") as file:
        for line in file:
            grid.append(line.strip("\n"))
    gears: Dict[Tuple[int, int], List[int]] = {}

    for grid_y in range(0, len(grid)):
        current_num = ""
        symbol = False

        for grid_x in range(0, len(grid[0])):
            c: str = grid[grid_y][grid_x]

            if c.isdigit():
                current_num += c
                if not symbol:
                    symbol, gear_x, gear_y = has_symbol(grid, grid_x, grid_y, "*")

            if current_num.isdigit() and (
                grid_x == len(grid[0]) - 1 or not grid[grid_y][grid_x + 1].isdigit()
            ):
                if symbol:
                    if not (gear_x, gear_y) in gears:
                        gears[(gear_x, gear_y)] = []
                    gears[(gear_x, gear_y)].append(int(current_num))
                current_num = ""
                symbol = False
    total = 0
    for pos, nums in gears.items():
        print(pos, nums)
        if len(nums) == 2:
            total += nums[0] * nums[1]
    print(total)


if __name__ == "__main__":
    part_one()
    part_two()
