#include <iostream>
using namespace std;

int main()
{
    double k = 1.0/10;
    double a1 = 100;
    double s = 0;

    double powk = 1;
    double n = 0;
    while (powk > 0)
    {
        //cout << a1 * pow(k, n-1) << endl;
        s += a1 * powk;
        powk *= k;
        n++;
    }

    cout << s << "\n" << n << endl;
}