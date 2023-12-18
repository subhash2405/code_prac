class Solution:
    def totalMoney(self, n: int) -> int:
        if n==1:
            return 1
        count=0
        a=n//7
        b=n%7
        i=0
        while i<a:
            count+=(28+7*i)
            i+=1
        j=1
        while j<=b:
            count+=(a+j)
            j+=1
        return count
        
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2023-12-06