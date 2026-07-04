class Solution:

    class FrozenCounter(Counter):
        def __hash__(self):
            return hash(tuple(sorted(self.items())))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for string in strs:
            c = Solution.FrozenCounter(string)
            if c in d:
                d[c].append(string)
            else:
                d[c]=[string]
        
        return list(d.values())


