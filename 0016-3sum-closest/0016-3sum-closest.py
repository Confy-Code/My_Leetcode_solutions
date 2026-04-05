class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        # INITIAL SUM
        result = nums[0] + nums[1] + nums[2]
        
        for idx in range(len(nums) - 2):
            left, right = idx + 1, len(nums) - 1

            while left < right:
                current_sum = nums[idx] + nums[left] + nums[right]
                # COMPARE THE DEVIATIONS OF BOTH OF THE SUMS FROM THE TARGET
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum

                # MOVING THE POINTERS
                if current_sum == target:
                    return current_sum

                elif current_sum > target:
                    right -= 1

                else:
                    left += 1

        return result




        