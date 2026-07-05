class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp = dict()
        
        for num in nums:
            temp[num] = 1
        longest = 0
        prevlongest = 0
        # print(temp)
        for num in temp:
            # print(num)
            start = num
            if temp.get(num):
                temp[num] = None
                longest = 1
                while temp.get(start+1, None) == 1:
                    longest += 1
                    temp[start+1] = None
                    start += 1
                start = num
                while temp.get(start-1, None) == 1:
                    longest += 1
                    temp[start-1] = None
                    start -= 1 
                print(longest)
                if longest > prevlongest:
                    prevlongest = longest
                longest = 0

        return prevlongest


