#include <iostream>
#include <fstream>
using namespace std;

const double PI = 3.1415;

// declaring functions
void area_of_circle (const double &R, double &L, double &A);

int main () {
  const int N = 10;
  double R[N];

  double area, perimeter;
  int i;

  for (i = 0; i < N-1 ; i++) {
    cout << "Enter radius of circle: ";
    cin >> R[i];
    cout << "i = " << i+1 << ": R = " << R[i] << "\n"; 
  }

  ofstream myfile ("AREA.DAT");
  for (i = 0; i < N-1; i++) {
    area_of_circle(R[i], perimeter, area);

    myfile << i+1 << ") R=" << R[i] << "; perimeter = " << perimeter << "\n";
    myfile << i+1 << ") R=" << R[i] << "; area = " << area << "\n";
  }

  myfile.close();
}

void area_of_circle (const double &R, double &L, double &A) {
  // we give the adress of the variable L and R
  // setting L and R => change the "global variables" L and R
  L = 2.0 * PI * R;
  A = PI * R * R ;
}