"""
Author: Noah Samuel Kipp
Date: 08.05.2026
Revised: -
Note: -

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Cast array to a set, check if set holds fewer values than array - if it does, the array contained duplicates
        return len(set(nums)) < len(nums)

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""