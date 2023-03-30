#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool desc(int a, int b) {
	return a > b;
}

int main() {
	int n, k;
	cin >> n >> k;
	int score[1000];
	for (int i = 0; i < n; i++) {
		int s;
		cin >> s;
		score[i] = s;
	}
	sort(score, score+n,desc);
	cout << score[k-1];

}