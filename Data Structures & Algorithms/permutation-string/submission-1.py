class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        freq_window = [0] * 26

        # build freq_s1
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1

        # first window
        for i in range(len(s1)):
            freq_window[ord(s2[i]) - ord('a')] += 1

        # initialize matches
        matches = 0
        for i in range(26):
            if freq_s1[i] == freq_window[i]:
                matches += 1

        # slide window
        for right in range(len(s1), len(s2)):

            # check before updating
            if matches == 26:
                return True

            # add new char
            idx = ord(s2[right]) - ord('a')
            freq_window[idx] += 1

            if freq_window[idx] == freq_s1[idx]:
                matches += 1
            elif freq_window[idx] == freq_s1[idx] + 1:
                matches -= 1

            # remove old char
            idx = ord(s2[right - len(s1)]) - ord('a')
            freq_window[idx] -= 1

            if freq_window[idx] == freq_s1[idx]:
                matches += 1
            elif freq_window[idx] == freq_s1[idx] - 1:
                matches -= 1

        return matches == 26