#include<iostream>
using namespace std;

int main() {
	int n; 
	double max = 0;
	double avg = 0, sum = 0;
	cin >> n; 
	double score[1000];
	for (int i = 0; i < n; i++) {
		cin >> score[i]; 
		if (score[i] > max) max = score[i];
	}
	for (int j = 0; j < n; j++) {
		score[j] = score[j] / max * 100;
		sum += score[j];
	}
	avg = sum / n;
	cout << avg; 
}