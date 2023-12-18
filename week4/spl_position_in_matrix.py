class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        a=[0]*m
        b=[0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    a[i]+=1
                    b[j]+=1
        count=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and a[i]==1 and b[j]==1:
                    count+=1
        return count
    # https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2023-12-13