#include <iostream>
#include <chrono>
#include <random>

using namespace std;

int main() {
  uniform_int_distribution<int> dist(0, 50);
  mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

  cout << dist(rng) << '\n';

  return 0;
}