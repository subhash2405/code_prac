class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                if len(res)==0:
                    res+=num[i:i+3]
                    continue
                else:
                    if int(res[0])>=int(num[i]):
                        continue
                    else:
                        res=""
                        res+=num[i:i+3]
        return res


        
        # https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2023-12-04