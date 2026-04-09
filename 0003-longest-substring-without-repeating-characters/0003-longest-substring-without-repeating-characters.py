class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        length = 0
        dict_index = {}

        for idx in range(len(s)):
            if s[idx] in dict_index:
                if dict_index[s[idx]] >= left:
                    left = dict_index[s[idx]] + 1

            dict_index[s[idx]] = idx
            length = max(length, idx - left + 1)

        return length
            
            
        