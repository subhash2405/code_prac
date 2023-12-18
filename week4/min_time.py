class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(0,len(points)-1):
            x=abs(points[i][0]-points[i+1][0])
            y=abs(points[i][1]-points[i+1][1])
            minv=min(x,y)
            time+=minv
            time=time+max(x,y)-minv
        return time



        # https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2023-12-03