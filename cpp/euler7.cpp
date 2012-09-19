/*
 * Find the 10001st prime.
 */
#include <iostream>
#include <math.h>

using namespace std;


/*
 * Built a list of numbers up to n.
 */
void range(int n, int nums[]) {
    for (int i = 0; i < n; i++) {
        nums[i] = i;
    }
}


/*
 * Build a list of primes up to n.
 * The list will contain 0s at all non primes indices.
 */
void primes(int n, int sieve[]) {
    int root;
    int index;
    range(n, sieve);
    sieve[1] = 0;
    if (n < 2) {
        return;
    }
    root = sqrt(n);
    index = 0;
    while (index <= root) {
        if (sieve[index] != 0) {
            int i = pow(index, 2);
            while (i < n) {
                sieve[i] = 0;
                i += index;
            }
        }
        index++;
    }
}

int main() {
    int target = 10001;
    int n = 110000;
    int nums[n];
    primes(n, nums);
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            count++;
            if (count == target) {
                cout << nums[i] << endl;
            }
        }
    }
}
