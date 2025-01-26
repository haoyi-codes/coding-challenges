#!/usr/bin/env python3

# File Name: palindrome_number.py
# Description: palindrome_number python coding challenge from leetcode.

# Copyright (c) 2025 Aryan
# SPDX-License-Identifier: BSD-3-Clause

# Version: 1.0.0

class Solution:
    """
    This is a class that finds the solution to the "Palindrome Number" problem from leetcode.

    Methods:
        is_palindrome: check if given integer is a palindrome.
    """

    def is_palindrome(self, x:int) -> bool:
        """
        Check if the given integer is a palindrome.

        Args:
            self: The instance of the class.
            x (int): The given integer that we need to check.

        Returns:
            bool: return True if x is a palindrome, else return False. 
        """

        # If the integer is negative then it immediately isn't a palindrome.
        if x < 0:
            return False

        # We can convert the integer to a string so we can reverse it.
        x_str = str(x)
        x_str_rev = x_str[::-1]

        # Compare if the reversed integer is the same as the original integer
        # and return True if it is.
        if x_str == x_str_rev:
            return True
        else:
            return False


def main():
    """
    Provides 3 test cases for the is_palindrome fucntion.
    """
    # Create the objects.
    t1 = Solution()
    t2 = Solution()
    t3 = Solution()

    # Run the is_palindrome function.
    a1 = t1.is_palindrome(121)
    a2 = t2.is_palindrome(-121)
    a3 = t3.is_palindrome(10)

    # See if we have passed the tests.
    print(f"Output: {a1}")
    print(f"Expected output: True")
    if a1 is True:
        print("Test 1 passed.\n")
    else:
        print("Test 1 failed.\n")

    print(f"Output: {a2}")
    print(f"Expected output: False")
    if a2 is False:
        print("Test 2 passed.\n")
    else:
        print("Test 2 failed.\n")

    print(f"Output: {a3}")
    print(f"Expected output: False")
    if a3 is False:
        print("Test 3 passed.")
    else:
        print("Test 3 failed.")


if __name__ == "__main__":
    main()
