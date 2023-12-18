class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=0
        while (high-low)>1:
            mid=(low+high)//2
            a=0
            # b=0
            for i in range(len(piles)):    
                if piles[i]<(mid):
                    a+=1
                elif piles[i]%(mid)==0:
                    a+=piles[i]//(mid)
                else:
                    a+=piles[i]//(mid) + 1
            if a>h:
                low=mid
            else:
                high=mid
        return high
# https://leetcode.com/problems/koko-eating-bananas/