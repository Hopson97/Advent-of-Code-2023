import string
import re

if __name__ == "__main__":
    total = 0
    with open("AOC2023/day1.txt", "r") as f:
        for line in f:
            f = -1
            l = -1

            line = (
                line.replace("one", "one1one")
                .replace("two", "two2two")
                .replace("three", "three3three")
                .replace("four", "four4four")
                .replace("five", "five5five")
                .replace("six", "six6six")
                .replace("seven", "seven7seven")
                .replace("eight", "eight8eight")
                .replace("nine", "nine9nine")
            )
            line.replace("one1one", "1").replace("two2two", "2").replace(
                "three3three", "3"
            ).replace("four4four", "4").replace("five5five", "5").replace(
                "six6six", "6"
            ).replace(
                "seven7seven", "7"
            ).replace(
                "eight8eight", "8"
            ).replace(
                "nine9nine", "9"
            )

            for i in range(len(line)):
                if line[i] in string.digits:
                    if f == -1:
                        f = line[i]
                    else:
                        l = line[i]
            if l == -1:
                l = f
            print(line.strip("\n"), f" {f}{l}")
            total += int(f"{f}{l}")

    print(total)
