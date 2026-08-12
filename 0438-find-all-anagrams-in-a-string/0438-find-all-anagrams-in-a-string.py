from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter()
        result = []
        k = len(p)
        
        if k > len(s):
            return []

        for idx in range(k):
            window[s[idx]] += 1

        if window == Counter(p):
            result.append(0)

        left = 0

        for right in range(k, len(s)):
            window[s[right]] += 1
            window[s[left]] -= 1

            if window[s[left]] == 0:
                del window[s[left]]

            left += 1

            if window == Counter(p):
                result.append(left)

        return result       