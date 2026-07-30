class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for ch in strs:
            key = tuple(sorted(Counter(ch).items()))
            anagram.setdefault(key, []).append(ch)
        
        return [ana_list for ana_list in anagram.values()]