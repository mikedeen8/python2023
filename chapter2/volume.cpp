#include<iostream>
#include <cmath>
#include <chrono>

using namespace std::chrono;

using namespace std;


int main(void)
{
    auto start = high_resolution_clock::now();

    int r = 5;
    int V;

    V = 4 / 3 * M_PI * r;
    cout << "Volume: " << V << endl;

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << duration.count() << endl;


}