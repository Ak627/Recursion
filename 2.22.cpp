#include<iostream>
using namespace std;


void hah(int x);


int main() {
	hah(13);
}

void hah(int x) {
	cout << x << " ";
	if (x < 80) {
		hah(x += 5);
	}
	else if (x > 80) {
		hah(x -= 1);
	}
	else
		cout << x << endl;
}
