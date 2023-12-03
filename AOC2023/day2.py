from typing import Dict


def part_one():
    with open("AOC2023/day2.txt") as file:
        total = 0
        for line in file:
            game_id, games = line.split(":")

            counts = games.replace("\n", "").replace(",", "")
            minimums = {"red": 0, "blue": 0, "green": 0}

            for s in counts.split(";"):
                rgb = {"red": 0, "blue": 0, "green": 0}
                game = s[1:].split(" ")
                for i in range(0, len(game), 2):
                    print(game[i], game[i + 1])
                    count, colour = game[i], game[i + 1]
                    rgb[colour] += int(count)

                minimums["red"] = max(minimums["red"], rgb["red"])
                minimums["blue"] = max(minimums["blue"], rgb["blue"])
                minimums["green"] = max(minimums["green"], rgb["green"])

                if rgb["red"] > 12 or rgb["green"] > 13 or rgb["blue"] > 14:
                    break
            else:
                total += int(game_id.split(" ")[1])
        print(total)


def part_two():
    with open("AOC2023/day2.txt") as file:
        total = 0
        for line in file:
            _, games = line.split(":")

            counts = games.replace("\n", "").replace(",", "")
            minimums = {"red": 0, "blue": 0, "green": 0}

            for s in counts.split(";"):
                rgb = {"red": 0, "blue": 0, "green": 0}
                game = s[1:].split(" ")
                for i in range(0, len(game), 2):
                    count, colour = game[i], game[i + 1]
                    rgb[colour] += int(count)

                minimums["red"] = max(minimums["red"], rgb["red"])
                minimums["blue"] = max(minimums["blue"], rgb["blue"])
                minimums["green"] = max(minimums["green"], rgb["green"])

            print(minimums)

            total += (
                max(1, minimums["red"])
                * max(1, minimums["blue"])
                * max(1, minimums["green"])
            )

        print(total)


if __name__ == "__main__":
    part_one()
    part_two()
