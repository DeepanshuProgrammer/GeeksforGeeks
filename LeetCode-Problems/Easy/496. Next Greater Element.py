class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        ans=[]
        for i in range(n):
            j=0
            while(j<m):
                if nums1[i]==nums2[j]:
                    break
                j+=1
            for k in range(j+1,m):
                if nums2[k]>nums1[i]:
                    ans.append(nums2[k])
                    break
            else:
                ans.append(-1)
        return ans
