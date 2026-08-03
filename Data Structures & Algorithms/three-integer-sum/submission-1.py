class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i = 0
        result = []

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            l, r = i+1, len(sorted_nums) - 1
            while (l < r):
                current = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if current < 0 :
                    l += 1
                elif current > 0 :
                    r -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1 
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
        return result