class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pass = [1] * len(nums)
        right_pass = [1] * len(nums)
        answer = [0] * len(nums)
        
        product = 1

        for left in range(1, len(nums)):
            product *= nums[left - 1]
            left_pass[left] = product

        product = 1

        for right in range(len(nums) -1, -1, -1):
            if right == len(nums) -1:
                continue
            else:
                product *= nums[right + 1]
                right_pass[right] = product

        answer = [x * y for x, y in zip(right_pass, left_pass)]

        return answer

        
