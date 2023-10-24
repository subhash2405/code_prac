class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [1] * n

        lef = 1
        for i in range(1, n):
            lef*= nums[i - 1]
            left[i] = lef

        rt = 1
        for i in range(n - 2, -1, -1):
            rt*= nums[i + 1]
            right[i] = rt

        for i in range(n):
            result[i] = left[i] * right[i]

        return result
#https://leetcode.com/problems/product-of-array-except-self/description/