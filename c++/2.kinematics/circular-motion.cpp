#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>
using namespace std;

#define PI 3.1415

int main () {
  string buf;

  double x, y, vx, vy, x0, y0, R, t, t0, tf, dt;
  double theta, omega;

  // get data
  cout << "# enter the angular velocity (omega): \n";
  cin >> omega;
  getline(cin, buf);

  cout << "# enter the center of the circle (x0, y0) and its radius (R): \n";
  cin >> x0 >> y0 >> R;
  getline(cin, buf);

  cout << "# enter time information (t0, tf) and time interval (dt): \n";
  cin >> t0 >> tf >> dt;
  getline(cin, buf);

  // check
  if (R <= 0.0) {
    cerr << "Need R > 0 \n";
    exit(1);
  }

  if (omega <= 0.0) {
    cerr << "Need omega > 0 \n";
    exit(1);
  }

  cout << "Period (T) = " << (2 * PI) / omega << endl;

  ofstream data("circle.dat");
  data.precision(17); // precision to 17 digits floating point (= precision of a double)

  // loop
  for (t = t0; t <= tf; t += dt) {
    // angle
    theta = omega * (t - t0);
    
    // position
    x = x0 + R*cos(theta);
    y = y0 + R*sin(theta);

    // speed : v = dr/dt
    vx = -omega*R*sin(theta);
    vy = omega*R*cos(theta);

    data << t << " " << x << " " << y << " " << vx << " " << vy << " " << endl;
  }

  // if i want to plot with gnuplot (in terminal)
  // plot "circle.dat" using 1:2 with lines title "x(t)"
  // => plot t and x(t)
  // replot "circle.dat" using 1:3 with lines title "y(t)"
  // => plot t and y(t) on the first plot
}