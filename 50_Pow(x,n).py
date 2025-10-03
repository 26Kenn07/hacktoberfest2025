class Solution:
    def myPow(self, x: float, n: int) -> float:
        n = n-1
        if n==0:
            return

        return self.myPow(self.myPow(x, n), n-1)
