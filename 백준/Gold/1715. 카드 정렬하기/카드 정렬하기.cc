#include <iostream>
#include <vector>
#include <algorithm>
#include<string>
#include <utility>
#include<queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	priority_queue <long long int, vector<long long int>, greater<long long int>> pq;
	long long int n,m,min1,min2;
	long long int total = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		pq.push(a);
	}
	while (pq.size()>=2){
		min1 = pq.top();
		pq.pop();
		min2 = pq.top();
		pq.pop();
		total += ( min1 + min2);
		pq.push(min1 + min2);
	}
	cout << total << "\n";

}