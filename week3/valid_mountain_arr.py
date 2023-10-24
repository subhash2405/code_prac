class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n=len(arr)
        a=0
        b=0
        if n<3:
            return False
        ind=0
        for i in range(n-1):
            if arr[i]==arr[i+1]:
                return False
            if ind==0:
                if arr[i]<arr[i+1]:
                    ind=1
                    a+=1
                else:
                    ind=-1
                    b+=1
            else:
                if ind==1:
                    if arr[i]<arr[i+1]:
                        a+=1
                        continue
                    else:
                        ind=-1
                if ind==-1:
                    if arr[i]>arr[i+1]:
                        b+=1
                        continue
                    else:
                        return False
        
        if a==n-1 or b==n-1:
            return False
        else:
            return True
        return True
#https://leetcode.com/problems/valid-mountain-array/description/