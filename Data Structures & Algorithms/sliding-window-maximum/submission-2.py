from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        dq = deque()

        for right in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            while right - left + 1 > k:
                left += 1

            while dq and dq[0] < left:
                dq.popleft()

            if right - left + 1 == k:
                res.append(nums[dq[0]])
        return res