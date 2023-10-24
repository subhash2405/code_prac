class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n-1):
            a=nums.pop(n+i)
            nums.insert(2*i+1,a)
        return nums

#https://leetcode.com/problems/shuffle-the-array/description/