class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        high=len(height)-1
        maxv=0
        while low<high:
            if maxv<min(height[low],height[high])*(high-low):
                maxv=min(height[low],height[high])*(high-low)    
            if height[high]<height[low]:
                high-=1
            elif height[high]>height[low]:
                low+=1
            else:
                low+=1
                high-=1
        return maxv

        # https://leetcode.com/problems/container-with-most-water/