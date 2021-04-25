/*
 *  x = 2 mod 3,
 *  x = 3 mod 5,
 *  x = 5 mod 7,
 *
 * The smallest number for x is 68.
 * Input
 *      n
 *      r1 d1
 *      r2 d2
 *      ...
 *      rn dn
 * The example above will be
 *      3
 *      2 3
 *      3 5
 *      5 7
 */
#include <iostream>
#include <vector>

using namespace std;

// for example, 7t + 6 = 4 mod 5, -> t = 5j + 4, return 4
int getCoef(int k, int b, int r, int d) {
  for (int j = 0; j < d; ++j) {
    if ((k * j + b) % d == r) {
      return j;
    }
  }
  return -1;  // error
}

// run: cat crt_data1.txt | ./Chinese_Remainder_Theorem
int main() {
  ios::sync_with_stdio(false);
  int n;
  cin >> n;
  vector<int> R(n, 0), D(n, 0);  // remainders and divisors
  for (int i = 0; i < n; ++i) {
    cin >> R[i] >> D[i];
  }

  int k = D[n - 1], b = R[n - 1];
  for (int i = n - 2; i >= 0; --i) {
    b = b + k * getCoef(k, b, R[i], D[i]);
    k = k * D[i];
  }

  cout << b << '\n';
  return 0;
}
