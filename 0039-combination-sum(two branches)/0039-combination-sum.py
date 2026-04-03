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

            # we will include the element until we can't anymore
            # That is why we use idx (with no incrementation)
            helper(candidates, idx, stack, target - candidates[idx])

            # Backtracking will happen once we traced all possibilities of the same element
            stack.pop()
            helper(candidates, idx + 1, stack, target)

        helper(candidates, 0, [], target)
        return self.answer

        