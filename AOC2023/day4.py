from pprint import pprint


def part_one():
    n = 0
    with open("AOC2023/day4.txt") as file:
        for line in file:
            game, cards = line.strip("\n").split(":")

            winning_numbers, played_cards = cards.split("|")
            winning_numbers = winning_numbers.split()
            played_cards = played_cards.split()

            score = len(winning_numbers) - len(set(winning_numbers) - set(played_cards))

            n += (2 ** (score - 1)) if score > 0 else 0
    print(n)


def part_two():
    scratch_cards = 0

    copies = {}

    with open("AOC2023/day4.txt") as file:
        for line in file:
            game, cards = line.strip("\n").split(":")
            game_n = int(game.split()[1])

            if game_n not in copies:
                copies[game_n] = 1

            winning_numbers, played_cards = cards.split("|")
            winning_numbers = winning_numbers.split()

            played_cards = played_cards.split()
            score = len(winning_numbers) - len(set(winning_numbers) - set(played_cards))

            for n in range(score):
                copy = n + game_n + 1
                if copy not in copies:
                    copies[copy] = 1
                copies[copy] += copies.get(game_n, 1)

    total = 0
    for copy, count in copies.items():
        total += count

    print(total)


if __name__ == "__main__":
    part_one()
    part_two()
