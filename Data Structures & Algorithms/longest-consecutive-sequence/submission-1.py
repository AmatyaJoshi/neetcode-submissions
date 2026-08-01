class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        current_length = 1
        longest = 1
        sorted_arr = sorted(nums)

        for i in range(len(sorted_arr)-1):
            diff = sorted_arr[i+1] - sorted_arr[i]

            if diff == 0:
                continue
            elif diff == 1:
                current_length += 1
            else:
                longest = max(longest, current_length)
                current_length = 1

        longest = max(longest, current_length)
        return longest