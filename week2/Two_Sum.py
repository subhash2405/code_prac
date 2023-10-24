class Solution(object):
    def twoSum(self, nums, target):
        visited={}
        for i in range(len(nums)):
            visited[nums[i]]=i
        for i in range(len(nums)):
            a=target-nums[i]
            if a in visited and visited[a]!=i:
                return [visited[a],i]
