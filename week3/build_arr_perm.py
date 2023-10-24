class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        for i in range(len(nums)):
            a=nums[nums[i]]
            lis.append(a)
        return lis
#https://leetcode.com/problems/build-array-from-permutation/description/