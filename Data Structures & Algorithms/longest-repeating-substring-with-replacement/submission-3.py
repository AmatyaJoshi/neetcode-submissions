class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_len, max_freq = 0, 0, 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_freq, right - left + 1)
        return max_len