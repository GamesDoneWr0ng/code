#include <iostream>
using namespace std;
using namespace chrono;

int main()
{
    auto start = high_resolution_clock::now();

    int i = 0;
    while (i < 1000000000) {
        //cout << i << endl;
        i++;
    }
    
    auto stop = high_resolution_clock::now();
    auto mics = duration_cast<microseconds>(stop - start);

    auto ms = duration_cast<milliseconds>(mics);
    mics -= duration_cast<microseconds>(ms);
    auto secs = duration_cast<seconds>(ms);
    ms -= duration_cast<milliseconds>(secs);

    cout << secs.count() << " Seconds : " << ms.count() << " Milliseconds : " << mics.count() << " Microseconds" << endl;
}
// 272.8