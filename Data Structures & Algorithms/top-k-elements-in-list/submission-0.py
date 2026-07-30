class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        rev_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [n[0] for n in rev_freq[:k]]
        # for i, freq in frequency.items():
        #     if freq > 1:
        #         result.append(i)
        # return result