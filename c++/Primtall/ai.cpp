#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
using namespace chrono;

// Function to find prime numbers using the Sieve of Eratosthenes
vector<int> sieveOfEratosthenes(int n)
{
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    vector<bool> prime(n + 1, true);

    // Initialize the prime numbers vector
    vector<int> primes;

    // Perform the sieve operation
    for (int p = 2; p * p <= n; p++)
    {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true)
        {
            // Update all multiples of p
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }

    // Add all prime numbers to the vector
    for (int p = 2; p <= n; p++)
        if (prime[p])
            primes.push_back(p);

    // Return the vector of prime numbers
    return primes;
}

// Main function
int main()
{
    auto start = high_resolution_clock::now();

    // Upper bound for the range of numbers to be checked for primality
    int n = 1000000000;

    // Find the prime numbers in the specified range
    vector<int> primes = sieveOfEratosthenes(n);
/*
    // Print the prime numbers
    cout << "The prime numbers in the range 1 to " << n << " are:" << endl;
    for (int p : primes)
        cout << p << " ";
    cout << endl;
*/

    auto stop = high_resolution_clock::now();
    auto mics = duration_cast<microseconds>(stop - start);

    auto ms = duration_cast<milliseconds>(mics);
    mics -= duration_cast<microseconds>(ms);
    auto secs = duration_cast<seconds>(ms);
    ms -= duration_cast<milliseconds>(secs);

    cout << secs.count() << " Seconds : " << ms.count() << " Milliseconds : " << mics.count() << " Microseconds" << endl;

    return 0;
}
