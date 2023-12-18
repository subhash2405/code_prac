class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        else:
            # s=''.join(sorted(s))
            # t=''.join(sorted(t))
            # for i in range(len(s)):
            #     if(s[i]!=t[i]):
            #         return False
            # return True
            for i in set(s):
                if s.count(i)!=t.count(i):
                    return False
            return True
        
    # https://leetcode.com/problems/valid-anagram/?envType=daily-question&envId=2023-12-16