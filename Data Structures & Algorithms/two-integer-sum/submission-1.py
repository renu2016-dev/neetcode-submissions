class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # print(i)
            for j in range(i+1,len(nums)):
                # print(j, nums[i]+ nums[j])
                if nums[i]+ nums[j] == target:
                    print(i,j)
                    return [i,j]
        
                         