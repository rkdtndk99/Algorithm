#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int n, k; 
	int res = 1;
	int result=0; 
	int bottom = 1; 
	cin >> n >> k; 
	for (int i = 0; i < k; i++) {
		res *= n; 
		bottom *= (i+1); 
		n--; 
	}
	result = res / bottom;
	cout << result; 
}