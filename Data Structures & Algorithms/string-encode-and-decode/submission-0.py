class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result #"5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        length_char = ""
        result = []
        i = 0

        while i < len(s):
            if s[i] == '#':
                char_len = int(length_char)
                word = s[i+1:i+char_len + 1]
                result.append(word)
                length_char = ""
                i += (char_len + 1)
            else:
                length_char += s[i]
                i += 1
        return result
