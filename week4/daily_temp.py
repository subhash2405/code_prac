class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # arr=[temperatures[0]]
        # ans=[0]*len(temperatures)
        # count=0
        # for i in range(1,len(temperatures)):
        #     if temperatures[i-1]<temperatures[i]:
        #         while arr and arr[-1]<temperatures[i]:
        #             x=arr.pop()
        #             count+=1
        #             ans[temperatures.index(x)]+=count
        #         if arr:
        #             for k in arr:
        #                 ans[temperatures.index(k)]+=count
        #         count=0
        #         arr.append(temperatures[i])
        #     else:
        #         count=0
        #         arr.append(temperatures[i])
        # return ans
        arr=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while arr and temperatures[arr[-1]]<temperatures[i]:
                res[arr[-1]]=i-arr[-1]
                arr.pop()
            arr.append(i)
        return res
# https://leetcode.com/problems/daily-temperatures/