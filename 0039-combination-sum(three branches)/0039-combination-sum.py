class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.answer = []
        self.set_1 = set()

        def helper(candidates, stack, idx, target):
            # BASE CASE 1: IF TARGET IS NEGATIVE, THERE IS NO NEED TO KEEP GOING DEEP
            if idx == len(candidates) or target < 0:
                return 
            
            # BASE CASE 2: IF WE MEET OUR BASE CASE
            # WE REMOVE THE DUPLICATES USING HASHABLE DATATYPES

            if target == 0:
                stack_tuple = tuple(stack)
                if stack_tuple not in self.set_1:
                    self.answer.append(list(stack))
                    self.set_1.add(stack_tuple)
                return
            
            stack.append(candidates[idx])

            # INCLUDE ONCE
            helper(candidates, stack, idx + 1, target - candidates[idx])

            # INCLUDE MULTIPLE TIMES
            helper(candidates, stack, idx, target - candidates[idx])

            # BACKTRACKING - EXCLUDE ONCE
            stack.pop()
            helper(candidates, stack, idx + 1, target)

        helper(candidates, [], 0, target)
        return self.answer    