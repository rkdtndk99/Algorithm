#include<iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 10000; i++) {
        for (int j = 0; j < i; j++) {
            sum = j;
            for (int k = 1; k < i;k*=10) {
                sum += (j / k) % 10;
            }
            if (i == sum) {   //생성자 존재
                break;
            }
            else if (j == i-1) {
                cout << i << endl;
                break;
            }
        }
    }
}

