#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int arr[1000];
	int n;
	cin >> n; 
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr+n); 
	for (int i = 0; i < n; i++) {
		cout << arr[i] << endl;
	}
}
