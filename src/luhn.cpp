#include <iostream>
#include <cmath>

using std::string;
using std::cout;
using std::cin;

int main() {

  long int cc;
  long int cc_copy;
  int count = 0;
  int sum = 0;

  cout << "------ Luhn Algorithm: CC Validator ------" << "\n";
  cout << "Enter CC to check the validity of: ";
  cin >> cc;

  cc_copy = cc;

  long int amex = cc / pow(10, 13); 
  long int master = cc / pow(10, 14);
  long int visa[2];
  visa[0] = cc / pow(10, 12);
  visa[1] = cc / pow(10, 15);

  while (cc > 0) {
    int digit = cc % 10;
    cc /= 10;
    count++;

    if (count % 2 == 0) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
  }

  if (sum % 10 == 0) {
    cout << cc_copy << " is a valid CC " << "\n";
    if (amex == 34 || amex == 37) {
      cout << "Card Type: AMEX" << "\n";
    }
  
    if (master == 51 || master == 52 || master == 53 || master == 54 || master == 55){
      cout << "Card Type: MASTERCARD" << "\n";
    }

    if (visa[0] == 4 || visa[1] == 4) {
      cout << "Card Type: VISA" << "\n";
    }

  } else {
    cout << cc_copy << " is not a valid CC" << "\n";
  }
  return 0;
}