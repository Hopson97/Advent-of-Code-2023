#pragma once

#include <SFML/System/Clock.hpp>
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

// Helper functions for all aoc
namespace AdventOfCode
{
    // = = = = = = = = = = = = = = = = = = = = = = = =
    //		S T R I N G    H E L P E R S
    // = = = = = = = = = = = = = = = = = = = = = = = =
    std::vector<std::string> split(const std::string& input, char delim = ' ');
    std::string strip(const std::string& input, char remove);
    bool contains(const std::string& input, const std::string& find);

    // = = = = = = = = = = = = = = = = = = = = = = = =
    //		F I L E    H E L P E R S
    // = = = = = = = = = = = = = = = = = = = = = = = =
    std::string read_file_to_string(const std::filesystem::path& path);
    std::vector<std::string> read_file_as_lines(const std::filesystem::path& path);

    // = = = = = = = = = = = = = = = = = = = = = = = =
    //		B E N C H M A R K I N G
    // = = = = = = = = = = = = = = = = = = = = = = = =

    template <typename F>
    void benchmark(const char* name, F function, int n)
    {
        std::vector<std::int64_t> times(n);

        double total = 0.0;

        for (auto& time : times)
        {
            auto begin_time = std::chrono::high_resolution_clock::now();
            function();
            auto end_time = std::chrono::high_resolution_clock::now();

            std::chrono::duration<double, std::micro> difference = end_time - begin_time;

            total += difference.count();
            time = difference.count();
        }

        auto average = total / n;

        auto minimum = (*std::min_element(times.cbegin(), times.cend()));
        auto maximum = (*std::max_element(times.cbegin(), times.cend()));

        std::cout << "Results for benchmark: " << name << '\n'
                  << "Times benchmarked: " << n << "\n\n"
                  << "  Total time: " << total << " microseconds\n"
                  << "Average time: " << average << " microseconds\n"
                  << "Minimum time: " << minimum << " microseconds\n"
                  << "Maximum time: " << maximum << " microseconds\n"
                  << "       Range: " << (maximum - minimum) << " microseconds" << std::endl;
    }

} // namespace AdventOfCode