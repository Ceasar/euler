#include <stdio.h>
#include <math.h>

int main() {
  int greatest_prime_factor = 0;
  double target = 600851475143;
  double divisor = 2;
  while (divisor < target){
    if (fmod(target, divisor) == 0){
      target /= divisor;
      if (divisor > greatest_prime_factor)
        greatest_prime_factor = divisor;
      divisor = 2;
    }
    divisor++;
  }
  if (target > greatest_prime_factor)
    greatest_prime_factor = target;
  printf("%d\n", greatest_prime_factor);
}
