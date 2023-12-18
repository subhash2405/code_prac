class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        a=-1
        b=-1
        c=-1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
                a+=1
            if s[i]==')':
                if a==-1:
                    return False
                if stack[-1]=='{' or stack[-1]=='[':
                    return False 
                else:
                    while stack and stack[-1]!='(':
                            stack.pop()
                    if stack:
                        stack.pop()
                    a-=1
            if s[i]=='{':
                stack.append(s[i])
                b+=1
            if s[i]=='}':
                if b==-1:
                    return False
                if stack[-1]=='(' or stack[-1]=='[':
                    return False 
                else:
                    while stack and stack[-1]!='{':
                        stack.pop()
                    if stack:
                        stack.pop()
                    b-=1
            if s[i]=='[':
                stack.append(s[i])
                c+=1
            if s[i]==']':
                if c==-1:
                    return False
                if stack[-1]=='{' or stack[-1]=='(':
                    return False 
                else:
                    while stack and stack[-1]!='[':
                        stack.pop()
                    if stack:
                        stack.pop()
                    c-=1
        if len(stack)>=1:
            return False
        else:
            return True
        
        # https://leetcode.com/problems/valid-parentheses/submissions/1105796239/