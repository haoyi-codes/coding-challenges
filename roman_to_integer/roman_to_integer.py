#!/usr/bin/env python3

# File Name: roman_to_integer.py
# Description: roman_to_integer python coding challenge from leetcode.

# Copyright (c) 2025 Aryan
# SPDX-License-Identifier: BSD-3-Clause

# Version: 1.0.0

class Solution:
    """
    This is a class that finds the solution to the "Roman to Integer" problem from leetcode.

    Methods:
        roman_to_int: Convert a roman numeral to an integer.
    """

    def roman_to_int(self, s: str) -> int:
        """
        Convert a roman numeral to an integer.

        Args:
            self: The instance of the class.
            s (str): The given roman numeral that we need to convert.

        Returns:
            int: Return the integer value of the roman numeral
        """

        # This dictionary will represent values for roman numerals.
        roman_dict = {
                "I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000
            }

        # We will start at 0 and then add to this.
        number = 0

        # Go through each symbol of the roman numeral.
        for i in range(len(s)):
            # If there is another symbol after the current and the next
            # symbol is larger than our current symbol.
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                # Subtract the current symbol from our "number" since the pair
                # represents a smaller number than the second symbol on its
                # own.
                number -= roman_dict[s[i]]
            else:
                # Add the current symbol to our "number" since the pair doesn't
                # represent a smaller number than the second symbol on its own.
                number += roman_dict[s[i]]
        
        return number

def main():
    """
    Provides 3 test cases for the roman_to_int fucntion.
    """
    # Create the objects.
    t1 = Solution()
    t2 = Solution()
    t3 = Solution()

    # Run the roman_to_int function.
    a1 = t1.roman_to_int("III")
    a2 = t2.roman_to_int("LVIII")
    a3 = t3.roman_to_int("MCMXCIV")

    # See if we have passed the tests.
    print(f"Output: {a1}")
    print(f"Expected output: 3")
    if a1 == 3:
        print("Test 1 passed.\n")
    else:
        print("Test 1 failed.\n")

    print(f"Output: {a2}")
    print(f"Expected output: 58")
    if a2 == 58:
        print("Test 2 passed.\n")
    else:
        print("Test 2 failed.\n")

    print(f"Output: {a3}")
    print(f"Expected output: 1994")
    if a3 == 1994:
        print("Test 3 passed.")
    else:
        print("Test 3 failed.")


if __name__ == "__main__":
    main()
