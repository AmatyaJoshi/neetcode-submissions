class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = {}

        # for ch in strs:
        #     key = tuple(sorted(Counter(ch).items()))
        #     anagram.setdefault(key, []).append(ch)
        
        # return [ana_list for ana_list in anagram.values()]
        
        anagram = {}

        for ch in strs:
            count = [0] * 26
            for c in ch:
                index = ord(c) - ord('a')
                count[index] += 1
            anagram.setdefault(tuple(count), []).append(ch)
        return list(anagram.values())
