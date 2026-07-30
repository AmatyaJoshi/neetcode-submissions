class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        # nums[j] = target - nums[i]
        for i, num in enumerate(nums):
            ans = target - num
            if ans in sums:
                return [sums.get(ans, 0), i]
            sums[num] = i
        