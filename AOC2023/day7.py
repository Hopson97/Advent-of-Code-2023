from typing import Dict, TypeVar, List
from collections import namedtuple
from pprint import pprint


PRECS = {
    "A": "M",
    "K": "L",
    "Q": "K",
    "J": "J",
    "T": "I",
    "9": "H",
    "8": "G",
    "7": "F",
    "6": "E",
    "5": "D",
    "4": "C",
    "3": "B",
    "2": "A",
}

PRECS2 = {
    "A": "M",
    "K": "L",
    "Q": "K",
    "T": "J",
    "9": "I",
    "8": "H",
    "7": "G",
    "6": "F",
    "5": "E",
    "4": "D",
    "3": "C",
    "2": "B",
    "J": "A",
}


def five_of_a_kind(counts: List[int]):
    return len(counts) == 1


def four_of_a_kind(counts: List[int]):
    return len(counts) == 2 and counts[1] == 1


def full_house(counts: List[int]):
    return len(counts) == 2 and counts[0] == 3


def three_of_a_kind(counts: List[int]):
    return len(counts) == 3 and counts[0] == 3


def two_pair(counts: List[int]):
    return len(counts) == 3 and counts[0] == 2 and counts[1] == 2


def one_pair(counts: List[int]):
    return len(counts) == 4 and counts[0] == 2


def high_card(counts: List[int]):
    return len(counts) == 5


SCORE_CHECKS = [
    (five_of_a_kind, 7),
    (four_of_a_kind, 6),
    (full_house, 5),
    (three_of_a_kind, 4),
    (two_pair, 3),
    (one_pair, 2),
    (high_card, 1),
]


def calculate_cards_type(cards: str, p2: bool):
    card_counts: Dict[str | int, int] = {}
    for card in cards:
        if not card in card_counts:
            card_counts[card] = 0
        card_counts[card] += 1

    counts = [x for _, x in card_counts.items()]
    counts.sort()
    counts.reverse()

    if p2:
        c = 0
        if "J" in card_counts:
            c = card_counts["J"]
            card_counts.pop("J")

        print(card_counts, c)

    kind = 0
    for check, score in SCORE_CHECKS:
        if check(counts):
            kind = score
            break
    return kind


Suite = namedtuple("Suite", "cards, kind, bet, precedence")


def part_one():
    suites: List[Suite] = []
    with open("AOC2023/day7.txt") as file:
        for line in file:
            cards, bet = line.split()

            kind = calculate_cards_type(cards, False)
            precedence = "".join([PRECS[x] for x in cards])
            suites.append(Suite(cards, kind, bet, precedence))

    suites = sorted(suites, key=lambda x: x.kind)
    kinds: Dict[int, List[Suite]] = {}

    for suite in suites:
        if suite.kind not in kinds:
            kinds[suite.kind] = []
        kinds[suite.kind].append(suite)

    ranked_suites: List[Suite] = []
    for _, suites_list in kinds.items():
        suites_list = sorted(suites_list, key=lambda x: x.precedence)
        ranked_suites += suites_list
    total_winnings = 0
    for rank, suite in enumerate(ranked_suites):
        total_winnings += (rank + 1) * int(suite.bet)
    print(total_winnings)


def part_two():
    suites: List[Suite] = []
    with open("AOC2023/day7.txt") as file:
        for line in file:
            cards, bet = line.split()

            kind = calculate_cards_type(cards, True)
            precedence = "".join([PRECS[x] for x in cards])
            suites.append(Suite(cards, kind, bet, precedence))

    suites = sorted(suites, key=lambda x: x.kind)
    kinds: Dict[int, List[Suite]] = {}
    for suite in suites:
        if suite.kind not in kinds:
            kinds[suite.kind] = []
        kinds[suite.kind].append(suite)

    ranked_suites: List[Suite] = []
    for _, suites_list in kinds.items():
        suites_list = sorted(suites_list, key=lambda x: x.precedence)
        ranked_suites += suites_list
    total_winnings = 0
    for rank, suite in enumerate(ranked_suites):
        total_winnings += (rank + 1) * int(suite.bet)
    print(total_winnings)


if __name__ == "__main__":
    part_one()
    part_two()
