/*
 * Get the least common multiple of [1..20]
 */
#include <iostream>
#include <math.h>

using namespace std;

/*
 * Get the greatest common divisor of a and b.
 */
int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

/*
 * Get the least common multiple of a and b.
 */
int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}


int main() {
    int target = 20;
    int answer = 1;
    for (int i = 1; i < target; i++) {
        answer = lcm(answer, i);
    }
    cout << answer << endl;
}
