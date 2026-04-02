class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()

        def helper(nums, stack, idx):
            if idx == len(nums):
                self.result.append(list(stack))
                return 

            stack.append(nums[idx])
            helper(nums, stack, idx + 1)

            stack.pop()
            
            # REMOVING DUPLICATES
            i = idx + 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

            helper(nums, stack, i)
        
        helper(nums, [], 0)
        return self.result

