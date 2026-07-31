class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        right = 1

        # Left Pass
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        # Right Pass
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]      

        return ans