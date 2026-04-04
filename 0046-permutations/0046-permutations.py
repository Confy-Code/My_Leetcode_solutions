class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.answer = []

        def helper(nums, idx):
            if idx == len(nums):
                self.answer.append(list(nums))

            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                helper(nums, idx + 1)

                # BACKTRACKING PROCESS
                nums[i], nums[idx] = nums[idx], nums[i]
        
        helper(nums, 0)
        return self.answer



        