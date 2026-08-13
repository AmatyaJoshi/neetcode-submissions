class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        required = Counter(t)
        window = Counter()

        left, satisfied = 0, 0
        best_left, best_right = 0, 0
        min_len = float("inf")

        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == required[s[right]]:
                satisfied += 1
            while satisfied == len(required):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                    best_right = right
                if window[s[left]] == required[s[left]]:
                    satisfied -= 1
                window[s[left]] -= 1
                left += 1
        return s[best_left: best_right + 1] if min_len != float("inf") else ""

