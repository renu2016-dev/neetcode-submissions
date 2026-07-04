class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            sortedWord = ''.join(sorted(string))
            d[sortedWord].append(string)
        
        return list(d.values())


