#include<iostream>
using namespace std;

int main() {
	int N;
	int num_5=0, num_3=0;
	cin >> N; 
	for (int i = 0; i < N;i++) {
		for (int j = 0; j < 5;j++) {
			if (N == (i * 5) + (j * 3)) {
				num_5 = i;
				num_3 = j;
				break;
			}
		}
	}
	if (num_5 == 0 && num_3 == 0) {
		cout << -1;
	}
	else {
		cout << num_5 + num_3;
	}
}