#include <stdio.h>

int main() {
  int sum = 0;
  int a = 1; int b = 1;
  int limit = 4000000;
  while (a < limit && b < limit) {
    if (a > b){
      b += a;
      if (b % 2 == 0)
        sum += b;
    }
    else {
      a += b;
      if (a % 2 == 0)
        sum += a;
    }
  }
  printf("%d\n", sum);
}
