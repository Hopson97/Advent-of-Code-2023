#include "AOC2023/AOC2023.h"

template <int N = 128, typename F>
void benchmark(int year, int day, F partOne, F partTwo, int count)
{
    std::cout << "\n\n= = = = = = = = = = = = = = = = = = = = =\n";
    std::cout << "Benchmarking " << year << " day " << day << '\n';
    std::cout << "= = = = = = = = = = = = = = = = = = = = =\n";

    std::cout << "\n- - - - - - - - - - - -\n";
    std::cout << "Running part 1" << std::endl;
    std::cout << "- - - - - - - - - - - -\n";

    AdventOfCode::benchmark(
        "Part 1", [&partOne]() { partOne(); }, count);

    std::cout << "\n- - - - - - - - - - - -\n";
    std::cout << "Running part 2" << std::endl;
    std::cout << "- - - - - - - - - - - -\n";
    AdventOfCode::benchmark(
        "Part 2", [&partTwo]() { partTwo(); }, count);

    std::cout << "\n- - - - - - - - - - - -\n";
    std::cout << "Running part 1 and part 2" << std::endl;
    std::cout << "- - - - - - - - - - - -\n";
    AdventOfCode::benchmark(
        "Part 1 + Part 2",
        [&partOne, &partTwo]
        {
            partOne();
            partTwo();
        },
        count);
    std::cout << "\n\n";
}

int main()
{
    benchmark(2023, 1, AOC2023::day_1_part_1, AOC2023::day_1_part_2, 100);
}