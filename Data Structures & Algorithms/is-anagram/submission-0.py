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
                if tempS[char] <= 0:
                    del tempS[char]
            else:
                return False
        if len(tempS) == 0:
            return True
        else:
            return False
        