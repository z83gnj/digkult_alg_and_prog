// reklam.cpp

#include <locale>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

typedef struct {
	unsigned short nap;
	string varos;
	unsigned short darab;
} rendeles;

vector <rendeles> rendelesek;

void fel1() {
	cout << "1. feladat:" << endl;
	ifstream rendfile("rendel.txt");
	while (not rendfile.eof()) {
		rendeles egyrend;
		rendfile >> egyrend.nap >> egyrend.varos >> egyrend.darab >> ws;
		rendelesek.push_back(egyrend);
	}
	rendfile.close();
}

void fel2() {
	cout << "2. feladat:" << endl;
	cout << "A rendelések száma: " << rendelesek.size() << endl;
}

void fel3() {
	cout << "3. feladat:" << endl;
	unsigned short nap;
	cout << "Kérem adjon meg egy napot: ";
	cin >> nap;
	unsigned short rendszam = 0;
	unsigned short ri = 0;
	while (ri < rendelesek.size() and rendelesek[ri].nap <= nap) {
		if (rendelesek[ri].nap == nap)
			++rendszam;
		++ri;
	}
	cout << "A rendelések száma az adott napon: " << rendszam << endl;
}

void fel4() {
	cout << "4. feladat:" << endl;
	unsigned short nap = 1, nemvolt = 0;

	for (unsigned short ri = 0; ri < rendelesek.size(); ++ri) {
		if (rendelesek[ri].varos == "NR" and rendelesek[ri].nap != nap) {
			nemvolt += rendelesek[ri].nap - nap - 1;
			nap = rendelesek[ri].nap;
		}
	}
	nemvolt += 30 - nap;

	if (nemvolt > 0)
		cout << nemvolt << " nap nem volt a reklámban nem érintett városból rendelés" << endl;
	else 
		cout << "Minden nap volt rendelés a reklámban nem érintett városból" << endl;
}

void fel5() {
	cout << "5. feladat:" << endl;
	unsigned short maxrend = rendelesek[0].darab, maxnap = rendelesek[0].nap;

	for (unsigned short ri = 1; ri < rendelesek.size(); ++ri)
		if (rendelesek[ri].darab > maxrend) {
			maxrend = rendelesek[ri].darab;
			maxnap = rendelesek[ri].nap;
		}
	cout << "A legnagyobb darabszám: " << maxrend << ", a rendelés napja: " << maxnap << endl;
}

unsigned short osszes(string varos, unsigned short nap) {
	unsigned short ossz = 0;
	for (unsigned short ri = 0; ri < rendelesek.size(); ++ri)
		if (rendelesek[ri].varos == varos and rendelesek[ri].nap == nap)
			ossz += rendelesek[ri].darab;
	return ossz;
}

void fel7() {
	cout << "7. feladat:" << endl;
	unsigned short plossz = osszes("PL", 21);
	unsigned short tvossz = osszes("TV", 21);
	unsigned short nrossz = osszes("NR", 21);

	cout << "A rendelt termékek darabszáma a 21. napon PL: " << plossz << " TV: " << tvossz << " NR: " << nrossz << endl;
}

void fel8() {
	cout << "8. feladat:" << endl;
	string varosok[3] = { "PL","TV","NR" };
	unsigned short ossztiz[3][3] = {0,0,0, 0,0,0, 0,0,0};
	for (unsigned short ri = 0; ri < rendelesek.size(); ++ri) {
		unsigned short naptiz = (rendelesek[ri].nap-1)/10;
		unsigned short vartiz = 0;
		while (varosok[vartiz] != rendelesek[ri].varos)
			++vartiz;
		++ossztiz[vartiz][naptiz];
	}
	cout << "Napok\t1..10\t11..20\t21..30" << endl;
	for (unsigned short vartiz = 0; vartiz<3; ++vartiz) {
		cout << varosok[vartiz];
		for(unsigned short naptiz = 0; naptiz<3; ++naptiz) {
			cout << '\t' << ossztiz[vartiz][naptiz];
		}
		cout << endl;
	}
	ofstream kampfile("kampany.txt");
	kampfile << "Napok\t1..10\t11..20\t21..30" << endl;
	for (unsigned short vartiz = 0; vartiz < 3; ++vartiz) {
		kampfile << varosok[vartiz];
		for (unsigned short naptiz = 0; naptiz < 3; ++naptiz) {
			kampfile << '\t' << ossztiz[vartiz][naptiz];
		}
		kampfile << endl;
	}
	kampfile.close();
}

int main() {
	setlocale(LC_ALL,"hu_HU");
	fel1();
	fel2();
	fel3();
	fel4();
	fel5();
	fel7();
	fel8();

	return 0;
}