class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return nums[0] + 1
        elif len(nums) == 1:
            return 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return i
            elif nums[i] - nums[i-1] == 1 and i + 1 == len(nums) and nums[0] == 0:
                return i + 1
            elif nums[i] - nums[i-1] == 1 and i + 1 == len(nums) and nums[0] != 0:
                return 0