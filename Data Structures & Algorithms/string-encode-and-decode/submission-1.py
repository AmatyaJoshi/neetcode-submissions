class Solution:

    # Optimized
    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts) # 5#Hello5#World

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = s.find("#", i)
            word_len = int(s[i:j])
            next_i = j + word_len + 1
            result.append(s[j + 1 : next_i])
            i = next_i
        return result


    # My Solution:
    # def encode(self, strs: List[str]) -> str:
    #     result = ""
    #     for s in strs:
    #         result += f"{len(s)}#{s}"
    #     return result #"5#Hello5#World"

    # def decode(self, s: str) -> List[str]:
    #     length_char = ""
    #     result = []
    #     i = 0

    #     while i < len(s):
    #         if s[i] == '#':
    #             char_len = int(length_char)
    #             word = s[i+1:i+char_len + 1]
    #             result.append(word)
    #             length_char = ""
    #             i += (char_len + 1)
    #         else:
    #             length_char += s[i]
    #             i += 1
    #     return result
