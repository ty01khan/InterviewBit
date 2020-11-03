#include <iostream>
using namespace std;

bool isGreater(int x, int y) {
	if(x >= y) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	int x, y, cnt = 1;
	cout << "Let's be ready for BINARY SEARCH\n";
	cout << "Please enter a number in [0, 10] : ";
	cin >> y;
	cout << "Please enter a number to guess : ";
	while(true) {
		cin >> x;
		
		if(isGreater(x,y)) {
			if(x == y) {
				cout << "Hurray, You have guessed correct number in " << cnt << " step\n";
				break;
			}
			else {
				cout << "Oops, Not matched!. \nGuess some small number than earlier : ";
				cnt++;
			}
		}
		else {
			cout << "Oops, Not matched!. \nGuess some bigger number than earlier : ";
			cnt++;
		}
	}
	
	return 0;
}
