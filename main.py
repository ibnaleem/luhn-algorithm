class LuhnAlgorithm:
    def __init__(self, card_numbers):
        if isinstance(card_numbers, int):
            card_numbers = [card_numbers]
        self.card_numbers = card_numbers
        self.valid = [False] * len(self)

    def __len__(self) -> int:
        return len(self.card_numbers)

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

    def _add_all(self, card_number) -> int:
        """Sum all digits in the card number."""
        doubled_digits = self._double_other(card_number)
        sum_of_digits = sum(doubled_digits)
        return sum_of_digits

    def validate(self):
        """Validate the card numbers using the Luhn algorithm."""
        for i, card_number in enumerate(self.card_numbers):
            checksum = self._add_all(card_number)
            self.valid[i] = checksum % 10 == 0

        return self.valid
