class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)

        for idx in range(len(nums)):
            prefix_sum[idx] = nums[idx] + (prefix_sum[idx -1] if idx > 0 else 0)

        minimum_sum = 0

        result = float('-inf')

        for sum_ in prefix_sum:
            diff = sum_ - minimum_sum
            result = max(result, diff)

            minimum_sum = min(minimum_sum, sum_) 

        return result    