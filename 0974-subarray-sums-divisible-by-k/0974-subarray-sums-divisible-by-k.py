class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        counts = {0: 1}
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for idx in range(len(nums)):
            prefix_sum[idx] = nums[idx] + prefix_sum[idx -1]

        for sum_ in prefix_sum:
            remainder = sum_ % k

            if remainder in counts:
                result += counts[remainder]

            counts[remainder] = counts.get(remainder, 0) + 1

        return result

        