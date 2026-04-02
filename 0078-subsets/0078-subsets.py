class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtracking(nums, stack, idx):
            if idx == len(nums):
                self.result.append(list(stack))
                return 

            stack.append(nums[idx])
            backtracking(nums, stack, idx + 1)

            stack.pop()
            backtracking(nums, stack, idx + 1)

        backtracking(nums, [], 0)
        return self.result

        