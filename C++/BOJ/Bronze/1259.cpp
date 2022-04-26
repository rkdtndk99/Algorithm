#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
	string s; 
	while (true) {
		cin >> s;
        if (s == "0") {
			break; 
		}
		string s1 = s;
		reverse(s.begin(), s.end());
		if (s1 == s) {
			cout << "yes" << endl;
			continue; 
		}
		else {
			cout << "no" << endl;
			continue;
		}
	}
}