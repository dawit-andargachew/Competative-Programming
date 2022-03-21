#include <iostream>
#include <vector>
using namespace std;

void countSwaps(vector<int> a)
{
    int swapCounts = 0;
    int temp;
    for (int i = a.size() - 2; i >= 0; i--)
    {
        for (int j = 0; j <= i; j++)
        {
            if (a.at(j) > a.at(j + 1))
            {
                ++swapCounts;
                temp = a.at(j);
                a.at(j) = a.at(j + 1);
                a.at(j + 1) = temp;
            }
        }
    }

    cout << "Array is sorted in " << swapCounts << " swaps.\n";
    cout << "First Element: " << a.front() << '\n';
    cout << "Last Element: " << a.back();
}
