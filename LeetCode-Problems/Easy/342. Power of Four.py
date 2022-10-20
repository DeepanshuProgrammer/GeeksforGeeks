class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        else:
            x=4
            while(x<n):
                x *=4
            if x==n:
                return True
            else:
                return False
