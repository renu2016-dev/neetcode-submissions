class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        # print([i for i,j in sorted(counts.items(),key=lambda x:x[1], reverse=True)][:k])
        return [i for i,j in sorted(counts.items(),key=lambda x:x[1], reverse=True)][:k]