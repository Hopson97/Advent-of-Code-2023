from math import prod


def part_one():
    with open("AOC2023/day6.txt") as file:
        for line in file:
            if line.startswith("T"):
                times = [int(x) for x in line.split()[1:]]
            else:
                distances = [int(x) for x in line.split()[1:]]
            pass

    counts = []
    for race_time, max_dist in zip(times, distances):
        count = 0
        for speed in range(race_time + 1):
            dist = speed * (race_time - speed)
            if dist > max_dist:
                count += 1
        counts.append(count)
    print(prod(counts))  # counts


"""

let d = 9
let t = 7


"""


def part_two():
    with open("AOC2023/day6.txt") as file:
        for line in file:
            if line.startswith("T"):
                times = line.split()[1:]
            else:
                distances = line.split()[1:]
            pass

    time = int("".join(times))
    distance = int("".join(distances))
    print(time, distance)

    count = 0
    for speed in range(time + 1):
        dist = speed * (time - speed)
        if dist > distance:
            count += 1
    print(count)


if __name__ == "__main__":
    part_one()
    part_two()
