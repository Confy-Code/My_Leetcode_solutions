class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s < 2:
            return ""
         
        set_string = set(s)

        for idx, char in enumerate(s):
            if char.swapcase() not in set_string:
                left = self.longestNiceSubstring(s[:idx])
                right = self.longestNiceSubstring(s[idx + 1:])

                return left if len(left) >= len(right) else right
        return s
        