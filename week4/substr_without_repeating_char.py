class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] not in seen:
                longest = max(longest, i - start + 1)
            else:
                if seen[s[i]] < start:
                    longest = max(longest, i - start + 1)
                else:
                    start = seen[s[i]] + 1
            seen[s[i]] = i

        return longest
# https://leetcode.com/problems/longest-substring-without-repeating-characters/