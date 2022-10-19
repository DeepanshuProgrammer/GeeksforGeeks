class Solution:
    def inflection_point(self, A):
        N=len(A)
        low=0
        high=N-1
        while(low<=high):
            mid=(low+high)//2
            if mid== N-1 or A[mid]>A[mid+1]:
                return mid
            elif A[mid] >= A[low]:
                low=mid+1
            else:
                high=mid-1
        return high
    
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        ip=self.inflection_point(nums)
        if ip == n-1:
            return nums[0]
        return nums[ip+1]
                
