class Solution:

    class FrozenCounter:
        def __init__(self, iterable=None, **kwargs):
            # Build a Counter internally
            self._counter = Counter(iterable, **kwargs)
            # Store an immutable, sorted representation for hashing
            self._items = tuple(sorted(self._counter.items()))

        def __getitem__(self, key):
            return self._counter[key]

        def __iter__(self):
            return iter(self._counter)

        def __len__(self):
            return len(self._counter)

        def items(self):
            return self._counter.items()

        def __repr__(self):
            return f"FrozenCounter({dict(self._counter)})"

        def __eq__(self, other):
            if isinstance(other, Solution.FrozenCounter):
                return self._items == other._items
            return NotImplemented

        def __hash__(self):
            # Hash based on the immutable tuple of sorted items
            return hash(self._items)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for string in strs:
            c = Solution.FrozenCounter(string)
            if c in d:
                d[c].append(string)
            else:
                d[c]=[string]
        
        return list(d.values())


