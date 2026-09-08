class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        h = len(nums)-1

        while l<h:
            mid = (h+l) //2

            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                h = mid
        return l 
        

# Input: nums = [1,2,3,1]
# Output: 2

# https://leetcode.com/problems/find-peak-element/description/