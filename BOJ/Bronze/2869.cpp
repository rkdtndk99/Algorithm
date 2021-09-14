#include<iostream>
#include<cmath>
using namespace std;

int main() {
	double a, b, v;
	int day = 0;
	cin >> a >> b >> v;
	day = ceil((v - b) / (a - b));
	cout << day ; 
}
