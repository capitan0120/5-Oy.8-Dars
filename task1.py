class Solution:
    def isUgly(self, n: int) -> bool:
        k = n // 2 + 1
        if n == 1:
            return True
        else:
            for i in range(2, k):
                if n % i == 0:
                    n //= i
                if i > 5 and n != 1:
                    return False
                else:
                    continue
            return True