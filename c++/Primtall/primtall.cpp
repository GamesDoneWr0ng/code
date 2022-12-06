/*
startTime = time()

def check():
    isPrime = True

    for k in primes[:n+1]:
        if i % k == 0:
            isPrime = False
            break

    return isPrime

primes = []
i = 5
n = 0
while i < 100000:
    if check():
        print(i)
        primes.append(i)

    i += 2

    if check():
        print(i)
        primes.append(i)

    i += 4

    if i > primes[n]**2:
        n += 1

print("--- %s seconds ---" % (time() - startTime))
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
using namespace chrono;

vector< int > primes;
int i = 5;
int n = 0;

bool check() {
    for (int k : primes) {
        if (k >= primes[n+1]) {
            return true;
        }
        
        if (i % k == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    auto start = high_resolution_clock::now();

    while (i < 10000000)
    {
        if (check()) {
            //cout << i << '\n';
            primes.push_back(i);
        }
        i += 2;

        if (check()) {
            //cout << i << '\n';
            primes.push_back(i);
        }
        i += 4;

        if (i > pow(primes[n], 2)) {
            n++;
        }
    }
    
    auto stop = high_resolution_clock::now();
    auto mics = duration_cast<microseconds>(stop - start);

    auto ms = duration_cast<milliseconds>(mics);
    mics -= duration_cast<microseconds>(ms);
    auto secs = duration_cast<seconds>(ms);
    ms -= duration_cast<milliseconds>(secs);

    cout << secs.count() << " Seconds : " << ms.count() << " Milliseconds : " << mics.count() << " Microseconds" << endl;
}