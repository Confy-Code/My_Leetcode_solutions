class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(left, right):
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ""
        for idx in range(len(s)):
            odd_pal = helper(idx, idx)
            even_pal = helper(idx, idx + 1)

            result = max(result, odd_pal, even_pal, key = len)
        return result
        