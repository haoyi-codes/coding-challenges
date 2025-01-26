#!/usr/bin/env python3

# File Name: two_sum.py
# Description: two_sum python coding challenge from leetcode.

# Copyright (c) 2025 Aryan
# SPDX-License-Identifier: BSD-3-Clause

# Version: 1.1.1

class Solution:
    """
    This is a class that finds the solution to the "Two Sum" problem from leetcode.

    Methods:
        two_sum: find the two integers that add up to the target integer.
    """

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Find two integers in the given array that adds up to the target integer.

        Args:
            self: The instance of the class.
            nums (list[int]): The given array that includes the integers.
            target (int): The target number that two integers should add up to.

        Returns:
            list[int]: The position of the two integers in the array that add up
                       to the target.
        """

        # Create a hashmap to map the integers to the position in the array.
        hashmap = {}
        
        # Loop through the array.
        # i represents the index of the array and starts from 0.
        for i in range(len(nums)):
            # Find the compliment that is required to be added with nums[i] to
            # obtain the target.
            compliment = target - nums[i]

            # If the compliment already exists in our hashmap that means we have
            # found the number.
            if compliment in hashmap:
                # Return the index of the compliment as well as the current
                # index first, as the index of the compliment will be smaller than the
                # current index.
                return [hashmap[compliment], i]
            else:
                # If it doesn't exist in the index add the current integer to
                # the hashmap along with its index.
                hashmap[nums[i]] = i


def main():
    """
    Provides 3 test cases for the two_sum function
    """
    # Create the objects.
    t1 = Solution()
    t2 = Solution()
    t3 = Solution()

    # Run the two_sum function.
    a1 = t1.two_sum([2,7,11,15], 9)
    a2 = t2.two_sum([3,2,4], 6)
    a3 = t3.two_sum([3,3], 6)

    # See if we have passed the tests.
    print(f"Output: {a1}")
    print(f"Expected output: [0,1]")
    if a1 == [0,1]:
        print("Test 1 passed.\n")
    else:
        print("Test 1 failed.\n")

    print(f"Output: {a1}")
    print(f"Expected output: [1,2]")
    if a2 == [1,2]:
        print("Test 2 passed.\n")
    else:
        print("Test 2 failed.\n")

    print(f"Output: {a1}")
    print(f"Expected output: [0,1]")
    if a3 == [0,1]:
        print("Test 3 passed.")
    else:
        print("Test 3 failed.")


if __name__ == "__main__":
    main()
