#include <iostream>
#include <string>

using namespace std;

 int convert(int n) {
	string ns = "";

	int d = n;

	while (d > 0) {
		ns.append(to_string(d % 3));

		d /= 3;
	}

	ns = to_string(n % 3).append(ns);

	int r = 0;

	char* arr = &ns[0];

	for (int i = 0; i < ns.length(); i++) {
		r += (int(arr[i])-int('0')) * pow(3, i);
	}

	return r;
}

int main() {
	int r = 1000;

	for (int i = 0; i < 1000; i++) {
		int val = convert(i);
		if (val > 99 && val < 1000) {
			r = min(r, val);
		}
	}

	cout << r << endl;

	return 0;
}
