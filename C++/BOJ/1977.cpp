#include<iostream>
#include<string>
using namespace std;

int main() {
	int n, m;
	int min = 10000;
	int sum=0; 
	cin >> m >> n; 
	for (int i = 0; i <= 100;i++) {
		for (int k = m; k <= n; k++) {
			if (k == i * i) {
				sum += k;
				if (k < min) {
					min = k; 
				}
			}
			
		}
	}
	if (sum == 0) {
		cout << -1;
	}
	else{
		cout << sum << endl << min;
	}
}