#include <iostream>
using namespace std;
using namespace chrono;

int main()
{
    int a = 2;
    for (int i = 0; i < 2; i++)
    {
        a = 3;
    }

    cout << a;
}