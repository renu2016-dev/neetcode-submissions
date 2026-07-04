class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tempS = dict()
        for char in s:
            if char in tempS.keys():
                tempS[char] += 1
            else:
                tempS[char] = 1
        
        for char in t:
            if char in tempS.keys():
                tempS[char] -= 1
            else:
                return False

        for k, vs in tempS.items():
            if vs != 0:
                return False
        
        return True
        