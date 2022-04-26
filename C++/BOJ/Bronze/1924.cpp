#include<iostream>
#include<string>
using namespace std;

int main() {
	int month, day; 
	int index = 0;
	string d_list[7] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	cin >> month >> day;
	switch (month) {
	case 2:
		day += 31;
		break; 
	case 3:
		day += 31 + 28;
		break;
	case 4:
		day += 31*2 + 28;
		break;
	case 5:
		day += 31*2 + 30 + 28;
		break;
	case 6:
		day += 31*3 + 30 + 28;
		break;
	case 7:
		day += 31*3 + 30*2 + 28;
		break;
	case 8:
		day += 31*4 + 30*2 + 28;
		break;
	case 9:
		day += 31*5 + 30*2 + 28;
		break;
	case 10:
		day += 31*5 + 30*3 + 28;
		break;
	case 11:
		day += 31*6 + 30*3 + 28;
		break;
	case 12:
		day += 31*6 + 30*4 + 28;
		break;
	default:
		day = day;
		break; 
	}
	for (int i = 0; i < day; i++) {
		if (index == 6) {
			index = 0;
			continue;
		}
		index++;
	}
	cout << d_list[index];
}