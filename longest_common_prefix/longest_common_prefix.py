#!/usr/bin/env python3

# File Name: longest_common_prefix.py
# Description: longest_common_prefix python coding challenge from leetcode

# Copyright (c) 2025 Aryan
# SPDX-License-Identifier: BSD-3-Clause

# Version: 1.0.0

class Solution:
    """
    This is a class that finds the solution to the "Longest Common Prefix" problem from leetcode.

    Methods:
        longest_common_prefix: Find the longest common prefix amongst an array of
                               strings.
    """

    def longest_common_prefix(self, strs: list[str]) -> str:
        """
        Find the longest common prefix amongst an array of strings.

        Args:
            self: The instance of the class.
            strs (list[str]) : 

        Returns:
            str: returns the longest common prefix or "".
        """

        common_prefix = ""

        # Sort the list in alphabetical order therefore we can simplify by
        # comparing the last and the first word.
        strs = sorted(strs)

        # Obtain the first and last words.
        first_word = strs[0]
        last_word = strs[-1]

        # Find the shortest word.
        min_len = min(len(first_word), len(last_word))

        # Compare the prefix characters of the first and last word.
        for i in range(min_len):
            # If they are not the same return the current "common_prefix" value.
            if first_word[i] != last_word[i]:
                return common_prefix
            else:
                # Else append the common character to "common_prefix".
                common_prefix += first_word[i]

        return common_prefix

def main():
    """
    Provides 2 test cases for the is_palindrome fucntion.
    """
    # Create the objects.
    t1 = Solution()
    t2 = Solution()

    # Run the longest_common_prefix function.
    a1 = t1.longest_common_prefix(["flower", "flow", "flight"])
    a2 = t2.longest_common_prefix(["dog", "racecar", "car"])

    # See if we have passed the tests.
    print(f"Output: {a1}")
    print("Expected output: fl")

    if a1 == "fl":
        print("Test 1 passed.\n")
    else:
        print("Test 1 failed.\n")

    print(f"Output: {a2}")
    print("Expected output:")

    if a2 == "":
        print("Test 2 passed.\n")
    else:
        print("Test 2 failed.\n")


if __name__ == "__main__":
    main()
