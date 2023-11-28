#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target =10;

    auto result =find(numbers.begin(), numbers.end(), target);
    if (result != numbers.end())
    {
        cout << "Element " << target << " found at position: " << distance(numbers.begin(), result) << endl;
    }
    else
    {
        cout << "Element " << target << " not found in the vector." << endl;
    }

    return 0;
}
