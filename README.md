# Luhn Algorithm
The Luhn algorithm, also called the modulus 10 or mod 10 algorithm, validates various identification numbers like credit card and IMEI numbers. This repository is a Python implementation of the Luhn algorithm.

## Installation
```
pip/pip3 install Luhn-Algorithm
```

## Algorithm Overview
1. Double every alternate digit, beginning with the second-last digit, and then sum the individual digits of these products.
2. Add this sum to the sum of the digits that were not doubled.
3. If the last digit of the total is 0 (or, in more formal terms, if the total modulo 10 is congruent to 0), the number is considered valid.

### Example
Card to test: 
```
4003600000000014
```
Every alternate digit beginning with the second-last digit is:
```
40600001
```
Doubling each digit results in:
```
4 ⋅ 2 ⋅ 6 ⋅ 2 ⋅ 1 ⋅ 2 = 8 12 2 (zeros were removed for coherence)
```
Sum the individual digits of these products:
```
8 + 1 + 2 + 2 = 13 (12 = 1 + 2)
```
Add the sum to the sum of digits that were not doubled:
```
13 + 4 + 3 = 20 (zeros were removed for coherence)
```
`20 % 10 = 0`, therefore, `4003600000000014` is valid.

## Algorithm Implementation in Python
```python
class LuhnAlgorithm:
    def __init__(self, card_numbers):
        if isinstance(card_numbers, int):
            card_numbers = [card_numbers]
        self.card_numbers = card_numbers
        self.valid = [False] * len(self)
```
This Python class, `LuhnAlgorithm`, initialises with a parameter `card_numbers`. It checks if `card_numbers` is an integer; if so, it converts it into a list. The class stores `card_numbers` and initialises a list named `valid` with `False` values based on the length of `card_numbers`.

```python
def _double_other(self, card_number) -> list:
        """Double every other digit starting from the second-to-last digit."""
        card_array = [int(char) for char in str(card_number)]
        doubled_array = []

        for i in range(len(card_array) - 2, -1, -2):
            doubled_digit = card_array[i] * 2
            if doubled_digit > 9:
                doubled_digit -= 9  
            doubled_array.append(doubled_digit)
            doubled_array.append(card_array[i + 1] if i + 1 < len(card_array) else 0) 

        if len(card_array) % 2 != 0:
            doubled_array.append(card_array[0])

        return doubled_array
```
`_double_other` method takes a `card_number` as input and returns a list. The `card_number` is first converted into a string to enable iteration over its individual digits. This string representation is then transformed into a list of integers, `card_array`, using a list comprehension. Each character in the string is converted back into an integer, allowing for the processing of each digit individually. This conversion ensures that the Luhn algorithm can accurately double alternate digits and perform subsequent operations. Then, it iterates over the list, doubling every other digit starting from the second-to-last digit. If the doubled digit is greater than 9, it subtracts 9 from it. When a digit is doubled in the Luhn algorithm and the result exceeds 9, subtracting 9 from it yields the same value as the sum of the individual digits. For example, take the number 12, which in the context of the algorithm, is treated as 1 + 2 = 3. Similarly, subtracting 9 from 12 yields 3. This is because 12 - 9 = 3. This principle holds true for other numbers as well. For instance, with the number 15, it is 1 + 5 = 6 (in the context of Luhn algorithm). Subsequently, subtracting 9 from 15 also yields 6, as 15 - 9 = 6. The function appends the doubled digits and the next digit (unchanged) to a new list named `doubled_array`. If the length of the card number is odd, it appends the first digit of the card number to `doubled_array`. Finally, it returns `doubled_array`.

```python
def _add_all(self, card_number) -> int:
        """Sum all digits in the card number."""
        doubled_digits = self._double_other(card_number)
        sum_of_digits = sum(doubled_digits)
        return sum_of_digits
```
`_add_all` simply adds all integers in the `doubled_array` returned by `self._double_other(card_number)`.

```python
def validate(self):
        """Validate the card numbers using the Luhn algorithm."""
        for i, card_number in enumerate(self.card_numbers):
            checksum = self._add_all(card_number)
            self.valid[i] = checksum % 10 == 0

        return self.valid
```
This method, `validate`, checks the validity of card numbers using the Luhn algorithm. It iterates through each card number in the provided list, computing the checksum using the `_add_all` method. The validity of each card number is determined by whether the checksum modulo 10 equals zero. The results are stored in the `valid` list, indexed according to the position of each card number in the input list. Finally, the method returns the `valid` list containing the validation results for each card number.

## Usage
```python
card_numbers = [378282246310015, 4111111111111110, 5105105105105100]
validator = LuhnAlgorithm(card_numbers)
results = validator.validate()
print(results)
```
```
[False, False, True]
```
You can test this algorithm against a [list of PayPal's credit card numbers.](https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm)

## LICENSE
This repository is under the [GNU General Public License v3 (GPLv3)](https://github.com/ibnaleem/luhn-algorithm/blob/main/LICENSE)

## Acknowledgements
- [Hans Peter Luhn](https://en.wikipedia.org/wiki/Hans_Peter_Luhn)
