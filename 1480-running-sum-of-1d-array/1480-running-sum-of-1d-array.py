class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx - 1] + nums[idx]

        return prefix