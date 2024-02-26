class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted([x for x in str(num)])
        return int(nums[0] + nums[2]) + int(nums[1] + nums[3])