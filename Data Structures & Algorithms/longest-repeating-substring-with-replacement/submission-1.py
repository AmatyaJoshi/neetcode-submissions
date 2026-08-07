class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, max_len = 0, 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(freq.values())
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len