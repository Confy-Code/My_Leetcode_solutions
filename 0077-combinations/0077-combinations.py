class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.nums = [num for num in range(1, n + 1)]
        self.result = []

        def helper(stack, idx, k):
            if idx == len(self.nums):
                if len(stack) == k:
                    self.result.append(list(stack))
                return 

            stack.append(self.nums[idx])
            helper(stack, idx + 1, k)

            # BACKTRACKING
            stack.pop()
            helper(stack, idx + 1, k)

        helper([], 0, k)
        return self.result
        