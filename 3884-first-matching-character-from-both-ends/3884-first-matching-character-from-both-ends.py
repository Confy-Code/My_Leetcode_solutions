class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        idx = 0
        
        while idx < n:
            if s[idx] == s[n - idx - 1]:
                return idx
            idx += 1

        return -1  