"""
217. Contains Duplicate
EASY
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums
        occurrence = 0
        output = False
        for i in nums:
            for j in nums:
                if i == j:
                    occurrence +=1
                    if occurrence ==2:
                        output = True
            occurrence = 0

        return output