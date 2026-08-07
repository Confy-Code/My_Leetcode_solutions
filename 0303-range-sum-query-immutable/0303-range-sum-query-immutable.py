class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0] * len(self.nums)
        prefix[0] = self.nums[0]

        for idx in range(1, len(self.nums)):
            prefix[idx] = prefix[idx - 1] + self.nums[idx]

        if left == 0:
            return prefix[right]
        
        return prefix[right] - prefix[left - 1] 
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)