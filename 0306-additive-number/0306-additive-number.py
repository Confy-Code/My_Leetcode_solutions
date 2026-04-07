class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        # if n is less than 3, that number can't be additive ever!
        if n < 3:
            return False

        # For first and second numbers

        for first in range(1, n):
            for second in range(first + 1, n):
                first_num = num[:first]
                second_num = num[first:second]

                # if we have numbers like 01, 02 where their length > 1 and their first element = 0, we try a different length, unless we have a literal '0'
                if(first_num[0] == '0' and len(first_num) > 1) or (second_num[0] == '0' and len(second_num) > 1):
                    continue

                remaining = num[second:]
                if self.helper(remaining, first_num, second_num):
                    return True

        return False

    def helper(self, remaining, first_num, second_num):
        # BASE CASE: IF SLICE OFF TILL AN EMPTY STRING
        if remaining == "":
            return True

        addition = int(first_num) + int(second_num)
        
        if remaining.startswith(str(addition)):
            remaining = remaining[len(str(addition)):]   # We slice the 'sum' number off the remaining part
            return self.helper(remaining, second_num, addition) # First number = recent second number --- Second number = addition we summed up

        return False


    

            