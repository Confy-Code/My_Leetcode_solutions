class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.answer = []
    
        def helper(candidates, idx, stack, target):

            if idx == len(candidates) or target < 0:
                return
            
            if target == 0:
                self.answer.append(list(stack))
                return
            
            stack.append(candidates[idx])

            helper(candidates, idx, stack, target - candidates[idx])

            stack.pop()
            helper(candidates, idx + 1, stack, target)

        helper(candidates, 0, [], target)
        return self.answer

        