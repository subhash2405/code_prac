class Solution:
    def isPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        s=s.lower()
        while low<=high:
            if not s[low].isalnum():
                low+=1
                continue
            elif not s[high].isalnum():
                high-=1
                continue
            elif s[low]==s[high]:
                low+=1
                high-=1
            else:
                return False
        return True
            
        # https://leetcode.com/problems/valid-palindrome/