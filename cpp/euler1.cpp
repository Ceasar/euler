/*
 * Add all the natural numbers below 1000 that are multiples of 3 or 5.
 */
#include <iostream>

using namespace std;


int main() {
    int sum = 0;
    int i = 0;
    for (i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
        }
    }
    cout << sum << endl;
}
