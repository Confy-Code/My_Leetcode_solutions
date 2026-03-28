class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = sum(1 for num in nums1 if num % 2 != 0)
        
        construct_even = (odds == 0) or (odds >= 1)
        construct_odd = (odds >= 1)

        return construct_even or construct_od    