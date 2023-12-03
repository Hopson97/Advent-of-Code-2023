#include "AdventOfCode.h"

namespace AdventOfCode
{
    // = = = = = = = = = = = = = = = = = = = = = = = =
    //		S T R I N G    H E L P E R S
    // = = = = = = = = = = = = = = = = = = = = = = = =
    std::vector<std::string> split(const std::string& input, char delim = ' ')
    {
        std::vector<std::string> tokens;

        std::stringstream stream(input);
        std::string token;
        while (std::getline(stream, token, delim))
        {
            tokens.push_back(token);
        }
        return tokens;
    }

    std::string strip(const std::string& input, char remove)
    {
        auto copy = std::string(input);
        copy.erase(std::remove(copy.cbegin(), copy.cend(), remove), copy.cend());
        return copy;
    }

    bool contains(const std::string& input, const std::string& find)
    {
        return input.find(find) != std::string::npos;
    }

    std::string read_file_to_string(const std::filesystem::path& path)
    {
        std::ifstream in_file(path);
        std::string content((std::istreambuf_iterator<char>(in_file)),
                            (std::istreambuf_iterator<char>()));

        return content;
    }

    std::vector<std::string> read_file_as_lines(const std::filesystem::path& path)
    {
        std::ifstream inFile(path);
        std::vector<std::string> lines;
        std::string line;
        while (std::getline(inFile, line))
        {
            lines.push_back(line);
        };
        return lines;
    }
} // namespace AdventOfCode