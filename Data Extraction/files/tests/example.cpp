#include <iostream>
#include <algorithm>

std::string example_function(std::string &input)
{
    std::reverse(input.begin(), input.end());
    return input;
}

int main()
{
    std::string x = "Hello World";
    std::cout << example_function(x) << std::endl;
    return 0;
}