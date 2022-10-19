class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ht={}
        for i in nums:
            if i ==0:
                continue
            elif i in ht:
                ht[i] +=1
            else:
                ht[i]=1
        if ht=={}:
            return 0
        else:
            c=0
            for key in ht.keys():
                c +=1
            return c
