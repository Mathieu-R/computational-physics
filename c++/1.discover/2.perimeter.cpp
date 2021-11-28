#include <iostream>
#include <fstream>
using namespace std;

int main() {
  const double PI = 3.1415;
  const int N = 10;
  double R[N]; // N-entry vector containing radius

  double area, perimeter;
  int i;

  for (i = 0; i < N-1 ; i++) {
    cout << "R = ";
    cin >> R[i];

    perimeter = 2.0 * PI * R[i];
    area = PI * (R[i] * R[i]);

    cout << "circle perimeter : " << perimeter << "\n";
    cout << "circle area: " << area << "\n";
  } 

  ofstream dataFile ("data.DAT");
  dataFile.close();
}