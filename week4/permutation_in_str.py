class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        b = len(s2)
        if a > b:
            return False
        k = b - a + 1
        for i in range(k):
            st=""
            flag = 0
            x = 0
            while x < a:
                if s2[i + x] in s1:
                    flag += 1
                    st+=s2[i+x]
                else:
                    break
                x += 1
            if flag == a and Counter(st)==Counter(s1):
                return True
        return False
# https://leetcode.com/problems/permutation-in-string/