class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        output = []
        left, right = 0, len(nums)- 1

        while left < right and right < len(nums):
            addition = sorted_nums[left] + sorted_nums[right]
            if addition > target:
                right -= 1

            if addition < target:
                left += 1

            if addition == target:
                idx_1 = nums.index(sorted_nums[left])
                output.append(idx_1)
                nums[idx_1] = "null"
                output.append(nums.index(sorted_nums[right]))
                break

        return output

        