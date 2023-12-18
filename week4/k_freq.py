class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        r=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for j in range(k):
            maxV=0
            max_num=0
            for key,value in dic.items():
                if value>maxV:
                    maxV=value
                    max_num=key
            r.append(max_num)
            dic.pop(max_num)
        return r

        
        # https://leetcode.com/problems/top-k-frequent-elements/submissions/1107161278/