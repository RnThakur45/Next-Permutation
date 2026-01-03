🔁 Next Permutation (In-Place Algorithm)

  This program implements the Next Permutation algorithm, which rearranges numbers into the next lexicographically greater permutation of the given list.
  If no such permutation exists, it rearranges the list into the lowest possible order (sorted ascending).

📌 Problem Statement

Given an array of integers, modify it in-place to produce the next permutation.

If the array is already in descending order, return the first permutation.

🧠 Algorithm Overview

The algorithm follows four key steps:

Find Pivot

  Traverse from right to left.
  
  Find the first index piv where nums[piv] < nums[piv + 1].

If No Pivot Found

  The array is in descending order.

  Reverse the entire array to get the smallest permutation.

Swap

  Find the smallest element on the right of piv that is greater than nums[piv].
  
  Swap them.

Reverse Suffix

  Reverse the subarray to the right of the pivot.
