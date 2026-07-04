class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = dict()
        for num in nums:
            if num in temp.keys():
                return True
            else:
                temp[num] = True
        
        return False