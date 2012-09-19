/*
 * Find the 10001st prime.
 */
#include <iostream>
#include <math.h>

using namespace std;


/*
 * Built a list of numbers up to n.
 */
void range(unsigned long n, unsigned long nums[]) {
    for (unsigned long i = 0; i < n; i++) {
        nums[i] = i;
    }
}

/*
 * Repeat a value n times.
 */
void repeat(unsigned long n, bool val, bool nums[]) {
    for (unsigned long i = 0; i < n; i++) {
        nums[i] = val;
    }
}


/*
 * Build a boolean vector where a 1 at index n indicates n is prime.
 * The list will contain 0s at all non primes indices.
 */
void primes(unsigned long n, bool sieve[]) {
    unsigned long root;
    unsigned long i;
    repeat(n, true, sieve);
    sieve[0] = false;
    sieve[1] = false;
    if (n < 2) {
        return;
    }
    root = sqrt(n);
    i = 0;
    while (i <= root) {
        if (sieve[i]) {
            unsigned long j = pow(i, 2);
            while (j < n) {
                sieve[j] = false;
                j += i;
            }
        }
        i++;
    }
}

int main() {
    unsigned long n = 1000000;
    bool nums[n];
    primes(n, nums);
    unsigned long sum = 0;
    for (unsigned long i = 0; i < n; i++) {
        if (nums[i]) {
            sum += i;
        }
    }
    cout << sum << endl;
}
