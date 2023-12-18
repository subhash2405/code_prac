class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for string in strs:
            sort=''.join(sorted(string))
            if sort not in dic:
                dic[sort]=[]
            dic[sort].append(string)
        return dic.values()
# https://leetcode.com/problems/group-anagrams/