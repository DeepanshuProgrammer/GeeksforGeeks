class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i] =nums[i]+prefix[i-1]
        
        for i in range(0,n):
            if i==0:
                if (prefix[n-1]-prefix[i])==0:
                    return i
            elif i==n:
                if prefix[n-2]==0:
                    return i
            else:
                if prefix[i-1]==(prefix[n-1]-prefix[i]):
                    return i
        
        return -1
