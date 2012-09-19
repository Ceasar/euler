/*
 * Find the 10001st prime.
 */
#include <iostream>
#include <math.h>

using namespace std;


/*
 * Built a list of numbers up to n.
 */
void range(long n, long nums[]) {
    for (long i = 0; i < n; i++) {
        nums[i] = i;
    }
}


/*
 * Build a list of primes up to n.
 * The list will contain 0s at all non primes indices.
 */
void primes(long n, long sieve[]) {
    long root;
    long index;
    range(n, sieve);
    sieve[1] = 0;
    if (n < 2) {
        return;
    }
    root = sqrt(n);
    index = 0;
    while (index <= root) {
        if (sieve[index] != 0) {
            long i = pow(index, 2);
            while (i < n) {
                sieve[i] = 0;
                i += index;
            }
        }
        index++;
    }
}

int main() {
    long target = 10001;
    long n = 110000;
    long nums[n];
    primes(n, nums);
    long count = 0;
    for (long i = 0; i < n; i++) {
        if (nums[i] != 0) {
            count++;
            if (count == target) {
                cout << nums[i] << endl;
            }
        }
    }
}
