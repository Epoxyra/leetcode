class Solution:
    def climbStairs(self, n: int) -> int:
        # After looking at the results for the first values of n, we can notice it is a Fibonacci sequence.
        # To get to step n, we need to do go up 1 step from step n - 1 or to go up 2 steps from step n - 2.
        # Thus, the total number of combinations for n steps is equal to the number of combinations to get 
        # to n - 1 plus the number of combinations to get to n - 2

        if n <= 1:
            return 1
        var_1 = 1
        var_2 = 1
        res = 0
        for _ in range(n - 1):
            res = var_1 + var_2
            var_2 = var_1
            var_1 = res
        return res
