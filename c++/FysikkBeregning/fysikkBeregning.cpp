/*a = 2.0
v = 0.0
s = 0.0
t = 0.0

dt = 1E-5
t_slutt = 5

while round(t, 8) < t_slutt:
    v += a * dt
    s += v * dt
    t += dt

print(f"t = {t:.5} s = {s:.5} v = {v:.5}")*/

#include <iostream>
using namespace std;

int main()
{
    double a = 2.0;
    double v = 0.0;
    double s = 0;
    double t = 0;

    double dt = 1E-8;
    double t_slutt = 3.0;

    while (t < t_slutt)
    {
        v += a * dt;
        s += v * dt;
        t += dt;
    }

    cout << "t = " << t << " s = " << s << " v = " << v << endl;
}