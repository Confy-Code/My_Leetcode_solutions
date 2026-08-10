class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        counts = {0: 1}
        result = 0

        for idx in range(1, len(nums)):
            prefix_sum[idx] = prefix_sum[idx -1] + nums[idx]

        for sum_ in prefix_sum:    # used sum_ to avoid keyword 'sum'
            needed_sum = sum_ - k

            if needed_sum in counts:
                result += counts[needed_sum]

            counts[sum_] = counts.get(sum_, 0) + 1

        return result           