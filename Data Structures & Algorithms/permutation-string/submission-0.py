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

        # check first window
        if freq_window == freq_s1:
            return True

        # slide window
        for right in range(len(s1), len(s2)):
            # add new char
            freq_window[ord(s2[right]) - ord('a')] += 1

            # remove old char
            freq_window[ord(s2[right - len(s1)]) - ord('a')] -= 1

            # check
            if freq_window == freq_s1:
                return True

        return False